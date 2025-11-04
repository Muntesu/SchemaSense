"""
AI-Powered Test Failure Analyzer

Analyzes pytest test failures using Groq (Llama 3.1-8B-instant) API
and generates comprehensive reports with root cause analysis, impact assessment,
and suggested fixes.
"""

import html as html_module
import json
import os
import re
import sys
import xml.etree.ElementTree as ET
from dataclasses import dataclass, field
from datetime import datetime
from pathlib import Path
from typing import Dict, List, Optional, Tuple

try:
    from groq import Groq
except ImportError:
    raise ImportError(
        "groq package is required. Install it with: pip install groq"
    )

from test.ai_config import AIConfig


@dataclass
class RequestDetails:
    """HTTP request details extracted from test failure."""
    method: str = ""  # GET, POST, PUT, PATCH, DELETE
    url: str = ""  # Full URL with query params
    path: str = ""  # API endpoint path
    query_params: Dict[str, str] = field(default_factory=dict)  # Query parameters
    headers: Dict[str, str] = field(default_factory=dict)
    body: Optional[str] = None  # Request body (JSON string or None)


@dataclass
class FailureInfo:
    """Information about a test failure."""
    test_name: str
    test_file: str
    error_message: str
    stack_trace: str = ""
    error_type: str = ""
    duration: float = 0.0
    line_number: Optional[int] = None
    request_details: Optional[RequestDetails] = None  # HTTP request details


@dataclass
class FailureAnalysis:
    """AI analysis of a test failure."""
    failure_info: FailureInfo
    root_cause: str = ""
    impact: str = ""  # High, Medium, Low
    suggested_fix: str = ""
    similar_patterns: str = ""
    confidence: str = ""  # High, Medium, Low


