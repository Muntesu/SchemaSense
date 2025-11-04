#!/usr/bin/env python3
"""
AI-Powered VCR Test Analysis Script

Analyzes Schemathesis VCR YAML output using Groq AI to determine which tests
bring value and should be kept vs which can be skipped.

This script:
1. Reads Schemathesis VCR YAML file
2. Sends test data to Groq for analysis
3. Gets structured recommendations for each test
4. Generates a filtered report that can be used to filter tests before conversion

Usage:
    python analyze_vcr_with_ai.py <vcr_file.yaml> [--output filtered_vcr.yaml] [--max-tests N]
"""

import sys
import json
import yaml
from pathlib import Path
from typing import Dict, List, Any, Optional
from dataclasses import dataclass, asdict
import argparse

# Add parent directory to path for imports
sys.path.insert(0, str(Path(__file__).parent.parent / "openapi-python" / "test"))

try:
    from groq import Groq
    from ai_config import AIConfig
except ImportError as e:
    print(f"Error importing dependencies: {e}")
    print("Please ensure groq and ai_config are available")
    sys.exit(1)


@dataclass
class TestAnalysis:
    """Analysis result for a single test."""
    test_id: str
    phase: str
    method: str
    path: str
    status_code: int
    should_keep: bool
    value_level: str  # "high", "medium", "low"
    reason: str
    issues: List[str]
    recommendations: List[str]
    randomized_request_data: Optional[Dict[str, str]] = None  # Python expressions for random data
    required_imports: Optional[List[str]] = None  # Imports needed for randomization


@dataclass
class VCRTest:
    """Represents a single test from VCR YAML."""
    test_id: str
    phase: str
    method: str
    path: str
    query_params: Dict[str, Any]
    headers: Dict[str, Any]
    body: Optional[Any]
    status_code: int
    response_body: Optional[Any]
    failed_checks: List[str]
    original_status: str  # "SUCCESS" or "FAILURE"


