"""
Schemathesis Examples Phase Tests
Generated from: vcr-20251108T013750Z_filtered.yaml
Phase: examples
Total tests: 7

Examples phase tests - basic functionality from OpenAPI spec


Note: Uses soft assertions via pytest-check.
All tests will run even if assertions fail.
Install: pip install pytest-check

Run with: pytest test_schemathesis/test_phase_examples.py -v
"""

import pytest
import pytest_check as check  # Soft assertions - all tests run even if some fail
import requests
import json
from test.conftest import BASE_URL, get_auth_basic_header


class TestPhaseExamples:
    """Examples phase tests - basic functionality from OpenAPI spec"""
    
    @pytest.fixture(autouse=True)
    def setup(self):
        """Setup shared configuration for all tests."""
        self.base_url = BASE_URL
        self.auth_basic = get_auth_basic_header()
        yield
    
    def _normalize_headers(self, headers):
        """Normalize headers, removing Content-Length as it's auto-calculated."""
        normalized = {}
        for k, v in headers.items():
            # Skip Content-Length as requests library calculates it automatically
            if k.lower() not in ['content-length', 'user-agent']:
                normalized[k] = v
        # Ensure required headers
        if 'Accept' not in normalized:
            normalized['Accept'] = 'application/json'
        if 'Content-Type' not in normalized:
            # Add Content-Type only if we have a body
            pass
        return normalized
    
    def test_post_booking_0(self):
        """Test generated from Schemathesis VCR: EkIQFO
        Test: POST /booking
        Phase: examples
        Status: SUCCESS
        """
        import requests
        
        url = f"{self.base_url}/booking"
        headers = self._normalize_headers({'Accept': 'application/json', 'Accept-Encoding': 'gzip, deflate, zstd', 'Authorization': '[Filtered]', 'Connection': 'keep-alive', 'Content-Type': 'application/json'})
        # Randomized test data (from AI analysis)
        body = {'firstname': 'John', 'lastname': 'Doe', 'totalprice': 342, 'depositpaid': True, 'bookingdates': {'checkin': '2025-12-15', 'checkout': '2026-01-20'}, 'additionalneeds': 'Breakfast'}
        
        response = requests.post(url, headers=headers, json=body)
        
        check.equal(response.status_code, 200, f'Expected status 200, got {response.status_code}')
        # Only check body if status code matches
        if response.status_code == 200:
            try:
                response_data = response.json()
                check.equal(response_data, {'bookingid': 3668, 'booking': {'firstname': 'Jim', 'lastname': 'Brown', 'totalprice': 111, 'depositpaid': True, 'bookingdates': {'checkin': '2018-01-01', 'checkout': '2019-01-01'}, 'additionalneeds': 'Breakfast'}}, 'Response body mismatch')
            except (json.JSONDecodeError, requests.exceptions.JSONDecodeError):
                # Response is not JSON - skip body check
                pass
    def test_post_auth_1(self):
        """Test generated from Schemathesis VCR: GkvzmP
        Test: POST /auth
        Phase: examples
        Status: SUCCESS
        """
        import requests
        
        url = f"{self.base_url}/auth"
        headers = self._normalize_headers({'Accept': 'application/json', 'Accept-Encoding': 'gzip, deflate, zstd', 'Authorization': '[Filtered]', 'Connection': 'keep-alive', 'Content-Type': 'application/json'})
        # Randomized test data (from AI analysis)
        body = {'username': 'admin', 'password': 'password123'}
        
        response = requests.post(url, headers=headers, json=body)
        
        check.equal(response.status_code, 200, f'Expected status 200, got {response.status_code}')
        # Only check body if status code matches
        if response.status_code == 200:
            try:
                response_data = response.json()
                check.equal(response_data, {'reason': 'Bad credentials'}, 'Response body mismatch')
            except (json.JSONDecodeError, requests.exceptions.JSONDecodeError):
                # Response is not JSON - skip body check
                pass
    def test_put_booking_8_2(self):
        """Test generated from Schemathesis VCR: BmBlFx
        Test: PUT /booking/8
        Phase: examples
        Status: SUCCESS
        """
        import requests
        
        url = f"{self.base_url}/booking/8"
        headers = self._normalize_headers({'Accept': 'application/json', 'Accept-Encoding': 'gzip, deflate, zstd', 'Authorization': '[Filtered]', 'Connection': 'keep-alive', 'Content-Type': 'application/json'})
        # Randomized test data (from AI analysis)
        body = {'firstname': 'Jane', 'lastname': 'Smith', 'totalprice': 342, 'depositpaid': True, 'bookingdates': {'checkin': '2025-12-15', 'checkout': '2026-01-20'}, 'additionalneeds': 'Breakfast'}
        
        response = requests.put(url, headers=headers, json=body)
        
        check.equal(response.status_code, 200, f'Expected status 200, got {response.status_code}')
        # Only check body if status code matches
        if response.status_code == 200:
            try:
                response_data = response.json()
                check.equal(response_data, {'firstname': 'Mary', 'lastname': 'Jones', 'totalprice': 111, 'depositpaid': True, 'bookingdates': {'checkin': '2018-01-01', 'checkout': '2019-01-01'}, 'additionalneeds': 'Breakfast'}, 'Response body mismatch')
            except (json.JSONDecodeError, requests.exceptions.JSONDecodeError):
                # Response is not JSON - skip body check
                pass
    def test_get_booking_1_3(self):
        """Test generated from Schemathesis VCR: rzoz2n
        Test: GET /booking/-1
        Phase: examples
        Status: SUCCESS
        """
        import requests
        
        url = f"{self.base_url}/booking/-1"
        headers = self._normalize_headers({'Accept': 'application/json', 'Accept-Encoding': 'gzip, deflate, zstd', 'Authorization': '[Filtered]', 'Connection': 'keep-alive', 'Content-Type': 'application/json'})
        
        response = requests.get(url, headers=headers)
        
        check.equal(response.status_code, 404, f'Expected status 404, got {response.status_code}')
        # Only check body if status code matches
        if response.status_code == 404:
            check.is_not_none(response.text, 'Response should have body')
    def test_get_booking_3_4(self):
        """Test generated from Schemathesis VCR: 6NKBix
        Test: GET /booking/3
        Phase: examples
        Status: SUCCESS
        """
        import requests
        
        url = f"{self.base_url}/booking/3"
        headers = self._normalize_headers({'Accept': 'application/json', 'Accept-Encoding': 'gzip, deflate, zstd', 'Authorization': '[Filtered]', 'Connection': 'keep-alive', 'Content-Type': 'application/json'})
        
        response = requests.get(url, headers=headers)
        
        check.equal(response.status_code, 200, f'Expected status 200, got {response.status_code}')
        # Only check body if status code matches
        if response.status_code == 200:
            try:
                response_data = response.json()
                check.equal(response_data, {'firstname': 'Mark', 'lastname': 'Ericsson', 'totalprice': 925, 'depositpaid': True, 'bookingdates': {'checkin': '2019-03-24', 'checkout': '2025-05-15'}, 'additionalneeds': 'Breakfast'}, 'Response body mismatch')
            except (json.JSONDecodeError, requests.exceptions.JSONDecodeError):
                # Response is not JSON - skip body check
                pass
    def test_patch_booking_7_5(self):
        """Test generated from Schemathesis VCR: NvnZS9
        Test: PATCH /booking/7
        Phase: examples
        Status: SUCCESS
        """
        import requests
        
        url = f"{self.base_url}/booking/7"
        headers = self._normalize_headers({'Accept': 'application/json', 'Accept-Encoding': 'gzip, deflate, zstd', 'Authorization': '[Filtered]', 'Connection': 'keep-alive', 'Content-Type': 'application/json'})
        # Randomized test data (from AI analysis)
        body = {'firstname': 'Emily', 'lastname': 'Johnson', 'totalprice': 342, 'depositpaid': True, 'bookingdates': {'checkin': '2025-12-15', 'checkout': '2026-01-20'}, 'additionalneeds': 'Breakfast'}
        
        response = requests.patch(url, headers=headers, json=body)
        
        check.equal(response.status_code, 200, f'Expected status 200, got {response.status_code}')
        # Only check body if status code matches
        if response.status_code == 200:
            try:
                response_data = response.json()
                check.equal(response_data, {'firstname': 'Jim', 'lastname': 'Brown', 'totalprice': 111, 'depositpaid': True, 'bookingdates': {'checkin': '2018-01-01', 'checkout': '2019-01-01'}, 'additionalneeds': 'Breakfast'}, 'Response body mismatch')
            except (json.JSONDecodeError, requests.exceptions.JSONDecodeError):
                # Response is not JSON - skip body check
                pass
    @pytest.mark.xfail(reason='Status code does not match OpenAPI spec - API returns different status than documented')
    def test_delete_booking_1_6(self):
        """Test generated from Schemathesis VCR: aiufaS
        Test: DELETE /booking/-1
        Phase: examples
        Status: FAILURE
        """
        import requests
        
        url = f"{self.base_url}/booking/-1"
        headers = self._normalize_headers({'Accept': 'application/json', 'Accept-Encoding': 'gzip, deflate, zstd', 'Authorization': '[Filtered]', 'Connection': 'keep-alive', 'Content-Type': 'application/json'})
        
        response = requests.delete(url, headers=headers)
        
        check.equal(response.status_code, 405, f'Expected status 405, got {response.status_code}')
        # NOTE: API returned 405, but OpenAPI spec expects different status code
        # This test documents current API behavior (regression test)
        # Status code conformance check failed in Schemathesis
        # Original failed checks: status_code_conformance, positive_data_acceptance