class FailureAnalyzer:
    """Analyzes test failures using LLM."""
    
    def __init__(self, api_key: Optional[str] = None):
        """Initialize the analyzer with Groq API client."""
        if api_key is None:
            api_key = AIConfig.get_api_key()
        
        self.client = Groq(api_key=api_key)
        self.model = AIConfig.GROQ_MODEL
        self.analysis_cache: Dict[str, FailureAnalysis] = {}
        
    def parse_junit_xml(self, xml_file: Path) -> List[FailureInfo]:
        """Parse pytest JUnit XML output to extract failures."""
        if not xml_file.exists():
            raise FileNotFoundError(f"JUnit XML file not found: {xml_file}")
        
        try:
            tree = ET.parse(xml_file)
            root = tree.getroot()
        except Exception as e:
            raise ValueError(f"Failed to parse XML file {xml_file}: {e}")
        
        failures: List[FailureInfo] = []
        
        # Handle both JUnit XML formats (testsuites root or testsuite root)
        testsuites = root.findall('testsuite')
        if not testsuites:
            testsuites = [root] if root.tag == 'testsuite' else []
        
        total_testcases = 0
        for testsuite in testsuites:
            if testsuite is None:
                continue
                
            # Use .// to find testcases at any depth, not just direct children
            testcases = testsuite.findall('.//testcase')
            total_testcases += len(testcases)
            
            for testcase in testcases:
                if testcase is None:
                    continue
                    
                # Check for failure or error
                failure = testcase.find('failure')
                error = testcase.find('error')
                
                # Use explicit None check instead of 'or' operator (ElementTree elements can be falsy)
                if failure is not None:
                    failure_elem = failure
                elif error is not None:
                    failure_elem = error
                else:
                    continue  # No failure or error found
                
                if failure_elem is None:
                    print(f"Warning: failure_elem is None for testcase: {testcase.get('name', 'unknown')}", file=sys.stderr)
                    continue
                
                try:
                    classname = testcase.get('classname', '') if testcase is not None else ''
                    name = testcase.get('name', '') if testcase is not None else ''
                    
                    # Extract test file from classname or use testsuite name
                    test_file = testcase.get('file', '') if testcase is not None else ''
                    
                    # Try to extract from classname first (more reliable than testsuite name)
                    if not test_file and classname:
                        # Extract file from classname (e.g., "test.test_schemathesis.test_phase_fuzzing.TestPhaseFuzzing")
                        # Remove the class name (last part) and convert remaining parts to file path
                        parts = classname.split('.')
                        if len(parts) > 1:
                            # Remove the class name (last part), keep module path
                            module_parts = parts[:-1]  # e.g., ['test', 'test_schemathesis', 'test_phase_fuzzing']
                            test_file = '/'.join(module_parts) + '.py'  # e.g., 'test/test_schemathesis/test_phase_fuzzing.py'
                        elif len(parts) == 1:
                            # Fallback: just the class name, try to infer
                            test_file = parts[0].replace('.', '/') + '.py'
                    
                    # Only use testsuite name as last resort (and only if it looks like a file path)
                    if not test_file and testsuite is not None:
                        testsuite_name = testsuite.get('name', '') or ''
                        # Only use testsuite name if it looks like a file path (contains .py or /)
                        if testsuite_name and ('.py' in testsuite_name or '/' in testsuite_name):
                            test_file = testsuite_name
                    
                    # Extract error message - prefer message attribute, fall back to first line of text
                    error_message = ''
                    if hasattr(failure_elem, 'get'):
                        error_message = failure_elem.get('message', '')
                    if not error_message and hasattr(failure_elem, 'text') and failure_elem.text:
                        # Extract first meaningful line from stack trace
                        first_lines = failure_elem.text.strip().split('\n')[:3]
                        error_message = ' | '.join(line.strip() for line in first_lines if line.strip())[:500]
                    
                    error_type = failure_elem.get('type', '') if hasattr(failure_elem, 'get') else ''
                    stack_trace = failure_elem.text if (failure_elem is not None and hasattr(failure_elem, 'text')) else ''
                    
                    # Extract line number from stack trace if available
                    line_number = None
                    if stack_trace:
                        for line in stack_trace.split('\n'):
                            if 'File "' in line and 'line ' in line:
                                try:
                                    line_number = int(line.split('line ')[1].split(',')[0])
                                    break
                                except (ValueError, IndexError):
                                    pass
                    
                    duration = float(testcase.get('time', '0'))
                    
                    # Extract HTTP request details from test file source code
                    request_details = self._extract_request_details_from_file(
                        test_file, classname, name, stack_trace, error_message
                    )
                    
                    failure_info = FailureInfo(
                        test_name=f"{classname}::{name}" if classname else name,
                        test_file=test_file,
                        error_message=error_message,
                        stack_trace=stack_trace[:1000],  # Limit stack trace length
                        error_type=error_type,
                        duration=duration,
                        line_number=line_number,
                        request_details=request_details
                    )
                    failures.append(failure_info)
                    
                except (AttributeError, KeyError, ValueError) as e:
                    # Skip this test case if we can't parse it
                    test_name = testcase.get('name', 'unknown') if testcase is not None else 'unknown'
                    print(f"Warning: Could not parse failure info for testcase '{test_name}': {e}", file=sys.stderr)
                    import traceback
                    traceback.print_exc(file=sys.stderr)
                    continue
                except Exception as e:
                    # Catch any other exception
                    test_name = testcase.get('name', 'unknown') if testcase is not None else 'unknown'
                    print(f"Error: Unexpected exception parsing testcase '{test_name}': {e}", file=sys.stderr)
                    import traceback
                    traceback.print_exc(file=sys.stderr)
                    continue
        
        if not failures and total_testcases > 0:
            # No failures found - this is normal if all tests passed
            pass
        
        return failures
    
    def _extract_request_details_from_file(
        self, test_file: str, classname: str, test_name: str, stack_trace: str, error_message: str
    ) -> Optional[RequestDetails]:
        """Extract HTTP request details by reading the test file source code."""
        details = RequestDetails()
        
        # First try to read from source file
        try:
            # Resolve test file path
            test_file_path = None
            if test_file:
                # Extract just the filename if it's a full path
                filename = Path(test_file).name
                
                # Get the current working directory (where the script is run from)
                cwd = Path.cwd()
                
                # Try multiple possible locations
                possible_paths = [
                    Path(test_file),  # Full path as-is
                    cwd / test_file,  # Relative to current working directory
                    cwd / "openapi-python" / test_file,  # openapi-python/test/test_schemathesis/test_phase_fuzzing.py (from project root)
                    cwd / f"test/{filename}",  # test/test_phase_fuzzing.py
                    cwd / f"test/test_schemathesis/{filename}",  # test/test_schemathesis/test_phase_fuzzing.py
                    cwd / f"test/{test_file}",  # test/test_schemathesis/test_phase_fuzzing.py (if test_file is relative)
                    cwd / f"test/test_schemathesis/{test_file}",  # test/test_schemathesis/test_schemathesis/test_phase_fuzzing.py
                    # Also try from the script's directory (test/)
                    Path(__file__).parent / filename,  # test/test_phase_fuzzing.py (if script is in test/)
                    Path(__file__).parent / test_file,  # test/test_schemathesis/test_phase_fuzzing.py
                    Path(__file__).parent.parent / "test" / filename,  # ../test/test_phase_fuzzing.py
                    Path(__file__).parent.parent / "test" / test_file,  # ../test/test_schemathesis/test_phase_fuzzing.py
                ]
                
                for path in possible_paths:
                    if path.exists():
                        test_file_path = path
                        break
            
            if test_file_path and test_file_path.exists():
                source_code = test_file_path.read_text()
                # Extract test function code
                test_func_match = self._extract_test_function(source_code, classname, test_name)
                if test_func_match:
                    # Parse from test function source
                    self._parse_request_from_source(details, test_func_match)
                    # Return details if we found at least method or URL/path
                    if details.method or details.url or details.path:
                        # If we have method but no URL, try fallback to get URL
                        if details.method and not details.url and not details.path:
                            fallback_details = self._extract_request_details(test_name, stack_trace, error_message)
                            if fallback_details and (fallback_details.url or fallback_details.path):
                                details.url = fallback_details.url or details.url
                                details.path = fallback_details.path or details.path
                        return details
        except Exception as e:
            # Continue to fallback if extraction fails
            pass
        
        # Fallback: extract from stack trace and test name
        return self._extract_request_details(test_name, stack_trace, error_message)
    
    def _extract_test_function(self, source_code: str, classname: str, test_name: str) -> Optional[str]:
        """Extract the test function source code from the file."""
        # Find the test function by name
        # Pattern: def test_name(self): or def test_name(self) -> None:
        # Handle both class methods and standalone functions
        
        # If classname is provided, try to find the class first, then the method
        if classname:
            # Extract class name from classname (last part after last dot)
            class_name = classname.split('.')[-1] if '.' in classname else classname
            # Find the class definition
            class_pattern = rf'class\s+{re.escape(class_name)}\s*[\(:]'
            class_match = re.search(class_pattern, source_code)
            if class_match:
                # Search for the test function within the class scope
                # Start searching from the class definition
                class_start = class_match.end()
                # Find the test function within the class
                test_func_pattern = rf'def\s+{re.escape(test_name)}\s*\([^)]*\)[^:]*:'
                test_match = re.search(test_func_pattern, source_code[class_start:])
                if test_match:
                    # Adjust position to account for class_start offset
                    match_start = class_start + test_match.start()
                    match_end = class_start + test_match.end()
                    # Use the positions directly - create a simple match-like object
                    class MockMatch:
                        def __init__(self, start_pos, end_pos, original_match):
                            self._start = start_pos
                            self._end = end_pos
                            self._original = original_match
                        def start(self):
                            return self._start
                        def end(self):
                            return self._end
                        def group(self, i=0):
                            return self._original.group(i) if i == 0 else None
                    match = MockMatch(match_start, match_end, test_match)
                else:
                    match = None
            else:
                # Class not found, try searching the whole file
                test_func_pattern = rf'def\s+{re.escape(test_name)}\s*\([^)]*\)[^:]*:'
                match = re.search(test_func_pattern, source_code)
        else:
            # No classname, search the whole file
            test_func_pattern = rf'def\s+{re.escape(test_name)}\s*\([^)]*\)[^:]*:'
            match = re.search(test_func_pattern, source_code)
        
        if not match:
            return None
        
        # Extract the function body (everything until next def or end of class)
        start_pos = match.end()
        
        # Find the function body indentation
        lines = source_code[start_pos:].split('\n')
        if not lines:
            return None
        
        # Find the first non-empty line to determine indentation
        func_indent = None
        for line in lines:
            if line.strip():
                # Get the indentation of the function body
                indent_match = re.match(r'(\s*)', line)
                if indent_match:
                    func_indent = indent_match.group(1)
                break
        
        if not func_indent:
            return None
        
        # Extract function body until next def/class at same or less indent
        func_lines = []
        for line in lines:
            stripped = line.strip()
            if not stripped:
                func_lines.append(line)
                continue
            
            # Check if this is a new function/class (same or less indent)
            line_indent = re.match(r'(\s*)', line).group(1)
            
            # If we hit a new function/class at same or less indent, stop
            if len(line_indent) <= len(func_indent) and not line_indent.startswith(func_indent):
                if stripped.startswith('def ') or stripped.startswith('class '):
                    break
                # Also stop if we hit a non-empty line at less indent that's not part of our function
                if len(line_indent) < len(func_indent):
                    break
            
            # If we're still in the function body (same or greater indent), add the line
            if line_indent.startswith(func_indent) or len(line_indent) > len(func_indent):
                func_lines.append(line)
        
        return '\n'.join(func_lines)
    
    def _parse_request_from_source(self, details: RequestDetails, source_code: str):
        """Parse request details from test function source code - simplified approach."""
        # Get base URL
        try:
            from config import API_BASE_URL
            base_url = API_BASE_URL
        except ImportError:
            base_url = "https://restful-booker.herokuapp.com"
        
        # 1. Extract method from requests.put/get/post/patch/delete
        method_match = re.search(r'requests\.(get|post|put|patch|delete)\s*\(', source_code, re.IGNORECASE)
        if method_match:
            details.method = method_match.group(1).upper()
        
        # 2. Extract URL - look for url = f"{self.base_url}/path"
        url_match = re.search(r'url\s*=\s*f?["\']([^"\']+)["\']', source_code)
        if url_match:
            url_str = url_match.group(1)
            # Extract path after {self.base_url} or self.base_url}
            if '{self.base_url}' in url_str:
                path = url_str.split('{self.base_url}')[-1]
            elif 'self.base_url}' in url_str:
                path = url_str.split('self.base_url}')[-1]
            else:
                path = url_str
            # Clean up any remaining braces
            path = path.split('}')[-1] if '}' in path else path
            details.path = path
            details.url = f"{base_url}{path}"
        
        # 3. Extract headers - find headers = ... and extract dict with balanced braces
        headers_patterns = [
            r'headers\s*=\s*self\._normalize_headers\s*\(',
            r'headers\s*=\s*',
        ]
        for pattern in headers_patterns:
            match = re.search(pattern, source_code)
            if match:
                start = match.end()
                brace_pos = source_code.find('{', start)
                if brace_pos != -1:
                    # Find matching closing brace
                    brace_count = 0
                    for i in range(brace_pos, min(brace_pos + 1000, len(source_code))):
                        if source_code[i] == '{':
                            brace_count += 1
                        elif source_code[i] == '}':
                            brace_count -= 1
                            if brace_count == 0:
                                headers_str = source_code[brace_pos:i+1]
                                try:
                                    import ast
                                    headers_dict = ast.literal_eval(headers_str)
                                    if isinstance(headers_dict, dict):
                                        details.headers = headers_dict
                                        break
                                except Exception:
                                    pass
                break
        
        # 4. Extract body - find body = {...} or json={...} with balanced braces
        body_patterns = [
            r'body\s*=\s*',
            r'json\s*=\s*',
        ]
        for pattern in body_patterns:
            match = re.search(pattern, source_code)
            if match:
                start = match.end()
                brace_pos = source_code.find('{', start)
                if brace_pos != -1:
                    # Find matching closing brace
                    brace_count = 0
                    for i in range(brace_pos, min(brace_pos + 2000, len(source_code))):
                        if source_code[i] == '{':
                            brace_count += 1
                        elif source_code[i] == '}':
                            brace_count -= 1
                            if brace_count == 0:
                                body_str = source_code[brace_pos:i+1]
                                try:
                                    import ast
                                    body_obj = ast.literal_eval(body_str)
                                    # Format as pretty JSON
                                    details.body = json.dumps(body_obj, indent=2, ensure_ascii=False)
                                    break
                                except Exception:
                                    # Body contains function calls/expressions - store raw Python code
                                    details.body = body_str
                                    break
                break
    
    def _extract_request_details(self, test_name: str, stack_trace: str, error_message: str) -> Optional[RequestDetails]:
        """Extract HTTP request details from test name, stack trace, and error message."""
        details = RequestDetails()
        
        # Combine all text for searching
        search_text = (test_name + " " + stack_trace + " " + error_message).lower()
        
        # Extract method from test name or stack trace
        # Patterns: test_post_auth, test_booking_get, test_put_booking_8, etc.
        # Or from API calls: self.api.booking_post, requests.post, etc.
        method_patterns = [
            (r'\btest_(get|post|put|patch|delete)', lambda m: m.group(1).upper()),
            (r'\.(get|post|put|patch|delete)\s*\(', lambda m: m.group(1).upper()),
            (r'requests\.(get|post|put|patch|delete)', lambda m: m.group(1).upper()),
            (r'\.(auth|booking|ping)_(get|post|put|patch|delete)', lambda m: m.group(2).upper()),
            (r'\.(auth|booking|ping)_(get|post|put|patch|delete)', lambda m: m.group(2).upper()),
        ]
        
        for pattern, extractor in method_patterns:
            match = re.search(pattern, search_text, re.IGNORECASE)
            if match:
                details.method = extractor(match)
                break
        
        # If method not found, infer from test name
        if not details.method:
            details.method = self._infer_method_from_test_name(test_name)
        
        # Extract URL/path from stack trace or error message
        # Look for URL patterns: https://..., http://..., /booking/123, etc.
        url_patterns = [
            (r'https?://[^\s\'"<>\)]+', lambda m: m.group(0)),  # Full URLs
            (r'url\s*=\s*["\']([^"\']+)["\']', lambda m: m.group(1)),  # url = "https://..."
            (r'url\s*=\s*f?["\']([^"\']+)["\']', lambda m: m.group(1)),  # url = f"https://..."
            (r'["\']([^"\']*(?:/booking|/auth|/ping)[^"\']*)["\']', lambda m: m.group(1)),  # Paths in quotes
            (r'/(?:booking|auth|ping)[/\d\?]*', lambda m: m.group(0)),  # Common paths
        ]
        
        for pattern, extractor in url_patterns:
            match = re.search(pattern, stack_trace + " " + error_message, re.IGNORECASE)
            if match:
                url = extractor(match)
                if url.startswith('http'):
                    details.url = url
                    # Extract path from URL
                    try:
                        from urllib.parse import urlparse
                        parsed = urlparse(url)
                        details.path = parsed.path
                    except Exception:
                        pass
                else:
                    details.path = url if url.startswith('/') else '/' + url
                break
        
        # Extract path from test name if not found
        if not details.path and not details.url:
            # Patterns: test_post_auth, test_booking_get, test_put_booking_8
            path_patterns = [
                (r'\b(?:/booking|/auth|/ping)[/\w\d]*', lambda m: m.group(0)),
                (r'booking[/\d]+', lambda m: '/booking/' + m.group(0).split('/')[-1] if '/' in m.group(0) else '/booking'),
                (r'\bauth\b', lambda m: '/auth'),
                (r'\bping\b', lambda m: '/ping'),
            ]
            for pattern, extractor in path_patterns:
                match = re.search(pattern, test_name.lower())
                if match:
                    details.path = extractor(match)
                    break
        
        # Extract headers from stack trace - look for requests.post(url, headers=...) or headers dict
        headers_patterns = [
            r'headers\s*=\s*\{([^}]+)\}',
            r'headers\s*=\s*self\._normalize_headers\(([^)]+)\)',
            r'headers\s*=\s*\{([^}]+)\}',
        ]
        for pattern in headers_patterns:
            headers_match = re.search(pattern, stack_trace, re.DOTALL | re.IGNORECASE)
            if headers_match:
                headers_text = headers_match.group(1)
                # Try to parse headers dict-like structure
                for line in headers_text.split('\n'):
                    # Look for key: value patterns
                    header_match = re.search(r'["\']([^"\']+)["\']\s*:\s*["\']?([^,"\']+)["\']?', line)
                    if header_match:
                        key = header_match.group(1)
                        value = header_match.group(2)
                        details.headers[key] = value
                if details.headers:
                    break
        
        # Extract body from stack trace - look for json=..., body=..., or API method arguments
        # Use balanced brace matching to handle nested dictionaries
        for pattern_prefix in [
            r'json\s*=\s*',
            r'body\s*=\s*',
        ]:
            body_match = re.search(pattern_prefix, stack_trace, re.IGNORECASE)
            if body_match:
                start_pos = body_match.end()
                # Find the opening brace
                brace_pos = stack_trace.find('{', start_pos)
                if brace_pos == -1:
                    # Try to find body = Booking(...) pattern
                    func_match = re.search(r'body\s*=\s*([A-Za-z_]+)\(([^)]+)\)', stack_trace[start_pos:], re.IGNORECASE)
                    if func_match:
                        # This is a function call - extract arguments
                        body_text = func_match.group(2)
                        try:
                            body_dict = {}
                            # Parse keyword arguments
                            for kwarg_match in re.finditer(r'(\w+)\s*=\s*["\']?([^,\s\)]+)["\']?', body_text):
                                if kwarg_match.group(1) not in ['url', 'headers', 'method']:
                                    body_dict[kwarg_match.group(1)] = kwarg_match.group(2)
                            if body_dict:
                                details.body = json.dumps(body_dict, indent=2)
                                break
                        except Exception:
                            pass
                    continue
                
                # Match balanced braces
                brace_count = 0
                end_pos = brace_pos
                for i in range(brace_pos, len(stack_trace)):
                    if stack_trace[i] == '{':
                        brace_count += 1
                    elif stack_trace[i] == '}':
                        brace_count -= 1
                        if brace_count == 0:
                            end_pos = i + 1
                            break
                
                if brace_count == 0:
                    body_str = stack_trace[brace_pos:end_pos]
                    # Try to parse as Python dict/literal
                    try:
                        import ast
                        body_obj = ast.literal_eval(body_str)
                        if isinstance(body_obj, dict):
                            details.body = json.dumps(body_obj, indent=2)
                        else:
                            details.body = json.dumps(body_obj, indent=2, default=str)
                        break
                    except Exception:
                        # Fallback: try to parse manually
                        try:
                            body_dict = {}
                            for line in body_str.split('\n'):
                                # Look for key-value pairs
                                kv_match = re.search(r'["\']([^"\']+)["\']\s*:\s*["\']?([^,"\']+)["\']?', line)
                                if kv_match:
                                    body_dict[kv_match.group(1)] = kv_match.group(2)
                                # Also look for keyword arguments: key=value
                                kwarg_match = re.search(r'(\w+)\s*=\s*["\']?([^,\s\)]+)["\']?', line)
                                if kwarg_match and kwarg_match.group(1) not in ['url', 'headers', 'method']:
                                    body_dict[kwarg_match.group(1)] = kwarg_match.group(2)
                            if body_dict:
                                details.body = json.dumps(body_dict, indent=2)
                                break
                        except Exception:
                            details.body = body_str[:500]  # Truncate if too long
        
        # Only return details if we found at least method or path
        if details.method or details.path or details.url:
            return details
        return None
    
    def _infer_method_from_test_name(self, test_name: str) -> str:
        """Infer HTTP method from test name."""
        test_lower = test_name.lower()
        if 'get' in test_lower or 'fetch' in test_lower:
            return 'GET'
        elif 'post' in test_lower or 'create' in test_lower:
            return 'POST'
        elif 'put' in test_lower or 'update' in test_lower:
            return 'PUT'
        elif 'patch' in test_lower or 'partial' in test_lower:
            return 'PATCH'
        elif 'delete' in test_lower or 'remove' in test_lower:
            return 'DELETE'
        return ''
    
    def analyze_failure(self, failure: FailureInfo, verbose: bool = True) -> FailureAnalysis:
        """Analyze a single failure using LLM."""
        # Check cache first
        cache_key = f"{failure.test_name}:{failure.error_message[:100]}"
        if cache_key in self.analysis_cache:
            if verbose:
                print(f"  ✓ Using cached analysis for: {failure.test_name}")
            return self.analysis_cache[cache_key]
        
        # Prepare prompt for LLM
        prompt = self._create_analysis_prompt(failure)
        
        try:
            if verbose:
                print(f"  → Calling Groq API...", end='', flush=True)
            
            # Call Groq API
            response = self.client.chat.completions.create(
                model=self.model,
                messages=[
                    {
                        "role": "system",
                        "content": """You are an expert API testing and software quality engineer with deep knowledge of:
- REST API design patterns and best practices
- HTTP status codes and their meanings
- Common API failure patterns (authentication, validation, business logic, server errors)
- API testing methodologies (contract-based, property-based, integration testing)
- Root cause analysis techniques

Your task is to analyze API test failures and provide:
1. **Root Cause**: Identify the underlying technical or business reason for the failure
2. **Impact**: Assess severity (High/Medium/Low) considering business impact, user experience, and system reliability
3. **Suggested Fix**: Provide actionable, specific steps to resolve the issue (include code examples if relevant)
4. **Similar Patterns**: Identify other potential issues that might have the same root cause
5. **Confidence**: Rate your confidence in the analysis (High/Medium/Low)

Be specific, technical, and actionable. Focus on what the request/response tells us about the API behavior."""
                    },
                    {
                        "role": "user",
                        "content": prompt
                    }
                ],
                temperature=AIConfig.TEMPERATURE,
                max_tokens=AIConfig.MAX_TOKENS
            )
            
            if verbose:
                print(" ✓ Response received")
            
            # Parse response
            analysis_text = response.choices[0].message.content
            
            # Extract structured information from LLM response
            analysis = self._parse_llm_response(analysis_text, failure)
            self.analysis_cache[cache_key] = analysis
            
            return analysis
            
        except Exception as e:
            # Fallback analysis if LLM call fails
            if verbose:
                print(f" ✗ API call failed: {e}")
            print(f"Warning: LLM analysis failed for {failure.test_name}: {e}", file=sys.stderr)
            return FailureAnalysis(
                failure_info=failure,
                root_cause=f"Analysis failed: {str(e)}",
                impact="Unknown",
                suggested_fix="Review error manually",
                similar_patterns="",
                confidence="Low"
            )
    
    def _create_analysis_prompt(self, failure: FailureInfo) -> str:
        """Create prompt for LLM analysis."""
        # Build request details section
        request_section = ""
        if failure.request_details:
            req = failure.request_details
            request_section = f"""
**HTTP Request Details:**
- Method: {req.method or 'Unknown'}
- URL/Path: {req.url or req.path or 'Unknown'}
"""
            if req.headers:
                headers_str = "\n".join(f"  - {k}: {v}" for k, v in list(req.headers.items())[:5])  # Limit to 5 headers
                request_section += f"- Headers:\n{headers_str}\n"
            if req.body:
                body_preview = req.body[:300] + "..." if len(req.body) > 300 else req.body
                request_section += f"- Request Body:\n{body_preview}\n"
        
        prompt = f"""Analyze this API test failure and provide a structured response:

**Test Information:**
- Test Name: {failure.test_name}
- Test File: {failure.test_file}
- Error Type: {failure.error_type}
- Duration: {failure.duration:.2f}s
{request_section}
**Error Message:**
{failure.error_message}

**Stack Trace (relevant excerpts):**
{failure.stack_trace[:800] if failure.stack_trace else 'No stack trace available'}

**Analysis Instructions:**

1. **ROOT_CAUSE**: Analyze the failure considering:
   - What HTTP request was made (method, endpoint, headers, body)?
   - What was the expected vs actual response?
   - What does the error message indicate (authentication, validation, business logic, server error)?
   - What does the stack trace reveal about where/how it failed?
   - Is this a client-side issue (test code), server-side issue (API behavior), or contract mismatch?

2. **IMPACT**: Assess severity based on:
   - Does this affect critical functionality?
   - Could this cause data corruption or security issues?
   - Does this impact user experience?
   - Is this a production blocker or a minor issue?

3. **SUGGESTED_FIX**: Provide specific, actionable steps:
   - If it's a test issue: How to fix the test code?
   - If it's an API issue: What should be changed in the API?
   - If it's a contract mismatch: What needs to be aligned?
   - Include code examples or specific changes if relevant

4. **SIMILAR_PATTERNS**: Identify:
   - Other endpoints that might have the same issue
   - Similar error patterns to watch for
   - Common failure modes in this codebase

5. **CONFIDENCE**: Rate your confidence based on:
   - How clear is the error message?
   - How much context is available?
   - Is the root cause obvious or requires investigation?

Please provide analysis in this exact format:

ROOT_CAUSE: [Detailed explanation considering request details, error context, and technical analysis]
IMPACT: [High/Medium/Low - explain why with specific reasoning]
SUGGESTED_FIX: [Actionable steps with specific details - numbered list if multiple steps]
SIMILAR_PATTERNS: [What similar issues to watch for - bullet points if multiple]
CONFIDENCE: [High/Medium/Low - explain why]

Be specific, technical, and actionable. Focus on what the request/response tells us about the API behavior."""
        return prompt
    
    def _clean_markdown(self, text: str) -> str:
        """Remove markdown formatting artifacts like ** from text."""
        if not text:
            return ""
        # Remove ** markers used for bold in markdown
        text = text.replace('**', '')
        # Remove leading/trailing whitespace
        text = text.strip()
        return text
    
    def _extract_impact_level(self, impact_text: str) -> str:
        """Extract impact level (High/Medium/Low) from impact text."""
        if not impact_text:
            return "Unknown"
        
        impact_text = self._clean_markdown(impact_text)
        impact_lower = impact_text.lower()
        
        if 'high' in impact_lower:
            return "High"
        elif 'medium' in impact_lower:
            return "Medium"
        elif 'low' in impact_lower:
            return "Low"
        else:
            return "Unknown"
    
    def _parse_list_items(self, text: str) -> List[str]:
        """Parse numbered or bulleted list items from text."""
        if not text:
            return []
        
        # Clean markdown first
        text = self._clean_markdown(text)
        
        items = []
        
        # First, try to split by numbered patterns (handles concatenated items)
        # Pattern: number followed by dot and space (e.g., "1. ", "2. ", etc.)
        numbered_pattern = r'(\d+\.\s+)'
        numbered_matches = list(re.finditer(numbered_pattern, text))
        
        if len(numbered_matches) > 1:
            # Multiple numbered items found - split them
            for i, match in enumerate(numbered_matches):
                if i == 0:
                    continue
                
                # Extract item between previous match and current match
                prev_match = numbered_matches[i - 1]
                item_start = prev_match.start()
                item_end = match.start()
                item_text = text[item_start:item_end].strip()
                # Remove the number prefix
                item_text = re.sub(r'^\d+\.\s*', '', item_text).strip()
                if item_text:
                    items.append(item_text)
            
            # Extract the last item
            if numbered_matches:
                last_match = numbered_matches[-1]
                last_item = text[last_match.start():].strip()
                last_item = re.sub(r'^\d+\.\s*', '', last_item).strip()
                if last_item:
                    items.append(last_item)
        
        # If numbered parsing didn't work, try bullet points
        if not items:
            # Look for bullet points anywhere in text (not just line start)
            # Pattern: space or start, then bullet marker, then space
            bullet_pattern = r'(?:^|\s)([-*])\s+'
            bullet_matches = list(re.finditer(bullet_pattern, text))
            
            if len(bullet_matches) > 0:
                # Found bullet points - split them
                for i, match in enumerate(bullet_matches):
                    if i == 0:
                        # First bullet - check if there's prefix text
                        prefix_end = match.start()
                        if prefix_end > 0:
                            prefix = text[:prefix_end].strip()
                            # Only include prefix if it doesn't look like a list item
                            if prefix and not re.match(r'^\d+\.', prefix):
                                # This is probably intro text like "such as:" - skip it
                                pass
                    
                    # Extract item from this bullet to next bullet or end
                    item_start = match.end()  # Start after bullet marker and space
                    if i + 1 < len(bullet_matches):
                        item_end = bullet_matches[i + 1].start()
                        item_text = text[item_start:item_end].strip()
                    else:
                        item_text = text[item_start:].strip()
                    
                    if item_text:
                        items.append(item_text)
        
        # If still no items, try line-by-line parsing
        if not items:
            lines = text.split('\n')
            for line in lines:
                line = line.strip()
                if not line:
                    continue
                
                # Check for numbered list (1., 2., etc.)
                if re.match(r'^\d+\.', line):
                    item = re.sub(r'^\d+\.\s*', '', line).strip()
                    if item:
                        items.append(item)
                # Check for bullet points (-, *, etc.)
                elif re.match(r'^[-*]\s+', line):
                    item = re.sub(r'^[-*]\s+', '', line).strip()
                    if item:
                        items.append(item)
        
        # Last resort: try splitting by "number. " pattern anywhere in text
        if not items and numbered_matches:
            # Split by numbered patterns
            parts = re.split(r'(\d+\.\s+)', text)
            # parts will alternate: ['prefix', '1. ', 'item1', '2. ', 'item2', ...]
            for i in range(len(parts)):
                if re.match(r'^\d+\.\s+$', parts[i]):
                    # This is a number marker, next part is the item
                    if i + 1 < len(parts):
                        item = parts[i + 1].strip()
                        if item:
                            items.append(item)
        
        return items if items else [text]
    
    def _parse_llm_response(self, response: str, failure: FailureInfo) -> FailureAnalysis:
        """Parse LLM response into structured FailureAnalysis."""
        analysis = FailureAnalysis(failure_info=failure)
        
        # Extract structured fields from response
        lines = response.split('\n')
        current_field = None
        
        for line in lines:
            line = line.strip()
            if not line:
                continue
            
            if 'ROOT_CAUSE:' in line.upper():
                content = line.split(':', 1)[1].strip() if ':' in line else ""
                analysis.root_cause = self._clean_markdown(content)
                current_field = 'root_cause'
            elif 'IMPACT:' in line.upper():
                content = line.split(':', 1)[1].strip() if ':' in line else ""
                impact_text = self._clean_markdown(content)
                # Extract just the level (High/Medium/Low) for impact badge
                analysis.impact = self._extract_impact_level(impact_text)
                current_field = 'impact'
            elif 'SUGGESTED_FIX:' in line.upper():
                content = line.split(':', 1)[1].strip() if ':' in line else ""
                analysis.suggested_fix = self._clean_markdown(content)
                current_field = 'suggested_fix'
            elif 'SIMILAR_PATTERNS:' in line.upper():
                content = line.split(':', 1)[1].strip() if ':' in line else ""
                analysis.similar_patterns = self._clean_markdown(content)
                current_field = 'similar_patterns'
            elif 'CONFIDENCE:' in line.upper():
                content = line.split(':', 1)[1].strip() if ':' in line else ""
                confidence_text = self._clean_markdown(content)
                # Extract confidence level
                if 'high' in confidence_text.lower():
                    analysis.confidence = "High"
                elif 'medium' in confidence_text.lower():
                    analysis.confidence = "Medium"
                elif 'low' in confidence_text.lower():
                    analysis.confidence = "Low"
                else:
                    analysis.confidence = "Unknown"
                current_field = 'confidence'
            elif current_field and line:
                # Continue current field (multi-line content)
                cleaned_line = self._clean_markdown(line)
                if current_field == 'root_cause':
                    analysis.root_cause += " " + cleaned_line
                elif current_field == 'suggested_fix':
                    analysis.suggested_fix += " " + cleaned_line
                elif current_field == 'similar_patterns':
                    analysis.similar_patterns += " " + cleaned_line
        
        # Clean all fields
        analysis.root_cause = self._clean_markdown(analysis.root_cause)
        analysis.suggested_fix = self._clean_markdown(analysis.suggested_fix)
        analysis.similar_patterns = self._clean_markdown(analysis.similar_patterns)
        
        # Fallback: if parsing failed, use whole response
        if not analysis.root_cause:
            analysis.root_cause = self._clean_markdown(response[:200])
            analysis.impact = "Unknown"
            analysis.confidence = "Low"
        
        return analysis
    
    def _format_suggested_fix(self, fix_text: str) -> str:
        """Format suggested fix text as HTML list if it contains numbered items."""
        if not fix_text:
            return 'Manual review required'
        
        # Try to parse as list items
        items = self._parse_list_items(fix_text)
        
        if len(items) > 1:
            # Format as HTML ordered list
            html_list = '<ol style="margin: 10px 0; padding-left: 20px;">'
            for item in items:
                html_list += f'<li style="margin: 5px 0;">{html_module.escape(item)}</li>'
            html_list += '</ol>'
            return html_list
        else:
            # Single item or paragraph - just return cleaned text
            return html_module.escape(self._clean_markdown(fix_text))
    
    def _format_similar_patterns(self, patterns_text: str) -> str:
        """Format similar patterns text, handling bullet points."""
        if not patterns_text:
            return ''
        
        # Try to parse as list items (might be bullet points)
        items = self._parse_list_items(patterns_text)
        
        # Check if we have bullet points (starts with - or *)
        has_bullets = any(re.match(r'^[-*]', item) for item in items if items) or \
                     any(re.search(r'^\s*[-*]\s+', line) for line in patterns_text.split('\n'))
        
        if len(items) > 1 or has_bullets:
            # Format as HTML unordered list (bullet points)
            # Clean items - remove bullet markers if present
            cleaned_items = []
            for item in items:
                # Remove bullet markers
                cleaned = re.sub(r'^[-*]\s+', '', item).strip()
                if cleaned:
                    cleaned_items.append(cleaned)
            
            if cleaned_items:
                html_list = '<ul style="margin: 10px 0; padding-left: 20px;">'
                for item in cleaned_items:
                    html_list += f'<li style="margin: 5px 0;">{html_module.escape(item)}</li>'
                html_list += '</ul>'
                return html_list
        
        # Single item or paragraph - return cleaned text
        return html_module.escape(self._clean_markdown(patterns_text))
    
    def generate_report(
        self,
        failures: List[FailureInfo],
        analyses: List[FailureAnalysis],
        output_file: Optional[Path] = None,
        total_tests: int = 0,
        passed_tests: int = 0
    ) -> str:
        """Generate HTML report with failure analysis."""
        failed_count = len(failures)
        analysis_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
        # Generate HTML report
        html = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Test Failure Analysis Report</title>
    <style>
        body {{
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, sans-serif;
            max-width: 1200px;
            margin: 0 auto;
            padding: 20px;
            background-color: #f5f5f5;
        }}
        .header {{
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            padding: 30px;
            border-radius: 10px;
            margin-bottom: 30px;
        }}
        .summary {{
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
            gap: 20px;
            margin-bottom: 30px;
        }}
        .summary-card {{
            background: white;
            padding: 20px;
            border-radius: 8px;
            box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        }}
        .summary-card h3 {{
            margin: 0 0 10px 0;
            color: #333;
        }}
        .summary-card .number {{
            font-size: 2em;
            font-weight: bold;
            color: #667eea;
        }}
        .failure {{
            background: white;
            margin-bottom: 20px;
            padding: 20px;
            border-radius: 8px;
            box-shadow: 0 2px 4px rgba(0,0,0,0.1);
            border-left: 4px solid #e74c3c;
        }}
        .failure-header {{
            display: flex;
            justify-content: space-between;
            align-items: start;
            margin-bottom: 15px;
        }}
        .test-name {{
            font-weight: bold;
            color: #333;
            font-size: 1.1em;
        }}
        .impact-badge {{
            padding: 5px 15px;
            border-radius: 20px;
            font-size: 0.9em;
            font-weight: bold;
        }}
        .impact-high {{
            background: #fee;
            color: #c33;
        }}
        .impact-medium {{
            background: #ffeaa7;
            color: #d68910;
        }}
        .impact-low {{
            background: #dfe6e9;
            color: #636e72;
        }}
        .section {{
            margin-top: 15px;
        }}
        .section h4 {{
            color: #667eea;
            margin-bottom: 8px;
        }}
        .section-content {{
            background: #f8f9fa;
            padding: 12px;
            border-radius: 5px;
            border-left: 3px solid #667eea;
        }}
        .error-details {{
            background: #fff3cd;
            padding: 12px;
            border-radius: 5px;
            margin-top: 10px;
            font-family: monospace;
            font-size: 0.9em;
        }}
        .request-details {{
            background: #e8f4f8;
            padding: 12px;
            border-radius: 5px;
            margin-top: 10px;
            font-family: monospace;
            font-size: 0.9em;
            border-left: 3px solid #3498db;
        }}
        .request-details pre {{
            margin: 5px 0;
            white-space: pre-wrap;
            word-wrap: break-word;
        }}
        .footer {{
            text-align: center;
            color: #666;
            margin-top: 40px;
            padding: 20px;
        }}
    </style>