class VCRAnalyzer:
    """Analyzes VCR YAML files using Groq AI to determine test value."""
    
    def __init__(self):
        self.client = Groq(api_key=AIConfig.get_api_key())
        self.model = AIConfig.GROQ_MODEL
        self.analyses: Dict[str, TestAnalysis] = {}
    
    def load_vcr_file(self, vcr_file: Path) -> Dict[str, Any]:
        """Load and parse VCR YAML file."""
        if not vcr_file.exists():
            raise FileNotFoundError(f"VCR file not found: {vcr_file}")
        
        print(f"Loading VCR file: {vcr_file}")
        with open(vcr_file, 'r', encoding='utf-8') as f:
            vcr_data = yaml.safe_load(f)
        
        print(f"Loaded {len(vcr_data.get('http_interactions', []))} HTTP interactions")
        return vcr_data
    
    def extract_tests_from_vcr(self, vcr_data: Dict[str, Any]) -> List[VCRTest]:
        """Extract test information from VCR data."""
        tests = []
        interactions = vcr_data.get('http_interactions', [])
        
        for interaction in interactions:
            try:
                # Handle request/response - can be None in YAML
                request_raw = interaction.get('request')
                request = request_raw if request_raw is not None and isinstance(request_raw, dict) else {}
                
                response_raw = interaction.get('response')
                response = response_raw if response_raw is not None and isinstance(response_raw, dict) else {}
                
                # Extract test_id from interaction id field
                test_id = interaction.get('id', 'unknown')
                
                # Extract phase - can be at top level or nested in components.phase
                # Priority: top-level phase > components.phase
                phase = 'unknown'
                
                # First, try top-level phase (most common in newer Schemathesis versions)
                phase_obj = interaction.get('phase')
                if phase_obj is not None:
                    if isinstance(phase_obj, dict):
                        phase = phase_obj.get('name', 'unknown')
                    elif isinstance(phase_obj, str):
                        phase = phase_obj
                
                # Fallback: try components.phase (older Schemathesis versions or alternative format)
                if phase == 'unknown':
                    components = interaction.get('components')
                    if components is not None and isinstance(components, dict):
                        phase_obj = components.get('phase')
                        if phase_obj is not None:
                            if isinstance(phase_obj, dict):
                                phase = phase_obj.get('name', 'unknown')
                            elif isinstance(phase_obj, str):
                                phase = phase_obj
                
                # Extract status from interaction status field
                status = interaction.get('status', 'unknown')
                
                # Extract request details
                method = request.get('method', '')
                uri = request.get('uri', '')
                # Try to get base URL from config
                try:
                    from config import API_BASE_URL
                    base_url = API_BASE_URL
                except ImportError:
                    base_url = "https://restful-booker.herokuapp.com"
                path = uri.split('?')[0].replace(base_url, '')
                
                query_params = {}
                if '?' in uri:
                    from urllib.parse import parse_qs, urlparse
                    try:
                        parsed = urlparse(uri)
                        if parsed.query:  # Only parse if query string exists
                            try:
                                parsed_qs = parse_qs(parsed.query)
                                if parsed_qs is not None:  # Ensure parsed_qs is not None
                                    query_params = {k: v[0] if len(v) == 1 else v for k, v in parsed_qs.items()}
                            except (ValueError, TypeError):
                                # If parsing fails, leave empty
                                query_params = {}
                    except (ValueError, TypeError, AttributeError):
                        # If URL parsing fails, leave empty
                        query_params = {}
                
                # Handle headers - can be None in YAML
                headers_raw = request.get('headers')
                if headers_raw is None:
                    headers = {}
                elif isinstance(headers_raw, dict):
                    headers = headers_raw
                else:
                    headers = {}
                
                # Handle body - can be None in YAML
                body = None
                body_obj = request.get('body')
                if body_obj is not None:
                    if isinstance(body_obj, dict):
                        body = body_obj.get('string')
                    elif isinstance(body_obj, str):
                        body = body_obj
                if body:
                    try:
                        body = json.loads(body)
                    except (json.JSONDecodeError, TypeError):
                        body = str(body)
                
                # Extract response details
                status_code = 0
                status_obj = response.get('status')
                if status_obj is not None:
                    if isinstance(status_obj, dict):
                        code_str = status_obj.get('code', '0')
                        try:
                            status_code = int(code_str)
                        except (ValueError, TypeError):
                            status_code = 0
                    elif isinstance(status_obj, (int, str)):
                        try:
                            status_code = int(status_obj)
                        except (ValueError, TypeError):
                            status_code = 0
                
                response_body = None
                response_body_obj = response.get('body')
                if response_body_obj is not None:
                    if isinstance(response_body_obj, dict):
                        response_body = response_body_obj.get('string')
                        if response_body:
                            try:
                                response_body = json.loads(response_body)
                            except (json.JSONDecodeError, TypeError):
                                response_body = str(response_body)
                    elif isinstance(response_body_obj, str):
                        response_body = response_body_obj
                
                # Extract failed checks from checks list
                failed_checks = []
                checks = interaction.get('checks')
                if checks is not None and isinstance(checks, list):
                    failed_checks = [check.get('name', 'unknown') for check in checks if isinstance(check, dict) and check.get('status') == 'FAILURE']
                
                test = VCRTest(
                    test_id=test_id,
                    phase=phase,
                    method=method,
                    path=path,
                    query_params=query_params,
                    headers=headers,
                    body=body,
                    status_code=status_code,
                    response_body=response_body,
                    failed_checks=[str(fc) for fc in failed_checks],
                    original_status=status
                )
                tests.append(test)
            except Exception as e:
                test_id = interaction.get('id', 'unknown')
                print(f"Warning: Failed to extract test {test_id}: {e}")
                continue
        
        return tests
    
    def create_analysis_prompt(self, tests: List[VCRTest]) -> str:
        """Create comprehensive prompt for Groq to analyze tests."""
        
        # Group tests by phase for better context
        tests_by_phase = {}
        for test in tests:
            phase = test.phase
            if phase not in tests_by_phase:
                tests_by_phase[phase] = []
            tests_by_phase[phase].append(test)
        
        # Build test summary
        test_summaries = []
        for test in tests:
            summary = {
                'test_id': test.test_id,
                'phase': test.phase,
                'method': test.method,
                'path': test.path,
                'query_params': test.query_params if test.query_params else None,
                'status_code': test.status_code,
                'original_status': test.original_status,
                'failed_checks': test.failed_checks if test.failed_checks else None,
                'has_body': test.body is not None,
                'body_type': type(test.body).__name__ if test.body else None
            }
            # Truncate body if too large (more aggressive truncation for API limits)
            if test.body and isinstance(test.body, (dict, list)):
                body_str = json.dumps(test.body, ensure_ascii=False)
                # Get truncation length from config
                try:
                    from config import AI_BODY_PREVIEW_LENGTH
                    body_preview_length = AI_BODY_PREVIEW_LENGTH
                except ImportError:
                    body_preview_length = 200  # Default
                if len(body_str) > body_preview_length:
                    summary['body_preview'] = body_str[:body_preview_length] + "..."
                else:
                    summary['body_preview'] = body_str
            test_summaries.append(summary)
        
        prompt = f"""You are an expert API testing and quality assurance engineer with deep knowledge of:
- REST API design patterns and best practices
- Property-based testing (Schemathesis)
- Test value assessment and test optimization
- API contract validation
- Security testing requirements
- Test redundancy and coverage analysis

**Context:**
Schemathesis has generated {len(tests)} test cases from an OpenAPI specification for the Restful-Booker API.
These tests are organized into {len(tests_by_phase)} phases:
{chr(10).join(f"- {phase}: {len(tests_by_phase[phase])} tests" for phase in sorted(tests_by_phase.keys()))}

**Test Data:**
{json.dumps(test_summaries, indent=2, ensure_ascii=False)}

**Your Task:**
Analyze each test and determine:
1. **Should this test be kept?** (yes/no)
2. **Value level**: "high", "medium", or "low"
3. **Reason**: Brief explanation of why it should be kept or skipped
4. **Issues**: Any problems with the test (incorrect status codes, invalid expectations, etc.)
5. **Recommendations**: How to improve the test if kept

**Analysis Criteria:**

**High Value Tests (KEEP):**
- Tests that validate core API functionality (CRUD operations)
- Tests that validate authentication/authorization requirements
- Tests that validate proper error handling (404, 403, 400)
- Tests that validate query parameter filtering
- Tests that catch real API bugs or contract violations
- Tests that validate edge cases that are likely to occur in production

**Medium Value Tests (CONSIDER KEEPING):**
- Tests that validate boundary conditions
- Tests that validate input validation (but may be redundant)
- Tests that document API behavior (even if not ideal)

**Low Value Tests (SKIP):**
- Tests expecting 500 (server error) for invalid client input (should be 400)
- Tests expecting 200 (success) for clearly invalid input (indicates API validation gaps)
- Redundant tests (same scenario tested multiple times)
- Tests for unsupported HTTP methods (TRACE, etc.) unless security-focused
- Tests with malformed data that are unlikely to occur in real usage
- Tests that document API bugs rather than test correct behavior

**Special Considerations:**
- Tests expecting 500 for invalid input: These likely indicate API design issues (should return 400)
- Tests expecting 200 for invalid input: These indicate API validation gaps
- Fuzzing tests with random data: Evaluate if they catch real issues vs just generating noise
- Stateful tests: Look for redundancy - similar patterns repeated multiple times
- Coverage tests: Evaluate if they add unique coverage vs being redundant

**CRITICAL OUTPUT FORMAT REQUIREMENTS:**

You MUST respond with ONLY a JSON array. NO markdown, NO explanations, NO code blocks - just raw JSON.

Format: An array of objects, one per test. Each object MUST have these exact fields:

{{
  "test_id": "string (required)",
  "should_keep": true OR false (required - MUST be boolean, NOT string "yes"/"no"),
  "value_level": "high" OR "medium" OR "low" (required - string),
  "reason": "string explaining the decision (required)",
  "issues": ["list", "of", "issues"] (optional - empty array [] if none),
  "recommendations": ["list", "of", "recommendations"] (optional - empty array [] if none),
  "randomized_request_data": {{"field": "actual_value"}} (optional - only if test has request body)
}}

**Randomized Data Guidelines (for tests that should be kept with request bodies):**
- Provide ACTUAL random values (not code), as JSON values
- Randomize: IDs (e.g., 4521), names (e.g., "Michael", "Rodriguez"), prices (e.g., 378), dates (e.g., "2025-12-15"), booleans (true/false)
- Keep static: credentials (unless auth test), API endpoints, field names
- Ensure business logic: checkout > checkin, prices > 0, valid data types
- For POST /booking: randomize firstname, lastname, totalprice, depositpaid, dates, additionalneeds
- For PUT/PATCH: randomize same fields, keep booking ID static
- For DELETE/GET: no request body (omit randomized_request_data)
- For POST /auth: keep credentials static (username="admin", password="password123") unless testing auth failures

**CRITICAL**: Do NOT provide Python code. Provide actual values like {{"firstname": "John", "totalprice": 342}}

**CRITICAL - Response Assertions:**
When you randomize request data, the VCR response is INVALID! Add guidance in issues/recommendations:
- For POST/PUT/PATCH: Note "Response assertion invalid - bookingid is server-generated (don't assert 495), response should echo sent data (not VCR hardcoded values like 'Jim')"
- For GET: Note "Response cannot be validated against hardcoded values - data is dynamic"
- This is CRITICAL for every test you keep with randomized data!

**Important:**
- Be specific and technical in your analysis
- Consider the test's purpose in the context of the phase it belongs to
- Consider if the test catches real bugs vs just documents API quirks
- Consider redundancy - if multiple tests cover the same scenario, keep the best one
- Focus on tests that provide value for regression testing and API validation
- For tests with request bodies that should be kept, ALWAYS include randomized_request_data with actual values
- should_keep MUST be a boolean (true/false), NOT a string ("yes"/"no")

**EXAMPLE OUTPUT (showing correct format):**
[
  {{
    "test_id": "abc123",
    "should_keep": false,
    "value_level": "low",
    "reason": "Test expects 500 for invalid input",
    "issues": ["Should return 400, not 500"],
    "recommendations": []
  }},
  {{
    "test_id": "auth_test",
    "should_keep": true,
    "value_level": "high",
    "reason": "Validates authentication",
    "issues": [],
    "recommendations": ["Keep for regression testing"],
    "randomized_request_data": {{
      "username": "admin",
      "password": "password123"
    }}
  }},
  {{
    "test_id": "booking_test",
    "should_keep": true,
    "value_level": "high",
    "reason": "Validates core CRUD functionality",
    "issues": [],
    "recommendations": ["Keep for regression testing"],
    "randomized_request_data": {{
      "firstname": "Michael",
      "lastname": "Rodriguez",
      "totalprice": 378,
      "depositpaid": true,
      "bookingdates": {{
        "checkin": "2025-12-15",
        "checkout": "2026-01-20"
      }},
      "additionalneeds": "Breakfast"
    }}
  }}
]

**CRITICAL REMINDERS:**
- Provide actual JSON values, NOT Python code
- Example: "firstname": "Michael" (not "faker.first_name()")
- Example: "totalprice": 378 (not "random.randint(50, 500)")
- Strings should be JSON strings: "admin", numbers should be JSON numbers: 378, booleans should be JSON booleans: true/false

**Now analyze all {len(tests)} tests and respond with ONLY the JSON array:**"""
        
        return prompt
    
    def analyze_tests(self, tests: List[VCRTest], max_tests: Optional[int] = None, verbose: bool = True, batch_size: int = 10) -> Dict[str, TestAnalysis]:
        """Analyze tests using Groq AI with automatic batching for large requests."""
        
        # Limit number of tests if specified (for API cost management)
        if max_tests and max_tests > 0:
            tests_to_analyze = tests[:max_tests]
            if verbose:
                print(f"Analyzing first {len(tests_to_analyze)} of {len(tests)} tests (limited by --max-tests)")
        else:
            tests_to_analyze = tests
        
        if verbose:
            print(f"\nAnalyzing {len(tests_to_analyze)} tests with Groq AI...")
            print(f"Model: {self.model}")
            print(f"API Key: {'*' * 10}{AIConfig.get_api_key()[-4:] if AIConfig.get_api_key() else 'NOT SET'}")
        
        # Groq free tier limit is ~6000 tokens per request
        # Use batching to stay under limit
        try:
            from config import AI_MAX_TOKENS_PER_REQUEST
            MAX_TOKENS_PER_REQUEST = AI_MAX_TOKENS_PER_REQUEST
        except ImportError:
            MAX_TOKENS_PER_REQUEST = 5000  # Conservative limit
        
        # Process in batches (using while loop to handle dynamic batch size changes)
        batch_idx = 0
        batch_num = 0
        
        while batch_idx < len(tests_to_analyze):
            batch_tests = tests_to_analyze[batch_idx:batch_idx + batch_size]
            batch_num += 1
            
            # Calculate remaining batches dynamically
            remaining_tests = len(tests_to_analyze) - batch_idx
            estimated_remaining_batches = (remaining_tests + batch_size - 1) // batch_size
            
            if verbose:
                print(f"\nProcessing batch {batch_num} ({len(batch_tests)} tests, ~{estimated_remaining_batches} batches remaining)...")
            
            # Create prompt for this batch
            prompt = self.create_analysis_prompt(batch_tests)
            
            # Estimate token count (rough: 1 token ≈ 4 characters)
            estimated_tokens = len(prompt) // 4
            if verbose:
                print(f"  Estimated tokens: ~{estimated_tokens}")
            
            # If still too large, reduce batch size recursively
            if estimated_tokens > MAX_TOKENS_PER_REQUEST:
                print(f"  Warning: Batch too large ({estimated_tokens} tokens). Reducing batch size...")
                smaller_batch = max(1, batch_size // 2)
                return self.analyze_tests(tests, max_tests, verbose, batch_size=smaller_batch)
            
            try:
                if verbose:
                    print("  Sending request to Groq...")
                
                # Call Groq API
                response = self.client.chat.completions.create(
                    model=self.model,
                    messages=[
                        {
                            "role": "system",
                            "content": """You are an expert API testing and quality assurance engineer. 
You analyze test cases and determine their value for regression testing and API validation.
You provide structured, technical analysis with clear recommendations.
For tests that should be kept, you provide Python expressions for generating randomized test data to avoid hardcoded values.
You MUST respond with valid JSON only, no markdown, no explanations outside the JSON."""
                        },
                        {
                            "role": "user",
                            "content": prompt
                        }
                    ],
                    temperature=0.1,  # Low temperature for consistent, structured output
                    max_tokens=16000  # High token limit for comprehensive analysis with randomization data
                )
                
                if verbose:
                    print("  ✓ Response received from Groq")
                
                # Parse response
                analysis_text = response.choices[0].message.content
                
                # Try to parse as JSON
                try:
                    # Groq might return JSON wrapped in markdown code blocks
                    if analysis_text.strip().startswith('```'):
                        # Extract JSON from code block
                        lines = analysis_text.strip().split('\n')
                        json_lines = []
                        in_json = False
                        for line in lines:
                            if line.strip().startswith('```'):
                                if not in_json:
                                    in_json = True
                                else:
                                    break
                            elif in_json:
                                json_lines.append(line)
                        analysis_text = '\n'.join(json_lines)
                    
                    # Clean up common issues: convert "yes"/"no" strings to booleans
                    analysis_text = analysis_text.replace('"should_keep": "yes"', '"should_keep": true')
                    analysis_text = analysis_text.replace('"should_keep": "no"', '"should_keep": false')
                    
                    analysis_data = json.loads(analysis_text)
                    
                    # Handle both single object and array formats
                    if isinstance(analysis_data, dict):
                        if 'tests' in analysis_data:
                            analyses_list = analysis_data['tests']
                        elif 'results' in analysis_data:
                            analyses_list = analysis_data['results']
                        else:
                            # Assume it's a single analysis or the whole thing
                            analyses_list = [analysis_data] if 'test_id' in analysis_data else []
                    elif isinstance(analysis_data, list):
                        analyses_list = analysis_data
                    else:
                        raise ValueError(f"Unexpected analysis data format: {type(analysis_data)}")
                    
                    # Convert to TestAnalysis objects
                    for analysis_dict in analyses_list:
                        test_id = analysis_dict.get('test_id')
                        if not test_id:
                            continue
                        
                        # Find corresponding test for additional context
                        test = next((t for t in batch_tests if t.test_id == test_id), None)
                        
                        # Extract randomized data if present
                        randomized_data = analysis_dict.get('randomized_request_data')
                        required_imports = analysis_dict.get('required_imports', [])
                        
                        # Clean up randomized_data - remove description/note/example fields if present
                        if randomized_data and isinstance(randomized_data, dict):
                            # If it has description/note/example, it's in the template format
                            # Extract the actual data (everything except those meta fields)
                            cleaned_data = {k: v for k, v in randomized_data.items() 
                                          if k not in ['description', 'note', 'example']}
                            # If all that's left is empty or only meta fields, set to None
                            if not cleaned_data or all(k in ['description', 'note', 'example'] for k in randomized_data.keys()):
                                randomized_data = None
                            else:
                                randomized_data = cleaned_data
                        
                        analysis = TestAnalysis(
                            test_id=test_id,
                            phase=test.phase if test else 'unknown',
                            method=test.method if test else 'unknown',
                            path=test.path if test else 'unknown',
                            status_code=test.status_code if test else 0,
                            should_keep=analysis_dict.get('should_keep', False),
                            value_level=analysis_dict.get('value_level', 'low'),
                            reason=analysis_dict.get('reason', 'No reason provided'),
                            issues=analysis_dict.get('issues', []),
                            recommendations=analysis_dict.get('recommendations', []),
                            randomized_request_data=randomized_data,
                            required_imports=required_imports if required_imports else None
                        )
                        self.analyses[test_id] = analysis
                    
                    if verbose:
                        print(f"  ✓ Batch {batch_num} complete: {len(analyses_list)} tests analyzed")
                    
                except json.JSONDecodeError as e:
                    print(f"  Error: Failed to parse Groq response as JSON: {e}")
                    print(f"  Response length: {len(analysis_text)} characters")
                    print(f"  Response preview (first 1000 chars):\n{analysis_text[:1000]}")
                    print(f"  Response preview (last 500 chars):\n{analysis_text[-500:]}")
                    
                    # Try to extract valid test objects from incomplete JSON
                    import re
                    
                    # Strategy: Extract individual complete test objects, even if array is incomplete
                    # Pattern: { "test_id": "...", ... }
                    test_objects = []
                    
                    # Find all complete test objects in the response
                    # Look for patterns like: { "test_id": "xxx", ... } followed by , or ]
                    pattern = r'\{\s*"test_id"\s*:\s*"[^"]+?"[^}]*?\}'
                    matches = re.finditer(pattern, analysis_text, re.DOTALL)
                    
                    for match in matches:
                        try:
                            obj_text = match.group(0)
                            # Clean up common issues
                            obj_text = obj_text.replace('"should_keep": "yes"', '"should_keep": true')
                            obj_text = obj_text.replace('"should_keep": "no"', '"should_keep": false')
                            
                            # Try to parse this object
                            test_obj = json.loads(obj_text)
                            test_objects.append(test_obj)
                        except json.JSONDecodeError:
                            # Skip malformed objects
                            continue
                    
                    if test_objects:
                        if verbose:
                            print(f"  ⚠️  Response truncated by API - recovered {len(test_objects)}/{len(batch_tests)} tests")
                            print(f"  💡 Continuing with partial results...")
                        analyses_list = test_objects
                        
                        # If we got less than 80% of tests, reduce batch size for next iteration
                        if len(test_objects) < len(batch_tests) * 0.8 and batch_size > 5:
                            new_batch_size = max(5, batch_size // 2)
                            if verbose:
                                print(f"  💡 Will reduce batch size to {new_batch_size} for remaining batches")
                            batch_size = new_batch_size
                        # Don't raise - continue with what we got
                    else:
                        print("  ❌ Could not extract any valid test objects from response")
                        print(f"  Response appears to be truncated or malformed")
                        raise e
            
            except Exception as e:
                error_msg = str(e)
                if '413' in error_msg or 'too large' in error_msg.lower() or 'tokens' in error_msg.lower():
                    print(f"  Error: Request too large. Reducing batch size and retrying...")
                    # Recursively retry with smaller batch
                    smaller_batch = max(1, batch_size // 2)
                    return self.analyze_tests(tests, max_tests, verbose, batch_size=smaller_batch)
                else:
                    print(f"  Error during AI analysis: {e}")
                    import traceback
                    traceback.print_exc()
                    raise
            
            # Move to next batch
            batch_idx += batch_size
        
        # Final summary
        if verbose:
            kept = sum(1 for a in self.analyses.values() if a.should_keep)
            print(f"\n✓ Analysis complete: {len(self.analyses)} tests analyzed")
            print(f"  - Keep: {kept} tests")
            print(f"  - Skip: {len(self.analyses) - kept} tests")
        
        return self.analyses
    
    def generate_report(self, output_file: Optional[Path] = None) -> str:
        """Generate analysis report."""
        kept_tests = [a for a in self.analyses.values() if a.should_keep]
        skipped_tests = [a for a in self.analyses.values() if not a.should_keep]
        
        report = []
        report.append("=" * 80)
        report.append("VCR Test Analysis Report - Generated by Groq AI")
        report.append("=" * 80)
        report.append("")
        report.append(f"Total Tests Analyzed: {len(self.analyses)}")
        report.append(f"Tests to Keep: {len(kept_tests)} ({len(kept_tests)/len(self.analyses)*100:.1f}%)")
        report.append(f"Tests to Skip: {len(skipped_tests)} ({len(skipped_tests)/len(self.analyses)*100:.1f}%)")
        report.append("")
        
        # Summary by value level
        by_value = {}
        for analysis in self.analyses.values():
            level = analysis.value_level
            if level not in by_value:
                by_value[level] = {'keep': 0, 'skip': 0}
            if analysis.should_keep:
                by_value[level]['keep'] += 1
            else:
                by_value[level]['skip'] += 1
        
        report.append("Summary by Value Level:")
        for level in ['high', 'medium', 'low']:
            if level in by_value:
                keep = by_value[level]['keep']
                skip = by_value[level]['skip']
                total = keep + skip
                report.append(f"  {level.capitalize()}: {total} tests ({keep} keep, {skip} skip)")
        report.append("")
        
        # Tests to keep
        report.append("-" * 80)
        report.append("TESTS TO KEEP")
        report.append("-" * 80)
        for analysis in sorted(kept_tests, key=lambda x: (x.value_level, x.test_id)):
            report.append(f"\n[{analysis.value_level.upper()}] {analysis.test_id}")
            report.append(f"  Phase: {analysis.phase} | Method: {analysis.method} | Path: {analysis.path}")
            report.append(f"  Status Code: {analysis.status_code}")
            report.append(f"  Reason: {analysis.reason}")
            if analysis.issues:
                report.append(f"  Issues: {', '.join(analysis.issues)}")
            if analysis.recommendations:
                report.append(f"  Recommendations: {', '.join(analysis.recommendations)}")
            if analysis.randomized_request_data:
                report.append(f"  Randomized Data: {json.dumps(analysis.randomized_request_data, indent=4)}")
            if analysis.required_imports:
                report.append(f"  Required Imports: {', '.join(analysis.required_imports)}")
        
        # Tests to skip
        report.append("")
        report.append("-" * 80)
        report.append("TESTS TO SKIP")
        report.append("-" * 80)
        for analysis in sorted(skipped_tests, key=lambda x: (x.value_level, x.test_id)):
            report.append(f"\n[{analysis.value_level.upper()}] {analysis.test_id}")
            report.append(f"  Phase: {analysis.phase} | Method: {analysis.method} | Path: {analysis.path}")
            report.append(f"  Reason: {analysis.reason}")
            if analysis.issues:
                report.append(f"  Issues: {', '.join(analysis.issues)}")
        
        report_text = '\n'.join(report)
        
        if output_file:
            output_file.parent.mkdir(parents=True, exist_ok=True)
            output_file.write_text(report_text)
            print(f"\nReport saved to: {output_file}")
        
        return report_text
    
    def generate_filtered_vcr(self, original_vcr: Dict[str, Any], output_file: Path) -> Dict[str, Any]:
        """Generate filtered VCR YAML with only tests that should be kept."""
        kept_test_ids = {a.test_id for a in self.analyses.values() if a.should_keep}
        
        # Filter interactions
        filtered_interactions = []
        for interaction in original_vcr.get('http_interactions', []):
            test_id = interaction.get('id', '')
            if test_id in kept_test_ids:
                filtered_interactions.append(interaction)
        
        # Create filtered VCR
        filtered_vcr = original_vcr.copy()
        filtered_vcr['http_interactions'] = filtered_interactions
        
        # Save filtered VCR
        output_file.parent.mkdir(parents=True, exist_ok=True)
        with open(output_file, 'w', encoding='utf-8') as f:
            yaml.dump(filtered_vcr, f, default_flow_style=False, allow_unicode=True)
        
        print(f"Filtered VCR saved to: {output_file}")
        print(f"  Original: {len(original_vcr.get('http_interactions', []))} tests")
        print(f"  Filtered: {len(filtered_interactions)} tests")
        
        return filtered_vcr
    
    def save_analysis_json(self, output_file: Path):
        """Save analysis results as JSON for programmatic use."""
        analysis_data = {
            'total_tests': len(self.analyses),
            'tests_to_keep': sum(1 for a in self.analyses.values() if a.should_keep),
            'tests_to_skip': sum(1 for a in self.analyses.values() if not a.should_keep),
            'analyses': {test_id: asdict(analysis) for test_id, analysis in self.analyses.items()}
        }
        
        output_file.parent.mkdir(parents=True, exist_ok=True)
        with open(output_file, 'w', encoding='utf-8') as f:
            json.dump(analysis_data, f, indent=2, ensure_ascii=False)
        
        print(f"Analysis JSON saved to: {output_file}")


def main():
    """CLI entry point."""
    parser = argparse.ArgumentParser(
        description="Analyze Schemathesis VCR YAML using Groq AI to determine test value"
    )
    parser.add_argument(
        'vcr_file',
        type=Path,
        help='Path to Schemathesis VCR YAML file'
    )
    parser.add_argument(
        '--output',
        type=Path,
        help='Path to save filtered VCR YAML (default: <vcr_file>_filtered.yaml)'
    )
    parser.add_argument(
        '--report',
        type=Path,
        help='Path to save analysis report (default: <vcr_file>_analysis_report.txt)'
    )
    parser.add_argument(
        '--json',
        type=Path,
        help='Path to save analysis JSON (default: <vcr_file>_analysis.json)'
    )
    parser.add_argument(
        '--max-tests',
        type=int,
        default=None,
        help='Maximum number of tests to analyze (for cost management, default: all)'
    )
    parser.add_argument(
        '--no-filter',
        action='store_true',
        help='Only generate report, do not create filtered VCR'
    )
    parser.add_argument(
        '--batch-size',
        type=int,
        default=20,
        help='Number of tests per batch (default: 20, auto-reduced if request too large)'
    )
    
    args = parser.parse_args()
    
    # Check API key
    try:
        AIConfig.get_api_key()
    except ValueError as e:
        print(f"Error: {e}")
        print("Please configure Groq API key in ai_config.py or set GROQ_API_KEY environment variable")
        sys.exit(1)
    
    # Default output paths
    if not args.output:
        args.output = args.vcr_file.parent / f"{args.vcr_file.stem}_filtered.yaml"
    if not args.report:
        args.report = args.vcr_file.parent / f"{args.vcr_file.stem}_analysis_report.txt"
    if not args.json:
        args.json = args.vcr_file.parent / f"{args.vcr_file.stem}_analysis.json"
    
    # Analyze
    try:
        analyzer = VCRAnalyzer()
        
        # Load VCR
        vcr_data = analyzer.load_vcr_file(args.vcr_file)
        
        # Extract tests
        tests = analyzer.extract_tests_from_vcr(vcr_data)
        print(f"Extracted {len(tests)} tests from VCR")
        
        # Analyze with AI (analyses stored internally in analyzer)
        analyzer.analyze_tests(tests, max_tests=args.max_tests, verbose=True, batch_size=args.batch_size)
        
        # Generate report
        report = analyzer.generate_report(output_file=args.report)
        print("\n" + "=" * 80)
        print(report[:2000])  # Print first part of report
        print("...")
        print("=" * 80)
        
        # Save JSON
        analyzer.save_analysis_json(args.json)
        
        # Generate filtered VCR
        if not args.no_filter:
            analyzer.generate_filtered_vcr(vcr_data, args.output)
            print(f"\n✓ Analysis complete! Use filtered VCR: {args.output}")
        else:
            print(f"\n✓ Analysis complete! Report saved to: {args.report}")
        
    except Exception as e:
        print(f"Error: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)


if __name__ == "__main__":
    main()

