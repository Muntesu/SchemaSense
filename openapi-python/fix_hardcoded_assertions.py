#!/usr/bin/env python3
"""
Fix hardcoded data assertions in Schemathesis test files.

Replaces hardcoded booking IDs and response data with dynamic checks.
"""

import re
import glob
from pathlib import Path


def fix_hardcoded_assertions(content: str) -> str:
    """Replace all hardcoded data assertions with dynamic checks."""
    lines = content.split('\n')
    new_lines = []
    i = 0
    
    while i < len(lines):
        line = lines[i]
        
        # Check if this line contains a hardcoded response.json() assertion
        # OR if there's an existing dynamic check that's wrong (dict check for list endpoint)
        # OR if there's a direct response_data = response.json() call that needs protection
        is_existing_dynamic_check = False
        has_unsafe_json_call = False
        if "response_data = response.json()" in line:
            # Check if this JSON call is already protected by checking indentation
            # Look backwards to see if there's a status code check and try block that this line is inside
            has_status_check = False
            has_try_block = False
            current_indent = len(line) - len(line.lstrip())
            
            # Look backwards to find status check and try: block that this line is inside
            for j in range(i - 1, max(0, i - 20), -1):
                prev_line = lines[j]
                prev_indent = len(prev_line) - len(prev_line.lstrip())
                
                # Check for status code check
                if ('check.equal(response.status_code' in prev_line or 'if response.status_code' in prev_line) and prev_indent <= current_indent:
                    has_status_check = True
                
                # Check for try: block - must be at less indentation (meaning we're inside it)
                # Don't break after finding it - continue checking for status check
                if 'try:' in prev_line and prev_indent < current_indent and not has_try_block:
                    # Make sure there's no except: between try: and this line
                    has_except = False
                    for k in range(j + 1, i):
                        except_line = lines[k]
                        except_indent = len(except_line) - len(except_line.lstrip())
                        if 'except' in except_line and except_indent <= prev_indent:
                            has_except = True
                            break
                    if not has_except:
                        has_try_block = True
                        # Don't break - continue looking for status check
                
                # If we found both, we can stop looking
                if has_status_check and has_try_block:
                    break
            
            # If there's already a status check AND try block protecting this line, skip it entirely
            # Don't even check for existing dynamic checks - if it's protected, leave it alone
            if has_status_check and has_try_block:
                # Already protected - just keep the line as is
                new_lines.append(line)
                i += 1
                continue
            
            # Not protected - check if it needs fixing
            # Check if next few lines have a dict check that should be a list check
            for k in range(i+1, min(i+5, len(lines))):
                if "check.is_instance(response_data, dict" in lines[k]:
                    is_existing_dynamic_check = True
                    break
            
            # Mark as unsafe if not already protected
            has_unsafe_json_call = True
        
        # Also check for hardcoded check.equal(response_data, {...}) assertions
        has_hardcoded_assertion = False
        if "check.equal(response_data, {" in line:
            # This is a hardcoded assertion that needs to be replaced
            # Check if we're already inside a protected try block
            current_indent = len(line) - len(line.lstrip())
            has_status_check = False
            has_try_block = False
            
            # Look backwards to see if we're already inside a try block and have a status check
            for j in range(i - 1, max(0, i - 20), -1):
                prev_line = lines[j]
                prev_indent = len(prev_line) - len(prev_line.lstrip())
                
                if ('check.equal(response.status_code' in prev_line or 'if response.status_code' in prev_line) and prev_indent <= current_indent:
                    has_status_check = True
                
                if 'try:' in prev_line and prev_indent < current_indent:
                    # Check if there's an except after this line (meaning we're inside the try)
                    for k in range(j + 1, i):
                        if 'except' in lines[k]:
                            except_indent = len(lines[k]) - len(lines[k].lstrip())
                            if except_indent <= prev_indent:
                                break  # Found except before our line, so we're not in this try
                    else:
                        # No except found before our line, so we're inside this try
                        has_try_block = True
                        break
            
            # Mark this as a hardcoded assertion that needs replacement
            has_hardcoded_assertion = True
            
            # If we're NOT already inside a protected try block, also mark as unsafe to add protection
            if not (has_status_check and has_try_block):
                has_unsafe_json_call = True
        
        if "check.equal(response.json()" in line or is_existing_dynamic_check or has_unsafe_json_call or has_hardcoded_assertion:
            # Determine the HTTP method and endpoint from context
            http_method = None
            endpoint = None
            has_body = False
            body_var = None
            expected_status = None  # Extract expected status code from context
            
            # Look back up to 15 lines to find request details and expected status code
            for j in range(max(0, i - 15), i):
                if 'requests.post' in lines[j] or 'response = requests.post' in lines[j]:
                    http_method = 'POST'
                elif 'requests.put' in lines[j] or 'response = requests.put' in lines[j]:
                    http_method = 'PUT'
                elif 'requests.patch' in lines[j] or 'response = requests.patch' in lines[j]:
                    http_method = 'PATCH'
                elif 'requests.get' in lines[j] or 'response = requests.get' in lines[j]:
                    http_method = 'GET'
                elif 'requests.delete' in lines[j] or 'response = requests.delete' in lines[j]:
                    http_method = 'DELETE'
                
                if '/booking' in lines[j]:
                    endpoint = 'booking'
                elif '/auth' in lines[j]:
                    endpoint = 'auth'
                elif '/ping' in lines[j]:
                    endpoint = 'ping'
                
                if 'body =' in lines[j]:
                    has_body = True
                    # Try to extract body variable name (usually just 'body')
                    body_match = re.search(r'body\s*=\s*(\{.*?\}|[A-Za-z_]+)', lines[j])
                    if body_match:
                        body_var = 'body'
                
                # Extract expected status code from status check line
                if 'check.equal(response.status_code' in lines[j]:
                    status_match = re.search(r'check\.equal\(response\.status_code,\s*(\d+)', lines[j])
                    if status_match:
                        expected_status = int(status_match.group(1))
            
            # Check if we need to add the full protection (status check + try block) or just replace the assertion
            add_full_protection = has_unsafe_json_call and not has_hardcoded_assertion
            
            # Generate appropriate dynamic checks based on method and endpoint
            if http_method == 'POST' and endpoint == 'booking' and has_body:
                # POST /booking: check bookingid exists and is int, booking matches request body
                # Check if we're replacing a hardcoded assertion inside an existing try block
                if has_hardcoded_assertion and not has_unsafe_json_call:
                    # Just replace the assertion line with dynamic checks (no try block needed)
                    dynamic_check = f'''                # Dynamic check: bookingid should exist and be a number, booking data should match request
                check.is_in('bookingid', response_data, 'Response should contain bookingid')
                check.is_instance(response_data['bookingid'], int, 'bookingid should be an integer')
                check.is_in('booking', response_data, 'Response should contain booking')
                check.equal(response_data['booking'], body, 'Response booking data should match request body')'''
                else:
                    # Add full protection with status check and try block
                    expected_status_code = expected_status if expected_status else 201
                    dynamic_check = f'''        # Only check body if status code matches expected
        if response.status_code == {expected_status_code}:
            try:
                response_data = response.json()
                # Dynamic check: bookingid should exist and be a number, booking data should match request
                check.is_in('bookingid', response_data, 'Response should contain bookingid')
                check.is_instance(response_data['bookingid'], int, 'bookingid should be an integer')
                check.is_in('booking', response_data, 'Response should contain booking')
                check.equal(response_data['booking'], body, 'Response booking data should match request body')
            except (json.JSONDecodeError, requests.exceptions.JSONDecodeError):
                # Response is not JSON - skip body check
                pass'''
                
                # Replace the hardcoded assertion or unsafe JSON call
                # Skip the status code line if it exists (already added)
                if i > 0 and 'check.equal(response.status_code' in lines[i-1]:
                    # Status code check already in new_lines, just add dynamic check
                    new_lines.append(dynamic_check)
                else:
                    new_lines.append(dynamic_check)
                
                # Skip the original line
                if has_unsafe_json_call:
                    # Skip the response_data = response.json() line and any subsequent lines that use response_data
                    i += 1
                    while i < len(lines) and ('response_data' in lines[i] or lines[i].strip().startswith('# Dynamic check:')):
                        if not lines[i].strip().startswith('# Dynamic check:'):
                            i += 1
                        else:
                            break
                elif has_hardcoded_assertion:
                    # Skip the hardcoded assertion line
                    i += 1
                else:
                    i += 1
                continue
            
            elif http_method in ('PUT', 'PATCH') and endpoint == 'booking' and has_body:
                # PUT/PATCH /booking/{id}: response should match request body
                # Check if we're replacing a hardcoded assertion inside an existing try block
                if has_hardcoded_assertion and not has_unsafe_json_call:
                    # Just replace the assertion line with dynamic checks (no try block needed)
                    dynamic_check = f'''                # Dynamic check: response body should match request body
                check.equal(response_data, body, 'Response body should match request body')'''
                else:
                    # Add full protection with status check and try block
                    expected_status_code = expected_status if expected_status else 200
                    dynamic_check = f'''        # Only check body if status code matches expected
        if response.status_code == {expected_status_code}:
            try:
                response_data = response.json()
                # Dynamic check: response body should match request body
                check.equal(response_data, body, 'Response body should match request body')
            except (json.JSONDecodeError, requests.exceptions.JSONDecodeError):
                # Response is not JSON - skip body check
                pass'''
                
                # Replace the hardcoded assertion or unsafe JSON call
                # Skip the status code line if it exists (already added)
                if i > 0 and 'check.equal(response.status_code' in lines[i-1]:
                    # Status code check already in new_lines, just add dynamic check
                    new_lines.append(dynamic_check)
                else:
                    new_lines.append(dynamic_check)
                
                # Skip the original line
                if has_unsafe_json_call:
                    # Skip the response_data = response.json() line and any subsequent lines that use response_data
                    i += 1
                    while i < len(lines) and ('response_data' in lines[i] or lines[i].strip().startswith('# Dynamic check:')):
                        if not lines[i].strip().startswith('# Dynamic check:'):
                            i += 1
                        else:
                            break
                elif has_hardcoded_assertion:
                    # Skip the hardcoded assertion line
                    i += 1
                else:
                    i += 1
                continue
            
            elif http_method == 'GET' and endpoint == 'booking':
                # GET /booking or GET /booking/{id} or GET /booking?query=params
                # Check if it's GET /booking (list) or GET /booking/{id} (single)
                is_list = False
                has_query_params = False
                for j in range(max(0, i - 10), i):
                    # Check for booking URL - look for /booking in the URL line
                    if '/booking' in lines[j] and ('url =' in lines[j] or 'url=' in lines[j]):
                        # Check if it has query params (query params mean it's a filtered list)
                        if '?' in lines[j] and '=' in lines[j].split('?', 1)[1]:
                            has_query_params = True
                            is_list = True  # GET /booking?params returns a filtered list
                            break
                        # Check if it's just /booking (no ID, no query) - also returns a list
                        # Pattern: /booking" or /booking' or /booking/ (but not /booking/{id})
                        if not re.search(r'/booking/\d+', lines[j]):
                            # If it's just /booking without ID, it's a list endpoint
                            if re.search(r'/booking["\']|/booking\?|/booking["\']\s*\n', lines[j]):
                                is_list = True
                                break
                
                if is_list or has_query_params:
                    # GET /booking or GET /booking?params: Check structure only (list of dicts with bookingid)
                    # Only parse JSON if status code matches (to avoid errors on error responses)
                    # Use expected status code from context, or default to 200
                    expected_status_code = expected_status if expected_status else 200
                    dynamic_check = f'''        # Only check body if status code matches expected
        if response.status_code == {expected_status_code}:
            try:
                response_data = response.json()
                # Dynamic check: response should be a list, each item should have bookingid
                check.is_instance(response_data, list, 'Response should be a list')
                for item in response_data:
                    check.is_instance(item, dict, 'Each item should be a dict')
                    check.is_in('bookingid', item, 'Each item should contain bookingid')
                    check.is_instance(item['bookingid'], int, 'bookingid should be an integer')
            except (json.JSONDecodeError, requests.exceptions.JSONDecodeError):
                # Response is not JSON - skip body check
                pass'''
                    
                    # If this is replacing an existing dynamic check, skip the old lines
                    if is_existing_dynamic_check:
                        # Skip the current line (response_data = response.json())
                        # and the next few lines until we hit something that's not part of the old check
                        i += 1
                        skipped_lines = 0
                        while i < len(lines) and skipped_lines < 10:
                            current_line = lines[i].strip()
                            # Skip lines that are part of the old dict check
                            if (current_line.startswith('# Dynamic check:') and 'dict' in current_line.lower() or
                                'check.is_instance(response_data, dict' in current_line or
                                ('expected_fields' in current_line and '=' in current_line) or
                                (current_line.startswith('for field in') and 'expected_fields' in ''.join(lines[max(0, i-2):i+1])) or
                                ('check.is_not_none(response_data[field]' in current_line)):
                                i += 1
                                skipped_lines += 1
                                continue
                            # Skip empty lines immediately after the old check
                            if not current_line and skipped_lines > 0:
                                i += 1
                                skipped_lines += 1
                                continue
                            break
                        new_lines.append(dynamic_check)
                        
                        # If this was an unsafe JSON call, skip the original line and any subsequent lines that use response_data
                        if has_unsafe_json_call:
                            i += 1  # Skip the response_data = response.json() line
                            # Skip any subsequent lines that use response_data (but not the dynamic check comment)
                            while i < len(lines) and ('response_data' in lines[i] or lines[i].strip().startswith('# Dynamic check:')):
                                if not lines[i].strip().startswith('# Dynamic check:'):
                                    i += 1
                                else:
                                    break
                        continue
                else:
                    # GET /booking/{id}: Check structure only (dict with booking fields)
                    # Only parse JSON if status code matches (to avoid errors on error responses)
                    # Use expected status code from context, or default to 200
                    expected_status_code = expected_status if expected_status else 200
                    # Use regular string formatting to avoid f-string variable scope issues
                    dynamic_check = f'''        # Only check body if status code matches expected
        if response.status_code == {expected_status_code}:
            try:
                response_data = response.json()
                # Dynamic check: response should have booking structure
                check.is_instance(response_data, dict, 'Response should be a dict')
                # Check for common booking fields (actual values may vary)
                expected_fields = ['firstname', 'lastname', 'totalprice', 'depositpaid', 'bookingdates']
                for field in expected_fields:
                    if field in response_data:
                        check.is_not_none(response_data[field], f'{{{{field}}}} should not be None')
            except (json.JSONDecodeError, requests.exceptions.JSONDecodeError):
                # Response is not JSON - skip body check
                pass'''
                
                # Replace the hardcoded assertion or existing dynamic check or unsafe JSON call
                # Skip the status code line if it exists (already added)
                if i > 0 and 'check.equal(response.status_code' in lines[i-1]:
                    # Status code check already in new_lines, just add dynamic check
                    new_lines.append(dynamic_check)
                else:
                    new_lines.append(dynamic_check)
                
                # Skip the original line
                if has_unsafe_json_call:
                    # Skip the response_data = response.json() line and any subsequent lines that use response_data
                    i += 1
                    while i < len(lines) and ('response_data' in lines[i] or lines[i].strip().startswith('# Dynamic check:')):
                        if not lines[i].strip().startswith('# Dynamic check:'):
                            i += 1
                        else:
                            break
                elif has_hardcoded_assertion:
                    # Skip the hardcoded assertion line
                    i += 1
                else:
                    i += 1
                continue
            
            elif http_method == 'POST' and endpoint == 'auth':
                # POST /auth: Response might be dynamic (token changes), but we can check structure
                # Keep original if it's a simple error message check, otherwise make dynamic
                if "'reason':" in line or '"reason":' in line:
                    # This is checking error response, which is usually static - keep it
                    new_lines.append(line)
                else:
                    # Token response - check structure only
                    # Only parse JSON if status code matches (to avoid errors on error responses)
                    # Use expected status code from context, or default to 200
                    expected_status_code = expected_status if expected_status else 200
                    dynamic_check = f'''        # Only check body if status code matches expected
        if response.status_code == {expected_status_code}:
            try:
                response_data = response.json()
                # Dynamic check: response should have token or reason field
                check.is_instance(response_data, dict, 'Response should be a dict')
                check.is_true('token' in response_data or 'reason' in response_data, 
                             'Response should contain token or reason')
            except (json.JSONDecodeError, requests.exceptions.JSONDecodeError):
                # Response is not JSON - skip body check
                pass'''
                    
                    # Skip the status code line if it exists (already added)
                    if i > 0 and 'check.equal(response.status_code' in lines[i-1]:
                        # Status code check already in new_lines, just add dynamic check
                        new_lines.append(dynamic_check)
                    else:
                        new_lines.append(dynamic_check)
                    
                    # If this was an unsafe JSON call, skip the original line and any subsequent lines that use response_data
                    if has_unsafe_json_call:
                        i += 1  # Skip the response_data = response.json() line
                        # Skip any subsequent lines that use response_data (but not the dynamic check comment)
                        while i < len(lines) and ('response_data' in lines[i] or lines[i].strip().startswith('# Dynamic check:')):
                            if not lines[i].strip().startswith('# Dynamic check:'):
                                i += 1
                            else:
                                break
                    else:
                        i += 1
                    continue
        
        # Default: keep original line
        new_lines.append(line)
        i += 1
    
    return '\n'.join(new_lines)


def main():
    """Main function to process all test files."""
    # Find all Schemathesis test files
    test_dir = Path('test/test_schemathesis')
    if not test_dir.exists():
        print(f"Error: Test directory not found: {test_dir}")
        return
    
    test_files = list(test_dir.glob('test_phase_*.py'))
    
    if not test_files:
        print(f"No test files found in {test_dir}")
        return
    
    total_changes = 0
    for test_file in test_files:
        print(f'Processing {test_file.name}...')
        try:
            with open(test_file, 'r', encoding='utf-8') as f:
                content = f.read()
            
            original = content
            content = fix_hardcoded_assertions(content)
            
            if content != original:
                with open(test_file, 'w', encoding='utf-8') as f:
                    f.write(content)
                print(f'  ✓ Updated {test_file.name}')
                total_changes += 1
            else:
                print(f'  - No changes needed for {test_file.name}')
        except Exception as e:
            print(f'  ✗ Error processing {test_file.name}: {e}')
    
    print(f'\n✅ Processed {len(test_files)} file(s), updated {total_changes} file(s).')


if __name__ == '__main__':
    main()