</head>
<body>
    <div class="header">
        <h1>🤖 AI-Powered Test Failure Analysis Report</h1>
        <p>Generated: {analysis_time}</p>
    </div>
    
    <div class="summary">
        <div class="summary-card">
            <h3>Total Tests</h3>
            <div class="number">{total_tests}</div>
        </div>
        <div class="summary-card">
            <h3>Passed</h3>
            <div class="number" style="color: #27ae60;">{passed_tests}</div>
        </div>
        <div class="summary-card">
            <h3>Failed</h3>
            <div class="number" style="color: #e74c3c;">{failed_count}</div>
        </div>
        <div class="summary-card">
            <h3>Pass Rate</h3>
            <div class="number">{((passed_tests/total_tests)*100):.1f}%</div>
        </div>
    </div>
"""
        
        # Add failure analysis sections
        for i, (failure, analysis) in enumerate(zip(failures, analyses), 1):
            # Clean impact text - extract just the level (High/Medium/Low)
            impact_level = self._extract_impact_level(analysis.impact) if analysis.impact else "Unknown"
            impact_class = f"impact-{impact_level.lower()}"
            impact_text = impact_level
            
            # Pre-format the suggested fix (can't call methods in f-string expressions easily)
            formatted_fix = self._format_suggested_fix(analysis.suggested_fix)
            
            # Format stack trace
            stack_trace_html = ''
            if failure.stack_trace:
                stack_trace_html = f'<strong>Stack Trace:</strong><br><pre style="white-space: pre-wrap; word-wrap: break-word; margin: 5px 0; max-height: 300px; overflow-y: auto;">{html_module.escape(failure.stack_trace)}</pre>'
            
            # Simple request details display
            request_details_html = ''
            if failure.request_details:
                req = failure.request_details
                request_details_html = '<div class="request-details"><strong>🌐 HTTP Request:</strong><br><pre style="background: #f8f9fa; padding: 10px; border-radius: 5px; font-size: 0.85em; margin: 5px 0;">'
                
                # Method
                if req.method:
                    request_details_html += f'<strong>Method:</strong> {html_module.escape(req.method)}\n\n'
                
                # URL
                if req.url:
                    request_details_html += f'<strong>URL:</strong> {html_module.escape(req.url)}\n\n'
                elif req.path:
                    try:
                        from config import API_BASE_URL
                        url = f"{API_BASE_URL}{req.path}"
                    except ImportError:
                        url = f"https://restful-booker.herokuapp.com{req.path}"
                    request_details_html += f'<strong>URL:</strong> {html_module.escape(url)}\n\n'
                
                # Headers
                if req.headers:
                    request_details_html += '<strong>Headers:</strong>\n'
                    for key, value in req.headers.items():
                        if 'authorization' in key.lower() or 'password' in key.lower() or 'token' in key.lower():
                            value = value[:20] + '...' if len(value) > 20 else value
                        request_details_html += f'  {html_module.escape(key)}: {html_module.escape(value)}\n'
                    request_details_html += '\n'
                
                # Body
                if req.body:
                    request_details_html += '<strong>Body:</strong>\n'
                    body_display = req.body[:800] if len(req.body) > 800 else req.body
                    request_details_html += html_module.escape(body_display)
                    if len(req.body) > 800:
                        request_details_html += '\n...(truncated)'
                
                request_details_html += '</pre></div>'
            
            html += f"""
    <div class="failure">
        <div class="failure-header">
            <div>
                <div class="test-name">Failure #{i}: {html_module.escape(failure.test_name)}</div>
                <div style="color: #666; font-size: 0.9em; margin-top: 5px;">
                    {html_module.escape(failure.test_file)}
                    {f'(Line {failure.line_number})' if failure.line_number else ''}
                </div>
            </div>
            <span class="impact-badge {impact_class}">{impact_text} Impact</span>
        </div>
        
        {request_details_html}
        
        <div class="error-details">
            <strong>Error Type:</strong> {html_module.escape(failure.error_type or 'Unknown')}<br>
            <strong>Error Message:</strong><br>
            <pre style="white-space: pre-wrap; word-wrap: break-word; margin: 5px 0;">{html_module.escape(failure.error_message)}</pre>
            {stack_trace_html}
        </div>
        
        <div class="section">
            <h4>🔍 Root Cause</h4>
            <div class="section-content">
                {html_module.escape(analysis.root_cause or 'Analysis not available')}
            </div>
        </div>
        
        <div class="section">
            <h4>💡 Suggested Fix</h4>
            <div class="section-content">
                {formatted_fix}
            </div>
        </div>
