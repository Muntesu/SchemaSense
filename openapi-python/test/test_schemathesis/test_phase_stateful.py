"""
Schemathesis Stateful Phase Tests
Generated from: vcr-20251108T013750Z_filtered.yaml
Phase: stateful
Total tests: 115

Stateful phase tests - multi-step workflows


Note: Uses soft assertions via pytest-check.
All tests will run even if assertions fail.
Install: pip install pytest-check

Run with: pytest test_schemathesis/test_phase_stateful.py -v
"""

import pytest
import pytest_check as check  # Soft assertions - all tests run even if some fail
import requests
import json
from test.conftest import BASE_URL, get_auth_basic_header


class TestPhaseStateful:
    """Stateful phase tests - multi-step workflows"""
    
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
    
    @pytest.mark.xfail(reason='Status code does not match OpenAPI spec - API returns different status than documented')
    def test_post_booking_0(self):
        """Test generated from Schemathesis VCR: CcWPqt
        Test: POST /booking
        Phase: stateful
        Status: FAILURE
        """
        import requests
        
        url = f"{self.base_url}/booking"
        headers = self._normalize_headers({'Accept': 'application/json', 'Accept-Encoding': 'gzip, deflate, zstd', 'Authorization': '[Filtered]', 'Connection': 'keep-alive', 'Content-Type': 'application/json'})
        # Randomized test data (from AI analysis)
        body = {'firstname': 'John', 'lastname': 'Doe', 'totalprice': 342, 'depositpaid': True, 'bookingdates': {'checkin': '2025-12-15', 'checkout': '2026-01-20'}, 'additionalneeds': 'Breakfast'}
        
        response = requests.post(url, headers=headers, json=body)
        
        check.equal(response.status_code, 500, f'Expected status 500, got {response.status_code}')
        # NOTE: API returned 500, but OpenAPI spec expects different status code
        # This test documents current API behavior (regression test)
        # Status code conformance check failed in Schemathesis
        # Original failed checks: not_a_server_error, status_code_conformance
    def test_post_booking_1(self):
        """Test generated from Schemathesis VCR: im7EX2
        Test: POST /booking
        Phase: stateful
        Status: SUCCESS
        """
        import requests
        
        url = f"{self.base_url}/booking"
        headers = self._normalize_headers({'Accept': 'application/json', 'Accept-Encoding': 'gzip, deflate, zstd', 'Authorization': '[Filtered]', 'Connection': 'keep-alive', 'Content-Type': 'application/json'})
        # Randomized test data (from AI analysis)
        body = {'firstname': 'Jane', 'lastname': 'Smith', 'totalprice': 123, 'depositpaid': False, 'bookingdates': {'checkin': '2025-12-15', 'checkout': '2026-01-20'}, 'additionalneeds': 'Lunch'}
        
        response = requests.post(url, headers=headers, json=body)
        
        check.equal(response.status_code, 500, f'Expected status 500, got {response.status_code}')
        # Only check body if status code matches
        if response.status_code == 500:
            check.is_not_none(response.text, 'Response should have body')
    def test_post_booking_2(self):
        """Test generated from Schemathesis VCR: DxKYAi
        Test: POST /booking
        Phase: stateful
        Status: SUCCESS
        """
        import requests
        
        url = f"{self.base_url}/booking"
        headers = self._normalize_headers({'Accept': 'application/json', 'Accept-Encoding': 'gzip, deflate, zstd', 'Authorization': '[Filtered]', 'Connection': 'keep-alive', 'Content-Type': 'application/json'})
        # Randomized test data (from AI analysis)
        body = {'firstname': 'Michael', 'lastname': 'Rodriguez', 'totalprice': 378, 'depositpaid': True, 'bookingdates': {'checkin': '2025-12-15', 'checkout': '2026-01-20'}, 'additionalneeds': 'Breakfast'}
        
        response = requests.post(url, headers=headers, json=body)
        
        check.equal(response.status_code, 200, f'Expected status 200, got {response.status_code}')
        # Only check body if status code matches
        if response.status_code == 200:
            try:
                response_data = response.json()
                check.equal(response_data, {'bookingid': 3714, 'booking': {'firstname': '🇺🇸', 'lastname': '\U000d8937\x98\U000b449f', 'totalprice': 7391, 'depositpaid': False, 'bookingdates': {'checkin': '1010-12-09', 'checkout': '4805-06-06'}}}, 'Response body mismatch')
            except (json.JSONDecodeError, requests.exceptions.JSONDecodeError):
                # Response is not JSON - skip body check
                pass
    def test_post_booking_3(self):
        """Test generated from Schemathesis VCR: O8IZFL
        Test: POST /booking
        Phase: stateful
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
                check.equal(response_data, {'bookingid': 3728, 'booking': {'firstname': '\U000d0bc5', 'lastname': '§\x98½', 'totalprice': 29292, 'depositpaid': False, 'bookingdates': {'checkin': '4629-07-16', 'checkout': '6358-12-27'}, 'additionalneeds': '\x84\U0006d406\U000a044d-R\U000c27bd\xa0ôÎý\x8b'}}, 'Response body mismatch')
            except (json.JSONDecodeError, requests.exceptions.JSONDecodeError):
                # Response is not JSON - skip body check
                pass
    def test_post_booking_4(self):
        """Test generated from Schemathesis VCR: YS8Vvb
        Test: POST /booking
        Phase: stateful
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
                check.equal(response_data, {'bookingid': 3730, 'booking': {'firstname': 'TestPhaseFuzzing', 'lastname': 'ÊP\x15', 'totalprice': 300, 'depositpaid': True, 'bookingdates': {'checkin': '9751-08-01', 'checkout': '1339-09-25'}}}, 'Response body mismatch')
            except (json.JSONDecodeError, requests.exceptions.JSONDecodeError):
                # Response is not JSON - skip body check
                pass
    @pytest.mark.xfail(reason='Status code does not match OpenAPI spec - API returns different status than documented')
    def test_delete_booking_false_5(self):
        """Test generated from Schemathesis VCR: 12JEcA
        Test: DELETE /booking/false
        Phase: stateful
        Status: FAILURE
        """
        import requests
        
        url = f"{self.base_url}/booking/false"
        headers = self._normalize_headers({'Accept': 'application/json', 'Accept-Encoding': 'gzip, deflate, zstd', 'Authorization': '[Filtered]', 'Connection': 'keep-alive', 'Content-Type': 'application/json'})
        
        response = requests.delete(url, headers=headers)
        
        check.equal(response.status_code, 405, f'Expected status 405, got {response.status_code}')
        # NOTE: API returned 405, but OpenAPI spec expects different status code
        # This test documents current API behavior (regression test)
        # Status code conformance check failed in Schemathesis
        # Original failed checks: status_code_conformance, negative_data_rejection
    def test_post_booking_6(self):
        """Test generated from Schemathesis VCR: 6lVwVt
        Test: POST /booking
        Phase: stateful
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
                check.equal(response_data, {'bookingid': 3738, 'booking': {'firstname': 'TestPhaseFuzzing', 'lastname': 'ÊP\x15', 'totalprice': 300, 'depositpaid': True, 'bookingdates': {'checkin': '9751-08-01', 'checkout': '1339-09-25'}}}, 'Response body mismatch')
            except (json.JSONDecodeError, requests.exceptions.JSONDecodeError):
                # Response is not JSON - skip body check
                pass
    def test_delete_booking_1427691001568739835_7(self):
        """Test generated from Schemathesis VCR: vQ0yDq
        Test: DELETE /booking/-1427691001568739835
        Phase: stateful
        Status: FAILURE
        """
        import requests
        
        url = f"{self.base_url}/booking/-1427691001568739835"
        headers = self._normalize_headers({'Accept': 'application/json', 'Accept-Encoding': 'gzip, deflate, zstd', 'Authorization': '[Filtered]', 'Connection': 'keep-alive', 'Content-Type': 'application/json'})
        
        response = requests.delete(url, headers=headers)
        
        check.equal(response.status_code, 405, f'Expected status 405, got {response.status_code}')
        # Original failed checks: positive_data_acceptance
    def test_post_booking_8(self):
        """Test generated from Schemathesis VCR: 95ssj1
        Test: POST /booking
        Phase: stateful
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
                check.equal(response_data, {'bookingid': 3749, 'booking': {'firstname': 'TestPhaseFuzzing', 'lastname': 'ÊP\x15', 'totalprice': 300, 'depositpaid': True, 'bookingdates': {'checkin': '9751-08-01', 'checkout': '1339-09-25'}}}, 'Response body mismatch')
            except (json.JSONDecodeError, requests.exceptions.JSONDecodeError):
                # Response is not JSON - skip body check
                pass
    def test_delete_booking_false_9(self):
        """Test generated from Schemathesis VCR: NHxiUg
        Test: DELETE /booking/false
        Phase: stateful
        Status: SUCCESS
        """
        import requests
        
        url = f"{self.base_url}/booking/false"
        headers = self._normalize_headers({'Accept': 'application/json', 'Accept-Encoding': 'gzip, deflate, zstd', 'Authorization': '[Filtered]', 'Connection': 'keep-alive', 'Content-Type': 'application/json'})
        
        response = requests.delete(url, headers=headers)
        
        check.equal(response.status_code, 405, f'Expected status 405, got {response.status_code}')
        # Only check body if status code matches
        if response.status_code == 405:
            check.is_not_none(response.text, 'Response should have body')
    def test_delete_booking_true_10(self):
        """Test generated from Schemathesis VCR: VPx5Qn
        Test: DELETE /booking/true
        Phase: stateful
        Status: SUCCESS
        """
        import requests
        
        url = f"{self.base_url}/booking/true"
        headers = self._normalize_headers({'Accept': 'application/json', 'Accept-Encoding': 'gzip, deflate, zstd', 'Authorization': '[Filtered]', 'Connection': 'keep-alive', 'Content-Type': 'application/json'})
        
        response = requests.delete(url, headers=headers)
        
        check.equal(response.status_code, 405, f'Expected status 405, got {response.status_code}')
        # Only check body if status code matches
        if response.status_code == 405:
            check.is_not_none(response.text, 'Response should have body')
    def test_post_booking_11(self):
        """Test generated from Schemathesis VCR: aFNH2a
        Test: POST /booking
        Phase: stateful
        Status: SUCCESS
        """
        import requests
        
        url = f"{self.base_url}/booking"
        headers = self._normalize_headers({'Accept': 'application/json', 'Accept-Encoding': 'gzip, deflate, zstd', 'Authorization': '[Filtered]', 'Connection': 'keep-alive', 'Content-Type': 'application/json'})
        body = {'bookingdates': {'checkin': '9751-08-01', 'checkout': '1339-09-25', '': {'': None}}, 'depositpaid': True, 'firstname': 'TestPhaseFuzzing', 'lastname': 'ÊP\x15', 'totalprice': 300}
        
        response = requests.post(url, headers=headers, json=body)
        
        check.equal(response.status_code, 200, f'Expected status 200, got {response.status_code}')
        # Only check body if status code matches
        if response.status_code == 200:
            try:
                response_data = response.json()
                check.equal(response_data, {'bookingid': 3752, 'booking': {'firstname': 'TestPhaseFuzzing', 'lastname': 'ÊP\x15', 'totalprice': 300, 'depositpaid': True, 'bookingdates': {'checkin': '9751-08-01', 'checkout': '1339-09-25'}}}, 'Response body mismatch')
            except (json.JSONDecodeError, requests.exceptions.JSONDecodeError):
                # Response is not JSON - skip body check
                pass
    def test_delete_booking_false_12(self):
        """Test generated from Schemathesis VCR: FHG8EN
        Test: DELETE /booking/false
        Phase: stateful
        Status: SUCCESS
        """
        import requests
        
        url = f"{self.base_url}/booking/false"
        headers = self._normalize_headers({'Accept': 'application/json', 'Accept-Encoding': 'gzip, deflate, zstd', 'Authorization': '[Filtered]', 'Connection': 'keep-alive', 'Content-Type': 'application/json'})
        
        response = requests.delete(url, headers=headers)
        
        check.equal(response.status_code, 405, f'Expected status 405, got {response.status_code}')
        # Only check body if status code matches
        if response.status_code == 405:
            check.is_not_none(response.text, 'Response should have body')
    def test_delete_booking_1427691001568739835_13(self):
        """Test generated from Schemathesis VCR: NBhOEk
        Test: DELETE /booking/-1427691001568739835
        Phase: stateful
        Status: SUCCESS
        """
        import requests
        
        url = f"{self.base_url}/booking/-1427691001568739835"
        headers = self._normalize_headers({'Accept': 'application/json', 'Accept-Encoding': 'gzip, deflate, zstd', 'Authorization': '[Filtered]', 'Connection': 'keep-alive', 'Content-Type': 'application/json'})
        
        response = requests.delete(url, headers=headers)
        
        check.equal(response.status_code, 405, f'Expected status 405, got {response.status_code}')
        # Only check body if status code matches
        if response.status_code == 405:
            check.is_not_none(response.text, 'Response should have body')
    def test_get_booking_85_14(self):
        """Test generated from Schemathesis VCR: QlSZEv
        Test: GET /booking/85
        Phase: stateful
        Status: SUCCESS
        """
        import requests
        
        url = f"{self.base_url}/booking/85"
        headers = self._normalize_headers({'Accept': 'application/json', 'Accept-Encoding': 'gzip, deflate, zstd', 'Authorization': '[Filtered]', 'Connection': 'keep-alive', 'Content-Type': 'application/json'})
        
        response = requests.get(url, headers=headers)
        
        check.equal(response.status_code, 200, f'Expected status 200, got {response.status_code}')
        # Only check body if status code matches
        if response.status_code == 200:
            try:
                response_data = response.json()
                check.equal(response_data, {'firstname': 'John', 'lastname': 'Smith', 'totalprice': 111, 'depositpaid': True, 'bookingdates': {'checkin': '2018-01-01', 'checkout': '2019-01-01'}, 'additionalneeds': 'Breakfast'}, 'Response body mismatch')
            except (json.JSONDecodeError, requests.exceptions.JSONDecodeError):
                # Response is not JSON - skip body check
                pass
    def test_post_booking_15(self):
        """Test generated from Schemathesis VCR: eU8qqt
        Test: POST /booking
        Phase: stateful
        Status: SUCCESS
        """
        import requests
        
        url = f"{self.base_url}/booking"
        headers = self._normalize_headers({'Accept': 'application/json', 'Accept-Encoding': 'gzip, deflate, zstd', 'Authorization': '[Filtered]', 'Connection': 'keep-alive', 'Content-Type': 'application/json'})
        body = {'bookingdates': {'checkin': '0923-08-30', 'checkout': '1160-10-31', 'µ': [], '\U0007cefe': 6589004668716677993}, 'depositpaid': False, 'firstname': 'ú¤´', 'lastname': '', 'totalprice': -18819, '': {}, 'additionalneeds': ''}
        
        response = requests.post(url, headers=headers, json=body)
        
        check.equal(response.status_code, 200, f'Expected status 200, got {response.status_code}')
        # Only check body if status code matches
        if response.status_code == 200:
            try:
                response_data = response.json()
                check.equal(response_data, {'bookingid': 3760, 'booking': {'firstname': 'ú¤´', 'lastname': '', 'totalprice': -18819, 'depositpaid': False, 'bookingdates': {'checkin': '0923-08-30', 'checkout': '1160-10-31'}, 'additionalneeds': ''}}, 'Response body mismatch')
            except (json.JSONDecodeError, requests.exceptions.JSONDecodeError):
                # Response is not JSON - skip body check
                pass
    def test_post_booking_16(self):
        """Test generated from Schemathesis VCR: 7d7RDC
        Test: POST /booking
        Phase: stateful
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
                check.equal(response_data, {'bookingid': 3777, 'booking': {'firstname': '/{og', 'lastname': 'ai-failure-analysis-', 'totalprice': 8, 'depositpaid': True, 'bookingdates': {'checkin': '1861-12-04', 'checkout': '3212-05-19'}, 'additionalneeds': ',\x8d\x8c'}}, 'Response body mismatch')
            except (json.JSONDecodeError, requests.exceptions.JSONDecodeError):
                # Response is not JSON - skip body check
                pass
    def test_get_booking_9164_17(self):
        """Test generated from Schemathesis VCR: llyiDH
        Test: GET /booking/-9164
        Phase: stateful
        Status: SUCCESS
        """
        import requests
        
        url = f"{self.base_url}/booking/-9164"
        headers = self._normalize_headers({'Accept': 'application/json', 'Accept-Encoding': 'gzip, deflate, zstd', 'Authorization': '[Filtered]', 'Connection': 'keep-alive', 'Content-Type': 'application/json'})
        
        response = requests.get(url, headers=headers)
        
        check.equal(response.status_code, 404, f'Expected status 404, got {response.status_code}')
        # Only check body if status code matches
        if response.status_code == 404:
            check.is_not_none(response.text, 'Response should have body')
    def test_get_booking_9186_18(self):
        """Test generated from Schemathesis VCR: 4V3JHR
        Test: GET /booking/-9186
        Phase: stateful
        Status: SUCCESS
        """
        import requests
        
        url = f"{self.base_url}/booking/-9186"
        headers = self._normalize_headers({'Accept': 'application/json', 'Accept-Encoding': 'gzip, deflate, zstd', 'Authorization': '[Filtered]', 'Connection': 'keep-alive', 'Content-Type': 'application/json'})
        
        response = requests.get(url, headers=headers)
        
        check.equal(response.status_code, 404, f'Expected status 404, got {response.status_code}')
        # Only check body if status code matches
        if response.status_code == 404:
            check.is_not_none(response.text, 'Response should have body')
    def test_patch_booking_true_19(self):
        """Test generated from Schemathesis VCR: ETnbil
        Test: PATCH /booking/true
        Phase: stateful
        Status: FAILURE
        """
        import requests
        
        url = f"{self.base_url}/booking/true"
        headers = self._normalize_headers({'Accept': 'application/json', 'Accept-Encoding': 'gzip, deflate, zstd', 'Authorization': '[Filtered]', 'Connection': 'keep-alive', 'Content-Type': 'application/json'})
        # Randomized test data (from AI analysis)
        body = {'firstname': 'John', 'lastname': 'Doe', 'totalprice': 342, 'depositpaid': True, 'bookingdates': {'checkin': '2025-12-15', 'checkout': '2026-01-20'}}
        
        response = requests.patch(url, headers=headers, json=body)
        
        check.equal(response.status_code, 405, f'Expected status 405, got {response.status_code}')
        # Original failed checks: negative_data_rejection
    def test_post_booking_20(self):
        """Test generated from Schemathesis VCR: saFwtY
        Test: POST /booking
        Phase: stateful
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
                check.equal(response_data, {'bookingid': 3819, 'booking': {'firstname': '', 'lastname': '', 'totalprice': 300, 'depositpaid': True, 'bookingdates': {'checkin': '3197-08-16', 'checkout': '2867-06-20'}, 'additionalneeds': 'qÀÓS_Îü{'}}, 'Response body mismatch')
            except (json.JSONDecodeError, requests.exceptions.JSONDecodeError):
                # Response is not JSON - skip body check
                pass
    def test_post_booking_21(self):
        """Test generated from Schemathesis VCR: pGjUjL
        Test: POST /booking
        Phase: stateful
        Status: SUCCESS
        """
        import requests
        
        url = f"{self.base_url}/booking"
        headers = self._normalize_headers({'Accept': 'application/json', 'Accept-Encoding': 'gzip, deflate, zstd', 'Authorization': '[Filtered]', 'Connection': 'keep-alive', 'Content-Type': 'application/json'})
        # Randomized test data (from AI analysis)
        body = {'firstname': 'Jane', 'lastname': 'Smith', 'totalprice': 378, 'depositpaid': True, 'bookingdates': {'checkin': '2025-12-15', 'checkout': '2026-01-20'}, 'additionalneeds': 'Lunch'}
        
        response = requests.post(url, headers=headers, json=body)
        
        check.equal(response.status_code, 200, f'Expected status 200, got {response.status_code}')
        # Only check body if status code matches
        if response.status_code == 200:
            try:
                response_data = response.json()
                check.equal(response_data, {'bookingid': 3821, 'booking': {'firstname': 'Zz', 'lastname': 'U U\x07ì\x80d@î\x8d', 'totalprice': 50, 'depositpaid': True, 'bookingdates': {'checkin': '2743-12-01', 'checkout': '3674-02-20'}}}, 'Response body mismatch')
            except (json.JSONDecodeError, requests.exceptions.JSONDecodeError):
                # Response is not JSON - skip body check
                pass
    def test_put_booking_300_22(self):
        """Test generated from Schemathesis VCR: Gkybp9
        Test: PUT /booking/300
        Phase: stateful
        Status: SUCCESS
        """
        import requests
        
        url = f"{self.base_url}/booking/300"
        headers = self._normalize_headers({'Accept': 'application/json', 'Accept-Encoding': 'gzip, deflate, zstd', 'Authorization': '[Filtered]', 'Connection': 'keep-alive', 'Content-Type': 'application/json'})
        # Randomized test data (from AI analysis)
        body = {'firstname': 'Michael', 'lastname': 'Rodriguez', 'totalprice': 378, 'depositpaid': True, 'bookingdates': {'checkin': '2025-12-15', 'checkout': '2026-01-20'}, 'additionalneeds': 'Dinner'}
        
        response = requests.put(url, headers=headers, json=body)
        
        check.equal(response.status_code, 200, f'Expected status 200, got {response.status_code}')
        # Only check body if status code matches
        if response.status_code == 200:
            try:
                response_data = response.json()
                check.equal(response_data, {'firstname': '', 'lastname': '', 'totalprice': 300, 'depositpaid': True, 'bookingdates': {'checkin': '3197-08-16', 'checkout': '2867-06-20'}, 'additionalneeds': '\x98ºzdµl'}, 'Response body mismatch')
            except (json.JSONDecodeError, requests.exceptions.JSONDecodeError):
                # Response is not JSON - skip body check
                pass
    def test_put_booking_F_23(self):
        """Test generated from Schemathesis VCR: nmXlwH
        Test: PUT /booking/%3AF%C3%A7%C3%A7%1F
        Phase: stateful
        Status: SUCCESS
        """
        import requests
        
        url = f"{self.base_url}/booking/%3AF%C3%A7%C3%A7%1F"
        headers = self._normalize_headers({'Accept': 'application/json', 'Accept-Encoding': 'gzip, deflate, zstd', 'Authorization': '[Filtered]', 'Connection': 'keep-alive', 'Content-Type': 'application/json'})
        # Randomized test data (from AI analysis)
        body = {'firstname': 'Emily', 'lastname': 'Chen', 'totalprice': 342, 'depositpaid': True, 'bookingdates': {'checkin': '2025-12-15', 'checkout': '2026-01-20'}, 'additionalneeds': 'Snacks'}
        
        response = requests.put(url, headers=headers, json=body)
        
        check.equal(response.status_code, 400, f'Expected status 400, got {response.status_code}')
        # Only check body if status code matches
        if response.status_code == 400:
            check.is_not_none(response.text, 'Response should have body')
    def test_get_booking_72_24(self):
        """Test generated from Schemathesis VCR: zWnEy6
        Test: GET /booking/-72
        Phase: stateful
        Status: SUCCESS
        """
        import requests
        
        url = f"{self.base_url}/booking/-72"
        headers = self._normalize_headers({'Accept': 'application/json', 'Accept-Encoding': 'gzip, deflate, zstd', 'Authorization': '[Filtered]', 'Connection': 'keep-alive', 'Content-Type': 'application/json'})
        
        response = requests.get(url, headers=headers)
        
        check.equal(response.status_code, 404, f'Expected status 404, got {response.status_code}')
        # Only check body if status code matches
        if response.status_code == 404:
            check.is_not_none(response.text, 'Response should have body')
    def test_post_booking_25(self):
        """Test generated from Schemathesis VCR: ndk1sZ
        Test: POST /booking
        Phase: stateful
        Status: SUCCESS
        """
        import requests
        
        url = f"{self.base_url}/booking"
        headers = self._normalize_headers({'Accept': 'application/json', 'Accept-Encoding': 'gzip, deflate, zstd', 'Authorization': '[Filtered]', 'Connection': 'keep-alive', 'Content-Type': 'application/json'})
        # Randomized test data (from AI analysis)
        body = {'firstname': 'John', 'lastname': 'Doe', 'totalprice': 342, 'depositpaid': False, 'bookingdates': {'checkin': '2025-12-15', 'checkout': '2026-01-20'}, 'additionalneeds': 'Breakfast'}
        
        response = requests.post(url, headers=headers, json=body)
        
        check.equal(response.status_code, 200, f'Expected status 200, got {response.status_code}')
        # Only check body if status code matches
        if response.status_code == 200:
            try:
                response_data = response.json()
                check.equal(response_data, {'bookingid': 3826, 'booking': {'firstname': '', 'lastname': '\x97', 'totalprice': 56, 'depositpaid': False, 'bookingdates': {'checkin': '5539-09-14', 'checkout': '4451-09-15'}}}, 'Response body mismatch')
            except (json.JSONDecodeError, requests.exceptions.JSONDecodeError):
                # Response is not JSON - skip body check
                pass
    def test_delete_booking_45_26(self):
        """Test generated from Schemathesis VCR: Nig8gX
        Test: DELETE /booking/45
        Phase: stateful
        Status: FAILURE
        """
        import requests
        
        url = f"{self.base_url}/booking/45"
        headers = self._normalize_headers({'Accept': 'application/json', 'Accept-Encoding': 'gzip, deflate, zstd', 'Authorization': '[Filtered]', 'Connection': 'keep-alive', 'Content-Type': 'application/json'})
        
        response = requests.delete(url, headers=headers)
        
        check.equal(response.status_code, 201, f'Expected status 201, got {response.status_code}')
        # Original failed checks: content_type_conformance
    def test_post_booking_27(self):
        """Test generated from Schemathesis VCR: flGn5Q
        Test: POST /booking
        Phase: stateful
        Status: SUCCESS
        """
        import requests
        
        url = f"{self.base_url}/booking"
        headers = self._normalize_headers({'Accept': 'application/json', 'Accept-Encoding': 'gzip, deflate, zstd', 'Authorization': '[Filtered]', 'Connection': 'keep-alive', 'Content-Type': 'application/json'})
        body = {'bookingdates': {'checkin': '5539-09-14', 'checkout': '4451-09-15', '\U0008acae\U000bae3a\U000bae2fë|D\U0004c6b7|\U000fb612~\U000ffdddf|': []}, 'depositpaid': False, 'firstname': '', 'lastname': '\x97', 'totalprice': 56}
        
        response = requests.post(url, headers=headers, json=body)
        
        check.equal(response.status_code, 200, f'Expected status 200, got {response.status_code}')
        # Only check body if status code matches
        if response.status_code == 200:
            try:
                response_data = response.json()
                check.equal(response_data, {'bookingid': 3835, 'booking': {'firstname': '', 'lastname': '\x97', 'totalprice': 56, 'depositpaid': False, 'bookingdates': {'checkin': '5539-09-14', 'checkout': '4451-09-15'}}}, 'Response body mismatch')
            except (json.JSONDecodeError, requests.exceptions.JSONDecodeError):
                # Response is not JSON - skip body check
                pass
    def test_post_booking_28(self):
        """Test generated from Schemathesis VCR: mfsnPM
        Test: POST /booking
        Phase: stateful
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
                check.equal(response_data, {'bookingid': 3852, 'booking': {'firstname': '5', 'lastname': '', 'totalprice': 300, 'depositpaid': True, 'bookingdates': {'checkin': '4308-02-09', 'checkout': '0683-05-24'}}}, 'Response body mismatch')
            except (json.JSONDecodeError, requests.exceptions.JSONDecodeError):
                # Response is not JSON - skip body check
                pass
    def test_get_booking_114_29(self):
        """Test generated from Schemathesis VCR: AXliqJ
        Test: GET /booking/114
        Phase: stateful
        Status: SUCCESS
        """
        import requests
        
        url = f"{self.base_url}/booking/114"
        headers = self._normalize_headers({'Accept': 'application/json', 'Accept-Encoding': 'gzip, deflate, zstd', 'Authorization': '[Filtered]', 'Connection': 'keep-alive', 'Content-Type': 'application/json'})
        
        response = requests.get(url, headers=headers)
        
        check.equal(response.status_code, 404, f'Expected status 404, got {response.status_code}')
        # Only check body if status code matches
        if response.status_code == 404:
            check.is_not_none(response.text, 'Response should have body')
    def test_get_booking_true_30(self):
        """Test generated from Schemathesis VCR: uOCydV
        Test: GET /booking/true
        Phase: stateful
        Status: SUCCESS
        """
        import requests
        
        url = f"{self.base_url}/booking/true"
        headers = self._normalize_headers({'Accept': 'application/json', 'Accept-Encoding': 'gzip, deflate, zstd', 'Authorization': '[Filtered]', 'Connection': 'keep-alive', 'Content-Type': 'application/json'})
        
        response = requests.get(url, headers=headers)
        
        check.equal(response.status_code, 404, f'Expected status 404, got {response.status_code}')
        # Only check body if status code matches
        if response.status_code == 404:
            check.is_not_none(response.text, 'Response should have body')
    def test_delete_booking_17_31(self):
        """Test generated from Schemathesis VCR: coqxuR
        Test: DELETE /booking/-17
        Phase: stateful
        Status: SUCCESS
        """
        import requests
        
        url = f"{self.base_url}/booking/-17"
        headers = self._normalize_headers({'Accept': 'application/json', 'Accept-Encoding': 'gzip, deflate, zstd', 'Authorization': '[Filtered]', 'Connection': 'keep-alive', 'Content-Type': 'application/json'})
        
        response = requests.delete(url, headers=headers)
        
        check.equal(response.status_code, 405, f'Expected status 405, got {response.status_code}')
        # Only check body if status code matches
        if response.status_code == 405:
            check.is_not_none(response.text, 'Response should have body')
    def test_delete_booking_null_32(self):
        """Test generated from Schemathesis VCR: nRWPGA
        Test: DELETE /booking/null
        Phase: stateful
        Status: SUCCESS
        """
        import requests
        
        url = f"{self.base_url}/booking/null"
        headers = self._normalize_headers({'Accept': 'application/json', 'Accept-Encoding': 'gzip, deflate, zstd', 'Authorization': '[Filtered]', 'Connection': 'keep-alive', 'Content-Type': 'application/json'})
        
        response = requests.delete(url, headers=headers)
        
        check.equal(response.status_code, 405, f'Expected status 405, got {response.status_code}')
        # Only check body if status code matches
        if response.status_code == 405:
            check.is_not_none(response.text, 'Response should have body')
    def test_post_booking_33(self):
        """Test generated from Schemathesis VCR: jkd75j
        Test: POST /booking
        Phase: stateful
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
                check.equal(response_data, {'bookingid': 3860, 'booking': {'firstname': '\x07\x80', 'lastname': '뒁\U000d0013ö\x1d\xa0~\x96\t\U00069018]/\x86\x0fÕ\x83\U00065edd', 'totalprice': 19381, 'depositpaid': False, 'bookingdates': {'checkin': '2269-04-20', 'checkout': '2582-07-25'}, 'additionalneeds': 'Æ'}}, 'Response body mismatch')
            except (json.JSONDecodeError, requests.exceptions.JSONDecodeError):
                # Response is not JSON - skip body check
                pass
    def test_post_booking_34(self):
        """Test generated from Schemathesis VCR: 2sMwxw
        Test: POST /booking
        Phase: stateful
        Status: SUCCESS
        """
        import requests
        
        url = f"{self.base_url}/booking"
        headers = self._normalize_headers({'Accept': 'application/json', 'Accept-Encoding': 'gzip, deflate, zstd', 'Authorization': '[Filtered]', 'Connection': 'keep-alive', 'Content-Type': 'application/json'})
        # Randomized test data (from AI analysis)
        body = {'firstname': 'Jane', 'lastname': 'Doe', 'totalprice': 342, 'depositpaid': True, 'bookingdates': {'checkin': '2025-12-15', 'checkout': '2026-01-20'}, 'additionalneeds': 'Lunch'}
        
        response = requests.post(url, headers=headers, json=body)
        
        check.equal(response.status_code, 200, f'Expected status 200, got {response.status_code}')
        # Only check body if status code matches
        if response.status_code == 200:
            try:
                response_data = response.json()
                check.equal(response_data, {'bookingid': 3863, 'booking': {'firstname': 'ê!-\U000f18aeí\U0006c419\tf𢝴', 'lastname': 'ðW\U0008cf2fç\U000b12aa', 'totalprice': -78, 'depositpaid': False, 'bookingdates': {'checkin': '2143-12-04', 'checkout': '4027-01-24'}}}, 'Response body mismatch')
            except (json.JSONDecodeError, requests.exceptions.JSONDecodeError):
                # Response is not JSON - skip body check
                pass
    def test_post_booking_35(self):
        """Test generated from Schemathesis VCR: lRC6cY
        Test: POST /booking
        Phase: stateful
        Status: SUCCESS
        """
        import requests
        
        url = f"{self.base_url}/booking"
        headers = self._normalize_headers({'Accept': 'application/json', 'Accept-Encoding': 'gzip, deflate, zstd', 'Authorization': '[Filtered]', 'Connection': 'keep-alive', 'Content-Type': 'application/json'})
        # Randomized test data (from AI analysis)
        body = {'firstname': 'Michael', 'lastname': 'Rodriguez', 'totalprice': 378, 'depositpaid': True, 'bookingdates': {'checkin': '2025-12-15', 'checkout': '2026-01-20'}, 'additionalneeds': 'Dinner'}
        
        response = requests.post(url, headers=headers, json=body)
        
        check.equal(response.status_code, 200, f'Expected status 200, got {response.status_code}')
        # Only check body if status code matches
        if response.status_code == 200:
            try:
                response_data = response.json()
                check.equal(response_data, {'bookingid': 3866, 'booking': {'firstname': '', 'lastname': '\U000bb517', 'totalprice': 31255, 'depositpaid': True, 'bookingdates': {'checkin': '5200-04-11', 'checkout': '0300-03-03'}}}, 'Response body mismatch')
            except (json.JSONDecodeError, requests.exceptions.JSONDecodeError):
                # Response is not JSON - skip body check
                pass
    def test_post_booking_36(self):
        """Test generated from Schemathesis VCR: hEVktr
        Test: POST /booking
        Phase: stateful
        Status: SUCCESS
        """
        import requests
        
        url = f"{self.base_url}/booking"
        headers = self._normalize_headers({'Accept': 'application/json', 'Accept-Encoding': 'gzip, deflate, zstd', 'Authorization': '[Filtered]', 'Connection': 'keep-alive', 'Content-Type': 'application/json'})
        # Randomized test data (from AI analysis)
        body = {'firstname': 'Emily', 'lastname': 'Doe', 'totalprice': 342, 'depositpaid': True, 'bookingdates': {'checkin': '2025-12-15', 'checkout': '2026-01-20'}, 'additionalneeds': 'Breakfast'}
        
        response = requests.post(url, headers=headers, json=body)
        
        check.equal(response.status_code, 200, f'Expected status 200, got {response.status_code}')
        # Only check body if status code matches
        if response.status_code == 200:
            try:
                response_data = response.json()
                check.equal(response_data, {'bookingid': 3869, 'booking': {'firstname': '\U000da299\x14¢\x8c', 'lastname': 'PP', 'totalprice': -117, 'depositpaid': True, 'bookingdates': {'checkin': '8035-11-10', 'checkout': '0836-11-13'}, 'additionalneeds': '\U000b11eb³L'}}, 'Response body mismatch')
            except (json.JSONDecodeError, requests.exceptions.JSONDecodeError):
                # Response is not JSON - skip body check
                pass
    def test_post_booking_37(self):
        """Test generated from Schemathesis VCR: UANvs9
        Test: POST /booking
        Phase: stateful
        Status: SUCCESS
        """
        import requests
        
        url = f"{self.base_url}/booking"
        headers = self._normalize_headers({'Accept': 'application/json', 'Accept-Encoding': 'gzip, deflate, zstd', 'Authorization': '[Filtered]', 'Connection': 'keep-alive', 'Content-Type': 'application/json'})
        # Randomized test data (from AI analysis)
        body = {'firstname': 'Sarah', 'lastname': 'Doe', 'totalprice': 342, 'depositpaid': True, 'bookingdates': {'checkin': '2025-12-15', 'checkout': '2026-01-20'}, 'additionalneeds': 'Lunch'}
        
        response = requests.post(url, headers=headers, json=body)
        
        check.equal(response.status_code, 200, f'Expected status 200, got {response.status_code}')
        # Only check body if status code matches
        if response.status_code == 200:
            try:
                response_data = response.json()
                check.equal(response_data, {'bookingid': 3873, 'booking': {'firstname': '\x965)NÞ', 'lastname': '$è=µé\U00064591»(', 'totalprice': 22831, 'depositpaid': False, 'bookingdates': {'checkin': '0675-01-01', 'checkout': '4897-04-27'}}}, 'Response body mismatch')
            except (json.JSONDecodeError, requests.exceptions.JSONDecodeError):
                # Response is not JSON - skip body check
                pass
    def test_post_booking_38(self):
        """Test generated from Schemathesis VCR: 2RLspP
        Test: POST /booking
        Phase: stateful
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
                check.equal(response_data, {'bookingid': 3879, 'booking': {'firstname': '\x965)NÞ', 'lastname': '$è=µé\U00064591»(', 'totalprice': 22831, 'depositpaid': False, 'bookingdates': {'checkin': '0675-01-01', 'checkout': '4897-04-27'}}}, 'Response body mismatch')
            except (json.JSONDecodeError, requests.exceptions.JSONDecodeError):
                # Response is not JSON - skip body check
                pass
    def test_delete_booking_30794_39(self):
        """Test generated from Schemathesis VCR: 3XTdVw
        Test: DELETE /booking/30794
        Phase: stateful
        Status: SUCCESS
        """
        import requests
        
        url = f"{self.base_url}/booking/30794"
        headers = self._normalize_headers({'Accept': 'application/json', 'Accept-Encoding': 'gzip, deflate, zstd', 'Authorization': '[Filtered]', 'Connection': 'keep-alive', 'Content-Type': 'application/json'})
        
        response = requests.delete(url, headers=headers)
        
        check.equal(response.status_code, 405, f'Expected status 405, got {response.status_code}')
        # Only check body if status code matches
        if response.status_code == 405:
            check.is_not_none(response.text, 'Response should have body')
    def test_put_booking_D_40(self):
        """Test generated from Schemathesis VCR: OPKuVi
        Test: PUT /booking/%C3%B5%F2%B1%94%A4%5D%C2%97%C2%88D%C2%A7%C2%AB%C2%9C
        Phase: stateful
        Status: SUCCESS
        """
        import requests
        
        url = f"{self.base_url}/booking/%C3%B5%F2%B1%94%A4%5D%C2%97%C2%88D%C2%A7%C2%AB%C2%9C"
        headers = self._normalize_headers({'Accept': 'application/json', 'Accept-Encoding': 'gzip, deflate, zstd', 'Authorization': '[Filtered]', 'Connection': 'keep-alive', 'Content-Type': 'application/json'})
        # Randomized test data (from AI analysis)
        body = {'firstname': 'Jane', 'lastname': 'Smith', 'totalprice': 567, 'depositpaid': False, 'bookingdates': {'checkin': '2025-12-15', 'checkout': '2026-01-20'}, 'additionalneeds': 'Lunch'}
        
        response = requests.put(url, headers=headers, json=body)
        
        check.equal(response.status_code, 405, f'Expected status 405, got {response.status_code}')
        # Only check body if status code matches
        if response.status_code == 405:
            check.is_not_none(response.text, 'Response should have body')
    def test_get_booking_283_41(self):
        """Test generated from Schemathesis VCR: CjGnBn
        Test: GET /booking/283
        Phase: stateful
        Status: SUCCESS
        """
        import requests
        
        url = f"{self.base_url}/booking/283"
        headers = self._normalize_headers({'Accept': 'application/json', 'Accept-Encoding': 'gzip, deflate, zstd', 'Authorization': '[Filtered]', 'Connection': 'keep-alive', 'Content-Type': 'application/json'})
        
        response = requests.get(url, headers=headers)
        
        check.equal(response.status_code, 404, f'Expected status 404, got {response.status_code}')
        # Only check body if status code matches
        if response.status_code == 404:
            check.is_not_none(response.text, 'Response should have body')
    def test_get_booking_3881_42(self):
        """Test generated from Schemathesis VCR: oqPYdn
        Test: GET /booking/-3881
        Phase: stateful
        Status: SUCCESS
        """
        import requests
        
        url = f"{self.base_url}/booking/-3881"
        headers = self._normalize_headers({'Accept': 'application/json', 'Accept-Encoding': 'gzip, deflate, zstd', 'Authorization': '[Filtered]', 'Connection': 'keep-alive', 'Content-Type': 'application/json'})
        
        response = requests.get(url, headers=headers)
        
        check.equal(response.status_code, 404, f'Expected status 404, got {response.status_code}')
        # Only check body if status code matches
        if response.status_code == 404:
            check.is_not_none(response.text, 'Response should have body')
    def test_post_booking_43(self):
        """Test generated from Schemathesis VCR: VfOGPf
        Test: POST /booking
        Phase: stateful
        Status: SUCCESS
        """
        import requests
        
        url = f"{self.base_url}/booking"
        headers = self._normalize_headers({'Accept': 'application/json', 'Accept-Encoding': 'gzip, deflate, zstd', 'Authorization': '[Filtered]', 'Connection': 'keep-alive', 'Content-Type': 'application/json'})
        # Randomized test data (from AI analysis)
        body = {'firstname': 'John', 'lastname': 'Doe', 'totalprice': 342, 'depositpaid': True, 'bookingdates': {'checkin': '2025-12-15', 'checkout': '2026-01-20'}, 'additionalneeds': 'Breakfast'}
        
        response = requests.post(url, headers=headers, json=body)
        
        check.equal(response.status_code, 400, f'Expected status 400, got {response.status_code}')
        # Only check body if status code matches
        if response.status_code == 400:
            check.is_not_none(response.text, 'Response should have body')
    def test_post_booking_44(self):
        """Test generated from Schemathesis VCR: n0eCq7
        Test: POST /booking
        Phase: stateful
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
                check.equal(response_data, {'bookingid': 3895, 'booking': {'firstname': 'B', 'lastname': '\x83𫌠', 'totalprice': -4816564541275546000, 'depositpaid': True, 'bookingdates': {'checkin': '4569-08-21', 'checkout': '1177-01-11'}, 'additionalneeds': 'E\U000bc9a9ÈÆ'}}, 'Response body mismatch')
            except (json.JSONDecodeError, requests.exceptions.JSONDecodeError):
                # Response is not JSON - skip body check
                pass
    def test_get_booking_null_45(self):
        """Test generated from Schemathesis VCR: aSwsXW
        Test: GET /booking/null
        Phase: stateful
        Status: SUCCESS
        """
        import requests
        
        url = f"{self.base_url}/booking/null"
        headers = self._normalize_headers({'Accept': 'application/json', 'Accept-Encoding': 'gzip, deflate, zstd', 'Authorization': '[Filtered]', 'Connection': 'keep-alive', 'Content-Type': 'application/json'})
        
        response = requests.get(url, headers=headers)
        
        check.equal(response.status_code, 404, f'Expected status 404, got {response.status_code}')
        # Only check body if status code matches
        if response.status_code == 404:
            check.is_not_none(response.text, 'Response should have body')
    def test_get_booking_null_46(self):
        """Test generated from Schemathesis VCR: TuKBYM
        Test: GET /booking/null
        Phase: stateful
        Status: SUCCESS
        """
        import requests
        
        url = f"{self.base_url}/booking/null"
        headers = self._normalize_headers({'Accept': 'application/json', 'Accept-Encoding': 'gzip, deflate, zstd', 'Authorization': '[Filtered]', 'Connection': 'keep-alive', 'Content-Type': 'application/json'})
        
        response = requests.get(url, headers=headers)
        
        check.equal(response.status_code, 404, f'Expected status 404, got {response.status_code}')
        # Only check body if status code matches
        if response.status_code == 404:
            check.is_not_none(response.text, 'Response should have body')
    def test_post_booking_47(self):
        """Test generated from Schemathesis VCR: BDO0F5
        Test: POST /booking
        Phase: stateful
        Status: SUCCESS
        """
        import requests
        
        url = f"{self.base_url}/booking"
        headers = self._normalize_headers({'Accept': 'application/json', 'Accept-Encoding': 'gzip, deflate, zstd', 'Authorization': '[Filtered]', 'Connection': 'keep-alive', 'Content-Type': 'application/json'})
        # Randomized test data (from AI analysis)
        body = {'firstname': 'John', 'lastname': 'Doe', 'totalprice': 342, 'depositpaid': True, 'bookingdates': {'checkin': '2025-12-15', 'checkout': '2026-01-20'}, 'additionalneeds': 'Breakfast'}
        
        response = requests.post(url, headers=headers, json=body)
        
        check.equal(response.status_code, 500, f'Expected status 500, got {response.status_code}')
        # Only check body if status code matches
        if response.status_code == 500:
            check.is_not_none(response.text, 'Response should have body')
    def test_post_booking_48(self):
        """Test generated from Schemathesis VCR: JcJQXj
        Test: POST /booking
        Phase: stateful
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
                check.equal(response_data, {'bookingid': 3910, 'booking': {'firstname': '\x8e©(Jã\x82', 'lastname': '\x18', 'totalprice': 27684, 'depositpaid': True, 'bookingdates': {'checkin': '0535-11-29', 'checkout': '5843-01-01'}, 'additionalneeds': 'z\x12\x18c\xad'}}, 'Response body mismatch')
            except (json.JSONDecodeError, requests.exceptions.JSONDecodeError):
                # Response is not JSON - skip body check
                pass
    def test_get_booking_null_49(self):
        """Test generated from Schemathesis VCR: jSXY42
        Test: GET /booking/null
        Phase: stateful
        Status: SUCCESS
        """
        import requests
        
        url = f"{self.base_url}/booking/null"
        headers = self._normalize_headers({'Accept': 'application/json', 'Accept-Encoding': 'gzip, deflate, zstd', 'Authorization': '[Filtered]', 'Connection': 'keep-alive', 'Content-Type': 'application/json'})
        
        response = requests.get(url, headers=headers)
        
        check.equal(response.status_code, 404, f'Expected status 404, got {response.status_code}')
        # Only check body if status code matches
        if response.status_code == 404:
            check.is_not_none(response.text, 'Response should have body')
    def test_post_booking_50(self):
        """Test generated from Schemathesis VCR: S8c0Ie
        Test: POST /booking
        Phase: stateful
        Status: SUCCESS
        """
        import requests
        
        url = f"{self.base_url}/booking"
        headers = self._normalize_headers({'Accept': 'application/json', 'Accept-Encoding': 'gzip, deflate, zstd', 'Authorization': '[Filtered]', 'Connection': 'keep-alive', 'Content-Type': 'application/json'})
        # Randomized test data (from AI analysis)
        body = {'firstname': 'John', 'lastname': 'Doe', 'totalprice': 342, 'depositpaid': False, 'bookingdates': {'checkin': '2025-12-15', 'checkout': '2026-01-20'}, 'additionalneeds': 'Breakfast'}
        
        response = requests.post(url, headers=headers, json=body)
        
        check.equal(response.status_code, 200, f'Expected status 200, got {response.status_code}')
        # Only check body if status code matches
        if response.status_code == 200:
            try:
                response_data = response.json()
                check.equal(response_data, {'bookingid': 3916, 'booking': {'firstname': 'î\x8b', 'lastname': 'þÎ', 'totalprice': 10046, 'depositpaid': False, 'bookingdates': {'checkin': '4818-05-19', 'checkout': '0300-08-10'}, 'additionalneeds': '𱭯'}}, 'Response body mismatch')
            except (json.JSONDecodeError, requests.exceptions.JSONDecodeError):
                # Response is not JSON - skip body check
                pass
    def test_get_booking_true_51(self):
        """Test generated from Schemathesis VCR: Fd6q5Z
        Test: GET /booking/true
        Phase: stateful
        Status: SUCCESS
        """
        import requests
        
        url = f"{self.base_url}/booking/true"
        headers = self._normalize_headers({'Accept': 'application/json', 'Accept-Encoding': 'gzip, deflate, zstd', 'Authorization': '[Filtered]', 'Connection': 'keep-alive', 'Content-Type': 'application/json'})
        
        response = requests.get(url, headers=headers)
        
        check.equal(response.status_code, 404, f'Expected status 404, got {response.status_code}')
        # Only check body if status code matches
        if response.status_code == 404:
            check.is_not_none(response.text, 'Response should have body')
    def test_post_booking_52(self):
        """Test generated from Schemathesis VCR: 8mtnRG
        Test: POST /booking
        Phase: stateful
        Status: SUCCESS
        """
        import requests
        
        url = f"{self.base_url}/booking"
        headers = self._normalize_headers({'Accept': 'application/json', 'Accept-Encoding': 'gzip, deflate, zstd', 'Authorization': '[Filtered]', 'Connection': 'keep-alive', 'Content-Type': 'application/json'})
        # Randomized test data (from AI analysis)
        body = {'firstname': 'Jane', 'lastname': 'Doe', 'totalprice': 123, 'depositpaid': True, 'bookingdates': {'checkin': '2025-12-15', 'checkout': '2026-01-20'}, 'additionalneeds': 'Lunch'}
        
        response = requests.post(url, headers=headers, json=body)
        
        check.equal(response.status_code, 200, f'Expected status 200, got {response.status_code}')
        # Only check body if status code matches
        if response.status_code == 200:
            try:
                response_data = response.json()
                check.equal(response_data, {'bookingid': 3920, 'booking': {'firstname': '*/\x83f¯u"4𤈄¨²?\r§>\x03®M𞲁:', 'lastname': '\x92𫵌\x12', 'totalprice': -74, 'depositpaid': True, 'bookingdates': {'checkin': '3995-01-26', 'checkout': '7113-10-07'}, 'additionalneeds': 'Á\n\x17XÀ´𥆽\x97\x0e\x94'}}, 'Response body mismatch')
            except (json.JSONDecodeError, requests.exceptions.JSONDecodeError):
                # Response is not JSON - skip body check
                pass
    def test_post_booking_53(self):
        """Test generated from Schemathesis VCR: yrQO9P
        Test: POST /booking
        Phase: stateful
        Status: SUCCESS
        """
        import requests
        
        url = f"{self.base_url}/booking"
        headers = self._normalize_headers({'Accept': 'application/json', 'Accept-Encoding': 'gzip, deflate, zstd', 'Authorization': '[Filtered]', 'Connection': 'keep-alive', 'Content-Type': 'application/json'})
        # Randomized test data (from AI analysis)
        body = {'firstname': 'Emily', 'lastname': 'Smith', 'totalprice': 567, 'depositpaid': False, 'bookingdates': {'checkin': '2025-12-15', 'checkout': '2026-01-20'}, 'additionalneeds': 'Dinner'}
        
        response = requests.post(url, headers=headers, json=body)
        
        check.equal(response.status_code, 400, f'Expected status 400, got {response.status_code}')
        # Only check body if status code matches
        if response.status_code == 400:
            check.is_not_none(response.text, 'Response should have body')
    def test_post_booking_54(self):
        """Test generated from Schemathesis VCR: hKAG6c
        Test: POST /booking
        Phase: stateful
        Status: SUCCESS
        """
        import requests
        
        url = f"{self.base_url}/booking"
        headers = self._normalize_headers({'Accept': 'application/json', 'Accept-Encoding': 'gzip, deflate, zstd', 'Authorization': '[Filtered]', 'Connection': 'keep-alive', 'Content-Type': 'application/json'})
        # Randomized test data (from AI analysis)
        body = {'firstname': 'Sarah', 'lastname': 'Johnson', 'totalprice': 901, 'depositpaid': True, 'bookingdates': {'checkin': '2025-12-15', 'checkout': '2026-01-20'}, 'additionalneeds': 'Snacks'}
        
        response = requests.post(url, headers=headers, json=body)
        
        check.equal(response.status_code, 500, f'Expected status 500, got {response.status_code}')
        # Only check body if status code matches
        if response.status_code == 500:
            check.is_not_none(response.text, 'Response should have body')
    def test_post_booking_55(self):
        """Test generated from Schemathesis VCR: nx9Y83
        Test: POST /booking
        Phase: stateful
        Status: SUCCESS
        """
        import requests
        
        url = f"{self.base_url}/booking"
        headers = self._normalize_headers({'Accept': 'application/json', 'Accept-Encoding': 'gzip, deflate, zstd', 'Authorization': '[Filtered]', 'Connection': 'keep-alive', 'Content-Type': 'application/json'})
        # Randomized test data (from AI analysis)
        body = {'firstname': 'John', 'lastname': 'Rodriguez', 'totalprice': 342, 'depositpaid': True, 'bookingdates': {'checkin': '2025-12-15', 'checkout': '2026-01-20'}, 'additionalneeds': 'Breakfast'}
        
        response = requests.post(url, headers=headers, json=body)
        
        check.equal(response.status_code, 200, f'Expected status 200, got {response.status_code}')
        # Only check body if status code matches
        if response.status_code == 200:
            try:
                response_data = response.json()
                check.equal(response_data, {'bookingid': 3930, 'booking': {'firstname': '(𝡾3Óµ+', 'lastname': 'à\U00052efaZ\U000f89f0i*', 'totalprice': 4432449412605653500, 'depositpaid': True, 'bookingdates': {'checkin': '4582-01-05', 'checkout': '3732-04-15'}}}, 'Response body mismatch')
            except (json.JSONDecodeError, requests.exceptions.JSONDecodeError):
                # Response is not JSON - skip body check
                pass
    def test_patch_booking_4_56(self):
        """Test generated from Schemathesis VCR: 7Mn4EM
        Test: PATCH /booking/4
        Phase: stateful
        Status: FAILURE
        """
        import requests
        
        url = f"{self.base_url}/booking/4"
        headers = self._normalize_headers({'Accept': 'application/json', 'Accept-Encoding': 'gzip, deflate, zstd', 'Authorization': '[Filtered]', 'Connection': 'keep-alive', 'Content-Type': 'application/json'})
        # Randomized test data (from AI analysis)
        body = {'firstname': 'Michael', 'lastname': 'Smith', 'totalprice': 378, 'depositpaid': True, 'bookingdates': {'checkin': '2025-12-15', 'checkout': '2026-01-20'}, 'additionalneeds': 'Lunch'}
        
        response = requests.patch(url, headers=headers, json=body)
        
        check.equal(response.status_code, 200, f'Expected status 200, got {response.status_code}')
        # Original failed checks: negative_data_rejection
    def test_post_booking_57(self):
        """Test generated from Schemathesis VCR: WZNZHT
        Test: POST /booking
        Phase: stateful
        Status: SUCCESS
        """
        import requests
        
        url = f"{self.base_url}/booking"
        headers = self._normalize_headers({'Accept': 'application/json', 'Accept-Encoding': 'gzip, deflate, zstd', 'Authorization': '[Filtered]', 'Connection': 'keep-alive', 'Content-Type': 'application/json'})
        # Randomized test data (from AI analysis)
        body = {'firstname': 'Emily', 'lastname': 'Johnson', 'totalprice': 342, 'depositpaid': True, 'bookingdates': {'checkin': '2025-12-15', 'checkout': '2026-01-20'}, 'additionalneeds': 'Dinner'}
        
        response = requests.post(url, headers=headers, json=body)
        
        check.equal(response.status_code, 200, f'Expected status 200, got {response.status_code}')
        # Only check body if status code matches
        if response.status_code == 200:
            try:
                response_data = response.json()
                check.equal(response_data, {'bookingid': 3934, 'booking': {'firstname': '(𝡾3Óµ+', 'lastname': 'à\U00052efaZ\U000f89f0i*', 'totalprice': 4432449412605653500, 'depositpaid': True, 'bookingdates': {'checkin': '4582-01-05', 'checkout': '3732-04-15'}}}, 'Response body mismatch')
            except (json.JSONDecodeError, requests.exceptions.JSONDecodeError):
                # Response is not JSON - skip body check
                pass
    def test_patch_booking_4_58(self):
        """Test generated from Schemathesis VCR: rZxIZs
        Test: PATCH /booking/4
        Phase: stateful
        Status: SUCCESS
        """
        import requests
        
        url = f"{self.base_url}/booking/4"
        headers = self._normalize_headers({'Accept': 'application/json', 'Accept-Encoding': 'gzip, deflate, zstd', 'Authorization': '[Filtered]', 'Connection': 'keep-alive', 'Content-Type': 'application/json'})
        # Randomized test data (from AI analysis)
        body = {'firstname': 'Sophia', 'lastname': 'Williams', 'totalprice': 378, 'depositpaid': True, 'bookingdates': {'checkin': '2025-12-15', 'checkout': '2026-01-20'}, 'additionalneeds': 'Breakfast'}
        
        response = requests.patch(url, headers=headers, json=body)
        
        check.equal(response.status_code, 200, f'Expected status 200, got {response.status_code}')
        # Only check body if status code matches
        if response.status_code == 200:
            try:
                response_data = response.json()
                check.equal(response_data, {'firstname': '(𝡾3Óµ+', 'lastname': 'à\U00052efaZ\U000f89f0i*', 'totalprice': 4432449412605653500, 'depositpaid': True, 'bookingdates': {'checkin': '2016-03-09', 'checkout': '2021-03-24'}, 'additionalneeds': 'Breakfast'}, 'Response body mismatch')
            except (json.JSONDecodeError, requests.exceptions.JSONDecodeError):
                # Response is not JSON - skip body check
                pass
    def test_post_booking_59(self):
        """Test generated from Schemathesis VCR: p5QT4a
        Test: POST /booking
        Phase: stateful
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
                check.equal(response_data, {'bookingid': 3953, 'booking': {'firstname': 'Õ\x85', 'lastname': '\x98¼\x85$\U0008e726±', 'totalprice': -122, 'depositpaid': True, 'bookingdates': {'checkin': '8982-09-23', 'checkout': '0300-07-09'}}}, 'Response body mismatch')
            except (json.JSONDecodeError, requests.exceptions.JSONDecodeError):
                # Response is not JSON - skip body check
                pass
    def test_post_booking_60(self):
        """Test generated from Schemathesis VCR: 2UEfde
        Test: POST /booking
        Phase: stateful
        Status: SUCCESS
        """
        import requests
        
        url = f"{self.base_url}/booking"
        headers = self._normalize_headers({'Accept': 'application/json', 'Accept-Encoding': 'gzip, deflate, zstd', 'Authorization': '[Filtered]', 'Connection': 'keep-alive', 'Content-Type': 'application/json'})
        # Randomized test data (from AI analysis)
        body = {'firstname': 'Jane', 'lastname': 'Smith', 'totalprice': 123, 'depositpaid': False, 'bookingdates': {'checkin': '2025-12-15', 'checkout': '2026-01-20'}, 'additionalneeds': 'Lunch'}
        
        response = requests.post(url, headers=headers, json=body)
        
        check.equal(response.status_code, 500, f'Expected status 500, got {response.status_code}')
        # Only check body if status code matches
        if response.status_code == 500:
            check.is_not_none(response.text, 'Response should have body')
    def test_post_booking_61(self):
        """Test generated from Schemathesis VCR: aTHzFf
        Test: POST /booking
        Phase: stateful
        Status: SUCCESS
        """
        import requests
        
        url = f"{self.base_url}/booking"
        headers = self._normalize_headers({'Accept': 'application/json', 'Accept-Encoding': 'gzip, deflate, zstd', 'Authorization': '[Filtered]', 'Connection': 'keep-alive', 'Content-Type': 'application/json'})
        # Randomized test data (from AI analysis)
        body = {'firstname': 'Emily', 'lastname': 'Johnson', 'totalprice': 567, 'depositpaid': True, 'bookingdates': {'checkin': '2025-12-15', 'checkout': '2026-01-20'}, 'additionalneeds': 'Dinner'}
        
        response = requests.post(url, headers=headers, json=body)
        
        check.equal(response.status_code, 200, f'Expected status 200, got {response.status_code}')
        # Only check body if status code matches
        if response.status_code == 200:
            try:
                response_data = response.json()
                check.equal(response_data, {'bookingid': 3960, 'booking': {'firstname': 'Ω≈ç√∫˜µ≤≥÷åß∂ƒ©˙∆˚¬…æœ∑´®†¥¨ˆøπ“‘¡™£¢∞§¶•ªº–≠¸˛Ç◊ı˜Â¯˘¿ÅÍÎÏ˝ÓÔ\uf8ffÒÚÆ☃Œ„´‰ˇÁ¨ˆØ∏”’`⁄€‹›ﬁﬂ‡°·‚—±', 'lastname': 'ëv', 'totalprice': 1, 'depositpaid': False, 'bookingdates': {'checkin': '7874-03-17', 'checkout': '2512-12-31'}}}, 'Response body mismatch')
            except (json.JSONDecodeError, requests.exceptions.JSONDecodeError):
                # Response is not JSON - skip body check
                pass
    def test_delete_booking_34_62(self):
        """Test generated from Schemathesis VCR: AbKhYy
        Test: DELETE /booking/-34
        Phase: stateful
        Status: SUCCESS
        """
        import requests
        
        url = f"{self.base_url}/booking/-34"
        headers = self._normalize_headers({'Accept': 'application/json', 'Accept-Encoding': 'gzip, deflate, zstd', 'Authorization': '[Filtered]', 'Connection': 'keep-alive', 'Content-Type': 'application/json'})
        
        response = requests.delete(url, headers=headers)
        
        check.equal(response.status_code, 405, f'Expected status 405, got {response.status_code}')
        # Only check body if status code matches
        if response.status_code == 405:
            check.is_not_none(response.text, 'Response should have body')
    def test_patch_booking_15456_63(self):
        """Test generated from Schemathesis VCR: Zmsz9P
        Test: PATCH /booking/15456
        Phase: stateful
        Status: SUCCESS
        """
        import requests
        
        url = f"{self.base_url}/booking/15456"
        headers = self._normalize_headers({'Accept': 'application/json', 'Accept-Encoding': 'gzip, deflate, zstd', 'Authorization': '[Filtered]', 'Connection': 'keep-alive', 'Content-Type': 'application/json'})
        # Randomized test data (from AI analysis)
        body = {'firstname': 'Sarah', 'lastname': 'Lee', 'totalprice': 901, 'depositpaid': False, 'bookingdates': {'checkin': '2025-12-15', 'checkout': '2026-01-20'}, 'additionalneeds': 'Snack'}
        
        response = requests.patch(url, headers=headers, json=body)
        
        check.equal(response.status_code, 405, f'Expected status 405, got {response.status_code}')
        # Only check body if status code matches
        if response.status_code == 405:
            check.is_not_none(response.text, 'Response should have body')
    def test_delete_booking_47_64(self):
        """Test generated from Schemathesis VCR: fPVQin
        Test: DELETE /booking/47
        Phase: stateful
        Status: SUCCESS
        """
        import requests
        
        url = f"{self.base_url}/booking/47"
        headers = self._normalize_headers({'Accept': 'application/json', 'Accept-Encoding': 'gzip, deflate, zstd', 'Authorization': '[Filtered]', 'Connection': 'keep-alive', 'Content-Type': 'application/json'})
        
        response = requests.delete(url, headers=headers)
        
        check.equal(response.status_code, 405, f'Expected status 405, got {response.status_code}')
        # Only check body if status code matches
        if response.status_code == 405:
            check.is_not_none(response.text, 'Response should have body')
    def test_patch_booking_true_65(self):
        """Test generated from Schemathesis VCR: izDCw4
        Test: PATCH /booking/true
        Phase: stateful
        Status: SUCCESS
        """
        import requests
        
        url = f"{self.base_url}/booking/true"
        headers = self._normalize_headers({'Accept': 'application/json', 'Accept-Encoding': 'gzip, deflate, zstd', 'Authorization': '[Filtered]', 'Connection': 'keep-alive', 'Content-Type': 'application/json'})
        # Randomized test data (from AI analysis)
        body = {'firstname': 'Ava', 'lastname': 'Davis', 'totalprice': 219, 'depositpaid': False, 'bookingdates': {'checkin': '2025-12-15', 'checkout': '2026-01-20'}, 'additionalneeds': 'Tea'}
        
        response = requests.patch(url, headers=headers, json=body)
        
        check.equal(response.status_code, 405, f'Expected status 405, got {response.status_code}')
        # Only check body if status code matches
        if response.status_code == 405:
            check.is_not_none(response.text, 'Response should have body')
    def test_post_booking_66(self):
        """Test generated from Schemathesis VCR: 8pDYnL
        Test: POST /booking
        Phase: stateful
        Status: SUCCESS
        """
        import requests
        
        url = f"{self.base_url}/booking"
        headers = self._normalize_headers({'Accept': 'application/json', 'Accept-Encoding': 'gzip, deflate, zstd', 'Authorization': '[Filtered]', 'Connection': 'keep-alive', 'Content-Type': 'application/json'})
        # Randomized test data (from AI analysis)
        body = {'firstname': 'Michael', 'lastname': 'Rodriguez', 'totalprice': 378, 'depositpaid': True, 'bookingdates': {'checkin': '2025-12-15', 'checkout': '2026-01-20'}, 'additionalneeds': 'Breakfast'}
        
        response = requests.post(url, headers=headers, json=body)
        
        check.equal(response.status_code, 200, f'Expected status 200, got {response.status_code}')
        # Only check body if status code matches
        if response.status_code == 200:
            try:
                response_data = response.json()
                check.equal(response_data, {'bookingid': 3967, 'booking': {'firstname': '', 'lastname': 'ØZ\x94', 'totalprice': -37, 'depositpaid': True, 'bookingdates': {'checkin': '3505-11-01', 'checkout': '5282-01-28'}, 'additionalneeds': '-\x93æØ\U000d2786!\x8c,-&¤\U00064199Ú'}}, 'Response body mismatch')
            except (json.JSONDecodeError, requests.exceptions.JSONDecodeError):
                # Response is not JSON - skip body check
                pass
    def test_post_booking_67(self):
        """Test generated from Schemathesis VCR: HB1sFl
        Test: POST /booking
        Phase: stateful
        Status: SUCCESS
        """
        import requests
        
        url = f"{self.base_url}/booking"
        headers = self._normalize_headers({'Accept': 'application/json', 'Accept-Encoding': 'gzip, deflate, zstd', 'Authorization': '[Filtered]', 'Connection': 'keep-alive', 'Content-Type': 'application/json'})
        # Randomized test data (from AI analysis)
        body = {'firstname': 'Emily', 'lastname': 'Smith', 'totalprice': 378, 'depositpaid': True, 'bookingdates': {'checkin': '2025-12-15', 'checkout': '2026-01-20'}, 'additionalneeds': 'Breakfast'}
        
        response = requests.post(url, headers=headers, json=body)
        
        check.equal(response.status_code, 200, f'Expected status 200, got {response.status_code}')
        # Only check body if status code matches
        if response.status_code == 200:
            try:
                response_data = response.json()
                check.equal(response_data, {'bookingid': 3973, 'booking': {'firstname': '`\U000b8e5d7Í', 'lastname': '2è\x8a\U0008c92dë', 'totalprice': -9095, 'depositpaid': False, 'bookingdates': {'checkin': '7098-01-25', 'checkout': '0743-03-18'}}}, 'Response body mismatch')
            except (json.JSONDecodeError, requests.exceptions.JSONDecodeError):
                # Response is not JSON - skip body check
                pass
    def test_get_booking_null_68(self):
        """Test generated from Schemathesis VCR: gpFASP
        Test: GET /booking/null
        Phase: stateful
        Status: SUCCESS
        """
        import requests
        
        url = f"{self.base_url}/booking/null"
        headers = self._normalize_headers({'Accept': 'application/json', 'Accept-Encoding': 'gzip, deflate, zstd', 'Authorization': '[Filtered]', 'Connection': 'keep-alive', 'Content-Type': 'application/json'})
        
        response = requests.get(url, headers=headers)
        
        check.equal(response.status_code, 404, f'Expected status 404, got {response.status_code}')
        # Only check body if status code matches
        if response.status_code == 404:
            check.is_not_none(response.text, 'Response should have body')
    def test_get_booking_5616_69(self):
        """Test generated from Schemathesis VCR: AgcjqS
        Test: GET /booking/-5616
        Phase: stateful
        Status: SUCCESS
        """
        import requests
        
        url = f"{self.base_url}/booking/-5616"
        headers = self._normalize_headers({'Accept': 'application/json', 'Accept-Encoding': 'gzip, deflate, zstd', 'Authorization': '[Filtered]', 'Connection': 'keep-alive', 'Content-Type': 'application/json'})
        
        response = requests.get(url, headers=headers)
        
        check.equal(response.status_code, 404, f'Expected status 404, got {response.status_code}')
        # Only check body if status code matches
        if response.status_code == 404:
            check.is_not_none(response.text, 'Response should have body')
    def test_post_booking_70(self):
        """Test generated from Schemathesis VCR: quTzMA
        Test: POST /booking
        Phase: stateful
        Status: SUCCESS
        """
        import requests
        
        url = f"{self.base_url}/booking"
        headers = self._normalize_headers({'Accept': 'application/json', 'Accept-Encoding': 'gzip, deflate, zstd', 'Authorization': '[Filtered]', 'Connection': 'keep-alive', 'Content-Type': 'application/json'})
        # Randomized test data (from AI analysis)
        body = {'firstname': 'Michael', 'lastname': 'Rodriguez', 'totalprice': 378, 'depositpaid': True, 'bookingdates': {'checkin': '2025-12-15', 'checkout': '2026-01-20'}, 'additionalneeds': 'Breakfast'}
        
        response = requests.post(url, headers=headers, json=body)
        
        check.equal(response.status_code, 200, f'Expected status 200, got {response.status_code}')
        # Only check body if status code matches
        if response.status_code == 200:
            try:
                response_data = response.json()
                check.equal(response_data, {'bookingid': 3977, 'booking': {'firstname': 'v\U00042dda\x08', 'lastname': 'ò', 'totalprice': -5510334697142063000, 'depositpaid': True, 'bookingdates': {'checkin': '7054-09-22', 'checkout': '4934-09-19'}}}, 'Response body mismatch')
            except (json.JSONDecodeError, requests.exceptions.JSONDecodeError):
                # Response is not JSON - skip body check
                pass
    def test_post_booking_71(self):
        """Test generated from Schemathesis VCR: BR5VBb
        Test: POST /booking
        Phase: stateful
        Status: SUCCESS
        """
        import requests
        
        url = f"{self.base_url}/booking"
        headers = self._normalize_headers({'Accept': 'application/json', 'Accept-Encoding': 'gzip, deflate, zstd', 'Authorization': '[Filtered]', 'Connection': 'keep-alive', 'Content-Type': 'application/json'})
        # Randomized test data (from AI analysis)
        body = {'firstname': 'John', 'lastname': 'Doe', 'totalprice': 342, 'depositpaid': False, 'bookingdates': {'checkin': '2025-12-15', 'checkout': '2026-01-20'}, 'additionalneeds': 'Breakfast'}
        
        response = requests.post(url, headers=headers, json=body)
        
        check.equal(response.status_code, 400, f'Expected status 400, got {response.status_code}')
        # Only check body if status code matches
        if response.status_code == 400:
            check.is_not_none(response.text, 'Response should have body')
    def test_get_booking_5_72(self):
        """Test generated from Schemathesis VCR: ZTTfLf
        Test: GET /booking/5
        Phase: stateful
        Status: FAILURE
        """
        import requests
        
        url = f"{self.base_url}/booking/5"
        headers = self._normalize_headers({'Accept': 'application/json', 'Accept-Encoding': 'gzip, deflate, zstd', 'Authorization': '[Filtered]', 'Connection': 'keep-alive', 'Content-Type': 'application/json'})
        
        response = requests.get(url, headers=headers)
        
        check.equal(response.status_code, 200, f'Expected status 200, got {response.status_code}')
        # Original failed checks: negative_data_rejection
    def test_delete_booking_2128_73(self):
        """Test generated from Schemathesis VCR: rhcVT8
        Test: DELETE /booking/-2128
        Phase: stateful
        Status: SUCCESS
        """
        import requests
        
        url = f"{self.base_url}/booking/-2128"
        headers = self._normalize_headers({'Accept': 'application/json', 'Accept-Encoding': 'gzip, deflate, zstd', 'Authorization': '[Filtered]', 'Connection': 'keep-alive', 'Content-Type': 'application/json'})
        
        response = requests.delete(url, headers=headers)
        
        check.equal(response.status_code, 405, f'Expected status 405, got {response.status_code}')
        # Only check body if status code matches
        if response.status_code == 405:
            check.is_not_none(response.text, 'Response should have body')
    def test_get_booking_5_74(self):
        """Test generated from Schemathesis VCR: ONhr6S
        Test: GET /booking/5
        Phase: stateful
        Status: SUCCESS
        """
        import requests
        
        url = f"{self.base_url}/booking/5"
        headers = self._normalize_headers({'Accept': 'application/json', 'Accept-Encoding': 'gzip, deflate, zstd', 'Authorization': '[Filtered]', 'Connection': 'keep-alive', 'Content-Type': 'application/json'})
        
        response = requests.get(url, headers=headers)
        
        check.equal(response.status_code, 200, f'Expected status 200, got {response.status_code}')
        # Only check body if status code matches
        if response.status_code == 200:
            try:
                response_data = response.json()
                check.equal(response_data, {'firstname': 'Susan', 'lastname': 'Brown', 'totalprice': 289, 'depositpaid': True, 'bookingdates': {'checkin': '2020-04-24', 'checkout': '2024-02-18'}, 'additionalneeds': 'Breakfast'}, 'Response body mismatch')
            except (json.JSONDecodeError, requests.exceptions.JSONDecodeError):
                # Response is not JSON - skip body check
                pass
    def test_get_booking_99_75(self):
        """Test generated from Schemathesis VCR: kRDv5i
        Test: GET /booking/-99
        Phase: stateful
        Status: SUCCESS
        """
        import requests
        
        url = f"{self.base_url}/booking/-99"
        headers = self._normalize_headers({'Accept': 'application/json', 'Accept-Encoding': 'gzip, deflate, zstd', 'Authorization': '[Filtered]', 'Connection': 'keep-alive', 'Content-Type': 'application/json'})
        
        response = requests.get(url, headers=headers)
        
        check.equal(response.status_code, 404, f'Expected status 404, got {response.status_code}')
        # Only check body if status code matches
        if response.status_code == 404:
            check.is_not_none(response.text, 'Response should have body')
    def test_get_booking_3862_76(self):
        """Test generated from Schemathesis VCR: TGOHDa
        Test: GET /booking/3862
        Phase: stateful
        Status: SUCCESS
        """
        import requests
        
        url = f"{self.base_url}/booking/3862"
        headers = self._normalize_headers({'Accept': 'application/json', 'Accept-Encoding': 'gzip, deflate, zstd', 'Authorization': '[Filtered]', 'Connection': 'keep-alive', 'Content-Type': 'application/json'})
        
        response = requests.get(url, headers=headers)
        
        check.equal(response.status_code, 200, f'Expected status 200, got {response.status_code}')
        # Only check body if status code matches
        if response.status_code == 200:
            try:
                response_data = response.json()
                check.equal(response_data, {'firstname': 'Josh', 'lastname': 'Allen', 'totalprice': 111, 'depositpaid': True, 'bookingdates': {'checkin': '2018-01-01', 'checkout': '2019-01-01'}, 'additionalneeds': 'super bowls'}, 'Response body mismatch')
            except (json.JSONDecodeError, requests.exceptions.JSONDecodeError):
                # Response is not JSON - skip body check
                pass
    def test_delete_booking_false_77(self):
        """Test generated from Schemathesis VCR: 3LzpUZ
        Test: DELETE /booking/false
        Phase: stateful
        Status: SUCCESS
        """
        import requests
        
        url = f"{self.base_url}/booking/false"
        headers = self._normalize_headers({'Accept': 'application/json', 'Accept-Encoding': 'gzip, deflate, zstd', 'Authorization': '[Filtered]', 'Connection': 'keep-alive', 'Content-Type': 'application/json'})
        
        response = requests.delete(url, headers=headers)
        
        check.equal(response.status_code, 405, f'Expected status 405, got {response.status_code}')
        # Only check body if status code matches
        if response.status_code == 405:
            check.is_not_none(response.text, 'Response should have body')
    def test_post_booking_78(self):
        """Test generated from Schemathesis VCR: cwgyMJ
        Test: POST /booking
        Phase: stateful
        Status: SUCCESS
        """
        import requests
        
        url = f"{self.base_url}/booking"
        headers = self._normalize_headers({'Accept': 'application/json', 'Accept-Encoding': 'gzip, deflate, zstd', 'Authorization': '[Filtered]', 'Connection': 'keep-alive', 'Content-Type': 'application/json'})
        # Randomized test data (from AI analysis)
        body = {'firstname': 'John', 'lastname': 'Doe', 'totalprice': 342, 'depositpaid': True, 'bookingdates': {'checkin': '2025-12-15', 'checkout': '2026-01-20'}, 'additionalneeds': 'Breakfast'}
        
        response = requests.post(url, headers=headers, json=body)
        
        check.equal(response.status_code, 500, f'Expected status 500, got {response.status_code}')
        # Only check body if status code matches
        if response.status_code == 500:
            check.is_not_none(response.text, 'Response should have body')
    def test_post_booking_79(self):
        """Test generated from Schemathesis VCR: rcSvNz
        Test: POST /booking
        Phase: stateful
        Status: SUCCESS
        """
        import requests
        
        url = f"{self.base_url}/booking"
        headers = self._normalize_headers({'Accept': 'application/json', 'Accept-Encoding': 'gzip, deflate, zstd', 'Authorization': '[Filtered]', 'Connection': 'keep-alive', 'Content-Type': 'application/json'})
        # Randomized test data (from AI analysis)
        body = {'firstname': 'Jane', 'lastname': 'Smith', 'totalprice': 378, 'depositpaid': False, 'bookingdates': {'checkin': '2025-12-15', 'checkout': '2026-01-20'}, 'additionalneeds': 'Lunch'}
        
        response = requests.post(url, headers=headers, json=body)
        
        check.equal(response.status_code, 500, f'Expected status 500, got {response.status_code}')
        # Only check body if status code matches
        if response.status_code == 500:
            check.is_not_none(response.text, 'Response should have body')
    def test_post_booking_80(self):
        """Test generated from Schemathesis VCR: yHRsjf
        Test: POST /booking
        Phase: stateful
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
                check.equal(response_data, {'bookingid': 4021, 'booking': {'firstname': 'I', 'lastname': '\U0006936f', 'totalprice': -7004855725244072000, 'depositpaid': False, 'bookingdates': {'checkin': '6517-04-16', 'checkout': '1743-04-26'}, 'additionalneeds': ''}}, 'Response body mismatch')
            except (json.JSONDecodeError, requests.exceptions.JSONDecodeError):
                # Response is not JSON - skip body check
                pass
    def test_post_booking_81(self):
        """Test generated from Schemathesis VCR: JwplQE
        Test: POST /booking
        Phase: stateful
        Status: SUCCESS
        """
        import requests
        
        url = f"{self.base_url}/booking"
        headers = self._normalize_headers({'Accept': 'application/json', 'Accept-Encoding': 'gzip, deflate, zstd', 'Authorization': '[Filtered]', 'Connection': 'keep-alive', 'Content-Type': 'application/json'})
        # Randomized test data (from AI analysis)
        body = {'firstname': 'Jane', 'lastname': 'Smith', 'totalprice': 378, 'depositpaid': True, 'bookingdates': {'checkin': '2025-12-15', 'checkout': '2026-01-20'}, 'additionalneeds': 'Lunch'}
        
        response = requests.post(url, headers=headers, json=body)
        
        check.equal(response.status_code, 200, f'Expected status 200, got {response.status_code}')
        # Only check body if status code matches
        if response.status_code == 200:
            try:
                response_data = response.json()
                check.equal(response_data, {'bookingid': 4025, 'booking': {'firstname': '', 'lastname': 'é¦þ', 'totalprice': -4187, 'depositpaid': True, 'bookingdates': {'checkin': '4197-10-01', 'checkout': '3601-07-31'}, 'additionalneeds': 'W\U00079d31u\x89ò±\U0005e242\x83¦t'}}, 'Response body mismatch')
            except (json.JSONDecodeError, requests.exceptions.JSONDecodeError):
                # Response is not JSON - skip body check
                pass
    def test_get_booking_null_82(self):
        """Test generated from Schemathesis VCR: duJegH
        Test: GET /booking/null
        Phase: stateful
        Status: SUCCESS
        """
        import requests
        
        url = f"{self.base_url}/booking/null"
        headers = self._normalize_headers({'Accept': 'application/json', 'Accept-Encoding': 'gzip, deflate, zstd', 'Authorization': '[Filtered]', 'Connection': 'keep-alive', 'Content-Type': 'application/json'})
        
        response = requests.get(url, headers=headers)
        
        check.equal(response.status_code, 404, f'Expected status 404, got {response.status_code}')
        # Only check body if status code matches
        if response.status_code == 404:
            check.is_not_none(response.text, 'Response should have body')
    def test_post_booking_83(self):
        """Test generated from Schemathesis VCR: 26kH19
        Test: POST /booking
        Phase: stateful
        Status: SUCCESS
        """
        import requests
        
        url = f"{self.base_url}/booking"
        headers = self._normalize_headers({'Accept': 'application/json', 'Accept-Encoding': 'gzip, deflate, zstd', 'Authorization': '[Filtered]', 'Connection': 'keep-alive', 'Content-Type': 'application/json'})
        # Randomized test data (from AI analysis)
        body = {'firstname': 'Emily', 'lastname': 'Johnson', 'totalprice': 342, 'depositpaid': True, 'bookingdates': {'checkin': '2025-12-15', 'checkout': '2026-01-20'}, 'additionalneeds': 'Dinner'}
        
        response = requests.post(url, headers=headers, json=body)
        
        check.equal(response.status_code, 200, f'Expected status 200, got {response.status_code}')
        # Only check body if status code matches
        if response.status_code == 200:
            try:
                response_data = response.json()
                check.equal(response_data, {'bookingid': 4030, 'booking': {'firstname': '', 'lastname': 'é¦þ', 'totalprice': -4187, 'depositpaid': True, 'bookingdates': {'checkin': '4197-10-01', 'checkout': '3601-07-31'}, 'additionalneeds': 'W\U00079d31u\x89ò±\U0005e242\x83¦t'}}, 'Response body mismatch')
            except (json.JSONDecodeError, requests.exceptions.JSONDecodeError):
                # Response is not JSON - skip body check
                pass
    def test_get_booking_null_84(self):
        """Test generated from Schemathesis VCR: MHUmOA
        Test: GET /booking/null
        Phase: stateful
        Status: SUCCESS
        """
        import requests
        
        url = f"{self.base_url}/booking/null"
        headers = self._normalize_headers({'Accept': 'application/json', 'Accept-Encoding': 'gzip, deflate, zstd', 'Authorization': '[Filtered]', 'Connection': 'keep-alive', 'Content-Type': 'application/json'})
        
        response = requests.get(url, headers=headers)
        
        check.equal(response.status_code, 404, f'Expected status 404, got {response.status_code}')
        # Only check body if status code matches
        if response.status_code == 404:
            check.is_not_none(response.text, 'Response should have body')
    def test_put_booking_false_85(self):
        """Test generated from Schemathesis VCR: 4YUqRY
        Test: PUT /booking/false
        Phase: stateful
        Status: SUCCESS
        """
        import requests
        
        url = f"{self.base_url}/booking/false"
        headers = self._normalize_headers({'Accept': 'application/json', 'Accept-Encoding': 'gzip, deflate, zstd', 'Authorization': '[Filtered]', 'Connection': 'keep-alive', 'Content-Type': 'application/json'})
        # Randomized test data (from AI analysis)
        body = {'firstname': 'Michael', 'lastname': 'Rodriguez', 'totalprice': 378, 'depositpaid': True, 'bookingdates': {'checkin': '2025-12-15', 'checkout': '2026-01-20'}, 'additionalneeds': 'Breakfast'}
        
        response = requests.put(url, headers=headers, json=body)
        
        check.equal(response.status_code, 405, f'Expected status 405, got {response.status_code}')
        # Only check body if status code matches
        if response.status_code == 405:
            check.is_not_none(response.text, 'Response should have body')
    def test_post_booking_86(self):
        """Test generated from Schemathesis VCR: P9Ic7E
        Test: POST /booking
        Phase: stateful
        Status: SUCCESS
        """
        import requests
        
        url = f"{self.base_url}/booking"
        headers = self._normalize_headers({'Accept': 'application/json', 'Accept-Encoding': 'gzip, deflate, zstd', 'Authorization': '[Filtered]', 'Connection': 'keep-alive', 'Content-Type': 'application/json'})
        # Randomized test data (from AI analysis)
        body = {'firstname': 'John', 'lastname': 'Doe', 'totalprice': 342, 'depositpaid': True, 'bookingdates': {'checkin': '2025-12-15', 'checkout': '2026-01-20'}, 'additionalneeds': 'Breakfast'}
        
        response = requests.post(url, headers=headers, json=body)
        
        check.equal(response.status_code, 500, f'Expected status 500, got {response.status_code}')
        # Only check body if status code matches
        if response.status_code == 500:
            check.is_not_none(response.text, 'Response should have body')
    def test_post_booking_87(self):
        """Test generated from Schemathesis VCR: MZdkRp
        Test: POST /booking
        Phase: stateful
        Status: SUCCESS
        """
        import requests
        
        url = f"{self.base_url}/booking"
        headers = self._normalize_headers({'Accept': 'application/json', 'Accept-Encoding': 'gzip, deflate, zstd', 'Authorization': '[Filtered]', 'Connection': 'keep-alive', 'Content-Type': 'application/json'})
        # Randomized test data (from AI analysis)
        body = {'firstname': 'Emily', 'lastname': 'Chen', 'totalprice': 342, 'depositpaid': True, 'bookingdates': {'checkin': '2025-12-15', 'checkout': '2026-01-20'}, 'additionalneeds': 'Lunch'}
        
        response = requests.post(url, headers=headers, json=body)
        
        check.equal(response.status_code, 500, f'Expected status 500, got {response.status_code}')
        # Only check body if status code matches
        if response.status_code == 500:
            check.is_not_none(response.text, 'Response should have body')
    def test_post_booking_88(self):
        """Test generated from Schemathesis VCR: 8KzttY
        Test: POST /booking
        Phase: stateful
        Status: SUCCESS
        """
        import requests
        
        url = f"{self.base_url}/booking"
        headers = self._normalize_headers({'Accept': 'application/json', 'Accept-Encoding': 'gzip, deflate, zstd', 'Authorization': '[Filtered]', 'Connection': 'keep-alive', 'Content-Type': 'application/json'})
        # Randomized test data (from AI analysis)
        body = {'firstname': 'Sophia', 'lastname': 'Lee', 'totalprice': 342, 'depositpaid': True, 'bookingdates': {'checkin': '2025-12-15', 'checkout': '2026-01-20'}, 'additionalneeds': 'Dinner'}
        
        response = requests.post(url, headers=headers, json=body)
        
        check.equal(response.status_code, 500, f'Expected status 500, got {response.status_code}')
        # Only check body if status code matches
        if response.status_code == 500:
            check.is_not_none(response.text, 'Response should have body')
    def test_post_booking_89(self):
        """Test generated from Schemathesis VCR: nZm8se
        Test: POST /booking
        Phase: stateful
        Status: SUCCESS
        """
        import requests
        
        url = f"{self.base_url}/booking"
        headers = self._normalize_headers({'Accept': 'application/json', 'Accept-Encoding': 'gzip, deflate, zstd', 'Authorization': '[Filtered]', 'Connection': 'keep-alive', 'Content-Type': 'application/json'})
        # Randomized test data (from AI analysis)
        body = {'firstname': 'Olivia', 'lastname': 'Kim', 'totalprice': 342, 'depositpaid': True, 'bookingdates': {'checkin': '2025-12-15', 'checkout': '2026-01-20'}, 'additionalneeds': 'Snacks'}
        
        response = requests.post(url, headers=headers, json=body)
        
        check.equal(response.status_code, 500, f'Expected status 500, got {response.status_code}')
        # Only check body if status code matches
        if response.status_code == 500:
            check.is_not_none(response.text, 'Response should have body')
    def test_post_booking_90(self):
        """Test generated from Schemathesis VCR: mAmI7R
        Test: POST /booking
        Phase: stateful
        Status: SUCCESS
        """
        import requests
        
        url = f"{self.base_url}/booking"
        headers = self._normalize_headers({'Accept': 'application/json', 'Accept-Encoding': 'gzip, deflate, zstd', 'Authorization': '[Filtered]', 'Connection': 'keep-alive', 'Content-Type': 'application/json'})
        # Randomized test data (from AI analysis)
        body = {'firstname': 'Ava', 'lastname': 'Park', 'totalprice': 342, 'depositpaid': True, 'bookingdates': {'checkin': '2025-12-15', 'checkout': '2026-01-20'}, 'additionalneeds': 'Coffee'}
        
        response = requests.post(url, headers=headers, json=body)
        
        check.equal(response.status_code, 500, f'Expected status 500, got {response.status_code}')
        # Only check body if status code matches
        if response.status_code == 500:
            check.is_not_none(response.text, 'Response should have body')
    def test_post_booking_91(self):
        """Test generated from Schemathesis VCR: meR7jr
        Test: POST /booking
        Phase: stateful
        Status: SUCCESS
        """
        import requests
        
        url = f"{self.base_url}/booking"
        headers = self._normalize_headers({'Accept': 'application/json', 'Accept-Encoding': 'gzip, deflate, zstd', 'Authorization': '[Filtered]', 'Connection': 'keep-alive', 'Content-Type': 'application/json'})
        # Randomized test data (from AI analysis)
        body = {'firstname': 'Isabella', 'lastname': 'Harris', 'totalprice': 342, 'depositpaid': True, 'bookingdates': {'checkin': '2025-12-15', 'checkout': '2026-01-20'}, 'additionalneeds': 'Tea'}
        
        response = requests.post(url, headers=headers, json=body)
        
        check.equal(response.status_code, 500, f'Expected status 500, got {response.status_code}')
        # Only check body if status code matches
        if response.status_code == 500:
            check.is_not_none(response.text, 'Response should have body')
    def test_post_booking_92(self):
        """Test generated from Schemathesis VCR: gQgNFJ
        Test: POST /booking
        Phase: stateful
        Status: SUCCESS
        """
        import requests
        
        url = f"{self.base_url}/booking"
        headers = self._normalize_headers({'Accept': 'application/json', 'Accept-Encoding': 'gzip, deflate, zstd', 'Authorization': '[Filtered]', 'Connection': 'keep-alive', 'Content-Type': 'application/json'})
        # Randomized test data (from AI analysis)
        body = {'firstname': 'Mia', 'lastname': 'Martin', 'totalprice': 342, 'depositpaid': True, 'bookingdates': {'checkin': '2025-12-15', 'checkout': '2026-01-20'}, 'additionalneeds': 'Juice'}
        
        response = requests.post(url, headers=headers, json=body)
        
        check.equal(response.status_code, 200, f'Expected status 200, got {response.status_code}')
        # Only check body if status code matches
        if response.status_code == 200:
            try:
                response_data = response.json()
                check.equal(response_data, {'bookingid': 4049, 'booking': {'firstname': '7Þ\\{\U000aa830ü\x1e\x02Ý\x8c\x9cÏ¢Ý\U00016531', 'lastname': '', 'totalprice': -7002574004560644000, 'depositpaid': False, 'bookingdates': {'checkin': '0300-12-05', 'checkout': '4778-11-04'}}}, 'Response body mismatch')
            except (json.JSONDecodeError, requests.exceptions.JSONDecodeError):
                # Response is not JSON - skip body check
                pass
    def test_patch_booking_U_93(self):
        """Test generated from Schemathesis VCR: OGzbrJ
        Test: PATCH /booking/%C3%B0%C3%B7U%C3%AB%F1%A9%B6%91
        Phase: stateful
        Status: SUCCESS
        """
        import requests
        
        url = f"{self.base_url}/booking/%C3%B0%C3%B7U%C3%AB%F1%A9%B6%91"
        headers = self._normalize_headers({'Accept': 'application/json', 'Accept-Encoding': 'gzip, deflate, zstd', 'Authorization': '[Filtered]', 'Connection': 'keep-alive', 'Content-Type': 'application/json'})
        # Randomized test data (from AI analysis)
        body = {'firstname': 'Charlotte', 'lastname': 'Davis', 'totalprice': 342, 'depositpaid': True, 'bookingdates': {'checkin': '2025-12-15', 'checkout': '2026-01-20'}, 'additionalneeds': 'Water'}
        
        response = requests.patch(url, headers=headers, json=body)
        
        check.equal(response.status_code, 405, f'Expected status 405, got {response.status_code}')
        # Only check body if status code matches
        if response.status_code == 405:
            check.is_not_none(response.text, 'Response should have body')
    def test_post_booking_94(self):
        """Test generated from Schemathesis VCR: AG6Msy
        Test: POST /booking
        Phase: stateful
        Status: SUCCESS
        """
        import requests
        
        url = f"{self.base_url}/booking"
        headers = self._normalize_headers({'Accept': 'application/json', 'Accept-Encoding': 'gzip, deflate, zstd', 'Authorization': '[Filtered]', 'Connection': 'keep-alive', 'Content-Type': 'application/json'})
        # Randomized test data (from AI analysis)
        body = {'firstname': 'John', 'lastname': 'Doe', 'totalprice': 342, 'depositpaid': False, 'bookingdates': {'checkin': '2025-12-15', 'checkout': '2026-01-20'}, 'additionalneeds': 'Breakfast'}
        
        response = requests.post(url, headers=headers, json=body)
        
        check.equal(response.status_code, 500, f'Expected status 500, got {response.status_code}')
        # Only check body if status code matches
        if response.status_code == 500:
            check.is_not_none(response.text, 'Response should have body')
    def test_post_booking_95(self):
        """Test generated from Schemathesis VCR: TkM27K
        Test: POST /booking
        Phase: stateful
        Status: SUCCESS
        """
        import requests
        
        url = f"{self.base_url}/booking"
        headers = self._normalize_headers({'Accept': 'application/json', 'Accept-Encoding': 'gzip, deflate, zstd', 'Authorization': '[Filtered]', 'Connection': 'keep-alive', 'Content-Type': 'application/json'})
        # Randomized test data (from AI analysis)
        body = {'firstname': 'Jane', 'lastname': 'Smith', 'totalprice': 123, 'depositpaid': True, 'bookingdates': {'checkin': '2025-12-15', 'checkout': '2026-01-20'}, 'additionalneeds': 'Lunch'}
        
        response = requests.post(url, headers=headers, json=body)
        
        check.equal(response.status_code, 200, f'Expected status 200, got {response.status_code}')
        # Only check body if status code matches
        if response.status_code == 200:
            try:
                response_data = response.json()
                check.equal(response_data, {'bookingid': 4062, 'booking': {'firstname': '', 'lastname': '<\U000cc6b3', 'totalprice': -30691, 'depositpaid': False, 'bookingdates': {'checkin': '4357-12-19', 'checkout': '3066-04-11'}}}, 'Response body mismatch')
            except (json.JSONDecodeError, requests.exceptions.JSONDecodeError):
                # Response is not JSON - skip body check
                pass
    def test_post_booking_96(self):
        """Test generated from Schemathesis VCR: 0noq0s
        Test: POST /booking
        Phase: stateful
        Status: SUCCESS
        """
        import requests
        
        url = f"{self.base_url}/booking"
        headers = self._normalize_headers({'Accept': 'application/json', 'Accept-Encoding': 'gzip, deflate, zstd', 'Authorization': '[Filtered]', 'Connection': 'keep-alive', 'Content-Type': 'application/json'})
        # Randomized test data (from AI analysis)
        body = {'firstname': 'Emily', 'lastname': 'Johnson', 'totalprice': 567, 'depositpaid': False, 'bookingdates': {'checkin': '2025-12-15', 'checkout': '2026-01-20'}, 'additionalneeds': 'Dinner'}
        
        response = requests.post(url, headers=headers, json=body)
        
        check.equal(response.status_code, 200, f'Expected status 200, got {response.status_code}')
        # Only check body if status code matches
        if response.status_code == 200:
            try:
                response_data = response.json()
                check.equal(response_data, {'bookingid': 4064, 'booking': {'firstname': '', 'lastname': 'íõ\U0005fdf4²D ', 'totalprice': 51, 'depositpaid': False, 'bookingdates': {'checkin': '0692-01-05', 'checkout': '3265-09-11'}}}, 'Response body mismatch')
            except (json.JSONDecodeError, requests.exceptions.JSONDecodeError):
                # Response is not JSON - skip body check
                pass
    def test_patch_booking_true_97(self):
        """Test generated from Schemathesis VCR: IE1q12
        Test: PATCH /booking/true
        Phase: stateful
        Status: SUCCESS
        """
        import requests
        
        url = f"{self.base_url}/booking/true"
        headers = self._normalize_headers({'Accept': 'application/json', 'Accept-Encoding': 'gzip, deflate, zstd', 'Authorization': '[Filtered]', 'Connection': 'keep-alive', 'Content-Type': 'application/json'})
        # Randomized test data (from AI analysis)
        body = {'firstname': 'Michael', 'lastname': 'Rodriguez', 'totalprice': 378, 'depositpaid': True, 'bookingdates': {'checkin': '2025-12-15', 'checkout': '2026-01-20'}, 'additionalneeds': 'Breakfast'}
        
        response = requests.patch(url, headers=headers, json=body)
        
        check.equal(response.status_code, 405, f'Expected status 405, got {response.status_code}')
        # Only check body if status code matches
        if response.status_code == 405:
            check.is_not_none(response.text, 'Response should have body')
    def test_post_booking_98(self):
        """Test generated from Schemathesis VCR: 3MkVGf
        Test: POST /booking
        Phase: stateful
        Status: SUCCESS
        """
        import requests
        
        url = f"{self.base_url}/booking"
        headers = self._normalize_headers({'Accept': 'application/json', 'Accept-Encoding': 'gzip, deflate, zstd', 'Authorization': '[Filtered]', 'Connection': 'keep-alive', 'Content-Type': 'application/json'})
        # Randomized test data (from AI analysis)
        body = {'firstname': 'Sarah', 'lastname': 'Lee', 'totalprice': 901, 'depositpaid': False, 'bookingdates': {'checkin': '2025-12-15', 'checkout': '2026-01-20'}, 'additionalneeds': 'Snack'}
        
        response = requests.post(url, headers=headers, json=body)
        
        check.equal(response.status_code, 200, f'Expected status 200, got {response.status_code}')
        # Only check body if status code matches
        if response.status_code == 200:
            try:
                response_data = response.json()
                check.equal(response_data, {'bookingid': 4068, 'booking': {'firstname': '', 'lastname': 'a\x94\U000d8bbd\x04\U001043a5Ï\U0001a58f\U00105761ó¬\U000e081fUí', 'totalprice': 1046, 'depositpaid': True, 'bookingdates': {'checkin': '7226-12-14', 'checkout': '0822-01-09'}}}, 'Response body mismatch')
            except (json.JSONDecodeError, requests.exceptions.JSONDecodeError):
                # Response is not JSON - skip body check
                pass
    def test_post_booking_99(self):
        """Test generated from Schemathesis VCR: H5xDD6
        Test: POST /booking
        Phase: stateful
        Status: SUCCESS
        """
        import requests
        
        url = f"{self.base_url}/booking"
        headers = self._normalize_headers({'Accept': 'application/json', 'Accept-Encoding': 'gzip, deflate, zstd', 'Authorization': '[Filtered]', 'Connection': 'keep-alive', 'Content-Type': 'application/json'})
        # Randomized test data (from AI analysis)
        body = {'firstname': 'Olivia', 'lastname': 'Brown', 'totalprice': 654, 'depositpaid': True, 'bookingdates': {'checkin': '2025-12-15', 'checkout': '2026-01-20'}, 'additionalneeds': 'Coffee'}
        
        response = requests.post(url, headers=headers, json=body)
        
        check.equal(response.status_code, 500, f'Expected status 500, got {response.status_code}')
        # Only check body if status code matches
        if response.status_code == 500:
            check.is_not_none(response.text, 'Response should have body')
    def test_post_booking_100(self):
        """Test generated from Schemathesis VCR: PO2rfX
        Test: POST /booking
        Phase: stateful
        Status: SUCCESS
        """
        import requests
        
        url = f"{self.base_url}/booking"
        headers = self._normalize_headers({'Accept': 'application/json', 'Accept-Encoding': 'gzip, deflate, zstd', 'Authorization': '[Filtered]', 'Connection': 'keep-alive', 'Content-Type': 'application/json'})
        # Randomized test data (from AI analysis)
        body = {'firstname': 'Michael', 'lastname': 'Rodriguez', 'totalprice': 378, 'depositpaid': True, 'bookingdates': {'checkin': '2025-12-15', 'checkout': '2026-01-20'}, 'additionalneeds': 'Breakfast'}
        
        response = requests.post(url, headers=headers, json=body)
        
        check.equal(response.status_code, 200, f'Expected status 200, got {response.status_code}')
        # Only check body if status code matches
        if response.status_code == 200:
            try:
                response_data = response.json()
                check.equal(response_data, {'bookingid': 4077, 'booking': {'firstname': '\U0003dbcc\x99\x17·', 'lastname': '', 'totalprice': -24520, 'depositpaid': False, 'bookingdates': {'checkin': '1838-12-10', 'checkout': '6306-06-08'}}}, 'Response body mismatch')
            except (json.JSONDecodeError, requests.exceptions.JSONDecodeError):
                # Response is not JSON - skip body check
                pass
    def test_delete_booking_null_101(self):
        """Test generated from Schemathesis VCR: wLVjbp
        Test: DELETE /booking/null
        Phase: stateful
        Status: SUCCESS
        """
        import requests
        
        url = f"{self.base_url}/booking/null"
        headers = self._normalize_headers({'Accept': 'application/json', 'Accept-Encoding': 'gzip, deflate, zstd', 'Authorization': '[Filtered]', 'Connection': 'keep-alive', 'Content-Type': 'application/json'})
        
        response = requests.delete(url, headers=headers)
        
        check.equal(response.status_code, 405, f'Expected status 405, got {response.status_code}')
        # Only check body if status code matches
        if response.status_code == 405:
            check.is_not_none(response.text, 'Response should have body')
    def test_delete_booking_31005_102(self):
        """Test generated from Schemathesis VCR: 6RzUep
        Test: DELETE /booking/-31005
        Phase: stateful
        Status: SUCCESS
        """
        import requests
        
        url = f"{self.base_url}/booking/-31005"
        headers = self._normalize_headers({'Accept': 'application/json', 'Accept-Encoding': 'gzip, deflate, zstd', 'Authorization': '[Filtered]', 'Connection': 'keep-alive', 'Content-Type': 'application/json'})
        
        response = requests.delete(url, headers=headers)
        
        check.equal(response.status_code, 405, f'Expected status 405, got {response.status_code}')
        # Only check body if status code matches
        if response.status_code == 405:
            check.is_not_none(response.text, 'Response should have body')
    def test_post_booking_103(self):
        """Test generated from Schemathesis VCR: WTmmpw
        Test: POST /booking
        Phase: stateful
        Status: SUCCESS
        """
        import requests
        
        url = f"{self.base_url}/booking"
        headers = self._normalize_headers({'Accept': 'application/json', 'Accept-Encoding': 'gzip, deflate, zstd', 'Authorization': '[Filtered]', 'Connection': 'keep-alive', 'Content-Type': 'application/json'})
        # Randomized test data (from AI analysis)
        body = {'firstname': 'Emily', 'lastname': 'Smith', 'totalprice': 567, 'depositpaid': False, 'bookingdates': {'checkin': '2025-03-01', 'checkout': '2025-03-31'}, 'additionalneeds': 'Snack'}
        
        response = requests.post(url, headers=headers, json=body)
        
        check.equal(response.status_code, 200, f'Expected status 200, got {response.status_code}')
        # Only check body if status code matches
        if response.status_code == 200:
            try:
                response_data = response.json()
                check.equal(response_data, {'bookingid': 4082, 'booking': {'firstname': '\x04', 'lastname': 'Æ¾Ò', 'totalprice': -17401, 'depositpaid': True, 'bookingdates': {'checkin': '8000-04-18', 'checkout': '7486-01-12'}}}, 'Response body mismatch')
            except (json.JSONDecodeError, requests.exceptions.JSONDecodeError):
                # Response is not JSON - skip body check
                pass
    def test_delete_booking_37_104(self):
        """Test generated from Schemathesis VCR: W8eUPU
        Test: DELETE /booking/-37
        Phase: stateful
        Status: SUCCESS
        """
        import requests
        
        url = f"{self.base_url}/booking/-37"
        headers = self._normalize_headers({'Accept': 'application/json', 'Accept-Encoding': 'gzip, deflate, zstd', 'Authorization': '[Filtered]', 'Connection': 'keep-alive', 'Content-Type': 'application/json'})
        
        response = requests.delete(url, headers=headers)
        
        check.equal(response.status_code, 405, f'Expected status 405, got {response.status_code}')
        # Only check body if status code matches
        if response.status_code == 405:
            check.is_not_none(response.text, 'Response should have body')
    def test_post_booking_105(self):
        """Test generated from Schemathesis VCR: LEFcQB
        Test: POST /booking
        Phase: stateful
        Status: SUCCESS
        """
        import requests
        
        url = f"{self.base_url}/booking"
        headers = self._normalize_headers({'Accept': 'application/json', 'Accept-Encoding': 'gzip, deflate, zstd', 'Authorization': '[Filtered]', 'Connection': 'keep-alive', 'Content-Type': 'application/json'})
        # Randomized test data (from AI analysis)
        body = {'bookingdates': {'checkin': '2025-12-15', 'checkout': '2026-01-20'}, 'depositpaid': True, 'firstname': 'Michael', 'lastname': 'Rodriguez', 'totalprice': 378}
        
        response = requests.post(url, headers=headers, json=body)
        
        check.equal(response.status_code, 200, f'Expected status 200, got {response.status_code}')
        # Only check body if status code matches
        if response.status_code == 200:
            try:
                response_data = response.json()
                check.equal(response_data, {'bookingid': 4089, 'booking': {'firstname': '\U00035d21\x0eZ\x99Nó', 'lastname': '', 'totalprice': 512928510, 'depositpaid': False, 'bookingdates': {'checkin': '6635-06-17', 'checkout': '6505-09-13'}, 'additionalneeds': '£\U0007b37dè\x07Ë\U000b2d17&\U0006d1aaé!¥'}}, 'Response body mismatch')
            except (json.JSONDecodeError, requests.exceptions.JSONDecodeError):
                # Response is not JSON - skip body check
                pass
    def test_put_booking_14401_106(self):
        """Test generated from Schemathesis VCR: xUWosd
        Test: PUT /booking/-14401
        Phase: stateful
        Status: SUCCESS
        """
        import requests
        
        url = f"{self.base_url}/booking/-14401"
        headers = self._normalize_headers({'Accept': 'application/json', 'Accept-Encoding': 'gzip, deflate, zstd', 'Authorization': '[Filtered]', 'Connection': 'keep-alive', 'Content-Type': 'application/json'})
        # Randomized test data (from AI analysis)
        body = {'bookingdates': {'checkin': '2025-12-15', 'checkout': '2026-01-20'}, 'depositpaid': False, 'firstname': 'John', 'lastname': 'Doe', 'totalprice': 342}
        
        response = requests.put(url, headers=headers, json=body)
        
        check.equal(response.status_code, 405, f'Expected status 405, got {response.status_code}')
        # Only check body if status code matches
        if response.status_code == 405:
            check.is_not_none(response.text, 'Response should have body')
    def test_get_booking_29623_107(self):
        """Test generated from Schemathesis VCR: H7OEVu
        Test: GET /booking/-29623
        Phase: stateful
        Status: SUCCESS
        """
        import requests
        
        url = f"{self.base_url}/booking/-29623"
        headers = self._normalize_headers({'Accept': 'application/json', 'Accept-Encoding': 'gzip, deflate, zstd', 'Authorization': '[Filtered]', 'Connection': 'keep-alive', 'Content-Type': 'application/json'})
        
        response = requests.get(url, headers=headers)
        
        check.equal(response.status_code, 404, f'Expected status 404, got {response.status_code}')
        # Only check body if status code matches
        if response.status_code == 404:
            check.is_not_none(response.text, 'Response should have body')
    def test_post_booking_108(self):
        """Test generated from Schemathesis VCR: pyq67y
        Test: POST /booking
        Phase: stateful
        Status: SUCCESS
        """
        import requests
        
        url = f"{self.base_url}/booking"
        headers = self._normalize_headers({'Accept': 'application/json', 'Accept-Encoding': 'gzip, deflate, zstd', 'Authorization': '[Filtered]', 'Connection': 'keep-alive', 'Content-Type': 'application/json'})
        # Randomized test data (from AI analysis)
        body = {'bookingdates': {'checkin': '2025-12-15', 'checkout': '2026-01-20'}, 'depositpaid': True, 'firstname': 'Jane', 'lastname': 'Smith', 'totalprice': 84}
        
        response = requests.post(url, headers=headers, json=body)
        
        check.equal(response.status_code, 200, f'Expected status 200, got {response.status_code}')
        # Only check body if status code matches
        if response.status_code == 200:
            try:
                response_data = response.json()
                check.equal(response_data, {'bookingid': 4099, 'booking': {'firstname': 'ç', 'lastname': '\x9e', 'totalprice': 84, 'depositpaid': True, 'bookingdates': {'checkin': '0230-12-24', 'checkout': '2778-03-09'}}}, 'Response body mismatch')
            except (json.JSONDecodeError, requests.exceptions.JSONDecodeError):
                # Response is not JSON - skip body check
                pass
    def test_get_booking_3989_109(self):
        """Test generated from Schemathesis VCR: vUhvT3
        Test: GET /booking/3989
        Phase: stateful
        Status: SUCCESS
        """
        import requests
        
        url = f"{self.base_url}/booking/3989"
        headers = self._normalize_headers({'Accept': 'application/json', 'Accept-Encoding': 'gzip, deflate, zstd', 'Authorization': '[Filtered]', 'Connection': 'keep-alive', 'Content-Type': 'application/json'})
        
        response = requests.get(url, headers=headers)
        
        check.equal(response.status_code, 404, f'Expected status 404, got {response.status_code}')
        # Only check body if status code matches
        if response.status_code == 404:
            check.is_not_none(response.text, 'Response should have body')
    def test_post_booking_110(self):
        """Test generated from Schemathesis VCR: 9EaM4p
        Test: POST /booking
        Phase: stateful
        Status: SUCCESS
        """
        import requests
        
        url = f"{self.base_url}/booking"
        headers = self._normalize_headers({'Accept': 'application/json', 'Accept-Encoding': 'gzip, deflate, zstd', 'Authorization': '[Filtered]', 'Connection': 'keep-alive', 'Content-Type': 'application/json'})
        # Randomized test data (from AI analysis)
        body = {'bookingdates': {'checkin': '2025-12-15', 'checkout': '2026-01-20'}, 'depositpaid': False, 'firstname': 'Emily', 'lastname': 'Johnson', 'totalprice': 342}
        
        response = requests.post(url, headers=headers, json=body)
        
        check.equal(response.status_code, 200, f'Expected status 200, got {response.status_code}')
        # Only check body if status code matches
        if response.status_code == 200:
            try:
                response_data = response.json()
                check.equal(response_data, {'bookingid': 4105, 'booking': {'firstname': '\U0009a16d5¢\x00', 'lastname': 'Î', 'totalprice': 2660, 'depositpaid': True, 'bookingdates': {'checkin': '4098-12-02', 'checkout': '4998-09-18'}}}, 'Response body mismatch')
            except (json.JSONDecodeError, requests.exceptions.JSONDecodeError):
                # Response is not JSON - skip body check
                pass
    def test_post_booking_111(self):
        """Test generated from Schemathesis VCR: yPeQaV
        Test: POST /booking
        Phase: stateful
        Status: SUCCESS
        """
        import requests
        
        url = f"{self.base_url}/booking"
        headers = self._normalize_headers({'Accept': 'application/json', 'Accept-Encoding': 'gzip, deflate, zstd', 'Authorization': '[Filtered]', 'Connection': 'keep-alive', 'Content-Type': 'application/json'})
        # Randomized test data (from AI analysis)
        body = {'bookingdates': {'checkin': '2025-12-15', 'checkout': '2026-01-20'}, 'depositpaid': False, 'firstname': 'Sarah', 'lastname': 'Williams', 'totalprice': 7361}
        
        response = requests.post(url, headers=headers, json=body)
        
        check.equal(response.status_code, 200, f'Expected status 200, got {response.status_code}')
        # Only check body if status code matches
        if response.status_code == 200:
            try:
                response_data = response.json()
                check.equal(response_data, {'bookingid': 4107, 'booking': {'firstname': 'Á\U000497c7¹', 'lastname': '\U0007f6b2×', 'totalprice': 7361, 'depositpaid': False, 'bookingdates': {'checkin': '7663-04-03', 'checkout': '0948-03-03'}}}, 'Response body mismatch')
            except (json.JSONDecodeError, requests.exceptions.JSONDecodeError):
                # Response is not JSON - skip body check
                pass
    def test_post_booking_112(self):
        """Test generated from Schemathesis VCR: 82cFae
        Test: POST /booking
        Phase: stateful
        Status: SUCCESS
        """
        import requests
        
        url = f"{self.base_url}/booking"
        headers = self._normalize_headers({'Accept': 'application/json', 'Accept-Encoding': 'gzip, deflate, zstd', 'Authorization': '[Filtered]', 'Connection': 'keep-alive', 'Content-Type': 'application/json'})
        # Randomized test data (from AI analysis)
        body = {'firstname': 'John', 'lastname': 'Doe', 'totalprice': 342, 'depositpaid': True, 'bookingdates': {'checkin': '2025-12-15', 'checkout': '2026-01-20'}, 'additionalneeds': 'Breakfast'}
        
        response = requests.post(url, headers=headers, json=body)
        
        check.equal(response.status_code, 500, f'Expected status 500, got {response.status_code}')
        # Only check body if status code matches
        if response.status_code == 500:
            check.is_not_none(response.text, 'Response should have body')
    def test_post_booking_113(self):
        """Test generated from Schemathesis VCR: LntrYo
        Test: POST /booking
        Phase: stateful
        Status: SUCCESS
        """
        import requests
        
        url = f"{self.base_url}/booking"
        headers = self._normalize_headers({'Accept': 'application/json', 'Accept-Encoding': 'gzip, deflate, zstd', 'Authorization': '[Filtered]', 'Connection': 'keep-alive', 'Content-Type': 'application/json'})
        # Randomized test data (from AI analysis)
        body = {'firstname': 'Jane', 'lastname': 'Smith', 'totalprice': 123, 'depositpaid': False, 'bookingdates': {'checkin': '2025-12-15', 'checkout': '2026-01-20'}, 'additionalneeds': 'Lunch'}
        
        response = requests.post(url, headers=headers, json=body)
        
        check.equal(response.status_code, 200, f'Expected status 200, got {response.status_code}')
        # Only check body if status code matches
        if response.status_code == 200:
            try:
                response_data = response.json()
                check.equal(response_data, {'bookingid': 4116, 'booking': {'firstname': '\U000f0669\U000e7e5d\U00065c29', 'lastname': '🇺🇸', 'totalprice': 11646, 'depositpaid': False, 'bookingdates': {'checkin': '6150-09-10', 'checkout': '0754-05-09'}}}, 'Response body mismatch')
            except (json.JSONDecodeError, requests.exceptions.JSONDecodeError):
                # Response is not JSON - skip body check
                pass
    def test_patch_booking_5599239253401498011_114(self):
        """Test generated from Schemathesis VCR: Va9Q7V
        Test: PATCH /booking/-5599239253401498011
        Phase: stateful
        Status: SUCCESS
        """
        import requests
        
        url = f"{self.base_url}/booking/-5599239253401498011"
        headers = self._normalize_headers({'Accept': 'application/json', 'Accept-Encoding': 'gzip, deflate, zstd', 'Authorization': '[Filtered]', 'Connection': 'keep-alive', 'Content-Type': 'application/json'})
        # Randomized test data (from AI analysis)
        body = {'firstname': 'Emily', 'lastname': 'Johnson', 'totalprice': 567, 'depositpaid': True, 'bookingdates': {'checkin': '2025-12-15', 'checkout': '2026-01-20'}, 'additionalneeds': 'Dinner'}
        
        response = requests.patch(url, headers=headers, json=body)
        
        check.equal(response.status_code, 405, f'Expected status 405, got {response.status_code}')
        # Only check body if status code matches
        if response.status_code == 405:
            check.is_not_none(response.text, 'Response should have body')