"""
            
            if analysis.similar_patterns:
                # Format similar patterns (might contain bullet points)
                formatted_patterns = self._format_similar_patterns(analysis.similar_patterns)
                html += f"""
        <div class="section">
            <h4>🔗 Similar Patterns</h4>
            <div class="section-content">
                {formatted_patterns}
            </div>
        </div>
"""
            
            html += f"""
        <div style="color: #666; font-size: 0.85em; margin-top: 10px;">
            Confidence: {analysis.confidence or 'Low'} | Duration: {failure.duration:.2f}s
        </div>
    </div>
"""
        
        html += """
    <div class="footer">
        <p>Powered by Groq (Llama 3.1-8B-instant) AI Analysis</p>
        <p>Generated by pytest AI Failure Analyzer</p>
    </div>
</body>
</html>
"""
        
        # Write to file if specified
        if output_file:
            output_file.parent.mkdir(parents=True, exist_ok=True)
            output_file.write_text(html)
            print(f"Report generated: {output_file}")
        
        return html
    
    def analyze_from_junit_xml(
        self,
        xml_file: Path,
        output_file: Optional[Path] = None,
        total_tests: int = 0,
        passed_tests: int = 0,
        max_failures: Optional[int] = None
    ) -> Tuple[List[FailureInfo], List[FailureAnalysis]]:
        """Parse JUnit XML and analyze all failures."""
        print(f"Parsing JUnit XML: {xml_file}")
        if not xml_file.exists():
            print(f"Error: XML file does not exist: {xml_file}", file=sys.stderr)
            return [], []
        
        failures = self.parse_junit_xml(xml_file)
        print(f"Parsed {len(failures)} failure(s) from XML", file=sys.stderr)
        
        if not failures:
            print("No failures found in JUnit XML.")
            return [], []
        
        # Limit number of failures if specified
        original_count = len(failures)
        if max_failures and max_failures > 0:
            failures = failures[:max_failures]
            print(f"Found {original_count} failure(s), analyzing first {len(failures)}...")
        else:
            print(f"Found {len(failures)} failure(s). Analyzing with AI...")
        
        # Verify API key is configured
        api_key = AIConfig.get_api_key()
        if not api_key:
            raise ValueError("Groq API key not configured. Check ai_config.py or GROQ_API_KEY environment variable.")
        print(f"Using API key: {api_key[:10]}...{api_key[-4:] if len(api_key) > 14 else ''}")
        
        analyses = []
        for i, failure in enumerate(failures, 1):
            print(f"\n[{i}/{len(failures)}] Analyzing: {failure.test_name}")
            try:
                analysis = self.analyze_failure(failure, verbose=True)
                analyses.append(analysis)
                print(f"  ✓ Analysis complete")
            except Exception as e:
                print(f"  ✗ Failed to analyze: {e}")
                # Add fallback analysis
                analyses.append(FailureAnalysis(
                    failure_info=failure,
                    root_cause=f"Analysis error: {str(e)}",
                    impact="Unknown",
                    suggested_fix="Review error manually",
                    similar_patterns="",
                    confidence="Low"
                ))
        
        # Generate report
        if analyses:
            report_path = output_file or Path("test_failure_analysis.html")
            self.generate_report(failures, analyses, report_path, total_tests, passed_tests)
        
        return failures, analyses


def main():
    """CLI entry point for failure analyzer."""
    import argparse
    
    parser = argparse.ArgumentParser(
        description="Analyze pytest test failures using AI (Groq Llama 3.1-8B)"
    )
    parser.add_argument(
        "--xml",
        type=Path,
        required=True,
        help="Path to pytest JUnit XML output file"
    )
    parser.add_argument(
        "--output",
        type=Path,
        default=Path("test_failure_analysis.html"),
        help="Output HTML report file (default: test_failure_analysis.html)"
    )
    parser.add_argument(
        "--total-tests",
        type=int,
        default=0,
        help="Total number of tests run"
    )
    parser.add_argument(
        "--passed-tests",
        type=int,
        default=0,
        help="Number of tests that passed"
    )
    
    parser.add_argument(
        "--max-failures",
        type=int,
        default=None,
        help="Maximum number of failures to analyze (default: all)"
    )
    
    args = parser.parse_args()
    
    # Check API key
    if not AIConfig.is_configured():
        print("Error: GROQ_API_KEY environment variable not set.")
        print("Get your free API key at: https://console.groq.com")
        sys.exit(1)
    
    # Analyze failures
    analyzer = FailureAnalyzer()
    failures, analyses = analyzer.analyze_from_junit_xml(
        args.xml,
        args.output,
        args.total_tests,
        args.passed_tests,
        max_failures=args.max_failures
    )
    
    print(f"\n✅ Analysis complete! Found {len(failures)} failure(s).")
    print(f"📊 Report generated: {args.output}")


if __name__ == "__main__":
    main()

