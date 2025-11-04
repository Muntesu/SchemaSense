"""
Auto-generated pytest tests from Schemathesis VCR cassette.
Generated from: reports/vcr-20251030T233336Z.yaml
Total tests: 167

Note: Uses soft assertions via pytest-check.
All tests will run even if assertions fail.
Install: pip install pytest-check

Run with: pytest test_generated_from_vcr.py -v
"""

import pytest
import pytest_check as check  # Soft assertions - all tests run even if some fail
import requests
import json


def test_post_auth_0():
    """Test generated from Schemathesis VCR: 21m3qa
    Test: POST /auth
    Status: SUCCESS
    """
    import requests
    
    url = f"https://restful-booker.herokuapp.com/auth"
    headers = {'User-Agent': 'schemathesis/4.3.15', 'Accept-Encoding': 'gzip, deflate, zstd', 'Accept': 'application/json', 'Connection': 'keep-alive', 'Authorization': 'Basic YWRtaW46cGFzc3dvcmQxMjM=', 'Content-Type': 'application/json', 'Content-Length': '49'}
    body = {'username': 'admin2', 'password': 'password123'}
    
    response = requests.post(url, headers=headers, json=body)
    
    check.equal(response.status_code, 200, f'Expected status 200, got {response.status_code}')
    check.equal(response.json(), {'reason': 'Bad credentials'}, 'Response body mismatch')

def test_post_booking_1():
    """Test generated from Schemathesis VCR: 1wnyvE
    Test: POST /booking
    Status: SUCCESS
    """
    import requests
    
    url = f"https://restful-booker.herokuapp.com/booking"
    headers = {'User-Agent': 'schemathesis/4.3.15', 'Accept-Encoding': 'gzip, deflate, zstd', 'Accept': 'application/json', 'Connection': 'keep-alive', 'Authorization': 'Basic YWRtaW46cGFzc3dvcmQxMjM=', 'Content-Type': 'application/json', 'Content-Length': '182'}
    body = {'firstname': 'Jim', 'lastname': 'Brown', 'totalprice': 111, 'depositpaid': True, 'bookingdates': {'checkin': '2018-01-01', 'checkout': '2019-01-01'}, 'additionalneeds': 'Breakfast'}
    
    response = requests.post(url, headers=headers, json=body)
    
    check.equal(response.status_code, 200, f'Expected status 200, got {response.status_code}')
    check.equal(response.json(), {'bookingid': 1435, 'booking': {'firstname': 'Jim', 'lastname': 'Brown', 'totalprice': 111, 'depositpaid': True, 'bookingdates': {'checkin': '2018-01-01', 'checkout': '2019-01-01'}, 'additionalneeds': 'Breakfast'}}, 'Response body mismatch')

def test_put_booking_8_2():
    """Test generated from Schemathesis VCR: jsrFPy
    Test: PUT /booking/8
    Status: SUCCESS
    """
    import requests
    
    url = f"https://restful-booker.herokuapp.com/booking/8"
    headers = {'User-Agent': 'schemathesis/4.3.15', 'Accept-Encoding': 'gzip, deflate, zstd', 'Accept': 'application/json', 'Connection': 'keep-alive', 'Authorization': 'Basic YWRtaW46cGFzc3dvcmQxMjM=', 'Content-Type': 'application/json', 'Content-Length': '183'}
    body = {'firstname': 'Mary', 'lastname': 'Jones', 'totalprice': 111, 'depositpaid': True, 'bookingdates': {'checkin': '2018-01-01', 'checkout': '2019-01-01'}, 'additionalneeds': 'Breakfast'}
    
    response = requests.put(url, headers=headers, json=body)
    
    check.equal(response.status_code, 200, f'Expected status 200, got {response.status_code}')
    check.equal(response.json(), {'firstname': 'Mary', 'lastname': 'Jones', 'totalprice': 111, 'depositpaid': True, 'bookingdates': {'checkin': '2018-01-01', 'checkout': '2019-01-01'}, 'additionalneeds': 'Breakfast'}, 'Response body mismatch')

def test_get_booking_3():
    """Test generated from Schemathesis VCR: g2BJKC
    Test: GET /booking
    Status: FAILURE
    """
    import requests
    
    url = f"https://restful-booker.herokuapp.com/booking"
    headers = {'User-Agent': 'schemathesis/4.3.15', 'Accept-Encoding': 'gzip, deflate, zstd', 'Accept': 'application/json', 'Connection': 'keep-alive', 'Authorization': 'Basic YWRtaW46cGFzc3dvcmQxMjM=', 'Content-Type': 'application/json'}
    
    response = requests.get(url, headers=headers)
    
    check.equal(response.status_code, 500, f'Expected status 500, got {response.status_code}')
    # Original failed checks: not_a_server_error, status_code_conformance

def test_get_booking_1_4():
    """Test generated from Schemathesis VCR: tEn8Te
    Test: GET /booking/-1
    Status: SUCCESS
    """
    import requests
    
    url = f"https://restful-booker.herokuapp.com/booking/-1"
    headers = {'User-Agent': 'schemathesis/4.3.15', 'Accept-Encoding': 'gzip, deflate, zstd', 'Accept': 'application/json', 'Connection': 'keep-alive', 'Authorization': 'Basic YWRtaW46cGFzc3dvcmQxMjM=', 'Content-Type': 'application/json'}
    
    response = requests.get(url, headers=headers)
    
    check.equal(response.status_code, 404, f'Expected status 404, got {response.status_code}')
    check.is_not_none(response.text, 'Response should have body')

def test_get_booking_3_5():
    """Test generated from Schemathesis VCR: Gjpm5w
    Test: GET /booking/3
    Status: SUCCESS
    """
    import requests
    
    url = f"https://restful-booker.herokuapp.com/booking/3"
    headers = {'User-Agent': 'schemathesis/4.3.15', 'Accept-Encoding': 'gzip, deflate, zstd', 'Accept': 'application/json', 'Connection': 'keep-alive', 'Authorization': 'Basic YWRtaW46cGFzc3dvcmQxMjM=', 'Content-Type': 'application/json'}
    
    response = requests.get(url, headers=headers)
    
    check.equal(response.status_code, 200, f'Expected status 200, got {response.status_code}')
    check.equal(response.json(), {'firstname': 'Mary', 'lastname': 'Ericsson', 'totalprice': 229, 'depositpaid': True, 'bookingdates': {'checkin': '2015-09-27', 'checkout': '2018-10-09'}}, 'Response body mismatch')

def test_delete_booking_1_6():
    """Test generated from Schemathesis VCR: XqZZp5
    Test: DELETE /booking/-1
    Status: FAILURE
    """
    import requests
    
    url = f"https://restful-booker.herokuapp.com/booking/-1"
    headers = {'User-Agent': 'schemathesis/4.3.15', 'Accept-Encoding': 'gzip, deflate, zstd', 'Accept': 'application/json', 'Connection': 'keep-alive', 'Authorization': 'Basic YWRtaW46cGFzc3dvcmQxMjM=', 'Content-Type': 'application/json', 'Content-Length': '0'}
    
    response = requests.delete(url, headers=headers)
    
    check.equal(response.status_code, 405, f'Expected status 405, got {response.status_code}')
    # Original failed checks: status_code_conformance, positive_data_acceptance

def test_patch_booking_7_7():
    """Test generated from Schemathesis VCR: WcP0uE
    Test: PATCH /booking/7
    Status: SUCCESS
    """
    import requests
    
    url = f"https://restful-booker.herokuapp.com/booking/7"
    headers = {'User-Agent': 'schemathesis/4.3.15', 'Accept-Encoding': 'gzip, deflate, zstd', 'Accept': 'application/json', 'Connection': 'keep-alive', 'Authorization': 'Basic YWRtaW46cGFzc3dvcmQxMjM=', 'Content-Type': 'application/json', 'Content-Length': '182'}
    body = {'firstname': 'Jim', 'lastname': 'Brown', 'totalprice': 111, 'depositpaid': True, 'bookingdates': {'checkin': '2018-01-01', 'checkout': '2019-01-01'}, 'additionalneeds': 'Breakfast'}
    
    response = requests.patch(url, headers=headers, json=body)
    
    check.equal(response.status_code, 200, f'Expected status 200, got {response.status_code}')
    check.equal(response.json(), {'firstname': 'Jim', 'lastname': 'Brown', 'totalprice': 111, 'depositpaid': True, 'bookingdates': {'checkin': '2018-01-01', 'checkout': '2019-01-01'}, 'additionalneeds': 'Breakfast'}, 'Response body mismatch')

def test_trace_auth_8():
    """Test generated from Schemathesis VCR: HYVheW
    Test: TRACE /auth
    Status: FAILURE
    """
    import requests
    
    url = f"https://restful-booker.herokuapp.com/auth"
    headers = {'User-Agent': 'schemathesis/4.3.15', 'Accept-Encoding': 'gzip, deflate, zstd', 'Accept': 'application/json', 'Connection': 'keep-alive', 'Authorization': 'Basic YWRtaW46cGFzc3dvcmQxMjM=', 'Content-Type': 'application/json', 'Content-Length': '49'}
    body = {'username': 'admin2', 'password': 'password123'}
    
    response = requests.trace(url, headers=headers, data=body)
    
    check.equal(response.status_code, 404, f'Expected status 404, got {response.status_code}')
    # Original failed checks: unsupported_method

def test_trace_booking_3_9():
    """Test generated from Schemathesis VCR: upMHKu
    Test: TRACE /booking/3
    Status: FAILURE
    """
    import requests
    
    url = f"https://restful-booker.herokuapp.com/booking/3"
    headers = {'User-Agent': 'schemathesis/4.3.15', 'Accept-Encoding': 'gzip, deflate, zstd', 'Accept': 'application/json', 'Connection': 'keep-alive', 'Authorization': 'Basic YWRtaW46cGFzc3dvcmQxMjM=', 'Content-Type': 'application/json', 'Content-Length': '0'}
    
    response = requests.trace(url, headers=headers)
    
    check.equal(response.status_code, 404, f'Expected status 404, got {response.status_code}')
    # Original failed checks: unsupported_method

def test_trace_booking_10():
    """Test generated from Schemathesis VCR: fnoz7R
    Test: TRACE /booking
    Status: FAILURE
    """
    import requests
    
    url = f"https://restful-booker.herokuapp.com/booking"
    headers = {'User-Agent': 'schemathesis/4.3.15', 'Accept-Encoding': 'gzip, deflate, zstd', 'Accept': 'application/json', 'Connection': 'keep-alive', 'Authorization': 'Basic YWRtaW46cGFzc3dvcmQxMjM=', 'Content-Type': 'application/json', 'Content-Length': '182'}
    body = {'firstname': 'Jim', 'lastname': 'Brown', 'totalprice': 111, 'depositpaid': True, 'bookingdates': {'checkin': '2018-01-01', 'checkout': '2019-01-01'}, 'additionalneeds': 'Breakfast'}
    
    response = requests.trace(url, headers=headers, data=body)
    
    check.equal(response.status_code, 404, f'Expected status 404, got {response.status_code}')
    # Original failed checks: unsupported_method

def test_delete_booking_6_11():
    """Test generated from Schemathesis VCR: xLvHcj
    Test: DELETE /booking/6
    Status: FAILURE
    """
    import requests
    
    url = f"https://restful-booker.herokuapp.com/booking/6"
    headers = {'User-Agent': 'schemathesis/4.3.15', 'Accept-Encoding': 'gzip, deflate, zstd', 'Accept': 'application/json', 'Connection': 'keep-alive', 'Content-Type': 'application/json', 'Content-Length': '0'}
    
    response = requests.delete(url, headers=headers)
    
    check.equal(response.status_code, 403, f'Expected status 403, got {response.status_code}')
    # Original failed checks: status_code_conformance, missing_required_header

def test_patch_booking_7_12():
    """Test generated from Schemathesis VCR: OqATnS
    Test: PATCH /booking/7
    Status: FAILURE
    """
    import requests
    
    url = f"https://restful-booker.herokuapp.com/booking/7"
    headers = {'User-Agent': 'schemathesis/4.3.15', 'Accept-Encoding': 'gzip, deflate, zstd', 'Accept': 'application/json', 'Connection': 'keep-alive', 'Content-Type': 'application/json', 'Content-Length': '182'}
    body = {'firstname': 'Jim', 'lastname': 'Brown', 'totalprice': 111, 'depositpaid': True, 'bookingdates': {'checkin': '2018-01-01', 'checkout': '2019-01-01'}, 'additionalneeds': 'Breakfast'}
    
    response = requests.patch(url, headers=headers, json=body)
    
    check.equal(response.status_code, 403, f'Expected status 403, got {response.status_code}')
    # Original failed checks: status_code_conformance, missing_required_header

def test_put_booking_8_13():
    """Test generated from Schemathesis VCR: XZFUb7
    Test: PUT /booking/8
    Status: FAILURE
    """
    import requests
    
    url = f"https://restful-booker.herokuapp.com/booking/8"
    headers = {'User-Agent': 'schemathesis/4.3.15', 'Accept-Encoding': 'gzip, deflate, zstd', 'Accept': 'application/json', 'Connection': 'keep-alive', 'Content-Type': 'application/json', 'Content-Length': '183'}
    body = {'firstname': 'Mary', 'lastname': 'Jones', 'totalprice': 111, 'depositpaid': True, 'bookingdates': {'checkin': '2018-01-01', 'checkout': '2019-01-01'}, 'additionalneeds': 'Breakfast'}
    
    response = requests.put(url, headers=headers, json=body)
    
    check.equal(response.status_code, 403, f'Expected status 403, got {response.status_code}')
    # Original failed checks: status_code_conformance, missing_required_header

def test_trace_ping_14():
    """Test generated from Schemathesis VCR: AZxlmm
    Test: TRACE /ping
    Status: FAILURE
    """
    import requests
    
    url = f"https://restful-booker.herokuapp.com/ping"
    headers = {'User-Agent': 'schemathesis/4.3.15', 'Accept-Encoding': 'gzip, deflate, zstd', 'Accept': 'application/json', 'Connection': 'keep-alive', 'Authorization': 'Basic YWRtaW46cGFzc3dvcmQxMjM=', 'Content-Type': 'application/json', 'Content-Length': '0'}
    
    response = requests.trace(url, headers=headers)
    
    check.equal(response.status_code, 404, f'Expected status 404, got {response.status_code}')
    # Original failed checks: unsupported_method

def test_get_booking_15():
    """Test generated from Schemathesis VCR: x8e01z
    Test: GET /booking
    Status: SUCCESS
    """
    import requests
    
    url = f"https://restful-booker.herokuapp.com/booking"
    headers = {'User-Agent': 'schemathesis/4.3.15', 'Accept-Encoding': 'gzip, deflate, zstd', 'Accept': 'application/json', 'Connection': 'keep-alive', 'Authorization': 'Basic YWRtaW46cGFzc3dvcmQxMjM=', 'Content-Type': 'application/json'}
    
    response = requests.get(url, headers=headers)
    
    check.equal(response.status_code, 200, f'Expected status 200, got {response.status_code}')
    check.equal(response.json(), [{'bookingid': 7}, {'bookingid': 1435}, {'bookingid': 163}], 'Response body mismatch')

def test_get_booking_16():
    """Test generated from Schemathesis VCR: HYQi19
    Test: GET /booking
    Status: SUCCESS
    """
    import requests
    
    url = f"https://restful-booker.herokuapp.com/booking"
    headers = {'User-Agent': 'schemathesis/4.3.15', 'Accept-Encoding': 'gzip, deflate, zstd', 'Accept': 'application/json', 'Connection': 'keep-alive', 'Authorization': 'Basic YWRtaW46cGFzc3dvcmQxMjM=', 'Content-Type': 'application/json'}
    
    response = requests.get(url, headers=headers)
    
    check.equal(response.status_code, 200, f'Expected status 200, got {response.status_code}')
    check.equal(response.json(), [], 'Response body mismatch')

def test_get_booking_17():
    """Test generated from Schemathesis VCR: bkkWkn
    Test: GET /booking
    Status: SUCCESS
    """
    import requests
    
    url = f"https://restful-booker.herokuapp.com/booking"
    headers = {'User-Agent': 'schemathesis/4.3.15', 'Accept-Encoding': 'gzip, deflate, zstd', 'Accept': 'application/json', 'Connection': 'keep-alive', 'Authorization': 'Basic YWRtaW46cGFzc3dvcmQxMjM=', 'Content-Type': 'application/json'}
    
    response = requests.get(url, headers=headers)
    
    check.equal(response.status_code, 200, f'Expected status 200, got {response.status_code}')
    check.equal(response.json(), [], 'Response body mismatch')

def test_get_booking_18():
    """Test generated from Schemathesis VCR: 0i5Btf
    Test: GET /booking
    Status: SUCCESS
    """
    import requests
    
    url = f"https://restful-booker.herokuapp.com/booking"
    headers = {'User-Agent': 'schemathesis/4.3.15', 'Accept-Encoding': 'gzip, deflate, zstd', 'Accept': 'application/json', 'Connection': 'keep-alive', 'Authorization': 'Basic YWRtaW46cGFzc3dvcmQxMjM=', 'Content-Type': 'application/json'}
    
    response = requests.get(url, headers=headers)
    
    check.equal(response.status_code, 200, f'Expected status 200, got {response.status_code}')
    check.equal(response.json(), [], 'Response body mismatch')

def test_get_booking_19():
    """Test generated from Schemathesis VCR: qa5bBQ
    Test: GET /booking
    Status: SUCCESS
    """
    import requests
    
    url = f"https://restful-booker.herokuapp.com/booking"
    headers = {'User-Agent': 'schemathesis/4.3.15', 'Accept-Encoding': 'gzip, deflate, zstd', 'Accept': 'application/json', 'Connection': 'keep-alive', 'Authorization': 'Basic YWRtaW46cGFzc3dvcmQxMjM=', 'Content-Type': 'application/json'}
    
    response = requests.get(url, headers=headers)
    
    check.equal(response.status_code, 200, f'Expected status 200, got {response.status_code}')
    check.equal(response.json(), [{'bookingid': 7}, {'bookingid': 1435}, {'bookingid': 163}], 'Response body mismatch')

def test_get_booking_20():
    """Test generated from Schemathesis VCR: Fb2cvQ
    Test: GET /booking
    Status: SUCCESS
    """
    import requests
    
    url = f"https://restful-booker.herokuapp.com/booking"
    headers = {'User-Agent': 'schemathesis/4.3.15', 'Accept-Encoding': 'gzip, deflate, zstd', 'Accept': 'application/json', 'Connection': 'keep-alive', 'Authorization': 'Basic YWRtaW46cGFzc3dvcmQxMjM=', 'Content-Type': 'application/json'}
    
    response = requests.get(url, headers=headers)
    
    check.equal(response.status_code, 200, f'Expected status 200, got {response.status_code}')
    check.equal(response.json(), [{'bookingid': 7}, {'bookingid': 1435}, {'bookingid': 163}], 'Response body mismatch')

def test_get_booking_21():
    """Test generated from Schemathesis VCR: NEGLOF
    Test: GET /booking
    Status: SUCCESS
    """
    import requests
    
    url = f"https://restful-booker.herokuapp.com/booking"
    headers = {'User-Agent': 'schemathesis/4.3.15', 'Accept-Encoding': 'gzip, deflate, zstd', 'Accept': 'application/json', 'Connection': 'keep-alive', 'Authorization': 'Basic YWRtaW46cGFzc3dvcmQxMjM=', 'Content-Type': 'application/json'}
    
    response = requests.get(url, headers=headers)
    
    check.equal(response.status_code, 200, f'Expected status 200, got {response.status_code}')
    check.equal(response.json(), [{'bookingid': 7}, {'bookingid': 1435}, {'bookingid': 163}], 'Response body mismatch')

def test_get_booking_22():
    """Test generated from Schemathesis VCR: u5RkIT
    Test: GET /booking
    Status: SUCCESS
    """
    import requests
    
    url = f"https://restful-booker.herokuapp.com/booking"
    headers = {'User-Agent': 'schemathesis/4.3.15', 'Accept-Encoding': 'gzip, deflate, zstd', 'Accept': 'application/json', 'Connection': 'keep-alive', 'Authorization': 'Basic YWRtaW46cGFzc3dvcmQxMjM=', 'Content-Type': 'application/json'}
    
    response = requests.get(url, headers=headers)
    
    check.equal(response.status_code, 200, f'Expected status 200, got {response.status_code}')
    check.equal(response.json(), [{'bookingid': 4}], 'Response body mismatch')

def test_get_booking_23():
    """Test generated from Schemathesis VCR: mDxtlv
    Test: GET /booking
    Status: SUCCESS
    """
    import requests
    
    url = f"https://restful-booker.herokuapp.com/booking"
    headers = {'User-Agent': 'schemathesis/4.3.15', 'Accept-Encoding': 'gzip, deflate, zstd', 'Accept': 'application/json', 'Connection': 'keep-alive', 'Authorization': 'Basic YWRtaW46cGFzc3dvcmQxMjM=', 'Content-Type': 'application/json'}
    
    response = requests.get(url, headers=headers)
    
    check.equal(response.status_code, 200, f'Expected status 200, got {response.status_code}')
    check.equal(response.json(), [], 'Response body mismatch')

def test_get_booking_24():
    """Test generated from Schemathesis VCR: mvGjVM
    Test: GET /booking
    Status: SUCCESS
    """
    import requests
    
    url = f"https://restful-booker.herokuapp.com/booking"
    headers = {'User-Agent': 'schemathesis/4.3.15', 'Accept-Encoding': 'gzip, deflate, zstd', 'Accept': 'application/json', 'Connection': 'keep-alive', 'Authorization': 'Basic YWRtaW46cGFzc3dvcmQxMjM=', 'Content-Type': 'application/json'}
    
    response = requests.get(url, headers=headers)
    
    check.equal(response.status_code, 200, f'Expected status 200, got {response.status_code}')
    check.equal(response.json(), [], 'Response body mismatch')

def test_get_booking_25():
    """Test generated from Schemathesis VCR: fEC1Z9
    Test: GET /booking
    Status: SUCCESS
    """
    import requests
    
    url = f"https://restful-booker.herokuapp.com/booking"
    headers = {'User-Agent': 'schemathesis/4.3.15', 'Accept-Encoding': 'gzip, deflate, zstd', 'Accept': 'application/json', 'Connection': 'keep-alive', 'Authorization': 'Basic YWRtaW46cGFzc3dvcmQxMjM=', 'Content-Type': 'application/json'}
    
    response = requests.get(url, headers=headers)
    
    check.equal(response.status_code, 200, f'Expected status 200, got {response.status_code}')
    check.equal(response.json(), [], 'Response body mismatch')

def test_get_booking_26():
    """Test generated from Schemathesis VCR: rCrlyy
    Test: GET /booking
    Status: SUCCESS
    """
    import requests
    
    url = f"https://restful-booker.herokuapp.com/booking"
    headers = {'User-Agent': 'schemathesis/4.3.15', 'Accept-Encoding': 'gzip, deflate, zstd', 'Accept': 'application/json', 'Connection': 'keep-alive', 'Authorization': 'Basic YWRtaW46cGFzc3dvcmQxMjM=', 'Content-Type': 'application/json'}
    
    response = requests.get(url, headers=headers)
    
    check.equal(response.status_code, 200, f'Expected status 200, got {response.status_code}')
    check.equal(response.json(), [{'bookingid': 7}, {'bookingid': 1435}, {'bookingid': 4}, {'bookingid': 163}], 'Response body mismatch')

def test_get_booking_27():
    """Test generated from Schemathesis VCR: lyHUHv
    Test: GET /booking
    Status: SUCCESS
    """
    import requests
    
    url = f"https://restful-booker.herokuapp.com/booking"
    headers = {'User-Agent': 'schemathesis/4.3.15', 'Accept-Encoding': 'gzip, deflate, zstd', 'Accept': 'application/json', 'Connection': 'keep-alive', 'Authorization': 'Basic YWRtaW46cGFzc3dvcmQxMjM=', 'Content-Type': 'application/json'}
    
    response = requests.get(url, headers=headers)
    
    check.equal(response.status_code, 200, f'Expected status 200, got {response.status_code}')
    check.equal(response.json(), [], 'Response body mismatch')

def test_get_booking_28():
    """Test generated from Schemathesis VCR: orvA9w
    Test: GET /booking
    Status: SUCCESS
    """
    import requests
    
    url = f"https://restful-booker.herokuapp.com/booking"
    headers = {'User-Agent': 'schemathesis/4.3.15', 'Accept-Encoding': 'gzip, deflate, zstd', 'Accept': 'application/json', 'Connection': 'keep-alive', 'Authorization': 'Basic YWRtaW46cGFzc3dvcmQxMjM=', 'Content-Type': 'application/json'}
    
    response = requests.get(url, headers=headers)
    
    check.equal(response.status_code, 200, f'Expected status 200, got {response.status_code}')
    check.equal(response.json(), [{'bookingid': 6}, {'bookingid': 7}, {'bookingid': 1435}, {'bookingid': 163}], 'Response body mismatch')

def test_get_booking_29():
    """Test generated from Schemathesis VCR: LD4ecP
    Test: GET /booking
    Status: SUCCESS
    """
    import requests
    
    url = f"https://restful-booker.herokuapp.com/booking"
    headers = {'User-Agent': 'schemathesis/4.3.15', 'Accept-Encoding': 'gzip, deflate, zstd', 'Accept': 'application/json', 'Connection': 'keep-alive', 'Authorization': 'Basic YWRtaW46cGFzc3dvcmQxMjM=', 'Content-Type': 'application/json'}
    
    response = requests.get(url, headers=headers)
    
    check.equal(response.status_code, 200, f'Expected status 200, got {response.status_code}')
    check.equal(response.json(), [], 'Response body mismatch')

def test_get_booking_30():
    """Test generated from Schemathesis VCR: A1gAdO
    Test: GET /booking
    Status: FAILURE
    """
    import requests
    
    url = f"https://restful-booker.herokuapp.com/booking"
    headers = {'User-Agent': 'schemathesis/4.3.15', 'Accept-Encoding': 'gzip, deflate, zstd', 'Accept': 'application/json', 'Connection': 'keep-alive', 'Authorization': 'Basic YWRtaW46cGFzc3dvcmQxMjM=', 'Content-Type': 'application/json'}
    
    response = requests.get(url, headers=headers)
    
    check.equal(response.status_code, 500, f'Expected status 500, got {response.status_code}')
    # Original failed checks: not_a_server_error, status_code_conformance

def test_get_ping_31():
    """Test generated from Schemathesis VCR: gDxmDo
    Test: GET /ping
    Status: FAILURE
    """
    import requests
    
    url = f"https://restful-booker.herokuapp.com/ping"
    headers = {'User-Agent': 'schemathesis/4.3.15', 'Accept-Encoding': 'gzip, deflate, zstd', 'Accept': 'application/json', 'Connection': 'keep-alive', 'Authorization': 'Basic YWRtaW46cGFzc3dvcmQxMjM=', 'Content-Type': 'application/json'}
    
    response = requests.get(url, headers=headers)
    
    check.equal(response.status_code, 201, f'Expected status 201, got {response.status_code}')
    # Original failed checks: content_type_conformance

def test_put_booking_0_32():
    """Test generated from Schemathesis VCR: doy9C5
    Test: PUT /booking/0
    Status: FAILURE
    """
    import requests
    
    url = f"https://restful-booker.herokuapp.com/booking/0"
    headers = {'User-Agent': 'schemathesis/4.3.15', 'Accept-Encoding': 'gzip, deflate, zstd', 'Accept': 'application/json', 'Connection': 'keep-alive', 'Authorization': 'Basic YWRtaW46cGFzc3dvcmQxMjM=', 'Content-Type': 'application/json', 'Content-Length': '141'}
    body = {'bookingdates': {'checkin': '2000-01-01', 'checkout': '2000-01-01'}, 'depositpaid': False, 'firstname': '', 'lastname': '', 'totalprice': 0}
    
    response = requests.put(url, headers=headers, json=body)
    
    check.equal(response.status_code, 405, f'Expected status 405, got {response.status_code}')
    # Original failed checks: status_code_conformance, positive_data_acceptance

def test_post_booking_33():
    """Test generated from Schemathesis VCR: RDablk
    Test: POST /booking
    Status: SUCCESS
    """
    import requests
    
    url = f"https://restful-booker.herokuapp.com/booking"
    headers = {'User-Agent': 'schemathesis/4.3.15', 'Accept-Encoding': 'gzip, deflate, zstd', 'Accept': 'application/json', 'Connection': 'keep-alive', 'Authorization': 'Basic YWRtaW46cGFzc3dvcmQxMjM=', 'Content-Type': 'application/json', 'Content-Length': '141'}
    body = {'bookingdates': {'checkin': '2000-01-01', 'checkout': '2000-01-01'}, 'depositpaid': False, 'firstname': '', 'lastname': '', 'totalprice': 0}
    
    response = requests.post(url, headers=headers, json=body)
    
    check.equal(response.status_code, 200, f'Expected status 200, got {response.status_code}')
    check.equal(response.json(), {'bookingid': 1471, 'booking': {'firstname': '', 'lastname': '', 'totalprice': 0, 'depositpaid': False, 'bookingdates': {'checkin': '2000-01-01', 'checkout': '2000-01-01'}}}, 'Response body mismatch')

def test_post_booking_34():
    """Test generated from Schemathesis VCR: wnzoGc
    Test: POST /booking
    Status: FAILURE
    """
    import requests
    
    url = f"https://restful-booker.herokuapp.com/booking"
    headers = {'User-Agent': 'schemathesis/4.3.15', 'Accept-Encoding': 'gzip, deflate, zstd', 'Accept': 'application/json', 'Connection': 'keep-alive', 'Authorization': 'Basic YWRtaW46cGFzc3dvcmQxMjM=', 'Content-Type': 'application/json', 'Content-Length': '2820'}
    body = {'bookingdates': {'checkin': '3755-10-01', 'checkout': '0300-06-10', 'Û': {'~\x0fÃÝ\U0004fffa\U001057b6': -179949562}, '\x9c\U000ef743\x13': [], '$\U000f5c04s\x9e': {'\x86¼K`\x85\x16V': [None, 2.7252383720688736e+16], 'ÜN\U000aacc3>Ôi\x0el\x9a': None, '\x84': -11360}, '8¢8': False, 'UÛZ+Æ\x86\U00051337\x04\xa0Çü\U000ad67a': [], 'Ø\U00108341\x9aë\U000709d8': {'': None}, '\U000f1db5\U0007f32c': [], '#ÕK\x9c': [[True, -3.183121062946998e-148], 2.6124227368011154e-107, [300, True]], '\x99ÿ': {'Ù\x08\U0006ad86»': [123, None, {'\x92\U000ce3d7v¿Äå\x17\U000e11dd': None, '\x80hâ\x8d': None}], '\U00109a87\x0c#': {'°ED/': [{'\U0009afaamPpÆ': 'Õ]b¯\U000b29d90E\x93\x06\U00048649ð\x0f\x97\x07\U000b746f|', 'पन्ह पन्ह त्र र्च कृकृ ड्ड न्हृे إلا بسم الله': '\x11', 'Nà\x052\U0004ce45\U000e754dè¿\U000a3c22示¤\U000199b3': None}], 'WÈ\U000ebcabH]\x83': {}}, 'ú': False}, '999999999999999999999999999999': {'ÎÏ\U000edd84òê\U00051543åº\x19\U0002ebe6ïe\U00043ca9': {'\x12XI𲆱#ú\x0fâç': True, '\U0005bad0\x88v\x16Ã\U000dcd72윲': -8593075783859678791, '\U000e5bb7\U00097d95\x97': '\x02'}, 'ì': [{}], 'Ï𨛱Ú¯¶': []}, '': {'ca\x07\U000c868fu\t.': None}, '\x93Ê𘎚': {}, '¼\U0001fcceâ_û>': {'Ê': {'m<\x17': '¼', ':§': None, '\x94ë 亵Í\x93\U00065ead\U0005603e\t\x89\x80': -98}, '6J\U00078805ã': {}, '\U000edb53\U000e80c3': []}, '\xa0': {'G': True, 'Ý': None, '': '£\x91\x80.òk/æþÆ'}, '÷ÚÆË': [{'\U000fe8de': [], '\rs\U00064840': 13048, 'z\U00070fdf\x97ä\x1eýd': {'µL&~f': 1.9, 'aÒ\x8eÏ6q\x1a\x9a\x82': 'v\U0008c5a1â:\U0007388ew<µ'}}, None], '\U000b004b?H0': [[-20939], 'ëlª8i±𥪟\x12', {}], '=ç': [], 'ÿ\x98': [None, 98, []], '\U000b94cf\U00093930+\U0004df21\x94': {'': [-89]}, "T\x94a'Q": [[], {'ªY\x1d𗥿\U000be371É\x01H': True, 'Âg': None, '\x11': -3.510080368990195e+258}]}, '': {'ñ\x86î\t𱹅Göô\ue20cV£\U000a9f85I': [{}, True, []], 'ü\U000e09af\U000efbcbd\x0e½': False, '¯\x06\x19Tt𣼨\x05': {}}}
    
    response = requests.post(url, headers=headers, json=body)
    
    check.equal(response.status_code, 500, f'Expected status 500, got {response.status_code}')
    # Original failed checks: not_a_server_error, status_code_conformance

def test_post_auth_35():
    """Test generated from Schemathesis VCR: 2QTvw2
    Test: POST /auth
    Status: SUCCESS
    """
    import requests
    
    url = f"https://restful-booker.herokuapp.com/auth"
    headers = {'User-Agent': 'schemathesis/4.3.15', 'Accept-Encoding': 'gzip, deflate, zstd', 'Accept': 'application/json', 'Connection': 'keep-alive', 'Authorization': 'Basic YWRtaW46cGFzc3dvcmQxMjM=', 'Content-Type': 'application/json', 'Content-Length': '2'}
    body = {}
    
    response = requests.post(url, headers=headers, json=body)
    
    check.equal(response.status_code, 200, f'Expected status 200, got {response.status_code}')
    check.equal(response.json(), {'reason': 'Bad credentials'}, 'Response body mismatch')

def test_post_auth_36():
    """Test generated from Schemathesis VCR: RZ3riK
    Test: POST /auth
    Status: FAILURE
    """
    import requests
    
    url = f"https://restful-booker.herokuapp.com/auth"
    headers = {'User-Agent': 'schemathesis/4.3.15', 'Accept-Encoding': 'gzip, deflate, zstd', 'Accept': 'application/json', 'Connection': 'keep-alive', 'Authorization': 'Basic YWRtaW46cGFzc3dvcmQxMjM=', 'Content-Type': 'application/json', 'Content-Length': '60'}
    body = ['å', {}, {}, {'\x9c\U000ef743\x13': []}, [], '']
    
    response = requests.post(url, headers=headers, json=body)
    
    check.equal(response.status_code, 200, f'Expected status 200, got {response.status_code}')
    # Original failed checks: negative_data_rejection

def test_delete_booking_0_37():
    """Test generated from Schemathesis VCR: lY5wpm
    Test: DELETE /booking/0
    Status: FAILURE
    """
    import requests
    
    url = f"https://restful-booker.herokuapp.com/booking/0"
    headers = {'User-Agent': 'schemathesis/4.3.15', 'Accept-Encoding': 'gzip, deflate, zstd', 'Accept': 'application/json', 'Connection': 'keep-alive', 'Authorization': 'Basic YWRtaW46cGFzc3dvcmQxMjM=', 'Content-Type': 'application/json', 'Content-Length': '0'}
    
    response = requests.delete(url, headers=headers)
    
    check.equal(response.status_code, 405, f'Expected status 405, got {response.status_code}')
    # Original failed checks: status_code_conformance, positive_data_acceptance

def test_patch_booking_0_38():
    """Test generated from Schemathesis VCR: XuiDGY
    Test: PATCH /booking/0
    Status: FAILURE
    """
    import requests
    
    url = f"https://restful-booker.herokuapp.com/booking/0"
    headers = {'User-Agent': 'schemathesis/4.3.15', 'Accept-Encoding': 'gzip, deflate, zstd', 'Accept': 'application/json', 'Connection': 'keep-alive', 'Authorization': 'Basic YWRtaW46cGFzc3dvcmQxMjM=', 'Content-Type': 'application/json', 'Content-Length': '141'}
    body = {'bookingdates': {'checkin': '2000-01-01', 'checkout': '2000-01-01'}, 'depositpaid': False, 'firstname': '', 'lastname': '', 'totalprice': 0}
    
    response = requests.patch(url, headers=headers, json=body)
    
    check.equal(response.status_code, 405, f'Expected status 405, got {response.status_code}')
    # Original failed checks: status_code_conformance, positive_data_acceptance

def test_get_booking_0_39():
    """Test generated from Schemathesis VCR: fDYsDn
    Test: GET /booking/0
    Status: SUCCESS
    """
    import requests
    
    url = f"https://restful-booker.herokuapp.com/booking/0"
    headers = {'User-Agent': 'schemathesis/4.3.15', 'Accept-Encoding': 'gzip, deflate, zstd', 'Accept': 'application/json', 'Connection': 'keep-alive', 'Authorization': 'Basic YWRtaW46cGFzc3dvcmQxMjM=', 'Content-Type': 'application/json'}
    
    response = requests.get(url, headers=headers)
    
    check.equal(response.status_code, 404, f'Expected status 404, got {response.status_code}')
    check.is_not_none(response.text, 'Response should have body')

def test_get_booking_40():
    """Test generated from Schemathesis VCR: B2OZun
    Test: GET /booking/%C2%B2%14
    Status: SUCCESS
    """
    import requests
    
    url = f"https://restful-booker.herokuapp.com/booking/%C2%B2%14"
    headers = {'User-Agent': 'schemathesis/4.3.15', 'Accept-Encoding': 'gzip, deflate, zstd', 'Accept': 'application/json', 'Connection': 'keep-alive', 'Authorization': 'Basic YWRtaW46cGFzc3dvcmQxMjM=', 'Content-Type': 'application/json'}
    
    response = requests.get(url, headers=headers)
    
    check.equal(response.status_code, 404, f'Expected status 404, got {response.status_code}')
    check.is_not_none(response.text, 'Response should have body')

def test_get_booking_1218237665_41():
    """Test generated from Schemathesis VCR: jaiLmL
    Test: GET /booking/-1218237665
    Status: SUCCESS
    """
    import requests
    
    url = f"https://restful-booker.herokuapp.com/booking/-1218237665"
    headers = {'User-Agent': 'schemathesis/4.3.15', 'Accept-Encoding': 'gzip, deflate, zstd', 'Accept': 'application/json', 'Connection': 'keep-alive', 'Authorization': 'Basic YWRtaW46cGFzc3dvcmQxMjM=', 'Content-Type': 'application/json'}
    
    response = requests.get(url, headers=headers)
    
    check.equal(response.status_code, 404, f'Expected status 404, got {response.status_code}')
    check.is_not_none(response.text, 'Response should have body')

def test_get_booking_300_42():
    """Test generated from Schemathesis VCR: KCyyHN
    Test: GET /booking/300
    Status: SUCCESS
    """
    import requests
    
    url = f"https://restful-booker.herokuapp.com/booking/300"
    headers = {'User-Agent': 'schemathesis/4.3.15', 'Accept-Encoding': 'gzip, deflate, zstd', 'Accept': 'application/json', 'Connection': 'keep-alive', 'Authorization': 'Basic YWRtaW46cGFzc3dvcmQxMjM=', 'Content-Type': 'application/json'}
    
    response = requests.get(url, headers=headers)
    
    check.equal(response.status_code, 404, f'Expected status 404, got {response.status_code}')
    check.is_not_none(response.text, 'Response should have body')

def test_get_booking_null_43():
    """Test generated from Schemathesis VCR: iH1HE5
    Test: GET /booking/null
    Status: SUCCESS
    """
    import requests
    
    url = f"https://restful-booker.herokuapp.com/booking/null"
    headers = {'User-Agent': 'schemathesis/4.3.15', 'Accept-Encoding': 'gzip, deflate, zstd', 'Accept': 'application/json', 'Connection': 'keep-alive', 'Authorization': 'Basic YWRtaW46cGFzc3dvcmQxMjM=', 'Content-Type': 'application/json'}
    
    response = requests.get(url, headers=headers)
    
    check.equal(response.status_code, 404, f'Expected status 404, got {response.status_code}')
    check.is_not_none(response.text, 'Response should have body')

def test_get_booking_44():
    """Test generated from Schemathesis VCR: 1Ewv6a
    Test: GET /booking
    Status: SUCCESS
    """
    import requests
    
    url = f"https://restful-booker.herokuapp.com/booking"
    headers = {'User-Agent': 'schemathesis/4.3.15', 'Accept-Encoding': 'gzip, deflate, zstd', 'Accept': 'application/json', 'Connection': 'keep-alive', 'Authorization': 'Basic YWRtaW46cGFzc3dvcmQxMjM=', 'Content-Type': 'application/json'}
    
    response = requests.get(url, headers=headers)
    
    check.equal(response.status_code, 200, f'Expected status 200, got {response.status_code}')
    check.equal(response.json(), [{'bookingid': 853}, {'bookingid': 697}, {'bookingid': 559}, {'bookingid': 141}, {'bookingid': 1066}, {'bookingid': 1230}, {'bookingid': 343}, {'bookingid': 344}, {'bookingid': 105}, {'bookingid': 596}, {'bookingid': 688}, {'bookingid': 3}, {'bookingid': 568}, {'bookingid': 553}, {'bookingid': 1394}, {'bookingid': 456}, {'bookingid': 863}, {'bookingid': 383}, {'bookingid': 803}, {'bookingid': 390}, {'bookingid': 631}, {'bookingid': 330}, {'bookingid': 53}, {'bookingid': 642}, {'bookingid': 154}, {'bookingid': 1307}, {'bookingid': 331}, {'bookingid': 5}, {'bookingid': 131}, {'bookingid': 728}, {'bookingid': 370}, {'bookingid': 907}, {'bookingid': 1443}, {'bookingid': 991}, {'bookingid': 679}, {'bookingid': 1074}, {'bookingid': 357}, {'bookingid': 264}, {'bookingid': 663}, {'bookingid': 266}, {'bookingid': 830}, {'bookingid': 1028}, {'bookingid': 116}, {'bookingid': 1190}, {'bookingid': 302}, {'bookingid': 560}, {'bookingid': 1409}, {'bookingid': 851}, {'bookingid': 37}, {'bookingid': 644}, {'bookingid': 18}, {'bookingid': 209}, {'bookingid': 1297}, {'bookingid': 360}, {'bookingid': 173}, {'bookingid': 1041}, {'bookingid': 806}, {'bookingid': 1086}, {'bookingid': 56}, {'bookingid': 1290}, {'bookingid': 1139}, {'bookingid': 498}, {'bookingid': 1093}, {'bookingid': 1038}, {'bookingid': 1042}, {'bookingid': 298}, {'bookingid': 332}, {'bookingid': 618}, {'bookingid': 338}, {'bookingid': 1122}, {'bookingid': 172}, {'bookingid': 687}, {'bookingid': 1037}, {'bookingid': 859}, {'bookingid': 1050}, {'bookingid': 314}, {'bookingid': 354}, {'bookingid': 225}, {'bookingid': 1452}, {'bookingid': 802}, {'bookingid': 166}, {'bookingid': 325}, {'bookingid': 543}, {'bookingid': 929}, {'bookingid': 689}, {'bookingid': 589}, {'bookingid': 974}, {'bookingid': 620}, {'bookingid': 938}, {'bookingid': 207}, {'bookingid': 1398}, {'bookingid': 1132}, {'bookingid': 232}, {'bookingid': 1205}, {'bookingid': 904}, {'bookingid': 1416}, {'bookingid': 382}, {'bookingid': 385}, {'bookingid': 340}, {'bookingid': 1369}, {'bookingid': 242}, {'bookingid': 255}, {'bookingid': 100}, {'bookingid': 347}, {'bookingid': 26}, {'bookingid': 1436}, {'bookingid': 1373}, {'bookingid': 162}, {'bookingid': 633}, {'bookingid': 717}, {'bookingid': 662}, {'bookingid': 750}, {'bookingid': 1342}, {'bookingid': 1203}, {'bookingid': 1405}, {'bookingid': 337}, {'bookingid': 77}, {'bookingid': 514}, {'bookingid': 516}, {'bookingid': 1138}, {'bookingid': 44}, {'bookingid': 71}, {'bookingid': 780}, {'bookingid': 1181}, {'bookingid': 677}, {'bookingid': 171}, {'bookingid': 1253}, {'bookingid': 150}, {'bookingid': 1019}, {'bookingid': 1097}, {'bookingid': 1322}, {'bookingid': 57}, {'bookingid': 551}, {'bookingid': 999}, {'bookingid': 1463}, {'bookingid': 829}, {'bookingid': 350}, {'bookingid': 183}, {'bookingid': 906}, {'bookingid': 1278}, {'bookingid': 1392}, {'bookingid': 833}, {'bookingid': 555}, {'bookingid': 998}, {'bookingid': 884}, {'bookingid': 299}, {'bookingid': 180}, {'bookingid': 240}, {'bookingid': 424}, {'bookingid': 1426}, {'bookingid': 1210}, {'bookingid': 1402}, {'bookingid': 132}, {'bookingid': 129}, {'bookingid': 60}, {'bookingid': 1103}, {'bookingid': 932}, {'bookingid': 706}, {'bookingid': 396}, {'bookingid': 810}, {'bookingid': 447}, {'bookingid': 1142}, {'bookingid': 768}, {'bookingid': 74}, {'bookingid': 488}, {'bookingid': 986}, {'bookingid': 1433}, {'bookingid': 1374}, {'bookingid': 968}, {'bookingid': 275}, {'bookingid': 1173}, {'bookingid': 1247}, {'bookingid': 46}, {'bookingid': 1288}, {'bookingid': 1321}, {'bookingid': 10}, {'bookingid': 205}, {'bookingid': 1125}, {'bookingid': 989}, {'bookingid': 509}, {'bookingid': 990}, {'bookingid': 185}, {'bookingid': 1299}, {'bookingid': 1262}, {'bookingid': 372}, {'bookingid': 1425}, {'bookingid': 984}, {'bookingid': 68}, {'bookingid': 453}, {'bookingid': 1000}, {'bookingid': 127}, {'bookingid': 975}, {'bookingid': 403}, {'bookingid': 123}, {'bookingid': 1155}, {'bookingid': 355}, {'bookingid': 936}, {'bookingid': 130}, {'bookingid': 195}, {'bookingid': 459}, {'bookingid': 875}, {'bookingid': 386}, {'bookingid': 473}, {'bookingid': 912}, {'bookingid': 1414}, {'bookingid': 670}, {'bookingid': 52}, {'bookingid': 634}, {'bookingid': 1143}, {'bookingid': 972}, {'bookingid': 472}, {'bookingid': 764}, {'bookingid': 336}, {'bookingid': 1040}, {'bookingid': 885}, {'bookingid': 1281}, {'bookingid': 319}, {'bookingid': 1313}, {'bookingid': 959}, {'bookingid': 603}, {'bookingid': 279}, {'bookingid': 476}, {'bookingid': 256}, {'bookingid': 1152}, {'bookingid': 1095}, {'bookingid': 816}, {'bookingid': 1378}, {'bookingid': 91}, {'bookingid': 783}, {'bookingid': 1175}, {'bookingid': 761}, {'bookingid': 6}, {'bookingid': 276}, {'bookingid': 1456}, {'bookingid': 632}, {'bookingid': 1213}, {'bookingid': 121}, {'bookingid': 930}, {'bookingid': 62}, {'bookingid': 135}, {'bookingid': 438}, {'bookingid': 1445}, {'bookingid': 755}, {'bookingid': 94}, {'bookingid': 762}, {'bookingid': 317}, {'bookingid': 594}, {'bookingid': 983}, {'bookingid': 1149}, {'bookingid': 398}, {'bookingid': 280}, {'bookingid': 1280}, {'bookingid': 1006}, {'bookingid': 770}, {'bookingid': 449}, {'bookingid': 93}, {'bookingid': 393}, {'bookingid': 795}, {'bookingid': 191}, {'bookingid': 598}, {'bookingid': 1465}, {'bookingid': 295}, {'bookingid': 416}, {'bookingid': 1263}, {'bookingid': 947}, {'bookingid': 445}, {'bookingid': 1298}, {'bookingid': 691}, {'bookingid': 1004}, {'bookingid': 1455}, {'bookingid': 891}, {'bookingid': 482}, {'bookingid': 1383}, {'bookingid': 193}, {'bookingid': 408}, {'bookingid': 1356}, {'bookingid': 465}, {'bookingid': 334}, {'bookingid': 1113}, {'bookingid': 648}, {'bookingid': 610}, {'bookingid': 368}, {'bookingid': 1244}, {'bookingid': 414}, {'bookingid': 1208}, {'bookingid': 813}, {'bookingid': 378}, {'bookingid': 1221}, {'bookingid': 558}, {'bookingid': 480}, {'bookingid': 1075}, {'bookingid': 914}, {'bookingid': 708}, {'bookingid': 98}, {'bookingid': 836}, {'bookingid': 318}, {'bookingid': 143}, {'bookingid': 1224}, {'bookingid': 1206}, {'bookingid': 430}, {'bookingid': 1434}, {'bookingid': 61}, {'bookingid': 1027}, {'bookingid': 583}, {'bookingid': 1087}, {'bookingid': 1193}, {'bookingid': 945}, {'bookingid': 55}, {'bookingid': 701}, {'bookingid': 857}, {'bookingid': 246}, {'bookingid': 729}, {'bookingid': 852}, {'bookingid': 953}, {'bookingid': 1202}, {'bookingid': 297}, {'bookingid': 995}, {'bookingid': 440}, {'bookingid': 925}, {'bookingid': 197}, {'bookingid': 148}, {'bookingid': 405}, {'bookingid': 621}, {'bookingid': 158}, {'bookingid': 1116}, {'bookingid': 32}, {'bookingid': 184}, {'bookingid': 21}, {'bookingid': 111}, {'bookingid': 707}, {'bookingid': 351}, {'bookingid': 1304}, {'bookingid': 1408}, {'bookingid': 247}, {'bookingid': 1147}, {'bookingid': 905}, {'bookingid': 547}, {'bookingid': 898}, {'bookingid': 655}, {'bookingid': 81}, {'bookingid': 903}, {'bookingid': 1115}, {'bookingid': 931}, {'bookingid': 566}, {'bookingid': 1377}, {'bookingid': 1340}, {'bookingid': 268}, {'bookingid': 1240}, {'bookingid': 526}, {'bookingid': 745}, {'bookingid': 669}, {'bookingid': 159}, {'bookingid': 427}, {'bookingid': 1014}, {'bookingid': 896}, {'bookingid': 50}, {'bookingid': 1068}, {'bookingid': 484}, {'bookingid': 869}, {'bookingid': 744}, {'bookingid': 532}, {'bookingid': 510}, {'bookingid': 892}, {'bookingid': 375}, {'bookingid': 971}, {'bookingid': 1049}, {'bookingid': 778}, {'bookingid': 1264}, {'bookingid': 490}, {'bookingid': 1025}, {'bookingid': 249}, {'bookingid': 434}, {'bookingid': 381}, {'bookingid': 1375}, {'bookingid': 42}, {'bookingid': 858}, {'bookingid': 1319}, {'bookingid': 534}, {'bookingid': 640}, {'bookingid': 767}, {'bookingid': 556}, {'bookingid': 1235}, {'bookingid': 1156}, {'bookingid': 394}, {'bookingid': 64}, {'bookingid': 48}, {'bookingid': 316}, {'bookingid': 1417}, {'bookingid': 1178}, {'bookingid': 835}, {'bookingid': 924}, {'bookingid': 28}, {'bookingid': 219}, {'bookingid': 75}, {'bookingid': 841}, {'bookingid': 756}, {'bookingid': 944}, {'bookingid': 142}, {'bookingid': 1137}, {'bookingid': 699}, {'bookingid': 935}, {'bookingid': 788}, {'bookingid': 528}, {'bookingid': 1404}, {'bookingid': 536}, {'bookingid': 1106}, {'bookingid': 733}, {'bookingid': 722}, {'bookingid': 577}, {'bookingid': 1131}, {'bookingid': 1231}, {'bookingid': 807}, {'bookingid': 423}, {'bookingid': 126}, {'bookingid': 31}, {'bookingid': 565}, {'bookingid': 409}, {'bookingid': 432}, {'bookingid': 629}, {'bookingid': 847}, {'bookingid': 1293}, {'bookingid': 1251}, {'bookingid': 1259}, {'bookingid': 1134}, {'bookingid': 758}, {'bookingid': 1296}, {'bookingid': 1347}, {'bookingid': 234}, {'bookingid': 411}, {'bookingid': 567}, {'bookingid': 239}, {'bookingid': 237}, {'bookingid': 1336}, {'bookingid': 241}, {'bookingid': 1232}, {'bookingid': 1236}, {'bookingid': 99}, {'bookingid': 96}, {'bookingid': 124}, {'bookingid': 617}, {'bookingid': 1442}, {'bookingid': 623}, {'bookingid': 429}, {'bookingid': 1024}, {'bookingid': 870}, {'bookingid': 1168}, {'bookingid': 656}, {'bookingid': 963}, {'bookingid': 693}, {'bookingid': 1388}, {'bookingid': 147}, {'bookingid': 1391}, {'bookingid': 1184}, {'bookingid': 229}, {'bookingid': 1316}, {'bookingid': 502}, {'bookingid': 1217}, {'bookingid': 160}, {'bookingid': 175}, {'bookingid': 1191}, {'bookingid': 1121}, {'bookingid': 222}, {'bookingid': 7}, {'bookingid': 1100}, {'bookingid': 1105}, {'bookingid': 960}, {'bookingid': 92}, {'bookingid': 1145}, {'bookingid': 911}, {'bookingid': 956}, {'bookingid': 1013}, {'bookingid': 580}, {'bookingid': 29}, {'bookingid': 1146}, {'bookingid': 544}, {'bookingid': 1005}, {'bookingid': 1180}, {'bookingid': 11}, {'bookingid': 786}, {'bookingid': 19}, {'bookingid': 627}, {'bookingid': 119}, {'bookingid': 494}, {'bookingid': 204}, {'bookingid': 1265}, {'bookingid': 23}, {'bookingid': 1334}, {'bookingid': 252}, {'bookingid': 518}, {'bookingid': 112}, {'bookingid': 138}, {'bookingid': 1079}, {'bookingid': 1033}, {'bookingid': 304}, {'bookingid': 1451}, {'bookingid': 606}, {'bookingid': 879}, {'bookingid': 575}, {'bookingid': 937}, {'bookingid': 216}, {'bookingid': 523}, {'bookingid': 479}, {'bookingid': 1209}, {'bookingid': 716}, {'bookingid': 1085}, {'bookingid': 1279}, {'bookingid': 1450}, {'bookingid': 564}, {'bookingid': 592}, {'bookingid': 842}, {'bookingid': 90}, {'bookingid': 513}, {'bookingid': 1201}, {'bookingid': 433}, {'bookingid': 363}, {'bookingid': 328}, {'bookingid': 942}, {'bookingid': 322}, {'bookingid': 59}, {'bookingid': 287}, {'bookingid': 926}, {'bookingid': 777}, {'bookingid': 608}, {'bookingid': 200}, {'bookingid': 273}, {'bookingid': 428}, {'bookingid': 703}, {'bookingid': 136}, {'bookingid': 740}, {'bookingid': 1441}, {'bookingid': 8}, {'bookingid': 326}, {'bookingid': 919}, {'bookingid': 402}, {'bookingid': 1062}, {'bookingid': 1301}, {'bookingid': 117}, {'bookingid': 1200}, {'bookingid': 47}, {'bookingid': 992}, {'bookingid': 1332}, {'bookingid': 349}, {'bookingid': 311}, {'bookingid': 961}, {'bookingid': 1226}, {'bookingid': 1350}, {'bookingid': 899}, {'bookingid': 1059}, {'bookingid': 281}, {'bookingid': 591}, {'bookingid': 151}, {'bookingid': 1080}, {'bookingid': 587}, {'bookingid': 1470}, {'bookingid': 749}, {'bookingid': 508}, {'bookingid': 817}, {'bookingid': 519}, {'bookingid': 486}, {'bookingid': 43}, {'bookingid': 140}, {'bookingid': 233}, {'bookingid': 798}, {'bookingid': 1268}, {'bookingid': 258}, {'bookingid': 1460}, {'bookingid': 1044}, {'bookingid': 1007}, {'bookingid': 108}, {'bookingid': 782}, {'bookingid': 1081}, {'bookingid': 213}, {'bookingid': 506}, {'bookingid': 1269}, {'bookingid': 1428}, {'bookingid': 625}, {'bookingid': 867}, {'bookingid': 1010}, {'bookingid': 917}, {'bookingid': 918}, {'bookingid': 1335}, {'bookingid': 769}, {'bookingid': 822}, {'bookingid': 1400}, {'bookingid': 952}, {'bookingid': 450}, {'bookingid': 35}, {'bookingid': 871}, {'bookingid': 1420}, {'bookingid': 751}, {'bookingid': 145}, {'bookingid': 675}, {'bookingid': 861}, {'bookingid': 1252}, {'bookingid': 682}, {'bookingid': 602}, {'bookingid': 1218}, {'bookingid': 20}, {'bookingid': 683}, {'bookingid': 496}, {'bookingid': 388}, {'bookingid': 362}, {'bookingid': 1360}, {'bookingid': 1212}, {'bookingid': 1043}, {'bookingid': 1357}, {'bookingid': 977}, {'bookingid': 1119}, {'bookingid': 1091}, {'bookingid': 238}, {'bookingid': 1459}, {'bookingid': 187}, {'bookingid': 1136}, {'bookingid': 664}, {'bookingid': 940}, {'bookingid': 189}, {'bookingid': 779}, {'bookingid': 1435}, {'bookingid': 1154}, {'bookingid': 1096}, {'bookingid': 478}, {'bookingid': 1092}, {'bookingid': 417}, {'bookingid': 1161}, {'bookingid': 981}, {'bookingid': 1123}, {'bookingid': 1223}, {'bookingid': 1275}, {'bookingid': 1073}, {'bookingid': 468}, {'bookingid': 451}, {'bookingid': 954}, {'bookingid': 367}, {'bookingid': 49}, {'bookingid': 674}, {'bookingid': 843}, {'bookingid': 1110}, {'bookingid': 1295}, {'bookingid': 1242}, {'bookingid': 475}, {'bookingid': 1287}, {'bookingid': 614}, {'bookingid': 371}, {'bookingid': 1054}, {'bookingid': 152}, {'bookingid': 1272}, {'bookingid': 702}, {'bookingid': 561}, {'bookingid': 1397}, {'bookingid': 599}, {'bookingid': 1192}, {'bookingid': 1364}, {'bookingid': 1076}, {'bookingid': 41}, {'bookingid': 310}, {'bookingid': 828}, {'bookingid': 600}, {'bookingid': 650}, {'bookingid': 210}, {'bookingid': 882}, {'bookingid': 609}, {'bookingid': 54}, {'bookingid': 464}, {'bookingid': 1067}, {'bookingid': 1411}, {'bookingid': 1088}, {'bookingid': 1127}, {'bookingid': 82}, {'bookingid': 346}, {'bookingid': 913}, {'bookingid': 342}, {'bookingid': 25}, {'bookingid': 613}, {'bookingid': 168}, {'bookingid': 415}, {'bookingid': 1029}, {'bookingid': 661}, {'bookingid': 581}, {'bookingid': 1153}, {'bookingid': 165}, {'bookingid': 1308}, {'bookingid': 190}, {'bookingid': 1325}, {'bookingid': 107}, {'bookingid': 790}, {'bookingid': 1317}, {'bookingid': 676}, {'bookingid': 773}, {'bookingid': 1026}, {'bookingid': 404}, {'bookingid': 887}, {'bookingid': 231}, {'bookingid': 1163}, {'bookingid': 873}, {'bookingid': 1285}, {'bookingid': 626}, {'bookingid': 872}, {'bookingid': 704}, {'bookingid': 574}, {'bookingid': 1429}, {'bookingid': 410}, {'bookingid': 1292}, {'bookingid': 1365}, {'bookingid': 208}, {'bookingid': 397}, {'bookingid': 1349}, {'bookingid': 9}, {'bookingid': 109}, {'bookingid': 115}, {'bookingid': 920}, {'bookingid': 800}, {'bookingid': 79}, {'bookingid': 902}, {'bookingid': 1237}, {'bookingid': 460}, {'bookingid': 1461}, {'bookingid': 732}, {'bookingid': 1351}, {'bookingid': 84}, {'bookingid': 950}, {'bookingid': 607}, {'bookingid': 548}, {'bookingid': 794}, {'bookingid': 313}, {'bookingid': 442}, {'bookingid': 139}, {'bookingid': 1270}, {'bookingid': 1045}, {'bookingid': 1018}, {'bookingid': 149}, {'bookingid': 288}, {'bookingid': 22}, {'bookingid': 1082}, {'bookingid': 505}, {'bookingid': 638}, {'bookingid': 395}, {'bookingid': 854}, {'bookingid': 444}, {'bookingid': 1070}, {'bookingid': 1129}, {'bookingid': 66}, {'bookingid': 550}, {'bookingid': 890}, {'bookingid': 1179}, {'bookingid': 391}, {'bookingid': 787}, {'bookingid': 1194}, {'bookingid': 122}, {'bookingid': 1327}, {'bookingid': 864}, {'bookingid': 1389}, {'bookingid': 40}, {'bookingid': 812}, {'bookingid': 1002}, {'bookingid': 1256}, {'bookingid': 652}, {'bookingid': 1437}, {'bookingid': 827}, {'bookingid': 72}, {'bookingid': 14}, {'bookingid': 752}, {'bookingid': 834}, {'bookingid': 4}, {'bookingid': 1148}, {'bookingid': 110}, {'bookingid': 1225}, {'bookingid': 537}, {'bookingid': 1187}, {'bookingid': 1065}, {'bookingid': 645}, {'bookingid': 259}, {'bookingid': 253}, {'bookingid': 177}, {'bookingid': 849}, {'bookingid': 261}, {'bookingid': 1108}, {'bookingid': 1053}, {'bookingid': 785}, {'bookingid': 1034}, {'bookingid': 85}, {'bookingid': 718}, {'bookingid': 673}, {'bookingid': 951}, {'bookingid': 366}, {'bookingid': 201}, {'bookingid': 1188}, {'bookingid': 156}, {'bookingid': 379}, {'bookingid': 658}, {'bookingid': 846}, {'bookingid': 1385}, {'bookingid': 573}, {'bookingid': 809}, {'bookingid': 284}, {'bookingid': 1052}, {'bookingid': 1320}, {'bookingid': 1211}, {'bookingid': 893}, {'bookingid': 771}, {'bookingid': 128}, {'bookingid': 743}, {'bookingid': 1310}, {'bookingid': 1379}, {'bookingid': 730}, {'bookingid': 192}, {'bookingid': 1058}, {'bookingid': 215}, {'bookingid': 356}, {'bookingid': 1329}, {'bookingid': 1162}, {'bookingid': 1371}, {'bookingid': 223}, {'bookingid': 441}, {'bookingid': 824}, {'bookingid': 457}, {'bookingid': 586}, {'bookingid': 1246}, {'bookingid': 538}, {'bookingid': 570}, {'bookingid': 272}, {'bookingid': 1063}, {'bookingid': 694}, {'bookingid': 605}, {'bookingid': 1128}, {'bookingid': 1453}, {'bookingid': 359}, {'bookingid': 1196}, {'bookingid': 527}, {'bookingid': 1166}, {'bookingid': 301}, {'bookingid': 1413}, {'bookingid': 1311}, {'bookingid': 76}, {'bookingid': 1167}, {'bookingid': 27}, {'bookingid': 80}, {'bookingid': 181}, {'bookingid': 1220}, {'bookingid': 539}, {'bookingid': 686}, {'bookingid': 520}, {'bookingid': 421}, {'bookingid': 696}, {'bookingid': 969}, {'bookingid': 102}, {'bookingid': 270}, {'bookingid': 463}, {'bookingid': 578}, {'bookingid': 1444}, {'bookingid': 1393}, {'bookingid': 1099}, {'bookingid': 12}, {'bookingid': 277}, {'bookingid': 593}, {'bookingid': 976}, {'bookingid': 731}, {'bookingid': 711}, {'bookingid': 839}, {'bookingid': 815}, {'bookingid': 324}, {'bookingid': 283}, {'bookingid': 878}, {'bookingid': 840}, {'bookingid': 292}, {'bookingid': 772}, {'bookingid': 499}, {'bookingid': 101}, {'bookingid': 1258}, {'bookingid': 220}, {'bookingid': 1118}, {'bookingid': 1169}, {'bookingid': 966}, {'bookingid': 641}, {'bookingid': 36}, {'bookingid': 1172}, {'bookingid': 1419}, {'bookingid': 1468}, {'bookingid': 1352}, {'bookingid': 469}, {'bookingid': 647}, {'bookingid': 87}, {'bookingid': 500}, {'bookingid': 1422}, {'bookingid': 1423}, {'bookingid': 1257}, {'bookingid': 285}, {'bookingid': 757}, {'bookingid': 65}, {'bookingid': 726}, {'bookingid': 15}, {'bookingid': 2}, {'bookingid': 723}, {'bookingid': 1440}, {'bookingid': 462}, {'bookingid': 1471}, {'bookingid': 374}, {'bookingid': 1017}, {'bookingid': 167}, {'bookingid': 886}, {'bookingid': 667}, {'bookingid': 980}, {'bookingid': 1195}, {'bookingid': 265}, {'bookingid': 1355}, {'bookingid': 1406}, {'bookingid': 739}, {'bookingid': 535}, {'bookingid': 17}, {'bookingid': 685}, {'bookingid': 821}, {'bookingid': 1431}, {'bookingid': 199}, {'bookingid': 993}, {'bookingid': 97}, {'bookingid': 1323}, {'bookingid': 1174}, {'bookingid': 789}, {'bookingid': 426}, {'bookingid': 294}, {'bookingid': 178}, {'bookingid': 1338}, {'bookingid': 1362}, {'bookingid': 957}, {'bookingid': 471}, {'bookingid': 1}, {'bookingid': 1238}, {'bookingid': 517}, {'bookingid': 439}, {'bookingid': 1367}, {'bookingid': 73}, {'bookingid': 364}, {'bookingid': 1111}, {'bookingid': 529}, {'bookingid': 1160}, {'bookingid': 1112}, {'bookingid': 1305}, {'bookingid': 649}, {'bookingid': 1104}, {'bookingid': 309}, {'bookingid': 106}, {'bookingid': 228}, {'bookingid': 67}, {'bookingid': 89}, {'bookingid': 698}, {'bookingid': 897}, {'bookingid': 1344}, {'bookingid': 531}, {'bookingid': 1446}, {'bookingid': 737}, {'bookingid': 1035}, {'bookingid': 1250}, {'bookingid': 763}, {'bookingid': 33}, {'bookingid': 943}, {'bookingid': 923}, {'bookingid': 962}, {'bookingid': 118}, {'bookingid': 866}, {'bookingid': 1277}, {'bookingid': 1229}, {'bookingid': 260}, {'bookingid': 860}, {'bookingid': 1330}, {'bookingid': 1363}, {'bookingid': 1055}, {'bookingid': 306}, {'bookingid': 546}, {'bookingid': 719}, {'bookingid': 1011}, {'bookingid': 668}, {'bookingid': 584}, {'bookingid': 1359}, {'bookingid': 492}, {'bookingid': 713}, {'bookingid': 1282}, {'bookingid': 1380}, {'bookingid': 250}, {'bookingid': 823}, {'bookingid': 746}, {'bookingid': 224}, {'bookingid': 1466}, {'bookingid': 797}, {'bookingid': 801}, {'bookingid': 521}, {'bookingid': 1022}, {'bookingid': 1023}, {'bookingid': 214}, {'bookingid': 1401}, {'bookingid': 1341}, {'bookingid': 1289}, {'bookingid': 305}, {'bookingid': 1273}, {'bookingid': 616}, {'bookingid': 291}, {'bookingid': 1370}, {'bookingid': 487}, {'bookingid': 637}, {'bookingid': 504}, {'bookingid': 725}, {'bookingid': 269}, {'bookingid': 1386}, {'bookingid': 1458}, {'bookingid': 493}, {'bookingid': 448}, {'bookingid': 1346}, {'bookingid': 881}, {'bookingid': 1243}, {'bookingid': 198}, {'bookingid': 420}, {'bookingid': 1061}, {'bookingid': 86}, {'bookingid': 657}, {'bookingid': 163}, {'bookingid': 985}, {'bookingid': 1182}, {'bookingid': 714}, {'bookingid': 1016}, {'bookingid': 814}, {'bookingid': 1312}, {'bookingid': 738}], 'Response body mismatch')

def test_get_booking_45():
    """Test generated from Schemathesis VCR: 4341Uv
    Test: GET /booking
    Status: SUCCESS
    """
    import requests
    
    url = f"https://restful-booker.herokuapp.com/booking"
    headers = {'User-Agent': 'schemathesis/4.3.15', 'Accept-Encoding': 'gzip, deflate, zstd', 'Accept': 'application/json', 'Connection': 'keep-alive', 'Authorization': 'Basic YWRtaW46cGFzc3dvcmQxMjM=', 'Content-Type': 'application/json'}
    
    response = requests.get(url, headers=headers)
    
    check.equal(response.status_code, 200, f'Expected status 200, got {response.status_code}')
    check.equal(response.json(), [{'bookingid': 853}, {'bookingid': 697}, {'bookingid': 559}, {'bookingid': 141}, {'bookingid': 1066}, {'bookingid': 1230}, {'bookingid': 343}, {'bookingid': 344}, {'bookingid': 105}, {'bookingid': 596}, {'bookingid': 688}, {'bookingid': 3}, {'bookingid': 568}, {'bookingid': 553}, {'bookingid': 1394}, {'bookingid': 456}, {'bookingid': 863}, {'bookingid': 383}, {'bookingid': 803}, {'bookingid': 390}, {'bookingid': 631}, {'bookingid': 330}, {'bookingid': 53}, {'bookingid': 642}, {'bookingid': 154}, {'bookingid': 1307}, {'bookingid': 331}, {'bookingid': 5}, {'bookingid': 131}, {'bookingid': 728}, {'bookingid': 370}, {'bookingid': 907}, {'bookingid': 1443}, {'bookingid': 991}, {'bookingid': 679}, {'bookingid': 1074}, {'bookingid': 357}, {'bookingid': 264}, {'bookingid': 663}, {'bookingid': 266}, {'bookingid': 830}, {'bookingid': 1028}, {'bookingid': 116}, {'bookingid': 1190}, {'bookingid': 302}, {'bookingid': 560}, {'bookingid': 1409}, {'bookingid': 851}, {'bookingid': 37}, {'bookingid': 644}, {'bookingid': 18}, {'bookingid': 209}, {'bookingid': 1297}, {'bookingid': 360}, {'bookingid': 173}, {'bookingid': 1041}, {'bookingid': 806}, {'bookingid': 1086}, {'bookingid': 56}, {'bookingid': 1290}, {'bookingid': 1139}, {'bookingid': 498}, {'bookingid': 1093}, {'bookingid': 1038}, {'bookingid': 1042}, {'bookingid': 298}, {'bookingid': 332}, {'bookingid': 618}, {'bookingid': 338}, {'bookingid': 1122}, {'bookingid': 172}, {'bookingid': 687}, {'bookingid': 1037}, {'bookingid': 859}, {'bookingid': 1050}, {'bookingid': 314}, {'bookingid': 354}, {'bookingid': 225}, {'bookingid': 1452}, {'bookingid': 802}, {'bookingid': 166}, {'bookingid': 325}, {'bookingid': 543}, {'bookingid': 929}, {'bookingid': 689}, {'bookingid': 589}, {'bookingid': 974}, {'bookingid': 620}, {'bookingid': 938}, {'bookingid': 207}, {'bookingid': 1398}, {'bookingid': 1132}, {'bookingid': 232}, {'bookingid': 1205}, {'bookingid': 904}, {'bookingid': 1416}, {'bookingid': 382}, {'bookingid': 385}, {'bookingid': 340}, {'bookingid': 1369}, {'bookingid': 242}, {'bookingid': 255}, {'bookingid': 100}, {'bookingid': 347}, {'bookingid': 26}, {'bookingid': 1436}, {'bookingid': 1373}, {'bookingid': 162}, {'bookingid': 633}, {'bookingid': 717}, {'bookingid': 662}, {'bookingid': 750}, {'bookingid': 1342}, {'bookingid': 1203}, {'bookingid': 1405}, {'bookingid': 337}, {'bookingid': 77}, {'bookingid': 514}, {'bookingid': 516}, {'bookingid': 1138}, {'bookingid': 44}, {'bookingid': 71}, {'bookingid': 780}, {'bookingid': 1181}, {'bookingid': 677}, {'bookingid': 171}, {'bookingid': 1253}, {'bookingid': 150}, {'bookingid': 1019}, {'bookingid': 1097}, {'bookingid': 1322}, {'bookingid': 57}, {'bookingid': 551}, {'bookingid': 999}, {'bookingid': 1463}, {'bookingid': 829}, {'bookingid': 350}, {'bookingid': 183}, {'bookingid': 906}, {'bookingid': 1278}, {'bookingid': 1392}, {'bookingid': 833}, {'bookingid': 555}, {'bookingid': 998}, {'bookingid': 884}, {'bookingid': 299}, {'bookingid': 180}, {'bookingid': 240}, {'bookingid': 424}, {'bookingid': 1426}, {'bookingid': 1210}, {'bookingid': 1402}, {'bookingid': 132}, {'bookingid': 129}, {'bookingid': 60}, {'bookingid': 1103}, {'bookingid': 932}, {'bookingid': 706}, {'bookingid': 396}, {'bookingid': 810}, {'bookingid': 447}, {'bookingid': 1142}, {'bookingid': 768}, {'bookingid': 74}, {'bookingid': 488}, {'bookingid': 986}, {'bookingid': 1433}, {'bookingid': 1374}, {'bookingid': 968}, {'bookingid': 275}, {'bookingid': 1173}, {'bookingid': 1247}, {'bookingid': 46}, {'bookingid': 1288}, {'bookingid': 1321}, {'bookingid': 10}, {'bookingid': 205}, {'bookingid': 1125}, {'bookingid': 989}, {'bookingid': 509}, {'bookingid': 990}, {'bookingid': 185}, {'bookingid': 1299}, {'bookingid': 1262}, {'bookingid': 372}, {'bookingid': 1425}, {'bookingid': 984}, {'bookingid': 68}, {'bookingid': 453}, {'bookingid': 1000}, {'bookingid': 127}, {'bookingid': 975}, {'bookingid': 403}, {'bookingid': 123}, {'bookingid': 1155}, {'bookingid': 355}, {'bookingid': 936}, {'bookingid': 130}, {'bookingid': 195}, {'bookingid': 459}, {'bookingid': 875}, {'bookingid': 386}, {'bookingid': 473}, {'bookingid': 912}, {'bookingid': 1414}, {'bookingid': 670}, {'bookingid': 52}, {'bookingid': 634}, {'bookingid': 1143}, {'bookingid': 972}, {'bookingid': 472}, {'bookingid': 764}, {'bookingid': 336}, {'bookingid': 1040}, {'bookingid': 885}, {'bookingid': 1281}, {'bookingid': 319}, {'bookingid': 1313}, {'bookingid': 959}, {'bookingid': 603}, {'bookingid': 279}, {'bookingid': 476}, {'bookingid': 256}, {'bookingid': 1152}, {'bookingid': 1095}, {'bookingid': 816}, {'bookingid': 1378}, {'bookingid': 91}, {'bookingid': 783}, {'bookingid': 1175}, {'bookingid': 761}, {'bookingid': 6}, {'bookingid': 276}, {'bookingid': 1456}, {'bookingid': 632}, {'bookingid': 1213}, {'bookingid': 121}, {'bookingid': 930}, {'bookingid': 62}, {'bookingid': 135}, {'bookingid': 438}, {'bookingid': 1445}, {'bookingid': 755}, {'bookingid': 94}, {'bookingid': 762}, {'bookingid': 317}, {'bookingid': 594}, {'bookingid': 983}, {'bookingid': 1149}, {'bookingid': 398}, {'bookingid': 280}, {'bookingid': 1280}, {'bookingid': 1006}, {'bookingid': 770}, {'bookingid': 449}, {'bookingid': 93}, {'bookingid': 393}, {'bookingid': 795}, {'bookingid': 191}, {'bookingid': 598}, {'bookingid': 1465}, {'bookingid': 295}, {'bookingid': 416}, {'bookingid': 1263}, {'bookingid': 947}, {'bookingid': 445}, {'bookingid': 1298}, {'bookingid': 691}, {'bookingid': 1004}, {'bookingid': 1455}, {'bookingid': 891}, {'bookingid': 482}, {'bookingid': 1383}, {'bookingid': 193}, {'bookingid': 408}, {'bookingid': 1356}, {'bookingid': 465}, {'bookingid': 334}, {'bookingid': 1113}, {'bookingid': 648}, {'bookingid': 610}, {'bookingid': 368}, {'bookingid': 1244}, {'bookingid': 414}, {'bookingid': 1208}, {'bookingid': 813}, {'bookingid': 378}, {'bookingid': 1221}, {'bookingid': 558}, {'bookingid': 480}, {'bookingid': 1075}, {'bookingid': 914}, {'bookingid': 708}, {'bookingid': 98}, {'bookingid': 836}, {'bookingid': 318}, {'bookingid': 143}, {'bookingid': 1224}, {'bookingid': 1206}, {'bookingid': 430}, {'bookingid': 1434}, {'bookingid': 61}, {'bookingid': 1027}, {'bookingid': 583}, {'bookingid': 1087}, {'bookingid': 1193}, {'bookingid': 945}, {'bookingid': 55}, {'bookingid': 701}, {'bookingid': 857}, {'bookingid': 246}, {'bookingid': 729}, {'bookingid': 852}, {'bookingid': 953}, {'bookingid': 1202}, {'bookingid': 297}, {'bookingid': 995}, {'bookingid': 440}, {'bookingid': 925}, {'bookingid': 197}, {'bookingid': 148}, {'bookingid': 405}, {'bookingid': 621}, {'bookingid': 158}, {'bookingid': 1116}, {'bookingid': 32}, {'bookingid': 184}, {'bookingid': 21}, {'bookingid': 111}, {'bookingid': 707}, {'bookingid': 351}, {'bookingid': 1304}, {'bookingid': 1408}, {'bookingid': 247}, {'bookingid': 1147}, {'bookingid': 905}, {'bookingid': 547}, {'bookingid': 898}, {'bookingid': 655}, {'bookingid': 81}, {'bookingid': 903}, {'bookingid': 1115}, {'bookingid': 931}, {'bookingid': 566}, {'bookingid': 1377}, {'bookingid': 1340}, {'bookingid': 268}, {'bookingid': 1240}, {'bookingid': 526}, {'bookingid': 745}, {'bookingid': 669}, {'bookingid': 159}, {'bookingid': 1474}, {'bookingid': 427}, {'bookingid': 1014}, {'bookingid': 896}, {'bookingid': 50}, {'bookingid': 1068}, {'bookingid': 484}, {'bookingid': 869}, {'bookingid': 744}, {'bookingid': 532}, {'bookingid': 510}, {'bookingid': 892}, {'bookingid': 375}, {'bookingid': 971}, {'bookingid': 1049}, {'bookingid': 778}, {'bookingid': 1264}, {'bookingid': 490}, {'bookingid': 1025}, {'bookingid': 249}, {'bookingid': 434}, {'bookingid': 381}, {'bookingid': 1375}, {'bookingid': 42}, {'bookingid': 858}, {'bookingid': 1319}, {'bookingid': 534}, {'bookingid': 640}, {'bookingid': 767}, {'bookingid': 556}, {'bookingid': 1235}, {'bookingid': 1156}, {'bookingid': 394}, {'bookingid': 64}, {'bookingid': 48}, {'bookingid': 316}, {'bookingid': 1417}, {'bookingid': 1178}, {'bookingid': 835}, {'bookingid': 924}, {'bookingid': 28}, {'bookingid': 219}, {'bookingid': 75}, {'bookingid': 841}, {'bookingid': 756}, {'bookingid': 944}, {'bookingid': 142}, {'bookingid': 1137}, {'bookingid': 699}, {'bookingid': 935}, {'bookingid': 788}, {'bookingid': 528}, {'bookingid': 1404}, {'bookingid': 536}, {'bookingid': 1106}, {'bookingid': 733}, {'bookingid': 722}, {'bookingid': 577}, {'bookingid': 1131}, {'bookingid': 1231}, {'bookingid': 807}, {'bookingid': 423}, {'bookingid': 126}, {'bookingid': 31}, {'bookingid': 565}, {'bookingid': 409}, {'bookingid': 432}, {'bookingid': 629}, {'bookingid': 847}, {'bookingid': 1293}, {'bookingid': 1251}, {'bookingid': 1259}, {'bookingid': 1134}, {'bookingid': 758}, {'bookingid': 1296}, {'bookingid': 1347}, {'bookingid': 234}, {'bookingid': 411}, {'bookingid': 567}, {'bookingid': 239}, {'bookingid': 237}, {'bookingid': 1336}, {'bookingid': 241}, {'bookingid': 1232}, {'bookingid': 1236}, {'bookingid': 99}, {'bookingid': 96}, {'bookingid': 124}, {'bookingid': 617}, {'bookingid': 1442}, {'bookingid': 623}, {'bookingid': 429}, {'bookingid': 1024}, {'bookingid': 870}, {'bookingid': 1168}, {'bookingid': 656}, {'bookingid': 963}, {'bookingid': 693}, {'bookingid': 1388}, {'bookingid': 147}, {'bookingid': 1391}, {'bookingid': 1184}, {'bookingid': 229}, {'bookingid': 1316}, {'bookingid': 502}, {'bookingid': 1217}, {'bookingid': 160}, {'bookingid': 175}, {'bookingid': 1191}, {'bookingid': 1121}, {'bookingid': 222}, {'bookingid': 7}, {'bookingid': 1100}, {'bookingid': 1105}, {'bookingid': 960}, {'bookingid': 92}, {'bookingid': 1145}, {'bookingid': 911}, {'bookingid': 956}, {'bookingid': 1013}, {'bookingid': 580}, {'bookingid': 29}, {'bookingid': 1146}, {'bookingid': 544}, {'bookingid': 1005}, {'bookingid': 1180}, {'bookingid': 11}, {'bookingid': 786}, {'bookingid': 19}, {'bookingid': 627}, {'bookingid': 119}, {'bookingid': 494}, {'bookingid': 204}, {'bookingid': 1265}, {'bookingid': 23}, {'bookingid': 1334}, {'bookingid': 252}, {'bookingid': 518}, {'bookingid': 112}, {'bookingid': 138}, {'bookingid': 1079}, {'bookingid': 1033}, {'bookingid': 304}, {'bookingid': 1451}, {'bookingid': 606}, {'bookingid': 879}, {'bookingid': 575}, {'bookingid': 937}, {'bookingid': 216}, {'bookingid': 523}, {'bookingid': 479}, {'bookingid': 1209}, {'bookingid': 716}, {'bookingid': 1085}, {'bookingid': 1279}, {'bookingid': 1450}, {'bookingid': 564}, {'bookingid': 592}, {'bookingid': 842}, {'bookingid': 90}, {'bookingid': 513}, {'bookingid': 1201}, {'bookingid': 433}, {'bookingid': 363}, {'bookingid': 328}, {'bookingid': 942}, {'bookingid': 322}, {'bookingid': 59}, {'bookingid': 287}, {'bookingid': 926}, {'bookingid': 777}, {'bookingid': 608}, {'bookingid': 200}, {'bookingid': 273}, {'bookingid': 428}, {'bookingid': 703}, {'bookingid': 136}, {'bookingid': 740}, {'bookingid': 1441}, {'bookingid': 8}, {'bookingid': 326}, {'bookingid': 919}, {'bookingid': 402}, {'bookingid': 1062}, {'bookingid': 1301}, {'bookingid': 117}, {'bookingid': 1200}, {'bookingid': 47}, {'bookingid': 992}, {'bookingid': 1332}, {'bookingid': 349}, {'bookingid': 311}, {'bookingid': 961}, {'bookingid': 1226}, {'bookingid': 1350}, {'bookingid': 899}, {'bookingid': 1059}, {'bookingid': 281}, {'bookingid': 591}, {'bookingid': 151}, {'bookingid': 1080}, {'bookingid': 587}, {'bookingid': 1470}, {'bookingid': 749}, {'bookingid': 508}, {'bookingid': 817}, {'bookingid': 519}, {'bookingid': 486}, {'bookingid': 43}, {'bookingid': 140}, {'bookingid': 233}, {'bookingid': 798}, {'bookingid': 1268}, {'bookingid': 258}, {'bookingid': 1460}, {'bookingid': 1044}, {'bookingid': 1007}, {'bookingid': 108}, {'bookingid': 782}, {'bookingid': 1081}, {'bookingid': 213}, {'bookingid': 506}, {'bookingid': 1269}, {'bookingid': 1428}, {'bookingid': 625}, {'bookingid': 867}, {'bookingid': 1010}, {'bookingid': 917}, {'bookingid': 918}, {'bookingid': 1335}, {'bookingid': 769}, {'bookingid': 822}, {'bookingid': 1400}, {'bookingid': 952}, {'bookingid': 450}, {'bookingid': 35}, {'bookingid': 871}, {'bookingid': 1420}, {'bookingid': 751}, {'bookingid': 145}, {'bookingid': 675}, {'bookingid': 861}, {'bookingid': 1252}, {'bookingid': 682}, {'bookingid': 602}, {'bookingid': 1218}, {'bookingid': 20}, {'bookingid': 683}, {'bookingid': 496}, {'bookingid': 388}, {'bookingid': 362}, {'bookingid': 1360}, {'bookingid': 1212}, {'bookingid': 1043}, {'bookingid': 1357}, {'bookingid': 977}, {'bookingid': 1119}, {'bookingid': 1091}, {'bookingid': 238}, {'bookingid': 1459}, {'bookingid': 187}, {'bookingid': 1136}, {'bookingid': 664}, {'bookingid': 940}, {'bookingid': 189}, {'bookingid': 779}, {'bookingid': 1472}, {'bookingid': 1435}, {'bookingid': 1154}, {'bookingid': 1096}, {'bookingid': 478}, {'bookingid': 1092}, {'bookingid': 417}, {'bookingid': 1161}, {'bookingid': 981}, {'bookingid': 1123}, {'bookingid': 1223}, {'bookingid': 1275}, {'bookingid': 1073}, {'bookingid': 468}, {'bookingid': 451}, {'bookingid': 954}, {'bookingid': 367}, {'bookingid': 49}, {'bookingid': 674}, {'bookingid': 843}, {'bookingid': 1110}, {'bookingid': 1295}, {'bookingid': 1242}, {'bookingid': 475}, {'bookingid': 1287}, {'bookingid': 614}, {'bookingid': 371}, {'bookingid': 1054}, {'bookingid': 152}, {'bookingid': 1272}, {'bookingid': 702}, {'bookingid': 561}, {'bookingid': 1397}, {'bookingid': 599}, {'bookingid': 1192}, {'bookingid': 1364}, {'bookingid': 1076}, {'bookingid': 41}, {'bookingid': 310}, {'bookingid': 828}, {'bookingid': 600}, {'bookingid': 650}, {'bookingid': 210}, {'bookingid': 882}, {'bookingid': 609}, {'bookingid': 54}, {'bookingid': 464}, {'bookingid': 1067}, {'bookingid': 1411}, {'bookingid': 1088}, {'bookingid': 1127}, {'bookingid': 82}, {'bookingid': 346}, {'bookingid': 913}, {'bookingid': 342}, {'bookingid': 25}, {'bookingid': 613}, {'bookingid': 168}, {'bookingid': 415}, {'bookingid': 1029}, {'bookingid': 661}, {'bookingid': 581}, {'bookingid': 1153}, {'bookingid': 165}, {'bookingid': 1308}, {'bookingid': 190}, {'bookingid': 1325}, {'bookingid': 107}, {'bookingid': 790}, {'bookingid': 1317}, {'bookingid': 676}, {'bookingid': 773}, {'bookingid': 1026}, {'bookingid': 404}, {'bookingid': 887}, {'bookingid': 231}, {'bookingid': 1163}, {'bookingid': 873}, {'bookingid': 1285}, {'bookingid': 626}, {'bookingid': 872}, {'bookingid': 704}, {'bookingid': 574}, {'bookingid': 1429}, {'bookingid': 410}, {'bookingid': 1292}, {'bookingid': 1365}, {'bookingid': 208}, {'bookingid': 397}, {'bookingid': 1349}, {'bookingid': 9}, {'bookingid': 109}, {'bookingid': 115}, {'bookingid': 920}, {'bookingid': 800}, {'bookingid': 79}, {'bookingid': 902}, {'bookingid': 1237}, {'bookingid': 460}, {'bookingid': 1461}, {'bookingid': 732}, {'bookingid': 1351}, {'bookingid': 84}, {'bookingid': 950}, {'bookingid': 607}, {'bookingid': 548}, {'bookingid': 794}, {'bookingid': 313}, {'bookingid': 442}, {'bookingid': 139}, {'bookingid': 1270}, {'bookingid': 1045}, {'bookingid': 1018}, {'bookingid': 149}, {'bookingid': 288}, {'bookingid': 22}, {'bookingid': 1082}, {'bookingid': 505}, {'bookingid': 638}, {'bookingid': 395}, {'bookingid': 854}, {'bookingid': 444}, {'bookingid': 1070}, {'bookingid': 1129}, {'bookingid': 66}, {'bookingid': 550}, {'bookingid': 890}, {'bookingid': 1179}, {'bookingid': 391}, {'bookingid': 787}, {'bookingid': 1194}, {'bookingid': 122}, {'bookingid': 1327}, {'bookingid': 864}, {'bookingid': 1389}, {'bookingid': 40}, {'bookingid': 812}, {'bookingid': 1002}, {'bookingid': 1256}, {'bookingid': 652}, {'bookingid': 1437}, {'bookingid': 827}, {'bookingid': 72}, {'bookingid': 14}, {'bookingid': 752}, {'bookingid': 834}, {'bookingid': 4}, {'bookingid': 1148}, {'bookingid': 110}, {'bookingid': 1225}, {'bookingid': 537}, {'bookingid': 1187}, {'bookingid': 1065}, {'bookingid': 645}, {'bookingid': 259}, {'bookingid': 253}, {'bookingid': 177}, {'bookingid': 849}, {'bookingid': 261}, {'bookingid': 1108}, {'bookingid': 1053}, {'bookingid': 785}, {'bookingid': 1034}, {'bookingid': 85}, {'bookingid': 718}, {'bookingid': 673}, {'bookingid': 951}, {'bookingid': 366}, {'bookingid': 201}, {'bookingid': 1188}, {'bookingid': 156}, {'bookingid': 379}, {'bookingid': 658}, {'bookingid': 846}, {'bookingid': 1385}, {'bookingid': 573}, {'bookingid': 809}, {'bookingid': 284}, {'bookingid': 1052}, {'bookingid': 1320}, {'bookingid': 1211}, {'bookingid': 893}, {'bookingid': 771}, {'bookingid': 128}, {'bookingid': 743}, {'bookingid': 1310}, {'bookingid': 1379}, {'bookingid': 730}, {'bookingid': 192}, {'bookingid': 1058}, {'bookingid': 215}, {'bookingid': 356}, {'bookingid': 1329}, {'bookingid': 1162}, {'bookingid': 1371}, {'bookingid': 223}, {'bookingid': 441}, {'bookingid': 824}, {'bookingid': 457}, {'bookingid': 586}, {'bookingid': 1246}, {'bookingid': 538}, {'bookingid': 570}, {'bookingid': 272}, {'bookingid': 1063}, {'bookingid': 694}, {'bookingid': 605}, {'bookingid': 1128}, {'bookingid': 1453}, {'bookingid': 359}, {'bookingid': 1196}, {'bookingid': 527}, {'bookingid': 1166}, {'bookingid': 301}, {'bookingid': 1413}, {'bookingid': 1311}, {'bookingid': 76}, {'bookingid': 1167}, {'bookingid': 27}, {'bookingid': 80}, {'bookingid': 181}, {'bookingid': 1220}, {'bookingid': 539}, {'bookingid': 686}, {'bookingid': 520}, {'bookingid': 421}, {'bookingid': 696}, {'bookingid': 969}, {'bookingid': 102}, {'bookingid': 270}, {'bookingid': 463}, {'bookingid': 578}, {'bookingid': 1444}, {'bookingid': 1393}, {'bookingid': 1099}, {'bookingid': 12}, {'bookingid': 277}, {'bookingid': 593}, {'bookingid': 976}, {'bookingid': 731}, {'bookingid': 711}, {'bookingid': 839}, {'bookingid': 815}, {'bookingid': 324}, {'bookingid': 283}, {'bookingid': 878}, {'bookingid': 840}, {'bookingid': 292}, {'bookingid': 772}, {'bookingid': 499}, {'bookingid': 101}, {'bookingid': 1258}, {'bookingid': 220}, {'bookingid': 1118}, {'bookingid': 1169}, {'bookingid': 966}, {'bookingid': 641}, {'bookingid': 36}, {'bookingid': 1172}, {'bookingid': 1419}, {'bookingid': 1468}, {'bookingid': 1352}, {'bookingid': 469}, {'bookingid': 647}, {'bookingid': 87}, {'bookingid': 500}, {'bookingid': 1422}, {'bookingid': 1423}, {'bookingid': 1257}, {'bookingid': 285}, {'bookingid': 757}, {'bookingid': 65}, {'bookingid': 726}, {'bookingid': 15}, {'bookingid': 2}, {'bookingid': 723}, {'bookingid': 1440}, {'bookingid': 462}, {'bookingid': 1471}, {'bookingid': 374}, {'bookingid': 1017}, {'bookingid': 167}, {'bookingid': 886}, {'bookingid': 667}, {'bookingid': 980}, {'bookingid': 1195}, {'bookingid': 265}, {'bookingid': 1355}, {'bookingid': 1406}, {'bookingid': 739}, {'bookingid': 535}, {'bookingid': 17}, {'bookingid': 685}, {'bookingid': 821}, {'bookingid': 1431}, {'bookingid': 199}, {'bookingid': 993}, {'bookingid': 97}, {'bookingid': 1323}, {'bookingid': 1174}, {'bookingid': 789}, {'bookingid': 426}, {'bookingid': 294}, {'bookingid': 178}, {'bookingid': 1338}, {'bookingid': 1362}, {'bookingid': 957}, {'bookingid': 471}, {'bookingid': 1}, {'bookingid': 1238}, {'bookingid': 517}, {'bookingid': 439}, {'bookingid': 1367}, {'bookingid': 73}, {'bookingid': 364}, {'bookingid': 1111}, {'bookingid': 529}, {'bookingid': 1160}, {'bookingid': 1112}, {'bookingid': 1305}, {'bookingid': 649}, {'bookingid': 1104}, {'bookingid': 309}, {'bookingid': 106}, {'bookingid': 228}, {'bookingid': 67}, {'bookingid': 89}, {'bookingid': 698}, {'bookingid': 897}, {'bookingid': 1344}, {'bookingid': 531}, {'bookingid': 1446}, {'bookingid': 737}, {'bookingid': 1035}, {'bookingid': 1250}, {'bookingid': 763}, {'bookingid': 33}, {'bookingid': 943}, {'bookingid': 923}, {'bookingid': 962}, {'bookingid': 118}, {'bookingid': 866}, {'bookingid': 1277}, {'bookingid': 1229}, {'bookingid': 260}, {'bookingid': 860}, {'bookingid': 1330}, {'bookingid': 1363}, {'bookingid': 1055}, {'bookingid': 306}, {'bookingid': 546}, {'bookingid': 719}, {'bookingid': 1011}, {'bookingid': 668}, {'bookingid': 584}, {'bookingid': 1359}, {'bookingid': 492}, {'bookingid': 713}, {'bookingid': 1282}, {'bookingid': 1380}, {'bookingid': 250}, {'bookingid': 823}, {'bookingid': 746}, {'bookingid': 224}, {'bookingid': 1466}, {'bookingid': 797}, {'bookingid': 801}, {'bookingid': 521}, {'bookingid': 1022}, {'bookingid': 1023}, {'bookingid': 214}, {'bookingid': 1401}, {'bookingid': 1341}, {'bookingid': 1289}, {'bookingid': 305}, {'bookingid': 1273}, {'bookingid': 616}, {'bookingid': 291}, {'bookingid': 1370}, {'bookingid': 487}, {'bookingid': 637}, {'bookingid': 504}, {'bookingid': 725}, {'bookingid': 269}, {'bookingid': 1386}, {'bookingid': 1458}, {'bookingid': 493}, {'bookingid': 448}, {'bookingid': 1346}, {'bookingid': 881}, {'bookingid': 1243}, {'bookingid': 198}, {'bookingid': 420}, {'bookingid': 1061}, {'bookingid': 86}, {'bookingid': 657}, {'bookingid': 163}, {'bookingid': 985}, {'bookingid': 1182}, {'bookingid': 714}, {'bookingid': 1016}, {'bookingid': 814}, {'bookingid': 1312}, {'bookingid': 738}], 'Response body mismatch')

def test_get_booking_46():
    """Test generated from Schemathesis VCR: lqkyJl
    Test: GET /booking
    Status: SUCCESS
    """
    import requests
    
    url = f"https://restful-booker.herokuapp.com/booking"
    headers = {'User-Agent': 'schemathesis/4.3.15', 'Accept-Encoding': 'gzip, deflate, zstd', 'Accept': 'application/json', 'Connection': 'keep-alive', 'Authorization': 'Basic YWRtaW46cGFzc3dvcmQxMjM=', 'Content-Type': 'application/json'}
    
    response = requests.get(url, headers=headers)
    
    check.equal(response.status_code, 200, f'Expected status 200, got {response.status_code}')
    check.equal(response.json(), [{'bookingid': 1471}], 'Response body mismatch')

def test_get_booking_47():
    """Test generated from Schemathesis VCR: H1NPiK
    Test: GET /booking
    Status: SUCCESS
    """
    import requests
    
    url = f"https://restful-booker.herokuapp.com/booking"
    headers = {'User-Agent': 'schemathesis/4.3.15', 'Accept-Encoding': 'gzip, deflate, zstd', 'Accept': 'application/json', 'Connection': 'keep-alive', 'Authorization': 'Basic YWRtaW46cGFzc3dvcmQxMjM=', 'Content-Type': 'application/json'}
    
    response = requests.get(url, headers=headers)
    
    check.equal(response.status_code, 200, f'Expected status 200, got {response.status_code}')
    check.equal(response.json(), [], 'Response body mismatch')

def test_get_booking_48():
    """Test generated from Schemathesis VCR: pgZaBo
    Test: GET /booking
    Status: SUCCESS
    """
    import requests
    
    url = f"https://restful-booker.herokuapp.com/booking"
    headers = {'User-Agent': 'schemathesis/4.3.15', 'Accept-Encoding': 'gzip, deflate, zstd', 'Accept': 'application/json', 'Connection': 'keep-alive', 'Authorization': 'Basic YWRtaW46cGFzc3dvcmQxMjM=', 'Content-Type': 'application/json'}
    
    response = requests.get(url, headers=headers)
    
    check.equal(response.status_code, 200, f'Expected status 200, got {response.status_code}')
    check.equal(response.json(), [], 'Response body mismatch')

def test_post_booking_49():
    """Test generated from Schemathesis VCR: kP8eCt
    Test: POST /booking
    Status: FAILURE
    """
    import requests
    
    url = f"https://restful-booker.herokuapp.com/booking"
    headers = {'User-Agent': 'schemathesis/4.3.15', 'Accept-Encoding': 'gzip, deflate, zstd', 'Accept': 'application/json', 'Connection': 'keep-alive', 'Authorization': 'Basic YWRtaW46cGFzc3dvcmQxMjM=', 'Content-Type': 'application/json', 'Content-Length': '2'}
    body = []
    
    response = requests.post(url, headers=headers, json=body)
    
    check.equal(response.status_code, 500, f'Expected status 500, got {response.status_code}')
    # Original failed checks: not_a_server_error, status_code_conformance

def test_post_booking_50():
    """Test generated from Schemathesis VCR: IonILT
    Test: POST /booking
    Status: SUCCESS
    """
    import requests
    
    url = f"https://restful-booker.herokuapp.com/booking"
    headers = {'User-Agent': 'schemathesis/4.3.15', 'Accept-Encoding': 'gzip, deflate, zstd', 'Accept': 'application/json', 'Connection': 'keep-alive', 'Authorization': 'Basic YWRtaW46cGFzc3dvcmQxMjM=', 'Content-Type': 'application/json', 'Content-Length': '2'}
    body = []
    
    response = requests.post(url, headers=headers, json=body)
    
    check.equal(response.status_code, 500, f'Expected status 500, got {response.status_code}')
    check.is_not_none(response.text, 'Response should have body')

def test_post_booking_51():
    """Test generated from Schemathesis VCR: 8tibY4
    Test: POST /booking
    Status: SUCCESS
    """
    import requests
    
    url = f"https://restful-booker.herokuapp.com/booking"
    headers = {'User-Agent': 'schemathesis/4.3.15', 'Accept-Encoding': 'gzip, deflate, zstd', 'Accept': 'application/json', 'Connection': 'keep-alive', 'Authorization': 'Basic YWRtaW46cGFzc3dvcmQxMjM=', 'Content-Type': 'application/json', 'Content-Length': '2'}
    body = []
    
    response = requests.post(url, headers=headers, json=body)
    
    check.equal(response.status_code, 500, f'Expected status 500, got {response.status_code}')
    check.is_not_none(response.text, 'Response should have body')

def test_post_booking_52():
    """Test generated from Schemathesis VCR: n4J6xW
    Test: POST /booking
    Status: SUCCESS
    """
    import requests
    
    url = f"https://restful-booker.herokuapp.com/booking"
    headers = {'User-Agent': 'schemathesis/4.3.15', 'Accept-Encoding': 'gzip, deflate, zstd', 'Accept': 'application/json', 'Connection': 'keep-alive', 'Authorization': 'Basic YWRtaW46cGFzc3dvcmQxMjM=', 'Content-Type': 'application/json', 'Content-Length': '51'}
    body = {'AÆ%i½\U000a00e0': {}, 'lastname': ''}
    
    response = requests.post(url, headers=headers, json=body)
    
    check.equal(response.status_code, 500, f'Expected status 500, got {response.status_code}')
    check.is_not_none(response.text, 'Response should have body')

def test_post_booking_53():
    """Test generated from Schemathesis VCR: e1VUoP
    Test: POST /booking
    Status: SUCCESS
    """
    import requests
    
    url = f"https://restful-booker.herokuapp.com/booking"
    headers = {'User-Agent': 'schemathesis/4.3.15', 'Accept-Encoding': 'gzip, deflate, zstd', 'Accept': 'application/json', 'Connection': 'keep-alive', 'Authorization': 'Basic YWRtaW46cGFzc3dvcmQxMjM=', 'Content-Type': 'application/json', 'Content-Length': '3870'}
    body = {'bookingdates': {'checkin': '6301-06-04', 'checkout': '3981-04-22', '\x1aÐàÝÁ\x84\\óoÊÕ\x12ì': [['', -1.7976931348623157e+308, -3168371905290728126]], '\U00069df7^¢\x10S\rµV\U0007817c7|': {'é': 6.554276809079677e+16, '\x96u\r×,': {'®Lwâ²¾': [2.006353591988432e+16], '\U0006a2c0𬾸Æ\U0005869a\U000d72a0öØ𬄫\x9dS.ÿÓÌB': 5656179528009760597, '\U0009a4f73\U00075e4beä\U0003e548\U000bf4c8': None}}, '\x9c<P': {'': None, '\U00040256\x94\U000dabc5': 27411}, '\U000f8cb3\U00089df9\x96n¤\u09ca\x81\U000ecc79': [3.300974394057742e+16, [False], [{'': 0.5, 'j"§ab': '¼½'}, 'E', [None]]], '\\\U00061040': [{'Õ»\x82\U000ba4ed\U000957ad´\x81#=ÙØ¦ì\U0005fcef1D\U000627dc|.': {'\x0b': 3.659308058839686e+183, '': {}}, '\U00061a19î,£G\x16': {'\U000d4926B\x13Gëiíµ\U0007f32eåÃm\t\U000d98ebØ÷³': {'\U0004e35d¼ÜY\U0009583cH': False, '': 3182837394982515.0, '\U00097c3dÓ': None}}, '>\x04\U0009b72b': {'\x8fp': {'#âù6': [{'\x88Þ': 300, '\x89¹X': '\xad_Í𗑢\U000e118c\x91\\\U000fa7c9¾p\U0001fd93\x1c\U0003764a«\x7f8n\x91¸ß\U00035500&', '\\': 14}]}, '\x04ÄéÐ': [52]}}, {'/\U000f1aea\U0007ea922P\U0010b66b:': '\U000621eb¥𦌎´𓉻', 'Ln\U00056841\U0004dd7c\U000507ae': None}], '': [{'\U00049835': []}, {'\x89·\U000ca327mD\x87\U0010d381\U0007e613s\U00064b65': {'\x97ø$\\]ï©]6¤o\x04ëEé\x0cK\U0009d7fb.]\x0cbë2\x13\x14': {}, '2\U000e3ef4\U00036eca¨\U0010e731è𗿇': [], '': ['Authorization', -2367]}, '\U000a05ce!W&': -26756, '': [1.1605593189307912e-304, None]}, {'í': None, '{_𣫬ÿ\x98\x95\U000c8084': False}], '\U00035761é_\U000f6683\x81¾\x19äùc': 1.1253930959590746e-215, '\x1d': {'Òï¶B\U00015f79\x9b\x85×ü\x05Gº': {'\U000c7ce1\x03\U000f2998_Ï': ['u', False, -69], '': {'ÅñïÕ\U00056410ã\x11': 'u', '\U000aa94d\x03': 2.204410358482761e-117, '\x8eY': ''}, '\U000a981eK\x19': []}, '\U000da588ÎJ\x9e-': {'': True, 'F': False, '𫜍\U00067131': ':\U000e6b45Øk\x9b\U000689b7o[¼'}}, 'application/json': {'䣶°ig\x86>\x15\x8eñ\x80Á': ['\U000a170b', '\U0007cea2\x1c', None], '': [92082522997739682058855268377744861378, [], [None, -4.5371653584839e+16, '\x84𤙓\U0005e6a7H×cLß']], '\U000e57b4W': {'': None, '\x0f\U00093e08ß¢õ\U0009bd87U': [{'\U00061fe7éü\x9d\x88ùÏì': None, 'hk\x1dud\U000b93d1\x0fØ\U00070583': 'Ì\U000e4a8b\U000c8130ñ', 'h': True}], 'ഠ;𗘲ä': {'': {}, '\x9cC!¥Ñ': {}, '\x81\U000ed90az': {}}}}, '\U00084078s\x91\x8bAl\x82GN3': {"#?ðº'\x9f\x91\x0c\x84 \x01>\U000edecc": {'\x84)\U000a24efe\x7f𩚫£': True, '¶7\U0005cb42': False}, 'N?\U0007ba06\x8e\U0010265bÏ^\U0007b560\x19i_\n\x81D': [], 'z8}\U00092651\U00103dc9\U0003b810': 300}}, 'depositpaid': True, 'firstname': '>B\U0009e94a \x01C¬\x7f§¾\x8d¥É\U000e5145\x92\U000e3673S\x81.C\x80÷&', 'lastname': 'xÊ', 'totalprice': -7081, '\x8d\U0009ab5a(Òs\xadª\U000f480f\U0007c909楥\x14': [], '\x06f \U00052729\xad\U0006d092û¯鹯\x03\U000addbd\x9e': []}
    
    response = requests.post(url, headers=headers, json=body)
    
    check.equal(response.status_code, 500, f'Expected status 500, got {response.status_code}')
    check.is_not_none(response.text, 'Response should have body')

def test_post_booking_54():
    """Test generated from Schemathesis VCR: XyJTi5
    Test: POST /booking
    Status: SUCCESS
    """
    import requests
    
    url = f"https://restful-booker.herokuapp.com/booking"
    headers = {'User-Agent': 'schemathesis/4.3.15', 'Accept-Encoding': 'gzip, deflate, zstd', 'Accept': 'application/json', 'Connection': 'keep-alive', 'Authorization': 'Basic YWRtaW46cGFzc3dvcmQxMjM=', 'Content-Type': 'application/json', 'Content-Length': '510'}
    body = {'bookingdates': {'checkin': '0815-02-24', 'checkout': '7875-10-09', '¿ª¢\x93\x12JUV𜺍L£pÙ': {'': True}, 'ÿ\U000901d5×D)®\x18': {'': [-230958785956092432, None, -1.3137325888406103e+127], '\x95^¸\x01H³Ìº': {}, '\x9cözÈ\U000d9ede\U0008a77d%Ø\x15|\U000684bdV\U00070726\x83\U00085ce5ῂ': '\x9c`Õ\x92JG'}}, 'depositpaid': True, 'firstname': 'KÛ', 'lastname': '', 'totalprice': -4563}
    
    response = requests.post(url, headers=headers, json=body)
    
    check.equal(response.status_code, 200, f'Expected status 200, got {response.status_code}')
    check.equal(response.json(), {'bookingid': 1490, 'booking': {'firstname': 'KÛ', 'lastname': '', 'totalprice': -4563, 'depositpaid': True, 'bookingdates': {'checkin': '0815-02-24', 'checkout': '7875-10-09'}}}, 'Response body mismatch')

def test_get_booking_false_55():
    """Test generated from Schemathesis VCR: rxrA39
    Test: GET /booking/false
    Status: SUCCESS
    """
    import requests
    
    url = f"https://restful-booker.herokuapp.com/booking/false"
    headers = {'User-Agent': 'schemathesis/4.3.15', 'Accept-Encoding': 'gzip, deflate, zstd', 'Accept': 'application/json', 'Connection': 'keep-alive', 'Authorization': 'Basic YWRtaW46cGFzc3dvcmQxMjM=', 'Content-Type': 'application/json'}
    
    response = requests.get(url, headers=headers)
    
    check.equal(response.status_code, 404, f'Expected status 404, got {response.status_code}')
    check.is_not_none(response.text, 'Response should have body')

def test_patch_booking_null_56():
    """Test generated from Schemathesis VCR: T5FX4P
    Test: PATCH /booking/null
    Status: FAILURE
    """
    import requests
    
    url = f"https://restful-booker.herokuapp.com/booking/null"
    headers = {'User-Agent': 'schemathesis/4.3.15', 'Accept-Encoding': 'gzip, deflate, zstd', 'Accept': 'application/json', 'Connection': 'keep-alive', 'Authorization': 'Basic YWRtaW46cGFzc3dvcmQxMjM=', 'Content-Type': 'application/json', 'Content-Length': '82'}
    body = {'firstname': 'KÛ', 'lastname': '', 'totalprice': -4563, 'depositpaid': True}
    
    response = requests.patch(url, headers=headers, json=body)
    
    check.equal(response.status_code, 405, f'Expected status 405, got {response.status_code}')
    # Original failed checks: status_code_conformance, negative_data_rejection

def test_post_booking_57():
    """Test generated from Schemathesis VCR: MJNlwU
    Test: POST /booking
    Status: SUCCESS
    """
    import requests
    
    url = f"https://restful-booker.herokuapp.com/booking"
    headers = {'User-Agent': 'schemathesis/4.3.15', 'Accept-Encoding': 'gzip, deflate, zstd', 'Accept': 'application/json', 'Connection': 'keep-alive', 'Authorization': 'Basic YWRtaW46cGFzc3dvcmQxMjM=', 'Content-Type': 'application/json', 'Content-Length': '51'}
    body = {'AÆ%i½\U000a00e0': {}, 'lastname': ''}
    
    response = requests.post(url, headers=headers, json=body)
    
    check.equal(response.status_code, 500, f'Expected status 500, got {response.status_code}')
    check.is_not_none(response.text, 'Response should have body')

def test_post_booking_58():
    """Test generated from Schemathesis VCR: jKZ4XJ
    Test: POST /booking
    Status: SUCCESS
    """
    import requests
    
    url = f"https://restful-booker.herokuapp.com/booking"
    headers = {'User-Agent': 'schemathesis/4.3.15', 'Accept-Encoding': 'gzip, deflate, zstd', 'Accept': 'application/json', 'Connection': 'keep-alive', 'Authorization': 'Basic YWRtaW46cGFzc3dvcmQxMjM=', 'Content-Type': 'application/json', 'Content-Length': '3870'}
    body = {'bookingdates': {'checkin': '6301-06-04', 'checkout': '3981-04-22', '\x1aÐàÝÁ\x84\\óoÊÕ\x12ì': [['', -1.7976931348623157e+308, -3168371905290728126]], '\U00069df7^¢\x10S\rµV\U0007817c7|': {'é': 6.554276809079677e+16, '\x96u\r×,': {'®Lwâ²¾': [2.006353591988432e+16], '\U0006a2c0𬾸Æ\U0005869a\U000d72a0öØ𬄫\x9dS.ÿÓÌB': 5656179528009760597, '\U0009a4f73\U00075e4beä\U0003e548\U000bf4c8': None}}, '\x9c<P': {'': None, '\U00040256\x94\U000dabc5': 27411}, '\U000f8cb3\U00089df9\x96n¤\u09ca\x81\U000ecc79': [3.300974394057742e+16, [False], [{'': 0.5, 'j"§ab': '¼½'}, 'E', [None]]], '\\\U00061040': [{'Õ»\x82\U000ba4ed\U000957ad´\x81#=ÙØ¦ì\U0005fcef1D\U000627dc|.': {'\x0b': 3.659308058839686e+183, '': {}}, '\U00061a19î,£G\x16': {'\U000d4926B\x13Gëiíµ\U0007f32eåÃm\t\U000d98ebØ÷³': {'\U0004e35d¼ÜY\U0009583cH': False, '': 3182837394982515.0, '\U00097c3dÓ': None}}, '>\x04\U0009b72b': {'\x8fp': {'#âù6': [{'\x88Þ': 300, '\x89¹X': '\xad_Í𗑢\U000e118c\x91\\\U000fa7c9¾p\U0001fd93\x1c\U0003764a«\x7f8n\x91¸ß\U00035500&', '\\': 14}]}, '\x04ÄéÐ': [52]}}, {'/\U000f1aea\U0007ea922P\U0010b66b:': '\U000621eb¥𦌎´𓉻', 'Ln\U00056841\U0004dd7c\U000507ae': None}], '': [{'\U00049835': []}, {'\x89·\U000ca327mD\x87\U0010d381\U0007e613s\U00064b65': {'\x97ø$\\]ï©]6¤o\x04ëEé\x0cK\U0009d7fb.]\x0cbë2\x13\x14': {}, '2\U000e3ef4\U00036eca¨\U0010e731è𗿇': [], '': ['Authorization', -2367]}, '\U000a05ce!W&': -26756, '': [1.1605593189307912e-304, None]}, {'í': None, '{_𣫬ÿ\x98\x95\U000c8084': False}], '\U00035761é_\U000f6683\x81¾\x19äùc': 1.1253930959590746e-215, '\x1d': {'Òï¶B\U00015f79\x9b\x85×ü\x05Gº': {'\U000c7ce1\x03\U000f2998_Ï': ['u', False, -69], '': {'ÅñïÕ\U00056410ã\x11': 'u', '\U000aa94d\x03': 2.204410358482761e-117, '\x8eY': ''}, '\U000a981eK\x19': []}, '\U000da588ÎJ\x9e-': {'': True, 'F': False, '𫜍\U00067131': ':\U000e6b45Øk\x9b\U000689b7o[¼'}}, 'application/json': {'䣶°ig\x86>\x15\x8eñ\x80Á': ['\U000a170b', '\U0007cea2\x1c', None], '': [92082522997739682058855268377744861378, [], [None, -4.5371653584839e+16, '\x84𤙓\U0005e6a7H×cLß']], '\U000e57b4W': {'': None, '\x0f\U00093e08ß¢õ\U0009bd87U': [{'\U00061fe7éü\x9d\x88ùÏì': None, 'hk\x1dud\U000b93d1\x0fØ\U00070583': 'Ì\U000e4a8b\U000c8130ñ', 'h': True}], 'ഠ;𗘲ä': {'': {}, '\x9cC!¥Ñ': {}, '\x81\U000ed90az': {}}}}, '\U00084078s\x91\x8bAl\x82GN3': {"#?ðº'\x9f\x91\x0c\x84 \x01>\U000edecc": {'\x84)\U000a24efe\x7f𩚫£': True, '¶7\U0005cb42': False}, 'N?\U0007ba06\x8e\U0010265bÏ^\U0007b560\x19i_\n\x81D': [], 'z8}\U00092651\U00103dc9\U0003b810': 300}}, 'depositpaid': True, 'firstname': '>B\U0009e94a \x01C¬\x7f§¾\x8d¥É\U000e5145\x92\U000e3673S\x81.C\x80÷&', 'lastname': 'xÊ', 'totalprice': -7081, '\x8d\U0009ab5a(Òs\xadª\U000f480f\U0007c909楥\x14': [], '\x06f \U00052729\xad\U0006d092û¯鹯\x03\U000addbd\x9e': []}
    
    response = requests.post(url, headers=headers, json=body)
    
    check.equal(response.status_code, 500, f'Expected status 500, got {response.status_code}')
    check.is_not_none(response.text, 'Response should have body')

def test_post_booking_59():
    """Test generated from Schemathesis VCR: J9UKr8
    Test: POST /booking
    Status: SUCCESS
    """
    import requests
    
    url = f"https://restful-booker.herokuapp.com/booking"
    headers = {'User-Agent': 'schemathesis/4.3.15', 'Accept-Encoding': 'gzip, deflate, zstd', 'Accept': 'application/json', 'Connection': 'keep-alive', 'Authorization': 'Basic YWRtaW46cGFzc3dvcmQxMjM=', 'Content-Type': 'application/json', 'Content-Length': '510'}
    body = {'bookingdates': {'checkin': '0815-02-24', 'checkout': '7875-10-09', '¿ª¢\x93\x12JUV𜺍L£pÙ': {'': True}, 'ÿ\U000901d5×D)®\x18': {'': [-230958785956092432, None, -1.3137325888406103e+127], '\x95^¸\x01H³Ìº': {}, '\x9cözÈ\U000d9ede\U0008a77d%Ø\x15|\U000684bdV\U00070726\x83\U00085ce5ῂ': '\x9c`Õ\x92JG'}}, 'depositpaid': True, 'firstname': 'KÛ', 'lastname': '', 'totalprice': -4563}
    
    response = requests.post(url, headers=headers, json=body)
    
    check.equal(response.status_code, 200, f'Expected status 200, got {response.status_code}')
    check.equal(response.json(), {'bookingid': 1499, 'booking': {'firstname': 'KÛ', 'lastname': '', 'totalprice': -4563, 'depositpaid': True, 'bookingdates': {'checkin': '0815-02-24', 'checkout': '7875-10-09'}}}, 'Response body mismatch')

def test_get_booking_false_60():
    """Test generated from Schemathesis VCR: me1cSh
    Test: GET /booking/false
    Status: SUCCESS
    """
    import requests
    
    url = f"https://restful-booker.herokuapp.com/booking/false"
    headers = {'User-Agent': 'schemathesis/4.3.15', 'Accept-Encoding': 'gzip, deflate, zstd', 'Accept': 'application/json', 'Connection': 'keep-alive', 'Authorization': 'Basic YWRtaW46cGFzc3dvcmQxMjM=', 'Content-Type': 'application/json'}
    
    response = requests.get(url, headers=headers)
    
    check.equal(response.status_code, 404, f'Expected status 404, got {response.status_code}')
    check.is_not_none(response.text, 'Response should have body')

def test_patch_booking_null_61():
    """Test generated from Schemathesis VCR: n4u2lA
    Test: PATCH /booking/null
    Status: SUCCESS
    """
    import requests
    
    url = f"https://restful-booker.herokuapp.com/booking/null"
    headers = {'User-Agent': 'schemathesis/4.3.15', 'Accept-Encoding': 'gzip, deflate, zstd', 'Accept': 'application/json', 'Connection': 'keep-alive', 'Authorization': 'Basic YWRtaW46cGFzc3dvcmQxMjM=', 'Content-Type': 'application/json', 'Content-Length': '82'}
    body = {'firstname': 'KÛ', 'lastname': '', 'totalprice': -4563, 'depositpaid': True}
    
    response = requests.patch(url, headers=headers, json=body)
    
    check.equal(response.status_code, 405, f'Expected status 405, got {response.status_code}')
    check.is_not_none(response.text, 'Response should have body')

def test_patch_booking_17781_62():
    """Test generated from Schemathesis VCR: f3smAj
    Test: PATCH /booking/17781
    Status: FAILURE
    """
    import requests
    
    url = f"https://restful-booker.herokuapp.com/booking/17781"
    headers = {'User-Agent': 'schemathesis/4.3.15', 'Accept-Encoding': 'gzip, deflate, zstd', 'Accept': 'application/json', 'Connection': 'keep-alive', 'Authorization': 'Basic YWRtaW46cGFzc3dvcmQxMjM=', 'Content-Type': 'application/json', 'Content-Length': '950'}
    body = {'bookingdates': {'checkin': '0815-02-24', 'checkout': '7875-10-09'}, 'depositpaid': False, 'firstname': 'KÛ', 'lastname': 'ñ\U000ef8f4\x0b\x8d', 'totalprice': -4563, 'Ì': {'}\x90²\U000d637dnÍ\x1d': [{'g\x15C±ÖIÛ\U000c5077%\U000db224Ä÷': {'𠾤p\U000bb514¾«®\x1f~û\U0006acca{_\U000e85c3È\x8aC\x81i': -4.530904450480263e+16, 'ØÂ\x89\U00066e81`\x15\U000b6245𣭘ÇáÅ\U000b3b2d?\U000e4d12\x858O\x1b\x9fyþy»\x9c\x85': 27, '\U000bc76b¾\U0003f8d0¥\U0006517e\U0010abf3': 3.4063481253963904e+16}, 'Þ': False, ')\x94Ò*\x81\U00068687ßy': -12}, {'Â2': {}, '_øo\x15uû\x07pL¥\x11\U0007f99e\U000479c7\U00081656': [-8.011741984698816e+178, '\x95\x90Ó,(\U000aafec\U0005ecc8n', -3.548245699223927e-254]}]}}
    
    response = requests.patch(url, headers=headers, json=body)
    
    check.equal(response.status_code, 405, f'Expected status 405, got {response.status_code}')
    # Original failed checks: positive_data_acceptance

def test_post_booking_63():
    """Test generated from Schemathesis VCR: xGJw49
    Test: POST /booking
    Status: SUCCESS
    """
    import requests
    
    url = f"https://restful-booker.herokuapp.com/booking"
    headers = {'User-Agent': 'schemathesis/4.3.15', 'Accept-Encoding': 'gzip, deflate, zstd', 'Accept': 'application/json', 'Connection': 'keep-alive', 'Authorization': 'Basic YWRtaW46cGFzc3dvcmQxMjM=', 'Content-Type': 'application/json', 'Content-Length': '51'}
    body = {'AÆ%i½\U000a00e0': {}, 'lastname': ''}
    
    response = requests.post(url, headers=headers, json=body)
    
    check.equal(response.status_code, 500, f'Expected status 500, got {response.status_code}')
    check.is_not_none(response.text, 'Response should have body')

def test_post_booking_64():
    """Test generated from Schemathesis VCR: lmMJVi
    Test: POST /booking
    Status: SUCCESS
    """
    import requests
    
    url = f"https://restful-booker.herokuapp.com/booking"
    headers = {'User-Agent': 'schemathesis/4.3.15', 'Accept-Encoding': 'gzip, deflate, zstd', 'Accept': 'application/json', 'Connection': 'keep-alive', 'Authorization': 'Basic YWRtaW46cGFzc3dvcmQxMjM=', 'Content-Type': 'application/json', 'Content-Length': '3870'}
    body = {'bookingdates': {'checkin': '6301-06-04', 'checkout': '3981-04-22', '\x1aÐàÝÁ\x84\\óoÊÕ\x12ì': [['', -1.7976931348623157e+308, -3168371905290728126]], '\U00069df7^¢\x10S\rµV\U0007817c7|': {'é': 6.554276809079677e+16, '\x96u\r×,': {'®Lwâ²¾': [2.006353591988432e+16], '\U0006a2c0𬾸Æ\U0005869a\U000d72a0öØ𬄫\x9dS.ÿÓÌB': 5656179528009760597, '\U0009a4f73\U00075e4beä\U0003e548\U000bf4c8': None}}, '\x9c<P': {'': None, '\U00040256\x94\U000dabc5': 27411}, '\U000f8cb3\U00089df9\x96n¤\u09ca\x81\U000ecc79': [3.300974394057742e+16, [False], [{'': 0.5, 'j"§ab': '¼½'}, 'E', [None]]], '\\\U00061040': [{'Õ»\x82\U000ba4ed\U000957ad´\x81#=ÙØ¦ì\U0005fcef1D\U000627dc|.': {'\x0b': 3.659308058839686e+183, '': {}}, '\U00061a19î,£G\x16': {'\U000d4926B\x13Gëiíµ\U0007f32eåÃm\t\U000d98ebØ÷³': {'\U0004e35d¼ÜY\U0009583cH': False, '': 3182837394982515.0, '\U00097c3dÓ': None}}, '>\x04\U0009b72b': {'\x8fp': {'#âù6': [{'\x88Þ': 300, '\x89¹X': '\xad_Í𗑢\U000e118c\x91\\\U000fa7c9¾p\U0001fd93\x1c\U0003764a«\x7f8n\x91¸ß\U00035500&', '\\': 14}]}, '\x04ÄéÐ': [52]}}, {'/\U000f1aea\U0007ea922P\U0010b66b:': '\U000621eb¥𦌎´𓉻', 'Ln\U00056841\U0004dd7c\U000507ae': None}], '': [{'\U00049835': []}, {'\x89·\U000ca327mD\x87\U0010d381\U0007e613s\U00064b65': {'\x97ø$\\]ï©]6¤o\x04ëEé\x0cK\U0009d7fb.]\x0cbë2\x13\x14': {}, '2\U000e3ef4\U00036eca¨\U0010e731è𗿇': [], '': ['Authorization', -2367]}, '\U000a05ce!W&': -26756, '': [1.1605593189307912e-304, None]}, {'í': None, '{_𣫬ÿ\x98\x95\U000c8084': False}], '\U00035761é_\U000f6683\x81¾\x19äùc': 1.1253930959590746e-215, '\x1d': {'Òï¶B\U00015f79\x9b\x85×ü\x05Gº': {'\U000c7ce1\x03\U000f2998_Ï': ['u', False, -69], '': {'ÅñïÕ\U00056410ã\x11': 'u', '\U000aa94d\x03': 2.204410358482761e-117, '\x8eY': ''}, '\U000a981eK\x19': []}, '\U000da588ÎJ\x9e-': {'': True, 'F': False, '𫜍\U00067131': ':\U000e6b45Øk\x9b\U000689b7o[¼'}}, 'application/json': {'䣶°ig\x86>\x15\x8eñ\x80Á': ['\U000a170b', '\U0007cea2\x1c', None], '': [92082522997739682058855268377744861378, [], [None, -4.5371653584839e+16, '\x84𤙓\U0005e6a7H×cLß']], '\U000e57b4W': {'': None, '\x0f\U00093e08ß¢õ\U0009bd87U': [{'\U00061fe7éü\x9d\x88ùÏì': None, 'hk\x1dud\U000b93d1\x0fØ\U00070583': 'Ì\U000e4a8b\U000c8130ñ', 'h': True}], 'ഠ;𗘲ä': {'': {}, '\x9cC!¥Ñ': {}, '\x81\U000ed90az': {}}}}, '\U00084078s\x91\x8bAl\x82GN3': {"#?ðº'\x9f\x91\x0c\x84 \x01>\U000edecc": {'\x84)\U000a24efe\x7f𩚫£': True, '¶7\U0005cb42': False}, 'N?\U0007ba06\x8e\U0010265bÏ^\U0007b560\x19i_\n\x81D': [], 'z8}\U00092651\U00103dc9\U0003b810': 300}}, 'depositpaid': True, 'firstname': '>B\U0009e94a \x01C¬\x7f§¾\x8d¥É\U000e5145\x92\U000e3673S\x81.C\x80÷&', 'lastname': 'xÊ', 'totalprice': -7081, '\x8d\U0009ab5a(Òs\xadª\U000f480f\U0007c909楥\x14': [], '\x06f \U00052729\xad\U0006d092û¯鹯\x03\U000addbd\x9e': []}
    
    response = requests.post(url, headers=headers, json=body)
    
    check.equal(response.status_code, 500, f'Expected status 500, got {response.status_code}')
    check.is_not_none(response.text, 'Response should have body')

def test_post_booking_65():
    """Test generated from Schemathesis VCR: D5rRtE
    Test: POST /booking
    Status: SUCCESS
    """
    import requests
    
    url = f"https://restful-booker.herokuapp.com/booking"
    headers = {'User-Agent': 'schemathesis/4.3.15', 'Accept-Encoding': 'gzip, deflate, zstd', 'Accept': 'application/json', 'Connection': 'keep-alive', 'Authorization': 'Basic YWRtaW46cGFzc3dvcmQxMjM=', 'Content-Type': 'application/json', 'Content-Length': '510'}
    body = {'bookingdates': {'checkin': '0815-02-24', 'checkout': '7875-10-09', '¿ª¢\x93\x12JUV𜺍L£pÙ': {'': True}, 'ÿ\U000901d5×D)®\x18': {'': [-230958785956092432, None, -1.3137325888406103e+127], '\x95^¸\x01H³Ìº': {}, '\x9cözÈ\U000d9ede\U0008a77d%Ø\x15|\U000684bdV\U00070726\x83\U00085ce5ῂ': '\x9c`Õ\x92JG'}}, 'depositpaid': True, 'firstname': 'KÛ', 'lastname': '', 'totalprice': -4563}
    
    response = requests.post(url, headers=headers, json=body)
    
    check.equal(response.status_code, 200, f'Expected status 200, got {response.status_code}')
    check.equal(response.json(), {'bookingid': 1511, 'booking': {'firstname': 'KÛ', 'lastname': '', 'totalprice': -4563, 'depositpaid': True, 'bookingdates': {'checkin': '0815-02-24', 'checkout': '7875-10-09'}}}, 'Response body mismatch')

def test_get_booking_false_66():
    """Test generated from Schemathesis VCR: 3GAyCz
    Test: GET /booking/false
    Status: SUCCESS
    """
    import requests
    
    url = f"https://restful-booker.herokuapp.com/booking/false"
    headers = {'User-Agent': 'schemathesis/4.3.15', 'Accept-Encoding': 'gzip, deflate, zstd', 'Accept': 'application/json', 'Connection': 'keep-alive', 'Authorization': 'Basic YWRtaW46cGFzc3dvcmQxMjM=', 'Content-Type': 'application/json'}
    
    response = requests.get(url, headers=headers)
    
    check.equal(response.status_code, 404, f'Expected status 404, got {response.status_code}')
    check.is_not_none(response.text, 'Response should have body')

def test_patch_booking_null_67():
    """Test generated from Schemathesis VCR: 3lMXFk
    Test: PATCH /booking/null
    Status: SUCCESS
    """
    import requests
    
    url = f"https://restful-booker.herokuapp.com/booking/null"
    headers = {'User-Agent': 'schemathesis/4.3.15', 'Accept-Encoding': 'gzip, deflate, zstd', 'Accept': 'application/json', 'Connection': 'keep-alive', 'Authorization': 'Basic YWRtaW46cGFzc3dvcmQxMjM=', 'Content-Type': 'application/json', 'Content-Length': '82'}
    body = {'firstname': 'KÛ', 'lastname': '', 'totalprice': -4563, 'depositpaid': True}
    
    response = requests.patch(url, headers=headers, json=body)
    
    check.equal(response.status_code, 405, f'Expected status 405, got {response.status_code}')
    check.is_not_none(response.text, 'Response should have body')

def test_patch_booking_false_68():
    """Test generated from Schemathesis VCR: oClw6G
    Test: PATCH /booking/false
    Status: SUCCESS
    """
    import requests
    
    url = f"https://restful-booker.herokuapp.com/booking/false"
    headers = {'User-Agent': 'schemathesis/4.3.15', 'Accept-Encoding': 'gzip, deflate, zstd', 'Accept': 'application/json', 'Connection': 'keep-alive', 'Authorization': 'Basic YWRtaW46cGFzc3dvcmQxMjM=', 'Content-Type': 'application/json', 'Content-Length': '301'}
    body = {'bookingdates': {'checkin': '0815-02-24', 'checkout': '7875-10-09'}, 'firstname': 'KÛ', 'lastname': '', 'totalprice': -4563, '\U00068023Dmö\xad': {}, '\x08°': {'\\Ûì-xy9Õ\U000ebd89\x91': []}, 'åT': [{}, [15717, [], [None, None, '']], {}], 'depositpaid': True}
    
    response = requests.patch(url, headers=headers, json=body)
    
    check.equal(response.status_code, 405, f'Expected status 405, got {response.status_code}')
    check.is_not_none(response.text, 'Response should have body')

def test_post_booking_69():
    """Test generated from Schemathesis VCR: 1Oe5B4
    Test: POST /booking
    Status: SUCCESS
    """
    import requests
    
    url = f"https://restful-booker.herokuapp.com/booking"
    headers = {'User-Agent': 'schemathesis/4.3.15', 'Accept-Encoding': 'gzip, deflate, zstd', 'Accept': 'application/json', 'Connection': 'keep-alive', 'Authorization': 'Basic YWRtaW46cGFzc3dvcmQxMjM=', 'Content-Type': 'application/json', 'Content-Length': '51'}
    body = {'AÆ%i½\U000a00e0': {}, 'lastname': ''}
    
    response = requests.post(url, headers=headers, json=body)
    
    check.equal(response.status_code, 500, f'Expected status 500, got {response.status_code}')
    check.is_not_none(response.text, 'Response should have body')

def test_post_booking_70():
    """Test generated from Schemathesis VCR: Lv1tJO
    Test: POST /booking
    Status: SUCCESS
    """
    import requests
    
    url = f"https://restful-booker.herokuapp.com/booking"
    headers = {'User-Agent': 'schemathesis/4.3.15', 'Accept-Encoding': 'gzip, deflate, zstd', 'Accept': 'application/json', 'Connection': 'keep-alive', 'Authorization': 'Basic YWRtaW46cGFzc3dvcmQxMjM=', 'Content-Type': 'application/json', 'Content-Length': '3870'}
    body = {'bookingdates': {'checkin': '6301-06-04', 'checkout': '3981-04-22', '\x1aÐàÝÁ\x84\\óoÊÕ\x12ì': [['', -1.7976931348623157e+308, -3168371905290728126]], '\U00069df7^¢\x10S\rµV\U0007817c7|': {'é': 6.554276809079677e+16, '\x96u\r×,': {'®Lwâ²¾': [2.006353591988432e+16], '\U0006a2c0𬾸Æ\U0005869a\U000d72a0öØ𬄫\x9dS.ÿÓÌB': 5656179528009760597, '\U0009a4f73\U00075e4beä\U0003e548\U000bf4c8': None}}, '\x9c<P': {'': None, '\U00040256\x94\U000dabc5': 27411}, '\U000f8cb3\U00089df9\x96n¤\u09ca\x81\U000ecc79': [3.300974394057742e+16, [False], [{'': 0.5, 'j"§ab': '¼½'}, 'E', [None]]], '\\\U00061040': [{'Õ»\x82\U000ba4ed\U000957ad´\x81#=ÙØ¦ì\U0005fcef1D\U000627dc|.': {'\x0b': 3.659308058839686e+183, '': {}}, '\U00061a19î,£G\x16': {'\U000d4926B\x13Gëiíµ\U0007f32eåÃm\t\U000d98ebØ÷³': {'\U0004e35d¼ÜY\U0009583cH': False, '': 3182837394982515.0, '\U00097c3dÓ': None}}, '>\x04\U0009b72b': {'\x8fp': {'#âù6': [{'\x88Þ': 300, '\x89¹X': '\xad_Í𗑢\U000e118c\x91\\\U000fa7c9¾p\U0001fd93\x1c\U0003764a«\x7f8n\x91¸ß\U00035500&', '\\': 14}]}, '\x04ÄéÐ': [52]}}, {'/\U000f1aea\U0007ea922P\U0010b66b:': '\U000621eb¥𦌎´𓉻', 'Ln\U00056841\U0004dd7c\U000507ae': None}], '': [{'\U00049835': []}, {'\x89·\U000ca327mD\x87\U0010d381\U0007e613s\U00064b65': {'\x97ø$\\]ï©]6¤o\x04ëEé\x0cK\U0009d7fb.]\x0cbë2\x13\x14': {}, '2\U000e3ef4\U00036eca¨\U0010e731è𗿇': [], '': ['Authorization', -2367]}, '\U000a05ce!W&': -26756, '': [1.1605593189307912e-304, None]}, {'í': None, '{_𣫬ÿ\x98\x95\U000c8084': False}], '\U00035761é_\U000f6683\x81¾\x19äùc': 1.1253930959590746e-215, '\x1d': {'Òï¶B\U00015f79\x9b\x85×ü\x05Gº': {'\U000c7ce1\x03\U000f2998_Ï': ['u', False, -69], '': {'ÅñïÕ\U00056410ã\x11': 'u', '\U000aa94d\x03': 2.204410358482761e-117, '\x8eY': ''}, '\U000a981eK\x19': []}, '\U000da588ÎJ\x9e-': {'': True, 'F': False, '𫜍\U00067131': ':\U000e6b45Øk\x9b\U000689b7o[¼'}}, 'application/json': {'䣶°ig\x86>\x15\x8eñ\x80Á': ['\U000a170b', '\U0007cea2\x1c', None], '': [92082522997739682058855268377744861378, [], [None, -4.5371653584839e+16, '\x84𤙓\U0005e6a7H×cLß']], '\U000e57b4W': {'': None, '\x0f\U00093e08ß¢õ\U0009bd87U': [{'\U00061fe7éü\x9d\x88ùÏì': None, 'hk\x1dud\U000b93d1\x0fØ\U00070583': 'Ì\U000e4a8b\U000c8130ñ', 'h': True}], 'ഠ;𗘲ä': {'': {}, '\x9cC!¥Ñ': {}, '\x81\U000ed90az': {}}}}, '\U00084078s\x91\x8bAl\x82GN3': {"#?ðº'\x9f\x91\x0c\x84 \x01>\U000edecc": {'\x84)\U000a24efe\x7f𩚫£': True, '¶7\U0005cb42': False}, 'N?\U0007ba06\x8e\U0010265bÏ^\U0007b560\x19i_\n\x81D': [], 'z8}\U00092651\U00103dc9\U0003b810': 300}}, 'depositpaid': True, 'firstname': '>B\U0009e94a \x01C¬\x7f§¾\x8d¥É\U000e5145\x92\U000e3673S\x81.C\x80÷&', 'lastname': 'xÊ', 'totalprice': -7081, '\x8d\U0009ab5a(Òs\xadª\U000f480f\U0007c909楥\x14': [], '\x06f \U00052729\xad\U0006d092û¯鹯\x03\U000addbd\x9e': []}
    
    response = requests.post(url, headers=headers, json=body)
    
    check.equal(response.status_code, 500, f'Expected status 500, got {response.status_code}')
    check.is_not_none(response.text, 'Response should have body')

def test_post_booking_71():
    """Test generated from Schemathesis VCR: qYKLhV
    Test: POST /booking
    Status: SUCCESS
    """
    import requests
    
    url = f"https://restful-booker.herokuapp.com/booking"
    headers = {'User-Agent': 'schemathesis/4.3.15', 'Accept-Encoding': 'gzip, deflate, zstd', 'Accept': 'application/json', 'Connection': 'keep-alive', 'Authorization': 'Basic YWRtaW46cGFzc3dvcmQxMjM=', 'Content-Type': 'application/json', 'Content-Length': '510'}
    body = {'bookingdates': {'checkin': '0815-02-24', 'checkout': '7875-10-09', '¿ª¢\x93\x12JUV𜺍L£pÙ': {'': True}, 'ÿ\U000901d5×D)®\x18': {'': [-230958785956092432, None, -1.3137325888406103e+127], '\x95^¸\x01H³Ìº': {}, '\x9cözÈ\U000d9ede\U0008a77d%Ø\x15|\U000684bdV\U00070726\x83\U00085ce5ῂ': '\x9c`Õ\x92JG'}}, 'depositpaid': True, 'firstname': 'KÛ', 'lastname': '', 'totalprice': -4563}
    
    response = requests.post(url, headers=headers, json=body)
    
    check.equal(response.status_code, 200, f'Expected status 200, got {response.status_code}')
    check.equal(response.json(), {'bookingid': 1522, 'booking': {'firstname': 'KÛ', 'lastname': '', 'totalprice': -4563, 'depositpaid': True, 'bookingdates': {'checkin': '0815-02-24', 'checkout': '7875-10-09'}}}, 'Response body mismatch')

def test_get_booking_false_72():
    """Test generated from Schemathesis VCR: OYFOyb
    Test: GET /booking/false
    Status: SUCCESS
    """
    import requests
    
    url = f"https://restful-booker.herokuapp.com/booking/false"
    headers = {'User-Agent': 'schemathesis/4.3.15', 'Accept-Encoding': 'gzip, deflate, zstd', 'Accept': 'application/json', 'Connection': 'keep-alive', 'Authorization': 'Basic YWRtaW46cGFzc3dvcmQxMjM=', 'Content-Type': 'application/json'}
    
    response = requests.get(url, headers=headers)
    
    check.equal(response.status_code, 404, f'Expected status 404, got {response.status_code}')
    check.is_not_none(response.text, 'Response should have body')

def test_patch_booking_null_73():
    """Test generated from Schemathesis VCR: ggwrES
    Test: PATCH /booking/null
    Status: SUCCESS
    """
    import requests
    
    url = f"https://restful-booker.herokuapp.com/booking/null"
    headers = {'User-Agent': 'schemathesis/4.3.15', 'Accept-Encoding': 'gzip, deflate, zstd', 'Accept': 'application/json', 'Connection': 'keep-alive', 'Authorization': 'Basic YWRtaW46cGFzc3dvcmQxMjM=', 'Content-Type': 'application/json', 'Content-Length': '82'}
    body = {'firstname': 'KÛ', 'lastname': '', 'totalprice': -4563, 'depositpaid': True}
    
    response = requests.patch(url, headers=headers, json=body)
    
    check.equal(response.status_code, 405, f'Expected status 405, got {response.status_code}')
    check.is_not_none(response.text, 'Response should have body')

def test_patch_booking_17781_74():
    """Test generated from Schemathesis VCR: rg4CBw
    Test: PATCH /booking/17781
    Status: SUCCESS
    """
    import requests
    
    url = f"https://restful-booker.herokuapp.com/booking/17781"
    headers = {'User-Agent': 'schemathesis/4.3.15', 'Accept-Encoding': 'gzip, deflate, zstd', 'Accept': 'application/json', 'Connection': 'keep-alive', 'Authorization': 'Basic YWRtaW46cGFzc3dvcmQxMjM=', 'Content-Type': 'application/json', 'Content-Length': '950'}
    body = {'bookingdates': {'checkin': '0815-02-24', 'checkout': '7875-10-09'}, 'depositpaid': False, 'firstname': 'KÛ', 'lastname': 'ñ\U000ef8f4\x0b\x8d', 'totalprice': -4563, 'Ì': {'}\x90²\U000d637dnÍ\x1d': [{'g\x15C±ÖIÛ\U000c5077%\U000db224Ä÷': {'𠾤p\U000bb514¾«®\x1f~û\U0006acca{_\U000e85c3È\x8aC\x81i': -4.530904450480263e+16, 'ØÂ\x89\U00066e81`\x15\U000b6245𣭘ÇáÅ\U000b3b2d?\U000e4d12\x858O\x1b\x9fyþy»\x9c\x85': 27, '\U000bc76b¾\U0003f8d0¥\U0006517e\U0010abf3': 3.4063481253963904e+16}, 'Þ': False, ')\x94Ò*\x81\U00068687ßy': -12}, {'Â2': {}, '_øo\x15uû\x07pL¥\x11\U0007f99e\U000479c7\U00081656': [-8.011741984698816e+178, '\x95\x90Ó,(\U000aafec\U0005ecc8n', -3.548245699223927e-254]}]}}
    
    response = requests.patch(url, headers=headers, json=body)
    
    check.equal(response.status_code, 405, f'Expected status 405, got {response.status_code}')
    check.is_not_none(response.text, 'Response should have body')

def test_post_booking_75():
    """Test generated from Schemathesis VCR: D8Sr2a
    Test: POST /booking
    Status: SUCCESS
    """
    import requests
    
    url = f"https://restful-booker.herokuapp.com/booking"
    headers = {'User-Agent': 'schemathesis/4.3.15', 'Accept-Encoding': 'gzip, deflate, zstd', 'Accept': 'application/json', 'Connection': 'keep-alive', 'Authorization': 'Basic YWRtaW46cGFzc3dvcmQxMjM=', 'Content-Type': 'application/json', 'Content-Length': '2'}
    body = []
    
    response = requests.post(url, headers=headers, json=body)
    
    check.equal(response.status_code, 500, f'Expected status 500, got {response.status_code}')
    check.is_not_none(response.text, 'Response should have body')

def test_post_booking_76():
    """Test generated from Schemathesis VCR: 8ulJdz
    Test: POST /booking
    Status: SUCCESS
    """
    import requests
    
    url = f"https://restful-booker.herokuapp.com/booking"
    headers = {'User-Agent': 'schemathesis/4.3.15', 'Accept-Encoding': 'gzip, deflate, zstd', 'Accept': 'application/json', 'Connection': 'keep-alive', 'Authorization': 'Basic YWRtaW46cGFzc3dvcmQxMjM=', 'Content-Type': 'application/json', 'Content-Length': '5'}
    body = False
    
    response = requests.post(url, headers=headers, json=body)
    
    check.equal(response.status_code, 400, f'Expected status 400, got {response.status_code}')
    check.is_not_none(response.text, 'Response should have body')

def test_post_booking_77():
    """Test generated from Schemathesis VCR: ae23Vh
    Test: POST /booking
    Status: SUCCESS
    """
    import requests
    
    url = f"https://restful-booker.herokuapp.com/booking"
    headers = {'User-Agent': 'schemathesis/4.3.15', 'Accept-Encoding': 'gzip, deflate, zstd', 'Accept': 'application/json', 'Connection': 'keep-alive', 'Authorization': 'Basic YWRtaW46cGFzc3dvcmQxMjM=', 'Content-Type': 'application/json', 'Content-Length': '1146'}
    body = {'bookingdates': {'checkin': '3764-11-20', 'checkout': '3171-10-07', '®': {}, 'Ò\U000a0b64': [], 'l': [-150158249498597820038500609135846647730, '\x87ì', None], '\x96sc\U000cbd05': [None, None, True], '¼»': [{'Wæ¶Ì&O;zo9áy\U000d42b1p|¡\x90\U0003f950𠬲q\x05': '', '': -88, '\U000dd0a0\U0001f258\x8bx': True}, 'êõ\x85\x06', {'\U000b772e': None}], '\U000f7027': {'\xadæ': {}, 'ä\x8c': [['', False, 2450497796403002.0]], '\x1bk\U000ddc2d\n\x84¼V\x8b\x91º': {'Á¡': '\x94'}}}, 'depositpaid': True, 'firstname': '\x1e\U000c5041é𡫙B', 'lastname': 'z\U0008ff15f\x8d', 'totalprice': 41, 'additionalneeds': 'NULL', '\tÀ': {'Ðqå\U000c9b8dõµ°K$\U000436db¸G\x8eÎ': {'': '\U000c3d45ñ\x07ÆÒ®9Ꭻ', '\x86¬\t\U000ea869\U00059b25ÒÃ$åN\U000f9a8b§\x10p)êI': '\x99\x16àøz', 'j': False}, 'òv\x1a\x94𐐦F¸1B\U0006cb9c\x99\U000ae5ffl\x0b': []}}
    
    response = requests.post(url, headers=headers, json=body)
    
    check.equal(response.status_code, 200, f'Expected status 200, got {response.status_code}')
    check.equal(response.json(), {'bookingid': 1534, 'booking': {'firstname': '\x1e\U000c5041é𡫙B', 'lastname': 'z\U0008ff15f\x8d', 'totalprice': 41, 'depositpaid': True, 'bookingdates': {'checkin': '3764-11-20', 'checkout': '3171-10-07'}, 'additionalneeds': 'NULL'}}, 'Response body mismatch')

def test_post_booking_78():
    """Test generated from Schemathesis VCR: jHXiQz
    Test: POST /booking
    Status: SUCCESS
    """
    import requests
    
    url = f"https://restful-booker.herokuapp.com/booking"
    headers = {'User-Agent': 'schemathesis/4.3.15', 'Accept-Encoding': 'gzip, deflate, zstd', 'Accept': 'application/json', 'Connection': 'keep-alive', 'Authorization': 'Basic YWRtaW46cGFzc3dvcmQxMjM=', 'Content-Type': 'application/json', 'Content-Length': '381'}
    body = {'bookingdates': {'checkin': '1599-09-10', 'checkout': '6262-05-23'}, 'depositpaid': False, 'firstname': '', 'lastname': 'Ú1H\U000d6d71\x1e\x13B\U000ded37', 'totalprice': 145703021073556611087125583480726753450, '·¿': [[{'Ú': None, '\U000c0630Ä\U00105215%\U000e208cË\\*': 1.9}, 17346, True]], '%\x91\U000aa53d¯\U00040448': []}
    
    response = requests.post(url, headers=headers, json=body)
    
    check.equal(response.status_code, 200, f'Expected status 200, got {response.status_code}')
    check.equal(response.json(), {'bookingid': 1543, 'booking': {'firstname': '', 'lastname': 'Ú1H\U000d6d71\x1e\x13B\U000ded37', 'totalprice': 1, 'depositpaid': False, 'bookingdates': {'checkin': '1599-09-10', 'checkout': '6262-05-23'}}}, 'Response body mismatch')

def test_post_booking_79():
    """Test generated from Schemathesis VCR: jebAQ6
    Test: POST /booking
    Status: SUCCESS
    """
    import requests
    
    url = f"https://restful-booker.herokuapp.com/booking"
    headers = {'User-Agent': 'schemathesis/4.3.15', 'Accept-Encoding': 'gzip, deflate, zstd', 'Accept': 'application/json', 'Connection': 'keep-alive', 'Authorization': 'Basic YWRtaW46cGFzc3dvcmQxMjM=', 'Content-Type': 'application/json', 'Content-Length': '1482'}
    body = {'bookingdates': {'checkin': '2972-10-27', 'checkout': '1002-04-03', '': {}, 'q': {}, '\x96\U000cf584S£Nñ\U00038d96Ê\x0b\x97\x12\U000aa1ea': {'': {}}, '1:Ûd\U000a8484\x0eGD\x9f\U000cfbc9\U000e4f82g³𠇍\x97\U000445e5)\U0007f909»\U0010f542\t¾\U000dbeaf': [{'\x1c': ''}, ['\x98\x1eëV{\x9aÚÍ]'], ['[\x97[M-jk\U000d674d\x04\x90\x07\x9b\x04\x8dUÿ', {'êPÿ"': 16888}, {}]], '\x0b¯': [{'LíÁ;\x9a': [[]]}, {}], '\x98¨\U0003ee13\x99\x900\x9cZ𪢼{ç\x19Q': [{'\U000483f8\x0b²\x16ä\U000553ff': 'óºãp'}], '\U00077b51\x94L': [4126088849982681785, {'\U000ae918yþèz\x7fÔ·Ó': None, '\x08\U0004c5adç\x04\U0001dd75v·C': 16814, 'Q¨¬8\U000f03e7': None}, {'µ\x9cå/\x85': -2.030342245607017e+16, '\U000908e2ïA\U000c1a6d\U000465a3\U00039fc2': -1.697075827363005e+18, 'µ': None}]}, 'depositpaid': True, 'firstname': 'zñ\U0010b41cÜ\U0005e1f1\x0b\nB', 'lastname': '/uè¤\U000eb05d\x1eø', 'totalprice': -7896, '\U0009a08b': [{}, {'êpY\x19\xa0é': [{}], '\U0009a4eai\x81¦𔉳Ël𪲆¿': [True], '': {'j\x15ÿ\x8c\U000c3ce0E=\x1d[\x1c\x9c#Õ\U00079fdf': ['Mx½', True, '']}}, 4.489787449993937e+16]}
    
    response = requests.post(url, headers=headers, json=body)
    
    check.equal(response.status_code, 200, f'Expected status 200, got {response.status_code}')
    check.equal(response.json(), {'bookingid': 1547, 'booking': {'firstname': 'zñ\U0010b41cÜ\U0005e1f1\x0b\nB', 'lastname': '/uè¤\U000eb05d\x1eø', 'totalprice': -7896, 'depositpaid': True, 'bookingdates': {'checkin': '2972-10-27', 'checkout': '1002-04-03'}}}, 'Response body mismatch')

def test_put_booking_true_80():
    """Test generated from Schemathesis VCR: pK2KLo
    Test: PUT /booking/true
    Status: SUCCESS
    """
    import requests
    
    url = f"https://restful-booker.herokuapp.com/booking/true"
    headers = {'User-Agent': 'schemathesis/4.3.15', 'Accept-Encoding': 'gzip, deflate, zstd', 'Accept': 'application/json', 'Connection': 'keep-alive', 'Authorization': 'Basic YWRtaW46cGFzc3dvcmQxMjM=', 'Content-Type': 'application/json', 'Content-Length': '207'}
    body = {'firstname': 'zñ\U0010b41cÜ\U0005e1f1\x0b\nB', 'lastname': '/uè¤\U000eb05d\x1eø', 'totalprice': -7896, 'bookingdates': {'checkin': '2972-10-27', 'checkout': '1002-04-03'}}
    
    response = requests.put(url, headers=headers, json=body)
    
    check.equal(response.status_code, 400, f'Expected status 400, got {response.status_code}')
    check.is_not_none(response.text, 'Response should have body')

def test_delete_booking_null_81():
    """Test generated from Schemathesis VCR: tRU3CW
    Test: DELETE /booking/null
    Status: FAILURE
    """
    import requests
    
    url = f"https://restful-booker.herokuapp.com/booking/null"
    headers = {'User-Agent': 'schemathesis/4.3.15', 'Accept-Encoding': 'gzip, deflate, zstd', 'Accept': 'application/json', 'Connection': 'keep-alive', 'Authorization': 'Basic YWRtaW46cGFzc3dvcmQxMjM=', 'Content-Type': 'application/json', 'Content-Length': '0'}
    
    response = requests.delete(url, headers=headers)
    
    check.equal(response.status_code, 405, f'Expected status 405, got {response.status_code}')
    # Original failed checks: status_code_conformance, negative_data_rejection

def test_post_booking_82():
    """Test generated from Schemathesis VCR: 8IsAUX
    Test: POST /booking
    Status: SUCCESS
    """
    import requests
    
    url = f"https://restful-booker.herokuapp.com/booking"
    headers = {'User-Agent': 'schemathesis/4.3.15', 'Accept-Encoding': 'gzip, deflate, zstd', 'Accept': 'application/json', 'Connection': 'keep-alive', 'Authorization': 'Basic YWRtaW46cGFzc3dvcmQxMjM=', 'Content-Type': 'application/json', 'Content-Length': '381'}
    body = {'bookingdates': {'checkin': '1599-09-10', 'checkout': '6262-05-23'}, 'depositpaid': False, 'firstname': '', 'lastname': 'Ú1H\U000d6d71\x1e\x13B\U000ded37', 'totalprice': 145703021073556611087125583480726753450, '·¿': [[{'Ú': None, '\U000c0630Ä\U00105215%\U000e208cË\\*': 1.9}, 17346, True]], '%\x91\U000aa53d¯\U00040448': []}
    
    response = requests.post(url, headers=headers, json=body)
    
    check.equal(response.status_code, 200, f'Expected status 200, got {response.status_code}')
    check.equal(response.json(), {'bookingid': 1551, 'booking': {'firstname': '', 'lastname': 'Ú1H\U000d6d71\x1e\x13B\U000ded37', 'totalprice': 1, 'depositpaid': False, 'bookingdates': {'checkin': '1599-09-10', 'checkout': '6262-05-23'}}}, 'Response body mismatch')

def test_post_booking_83():
    """Test generated from Schemathesis VCR: UBIysD
    Test: POST /booking
    Status: SUCCESS
    """
    import requests
    
    url = f"https://restful-booker.herokuapp.com/booking"
    headers = {'User-Agent': 'schemathesis/4.3.15', 'Accept-Encoding': 'gzip, deflate, zstd', 'Accept': 'application/json', 'Connection': 'keep-alive', 'Authorization': 'Basic YWRtaW46cGFzc3dvcmQxMjM=', 'Content-Type': 'application/json', 'Content-Length': '1482'}
    body = {'bookingdates': {'checkin': '2972-10-27', 'checkout': '1002-04-03', '': {}, 'q': {}, '\x96\U000cf584S£Nñ\U00038d96Ê\x0b\x97\x12\U000aa1ea': {'': {}}, '1:Ûd\U000a8484\x0eGD\x9f\U000cfbc9\U000e4f82g³𠇍\x97\U000445e5)\U0007f909»\U0010f542\t¾\U000dbeaf': [{'\x1c': ''}, ['\x98\x1eëV{\x9aÚÍ]'], ['[\x97[M-jk\U000d674d\x04\x90\x07\x9b\x04\x8dUÿ', {'êPÿ"': 16888}, {}]], '\x0b¯': [{'LíÁ;\x9a': [[]]}, {}], '\x98¨\U0003ee13\x99\x900\x9cZ𪢼{ç\x19Q': [{'\U000483f8\x0b²\x16ä\U000553ff': 'óºãp'}], '\U00077b51\x94L': [4126088849982681785, {'\U000ae918yþèz\x7fÔ·Ó': None, '\x08\U0004c5adç\x04\U0001dd75v·C': 16814, 'Q¨¬8\U000f03e7': None}, {'µ\x9cå/\x85': -2.030342245607017e+16, '\U000908e2ïA\U000c1a6d\U000465a3\U00039fc2': -1.697075827363005e+18, 'µ': None}]}, 'depositpaid': True, 'firstname': 'zñ\U0010b41cÜ\U0005e1f1\x0b\nB', 'lastname': '/uè¤\U000eb05d\x1eø', 'totalprice': -7896, '\U0009a08b': [{}, {'êpY\x19\xa0é': [{}], '\U0009a4eai\x81¦𔉳Ël𪲆¿': [True], '': {'j\x15ÿ\x8c\U000c3ce0E=\x1d[\x1c\x9c#Õ\U00079fdf': ['Mx½', True, '']}}, 4.489787449993937e+16]}
    
    response = requests.post(url, headers=headers, json=body)
    
    check.equal(response.status_code, 200, f'Expected status 200, got {response.status_code}')
    check.equal(response.json(), {'bookingid': 1553, 'booking': {'firstname': 'zñ\U0010b41cÜ\U0005e1f1\x0b\nB', 'lastname': '/uè¤\U000eb05d\x1eø', 'totalprice': -7896, 'depositpaid': True, 'bookingdates': {'checkin': '2972-10-27', 'checkout': '1002-04-03'}}}, 'Response body mismatch')

def test_put_booking_true_84():
    """Test generated from Schemathesis VCR: 5P06VW
    Test: PUT /booking/true
    Status: SUCCESS
    """
    import requests
    
    url = f"https://restful-booker.herokuapp.com/booking/true"
    headers = {'User-Agent': 'schemathesis/4.3.15', 'Accept-Encoding': 'gzip, deflate, zstd', 'Accept': 'application/json', 'Connection': 'keep-alive', 'Authorization': 'Basic YWRtaW46cGFzc3dvcmQxMjM=', 'Content-Type': 'application/json', 'Content-Length': '207'}
    body = {'firstname': 'zñ\U0010b41cÜ\U0005e1f1\x0b\nB', 'lastname': '/uè¤\U000eb05d\x1eø', 'totalprice': -7896, 'bookingdates': {'checkin': '2972-10-27', 'checkout': '1002-04-03'}}
    
    response = requests.put(url, headers=headers, json=body)
    
    check.equal(response.status_code, 400, f'Expected status 400, got {response.status_code}')
    check.is_not_none(response.text, 'Response should have body')

def test_delete_booking_null_85():
    """Test generated from Schemathesis VCR: kbjRBf
    Test: DELETE /booking/null
    Status: SUCCESS
    """
    import requests
    
    url = f"https://restful-booker.herokuapp.com/booking/null"
    headers = {'User-Agent': 'schemathesis/4.3.15', 'Accept-Encoding': 'gzip, deflate, zstd', 'Accept': 'application/json', 'Connection': 'keep-alive', 'Authorization': 'Basic YWRtaW46cGFzc3dvcmQxMjM=', 'Content-Type': 'application/json', 'Content-Length': '0'}
    
    response = requests.delete(url, headers=headers)
    
    check.equal(response.status_code, 405, f'Expected status 405, got {response.status_code}')
    check.is_not_none(response.text, 'Response should have body')

def test_post_booking_86():
    """Test generated from Schemathesis VCR: iiXidV
    Test: POST /booking
    Status: SUCCESS
    """
    import requests
    
    url = f"https://restful-booker.herokuapp.com/booking"
    headers = {'User-Agent': 'schemathesis/4.3.15', 'Accept-Encoding': 'gzip, deflate, zstd', 'Accept': 'application/json', 'Connection': 'keep-alive', 'Authorization': 'Basic YWRtaW46cGFzc3dvcmQxMjM=', 'Content-Type': 'application/json', 'Content-Length': '2'}
    body = []
    
    response = requests.post(url, headers=headers, json=body)
    
    check.equal(response.status_code, 500, f'Expected status 500, got {response.status_code}')
    check.is_not_none(response.text, 'Response should have body')

def test_post_booking_87():
    """Test generated from Schemathesis VCR: BRsNwa
    Test: POST /booking
    Status: SUCCESS
    """
    import requests
    
    url = f"https://restful-booker.herokuapp.com/booking"
    headers = {'User-Agent': 'schemathesis/4.3.15', 'Accept-Encoding': 'gzip, deflate, zstd', 'Accept': 'application/json', 'Connection': 'keep-alive', 'Authorization': 'Basic YWRtaW46cGFzc3dvcmQxMjM=', 'Content-Type': 'application/json', 'Content-Length': '388'}
    body = {'bookingdates': {'checkin': '7006-11-10', 'checkout': '1016-12-03', '`': [1.7976931348623155e+308], '\x12\U000e240c\x9a#À;': {'eZï5\x17g\x11\U0004061f\x98\x8e\x842雚L¯È\U00068e44µd\x85': []}}, 'depositpaid': False, 'firstname': '±8', 'lastname': 'iLS\x01', 'totalprice': 6394, 'è': [], 'additionalneeds': '\x81!O\x08\x8b'}
    
    response = requests.post(url, headers=headers, json=body)
    
    check.equal(response.status_code, 200, f'Expected status 200, got {response.status_code}')
    check.equal(response.json(), {'bookingid': 1559, 'booking': {'firstname': '±8', 'lastname': 'iLS\x01', 'totalprice': 6394, 'depositpaid': False, 'bookingdates': {'checkin': '7006-11-10', 'checkout': '1016-12-03'}, 'additionalneeds': '\x81!O\x08\x8b'}}, 'Response body mismatch')

def test_post_booking_88():
    """Test generated from Schemathesis VCR: oxd8WU
    Test: POST /booking
    Status: SUCCESS
    """
    import requests
    
    url = f"https://restful-booker.herokuapp.com/booking"
    headers = {'User-Agent': 'schemathesis/4.3.15', 'Accept-Encoding': 'gzip, deflate, zstd', 'Accept': 'application/json', 'Connection': 'keep-alive', 'Authorization': 'Basic YWRtaW46cGFzc3dvcmQxMjM=', 'Content-Type': 'application/json', 'Content-Length': '1252'}
    body = {'bookingdates': {'checkin': '5627-03-31', 'checkout': '9799-08-09', 'õ\U000bfb0b': [{'¦O': -2.4735529686621516e+16, ' ': {'ⷎ\x17\x98Ð\U0008cd6f_': '\x9fë\x8c\x00ÖÓÒÛ¥j', 'ª': None}}], ':\U00087bd3\U0003f3a5\U000ce27eÙ{.\x9f': [[1.6579682367588655e-148, {'none': None, '\x07碾': 'Ð\U0010cd72îæ¶¼', 'xÎ\U0004695bBîa`': None}, False], {'𓹆': {'': False}}, [None, None, None]], ';5': [{'': True}], 'ÿ+7\U00058ca4\U000eb1a8:¹np𣋹': {'\x0cý\U00067f0b´>\x01\x1ey\U000d0acb\U000ec296\x9c\U0009d1c9ª\U0008f172': [[], {}], '«3¾\U000e5984=\x8a\U0007e59c¯ïÙF\x89\U0010936aHd6': {'': ['']}, '_\U00108f85 \x94î³;\x87': []}, '暴Æî§\U00077f76': -22104}, 'depositpaid': False, 'firstname': '!ð𣱯', 'lastname': '\ue8aeðPÌÔE=yÖ\U000dd149\x03\U000b1ac1\x16»rM', 'totalprice': 23027, 'additionalneeds': '%Î\U00035c61\U00071a88', '': {'\U00048d75á#7:': 7.535471791209798e+21, '\x0cO': -120, '\U000e6a88Uä\x00\x03': False}, 'Uï3': []}
    
    response = requests.post(url, headers=headers, json=body)
    
    check.equal(response.status_code, 500, f'Expected status 500, got {response.status_code}')
    check.is_not_none(response.text, 'Response should have body')

def test_delete_booking_38_89():
    """Test generated from Schemathesis VCR: fVcX6t
    Test: DELETE /booking/38
    Status: FAILURE
    """
    import requests
    
    url = f"https://restful-booker.herokuapp.com/booking/38"
    headers = {'User-Agent': 'schemathesis/4.3.15', 'Accept-Encoding': 'gzip, deflate, zstd', 'Accept': 'application/json', 'Connection': 'keep-alive', 'Authorization': 'Basic YWRtaW46cGFzc3dvcmQxMjM=', 'Content-Type': 'application/json', 'Content-Length': '0'}
    
    response = requests.delete(url, headers=headers)
    
    check.equal(response.status_code, 405, f'Expected status 405, got {response.status_code}')
    # Original failed checks: positive_data_acceptance

def test_post_booking_90():
    """Test generated from Schemathesis VCR: Hsqq5U
    Test: POST /booking
    Status: SUCCESS
    """
    import requests
    
    url = f"https://restful-booker.herokuapp.com/booking"
    headers = {'User-Agent': 'schemathesis/4.3.15', 'Accept-Encoding': 'gzip, deflate, zstd', 'Accept': 'application/json', 'Connection': 'keep-alive', 'Authorization': 'Basic YWRtaW46cGFzc3dvcmQxMjM=', 'Content-Type': 'application/json', 'Content-Length': '388'}
    body = {'bookingdates': {'checkin': '7006-11-10', 'checkout': '1016-12-03', '`': [1.7976931348623155e+308], '\x12\U000e240c\x9a#À;': {'eZï5\x17g\x11\U0004061f\x98\x8e\x842雚L¯È\U00068e44µd\x85': []}}, 'depositpaid': False, 'firstname': '±8', 'lastname': 'iLS\x01', 'totalprice': 6394, 'è': [], 'additionalneeds': '\x81!O\x08\x8b'}
    
    response = requests.post(url, headers=headers, json=body)
    
    check.equal(response.status_code, 200, f'Expected status 200, got {response.status_code}')
    check.equal(response.json(), {'bookingid': 1565, 'booking': {'firstname': '±8', 'lastname': 'iLS\x01', 'totalprice': 6394, 'depositpaid': False, 'bookingdates': {'checkin': '7006-11-10', 'checkout': '1016-12-03'}, 'additionalneeds': '\x81!O\x08\x8b'}}, 'Response body mismatch')

def test_post_booking_91():
    """Test generated from Schemathesis VCR: 3dVYMs
    Test: POST /booking
    Status: SUCCESS
    """
    import requests
    
    url = f"https://restful-booker.herokuapp.com/booking"
    headers = {'User-Agent': 'schemathesis/4.3.15', 'Accept-Encoding': 'gzip, deflate, zstd', 'Accept': 'application/json', 'Connection': 'keep-alive', 'Authorization': 'Basic YWRtaW46cGFzc3dvcmQxMjM=', 'Content-Type': 'application/json', 'Content-Length': '1252'}
    body = {'bookingdates': {'checkin': '5627-03-31', 'checkout': '9799-08-09', 'õ\U000bfb0b': [{'¦O': -2.4735529686621516e+16, ' ': {'ⷎ\x17\x98Ð\U0008cd6f_': '\x9fë\x8c\x00ÖÓÒÛ¥j', 'ª': None}}], ':\U00087bd3\U0003f3a5\U000ce27eÙ{.\x9f': [[1.6579682367588655e-148, {'none': None, '\x07碾': 'Ð\U0010cd72îæ¶¼', 'xÎ\U0004695bBîa`': None}, False], {'𓹆': {'': False}}, [None, None, None]], ';5': [{'': True}], 'ÿ+7\U00058ca4\U000eb1a8:¹np𣋹': {'\x0cý\U00067f0b´>\x01\x1ey\U000d0acb\U000ec296\x9c\U0009d1c9ª\U0008f172': [[], {}], '«3¾\U000e5984=\x8a\U0007e59c¯ïÙF\x89\U0010936aHd6': {'': ['']}, '_\U00108f85 \x94î³;\x87': []}, '暴Æî§\U00077f76': -22104}, 'depositpaid': False, 'firstname': '!ð𣱯', 'lastname': '\ue8aeðPÌÔE=yÖ\U000dd149\x03\U000b1ac1\x16»rM', 'totalprice': 23027, 'additionalneeds': '%Î\U00035c61\U00071a88', '': {'\U00048d75á#7:': 7.535471791209798e+21, '\x0cO': -120, '\U000e6a88Uä\x00\x03': False}, 'Uï3': []}
    
    response = requests.post(url, headers=headers, json=body)
    
    check.equal(response.status_code, 500, f'Expected status 500, got {response.status_code}')
    check.is_not_none(response.text, 'Response should have body')

def test_delete_booking_38_92():
    """Test generated from Schemathesis VCR: TVwiqN
    Test: DELETE /booking/38
    Status: SUCCESS
    """
    import requests
    
    url = f"https://restful-booker.herokuapp.com/booking/38"
    headers = {'User-Agent': 'schemathesis/4.3.15', 'Accept-Encoding': 'gzip, deflate, zstd', 'Accept': 'application/json', 'Connection': 'keep-alive', 'Authorization': 'Basic YWRtaW46cGFzc3dvcmQxMjM=', 'Content-Type': 'application/json', 'Content-Length': '0'}
    
    response = requests.delete(url, headers=headers)
    
    check.equal(response.status_code, 405, f'Expected status 405, got {response.status_code}')
    check.is_not_none(response.text, 'Response should have body')

def test_patch_booking_93():
    """Test generated from Schemathesis VCR: PUm8ri
    Test: PATCH /booking/%12%C3%9D%F4%8B%B5%B4%F3%8C%A0%8C
    Status: SUCCESS
    """
    import requests
    
    url = f"https://restful-booker.herokuapp.com/booking/%12%C3%9D%F4%8B%B5%B4%F3%8C%A0%8C"
    headers = {'User-Agent': 'schemathesis/4.3.15', 'Accept-Encoding': 'gzip, deflate, zstd', 'Accept': 'application/json', 'Connection': 'keep-alive', 'Authorization': 'Basic YWRtaW46cGFzc3dvcmQxMjM=', 'Content-Type': 'application/json', 'Content-Length': '301'}
    body = {'\x07AYpç\U00075ff7': {}, 'depositpaid': False, 'additionalneeds': 'F\U000c0c4eÿJb\x9e:¼dà', '¿': {'+': False, 'äꖌ': [], '': {'\x9d': 29763}}, 'bookingdates': {'checkin': '7006-11-10', 'checkout': '1016-12-03'}, 'firstname': '±8', 'totalprice': 6394}
    
    response = requests.patch(url, headers=headers, json=body)
    
    check.equal(response.status_code, 405, f'Expected status 405, got {response.status_code}')
    check.is_not_none(response.text, 'Response should have body')

def test_patch_booking_14539_94():
    """Test generated from Schemathesis VCR: Y4Ov0P
    Test: PATCH /booking/-14539
    Status: SUCCESS
    """
    import requests
    
    url = f"https://restful-booker.herokuapp.com/booking/-14539"
    headers = {'User-Agent': 'schemathesis/4.3.15', 'Accept-Encoding': 'gzip, deflate, zstd', 'Accept': 'application/json', 'Connection': 'keep-alive', 'Authorization': 'Basic YWRtaW46cGFzc3dvcmQxMjM=', 'Content-Type': 'application/json', 'Content-Length': '320'}
    body = {'bookingdates': {'checkin': '7006-11-10', 'checkout': '1016-12-03'}, 'depositpaid': False, 'firstname': '\U0004d6f9v\x10', 'lastname': 'iLS\x01', 'totalprice': 6394, '': [[], [None], {'__main__': False, '\x90JÛ£í': -1.3237497143597602e+93, '"\U0003c473Le\x9fT\x1f': 1.40398212782247e+16}]}
    
    response = requests.patch(url, headers=headers, json=body)
    
    check.equal(response.status_code, 405, f'Expected status 405, got {response.status_code}')
    check.is_not_none(response.text, 'Response should have body')

def test_delete_booking_true_95():
    """Test generated from Schemathesis VCR: 4encir
    Test: DELETE /booking/true
    Status: SUCCESS
    """
    import requests
    
    url = f"https://restful-booker.herokuapp.com/booking/true"
    headers = {'User-Agent': 'schemathesis/4.3.15', 'Accept-Encoding': 'gzip, deflate, zstd', 'Accept': 'application/json', 'Connection': 'keep-alive', 'Authorization': 'Basic YWRtaW46cGFzc3dvcmQxMjM=', 'Content-Type': 'application/json', 'Content-Length': '0'}
    
    response = requests.delete(url, headers=headers)
    
    check.equal(response.status_code, 405, f'Expected status 405, got {response.status_code}')
    check.is_not_none(response.text, 'Response should have body')

def test_post_booking_96():
    """Test generated from Schemathesis VCR: 65Gezd
    Test: POST /booking
    Status: SUCCESS
    """
    import requests
    
    url = f"https://restful-booker.herokuapp.com/booking"
    headers = {'User-Agent': 'schemathesis/4.3.15', 'Accept-Encoding': 'gzip, deflate, zstd', 'Accept': 'application/json', 'Connection': 'keep-alive', 'Authorization': 'Basic YWRtaW46cGFzc3dvcmQxMjM=', 'Content-Type': 'application/json', 'Content-Length': '2'}
    body = []
    
    response = requests.post(url, headers=headers, json=body)
    
    check.equal(response.status_code, 500, f'Expected status 500, got {response.status_code}')
    check.is_not_none(response.text, 'Response should have body')

def test_post_booking_97():
    """Test generated from Schemathesis VCR: QbBBG3
    Test: POST /booking
    Status: SUCCESS
    """
    import requests
    
    url = f"https://restful-booker.herokuapp.com/booking"
    headers = {'User-Agent': 'schemathesis/4.3.15', 'Accept-Encoding': 'gzip, deflate, zstd', 'Accept': 'application/json', 'Connection': 'keep-alive', 'Authorization': 'Basic YWRtaW46cGFzc3dvcmQxMjM=', 'Content-Type': 'application/json', 'Content-Length': '3'}
    body = -49
    
    response = requests.post(url, headers=headers, json=body)
    
    check.equal(response.status_code, 400, f'Expected status 400, got {response.status_code}')
    check.is_not_none(response.text, 'Response should have body')

def test_post_booking_98():
    """Test generated from Schemathesis VCR: ZootkD
    Test: POST /booking
    Status: SUCCESS
    """
    import requests
    
    url = f"https://restful-booker.herokuapp.com/booking"
    headers = {'User-Agent': 'schemathesis/4.3.15', 'Accept-Encoding': 'gzip, deflate, zstd', 'Accept': 'application/json', 'Connection': 'keep-alive', 'Authorization': 'Basic YWRtaW46cGFzc3dvcmQxMjM=', 'Content-Type': 'application/json', 'Content-Length': '571'}
    body = {'bookingdates': {'checkin': '7306-03-08', 'checkout': '6287-06-19', 'É»)L': [[{'CÀ': [], 'á©À\U00050af9\U0003ad69µ|\U000a8d35e>÷Ñ\x01H': True, '': 300}], {'\x96\x144': {'Ú': None}}, {'hzÖ8': [-6863], '\U0005d1d5\x16»¢îQ¥@': [None, [], [True, '', 'B\x83¶\x19\U0005ab5d\U000ac49d<\U0004e7ccI\x19¦\U00037fff']]}]}, 'depositpaid': False, 'firstname': 'U', 'lastname': '𦄓', 'totalprice': 9678, 'additionalneeds': 'Ð\U00053a0d', '¤A': {}}
    
    response = requests.post(url, headers=headers, json=body)
    
    check.equal(response.status_code, 200, f'Expected status 200, got {response.status_code}')
    check.equal(response.json(), {'bookingid': 1576, 'booking': {'firstname': 'U', 'lastname': '𦄓', 'totalprice': 9678, 'depositpaid': False, 'bookingdates': {'checkin': '7306-03-08', 'checkout': '6287-06-19'}, 'additionalneeds': 'Ð\U00053a0d'}}, 'Response body mismatch')

def test_post_booking_99():
    """Test generated from Schemathesis VCR: ph0cyH
    Test: POST /booking
    Status: SUCCESS
    """
    import requests
    
    url = f"https://restful-booker.herokuapp.com/booking"
    headers = {'User-Agent': 'schemathesis/4.3.15', 'Accept-Encoding': 'gzip, deflate, zstd', 'Accept': 'application/json', 'Connection': 'keep-alive', 'Authorization': 'Basic YWRtaW46cGFzc3dvcmQxMjM=', 'Content-Type': 'application/json', 'Content-Length': '179'}
    body = {'bookingdates': {'checkin': '5733-03-12', 'checkout': '2378-04-15'}, 'depositpaid': True, 'firstname': 'ï', 'lastname': '', 'totalprice': 18753, 'additionalneeds': 'õ'}
    
    response = requests.post(url, headers=headers, json=body)
    
    check.equal(response.status_code, 200, f'Expected status 200, got {response.status_code}')
    check.equal(response.json(), {'bookingid': 1580, 'booking': {'firstname': 'ï', 'lastname': '', 'totalprice': 18753, 'depositpaid': True, 'bookingdates': {'checkin': '5733-03-12', 'checkout': '2378-04-15'}, 'additionalneeds': 'õ'}}, 'Response body mismatch')

def test_delete_booking_117_100():
    """Test generated from Schemathesis VCR: rg264a
    Test: DELETE /booking/117
    Status: FAILURE
    """
    import requests
    
    url = f"https://restful-booker.herokuapp.com/booking/117"
    headers = {'User-Agent': 'schemathesis/4.3.15', 'Accept-Encoding': 'gzip, deflate, zstd', 'Accept': 'application/json', 'Connection': 'keep-alive', 'Authorization': 'Basic YWRtaW46cGFzc3dvcmQxMjM=', 'Content-Type': 'application/json', 'Content-Length': '0'}
    
    response = requests.delete(url, headers=headers)
    
    check.equal(response.status_code, 201, f'Expected status 201, got {response.status_code}')
    # Original failed checks: content_type_conformance

def test_post_booking_101():
    """Test generated from Schemathesis VCR: 0VVlSC
    Test: POST /booking
    Status: SUCCESS
    """
    import requests
    
    url = f"https://restful-booker.herokuapp.com/booking"
    headers = {'User-Agent': 'schemathesis/4.3.15', 'Accept-Encoding': 'gzip, deflate, zstd', 'Accept': 'application/json', 'Connection': 'keep-alive', 'Authorization': 'Basic YWRtaW46cGFzc3dvcmQxMjM=', 'Content-Type': 'application/json', 'Content-Length': '179'}
    body = {'bookingdates': {'checkin': '5733-03-12', 'checkout': '2378-04-15'}, 'depositpaid': True, 'firstname': 'ï', 'lastname': '', 'totalprice': 18753, 'additionalneeds': 'õ'}
    
    response = requests.post(url, headers=headers, json=body)
    
    check.equal(response.status_code, 200, f'Expected status 200, got {response.status_code}')
    check.equal(response.json(), {'bookingid': 1584, 'booking': {'firstname': 'ï', 'lastname': '', 'totalprice': 18753, 'depositpaid': True, 'bookingdates': {'checkin': '5733-03-12', 'checkout': '2378-04-15'}, 'additionalneeds': 'õ'}}, 'Response body mismatch')

def test_delete_booking_117_102():
    """Test generated from Schemathesis VCR: 0Q8UlK
    Test: DELETE /booking/117
    Status: SUCCESS
    """
    import requests
    
    url = f"https://restful-booker.herokuapp.com/booking/117"
    headers = {'User-Agent': 'schemathesis/4.3.15', 'Accept-Encoding': 'gzip, deflate, zstd', 'Accept': 'application/json', 'Connection': 'keep-alive', 'Authorization': 'Basic YWRtaW46cGFzc3dvcmQxMjM=', 'Content-Type': 'application/json', 'Content-Length': '0'}
    
    response = requests.delete(url, headers=headers)
    
    check.equal(response.status_code, 405, f'Expected status 405, got {response.status_code}')
    check.is_not_none(response.text, 'Response should have body')

def test_delete_booking_7343655899138986579_103():
    """Test generated from Schemathesis VCR: 0TIZVV
    Test: DELETE /booking/7343655899138986579
    Status: SUCCESS
    """
    import requests
    
    url = f"https://restful-booker.herokuapp.com/booking/7343655899138986579"
    headers = {'User-Agent': 'schemathesis/4.3.15', 'Accept-Encoding': 'gzip, deflate, zstd', 'Accept': 'application/json', 'Connection': 'keep-alive', 'Authorization': 'Basic YWRtaW46cGFzc3dvcmQxMjM=', 'Content-Type': 'application/json', 'Content-Length': '0'}
    
    response = requests.delete(url, headers=headers)
    
    check.equal(response.status_code, 405, f'Expected status 405, got {response.status_code}')
    check.is_not_none(response.text, 'Response should have body')

def test_post_booking_104():
    """Test generated from Schemathesis VCR: JFXhOO
    Test: POST /booking
    Status: SUCCESS
    """
    import requests
    
    url = f"https://restful-booker.herokuapp.com/booking"
    headers = {'User-Agent': 'schemathesis/4.3.15', 'Accept-Encoding': 'gzip, deflate, zstd', 'Accept': 'application/json', 'Connection': 'keep-alive', 'Authorization': 'Basic YWRtaW46cGFzc3dvcmQxMjM=', 'Content-Type': 'application/json', 'Content-Length': '556'}
    body = {'bookingdates': {'checkin': '3877-12-20', 'checkout': '4607-04-08'}, 'depositpaid': True, 'firstname': 'ÿ\U000a06e0NN\x17Q$(堈\xa0Ø', 'lastname': '\\£w§>4ÿý', 'totalprice': 48, '\U00079f5e\x8eÕ¼ï\x84µv\x82': [[None, '䂮¥\U00076ed0', None], {'\U000bca17Y': {'': 'Authorization', '¯L\x9c\x95': None}}, {'': ['*Â!\x07õm\U000cb5bb\x9b\x7fà\x99÷ꀏ\U0001e9f6Su\x83±1$Ùà\x073ᥖ', None, 1.1047542258892161e+259]}]}
    
    response = requests.post(url, headers=headers, json=body)
    
    check.equal(response.status_code, 200, f'Expected status 200, got {response.status_code}')
    check.equal(response.json(), {'bookingid': 1587, 'booking': {'firstname': 'ÿ\U000a06e0NN\x17Q$(堈\xa0Ø', 'lastname': '\\£w§>4ÿý', 'totalprice': 48, 'depositpaid': True, 'bookingdates': {'checkin': '3877-12-20', 'checkout': '4607-04-08'}}}, 'Response body mismatch')

def test_get_booking_O_Y_J_z_w_g_105():
    """Test generated from Schemathesis VCR: qXcsKi
    Test: GET /booking/%C3%8FO%F2%BA%8D%98Y%C2%A4%00%C3%B6J%C2%B1%C2%AEz%40w%03g%F3%80%B4%97%22
    Status: SUCCESS
    """
    import requests
    
    url = f"https://restful-booker.herokuapp.com/booking/%C3%8FO%F2%BA%8D%98Y%C2%A4%00%C3%B6J%C2%B1%C2%AEz%40w%03g%F3%80%B4%97%22"
    headers = {'User-Agent': 'schemathesis/4.3.15', 'Accept-Encoding': 'gzip, deflate, zstd', 'Accept': 'application/json', 'Connection': 'keep-alive', 'Authorization': 'Basic YWRtaW46cGFzc3dvcmQxMjM=', 'Content-Type': 'application/json'}
    
    response = requests.get(url, headers=headers)
    
    check.equal(response.status_code, 404, f'Expected status 404, got {response.status_code}')
    check.is_not_none(response.text, 'Response should have body')

def test_get_booking_E_b_106():
    """Test generated from Schemathesis VCR: gABQmj
    Test: GET /booking/%F1%A3%97%AC%C3%BF%F1%86%AB%A2E%08b
    Status: SUCCESS
    """
    import requests
    
    url = f"https://restful-booker.herokuapp.com/booking/%F1%A3%97%AC%C3%BF%F1%86%AB%A2E%08b"
    headers = {'User-Agent': 'schemathesis/4.3.15', 'Accept-Encoding': 'gzip, deflate, zstd', 'Accept': 'application/json', 'Connection': 'keep-alive', 'Authorization': 'Basic YWRtaW46cGFzc3dvcmQxMjM=', 'Content-Type': 'application/json'}
    
    response = requests.get(url, headers=headers)
    
    check.equal(response.status_code, 404, f'Expected status 404, got {response.status_code}')
    check.is_not_none(response.text, 'Response should have body')

def test_post_booking_107():
    """Test generated from Schemathesis VCR: gWVaqU
    Test: POST /booking
    Status: SUCCESS
    """
    import requests
    
    url = f"https://restful-booker.herokuapp.com/booking"
    headers = {'User-Agent': 'schemathesis/4.3.15', 'Accept-Encoding': 'gzip, deflate, zstd', 'Accept': 'application/json', 'Connection': 'keep-alive', 'Authorization': 'Basic YWRtaW46cGFzc3dvcmQxMjM=', 'Content-Type': 'application/json', 'Content-Length': '2'}
    body = []
    
    response = requests.post(url, headers=headers, json=body)
    
    check.equal(response.status_code, 500, f'Expected status 500, got {response.status_code}')
    check.is_not_none(response.text, 'Response should have body')

def test_post_booking_108():
    """Test generated from Schemathesis VCR: 9ArFpa
    Test: POST /booking
    Status: SUCCESS
    """
    import requests
    
    url = f"https://restful-booker.herokuapp.com/booking"
    headers = {'User-Agent': 'schemathesis/4.3.15', 'Accept-Encoding': 'gzip, deflate, zstd', 'Accept': 'application/json', 'Connection': 'keep-alive', 'Authorization': 'Basic YWRtaW46cGFzc3dvcmQxMjM=', 'Content-Type': 'application/json', 'Content-Length': '2677'}
    body = {'bookingdates': {'checkin': '2944-03-18', 'checkout': '3359-04-06', '\x89𔀻0': {}, '': {'': {'\x10𜼜': {}, 'Ṱ̺̺̕o͞ ̷i̲̬͇̪͙n̝̗͕v̟̜̘̦͟o̶̙̰̠kè͚̮̺̪̹̱̤ ̖t̝͕̳̣̻̪͞h̼͓̲̦̳̘̲e͇̣̰̦̬͎ ̢̼̻̱̘h͚͎͙̜̣̲ͅi̦̲̣̰̤v̻͍e̺̭̳̪̰-m̢iͅn̖̺̞̲̯̰d̵̼̟͙̩̼̘̳ ̞̥̱̳̭r̛̗̘e͙p͠r̼̞̻̭̗e̺̠̣͟s̘͇̳͍̝͉e͉̥̯̞̲͚̬͜ǹ̬͎͎̟̖͇̤t͍̬̤͓̼̭͘ͅi̪̱n͠g̴͉ ͏͉ͅc̬̟h͡a̫̻̯͘o̫̟̖͍̙̝͉s̗̦̲.̨̹͈̣': 1503, '²\x00\U00066b14EW': {'\x94\U000d96d8': {}, 'U\U000ad0b5\n¡\x94î\U000af7e4l\x9e䓦=Ð': {'(ã\x10ù\U000a8abe\x17\x03': '\x04Ájò\x17\U000a0a48\x08Ñþ'}, '\x8e\U000cd750Zß\x00`©7¹\x98': -2.712773779348443e-227}}, '\U00016703.': {'Ñ\U00015e66å^': None, 'é': -26410, '': -4.647521143709179e+16}}, '\U0007947f\U001095b0ß4Uý': {'¦çt': {}, '𢗉ä.¨Ø\x05\x85µÉ': {}}, 'Ü\U000569f1h©\n\x95': [], '\x19{': False, '±ôôÇ±0túÅ\U000b911f\U000e4949\x9bv5\U0007a176\x98wa\x98¦l\U000e3fdd': [], '\x7fø\x99': {}, 'True': {}, '3\x82𣿠\U000d3c07;?Ýê': {'\U0008c080': [-1.7976931348623155e+308], 'Èª': {'Ûþ\x8d)\x07\x17\x12': -26566, '\U000d65b2': '@ðb', 'Ë\x15£º\x1d\U00071f70í': '\U0007fb093'}}, '\U00103e18𓘖pA\x8b2\x85\x80M\xad': {'ঽ\U00033355': [], '\x8dÛ\U0008d4b5qo±': {'\x13': {}, 'y\x02H¯\x16iÌ': {}}}, 'È\U0001ee38®\U000dbfcfÐ\U000ca8f5𲄄\U00083de3P¿\x18¨/\U000b36b0𤶻k¦¦h\U000576d8O\x80Anè¬aO': ''}, 'depositpaid': False, 'firstname': '\U000e7b54\U000ebb20', 'lastname': '', 'totalprice': 3014}
    
    response = requests.post(url, headers=headers, json=body)
    
    check.equal(response.status_code, 500, f'Expected status 500, got {response.status_code}')
    check.is_not_none(response.text, 'Response should have body')

def test_post_booking_109():
    """Test generated from Schemathesis VCR: uOxPH9
    Test: POST /booking
    Status: SUCCESS
    """
    import requests
    
    url = f"https://restful-booker.herokuapp.com/booking"
    headers = {'User-Agent': 'schemathesis/4.3.15', 'Accept-Encoding': 'gzip, deflate, zstd', 'Accept': 'application/json', 'Connection': 'keep-alive', 'Authorization': 'Basic YWRtaW46cGFzc3dvcmQxMjM=', 'Content-Type': 'application/json', 'Content-Length': '1150'}
    body = {'bookingdates': {'checkin': '9927-12-24', 'checkout': '5505-04-16', 'É]\U000ded64s,': {'': True, '³\U000423ffZbs\U000aba67ö\U000d11a6\x14': '\x87¼?P{\U0006c65f', '🏻👍🏻': None}, 'êLªï': [{'Oø6\x9aV=\x8dV\U000bc420\x0f\x92ô\x13\uf218t𠯞f': {}}, [28789, False, False], ['\U000d905c']]}, 'depositpaid': False, 'firstname': 'dÑ\x0e\x8b¬v\U0004e411\x9a+\n㝽\x17', 'lastname': '\U000aa88d', 'totalprice': -152724071192326535864254188247522378542, 'additionalneeds': 'ÝË¦¯𩠗\x0f\x90HI~', '<\x19îD': [6.405245648711291e-197, {'': None, '\x12\U00076296\U001044cdQ': 125, '\x89e(ºg8&\x98ë\x82=ü\x03Ë¥\U00063c07Æ¡\U00019d38%\x03L\x99²': True}, {'\U0004de5b|': -2.4346802688779766e-301, 'j\U0007f80e¾': {'é\x98\x9f\U00089725': 5.84563374817645e+16}, '\x91ºo\x17S\x8ew\x95×R': -2.7506144860247e-121}], 'x6°\x95\x0e³})óxÄ\x94iSä\\\r\x99½a': []}
    
    response = requests.post(url, headers=headers, json=body)
    
    check.equal(response.status_code, 200, f'Expected status 200, got {response.status_code}')
    check.equal(response.json(), {'bookingid': 1600, 'booking': {'firstname': 'dÑ\x0e\x8b¬v\U0004e411\x9a+\n㝽\x17', 'lastname': '\U000aa88d', 'totalprice': -1, 'depositpaid': False, 'bookingdates': {'checkin': '9927-12-24', 'checkout': '5505-04-16'}, 'additionalneeds': 'ÝË¦¯𩠗\x0f\x90HI~'}}, 'Response body mismatch')

def test_get_booking_Y_110():
    """Test generated from Schemathesis VCR: XdFnDT
    Test: GET /booking/Y
    Status: SUCCESS
    """
    import requests
    
    url = f"https://restful-booker.herokuapp.com/booking/Y"
    headers = {'User-Agent': 'schemathesis/4.3.15', 'Accept-Encoding': 'gzip, deflate, zstd', 'Accept': 'application/json', 'Connection': 'keep-alive', 'Authorization': 'Basic YWRtaW46cGFzc3dvcmQxMjM=', 'Content-Type': 'application/json'}
    
    response = requests.get(url, headers=headers)
    
    check.equal(response.status_code, 404, f'Expected status 404, got {response.status_code}')
    check.is_not_none(response.text, 'Response should have body')

def test_post_booking_111():
    """Test generated from Schemathesis VCR: 0PuTau
    Test: POST /booking
    Status: SUCCESS
    """
    import requests
    
    url = f"https://restful-booker.herokuapp.com/booking"
    headers = {'User-Agent': 'schemathesis/4.3.15', 'Accept-Encoding': 'gzip, deflate, zstd', 'Accept': 'application/json', 'Connection': 'keep-alive', 'Authorization': 'Basic YWRtaW46cGFzc3dvcmQxMjM=', 'Content-Type': 'application/json', 'Content-Length': '261'}
    body = {'bookingdates': {'checkin': '8305-10-23', 'checkout': '4112-08-17', '': [[None, True, '\x92¥'], None]}, 'depositpaid': True, 'firstname': 'ï>\x1d\U00047cb2.', 'lastname': 'eí뿛\U000f67c1R\U00095e90Ù', 'totalprice': 1761172676}
    
    response = requests.post(url, headers=headers, json=body)
    
    check.equal(response.status_code, 200, f'Expected status 200, got {response.status_code}')
    check.equal(response.json(), {'bookingid': 1605, 'booking': {'firstname': 'ï>\x1d\U00047cb2.', 'lastname': 'eí뿛\U000f67c1R\U00095e90Ù', 'totalprice': 1761172676, 'depositpaid': True, 'bookingdates': {'checkin': '8305-10-23', 'checkout': '4112-08-17'}}}, 'Response body mismatch')

def test_post_booking_112():
    """Test generated from Schemathesis VCR: Fh8nBX
    Test: POST /booking
    Status: SUCCESS
    """
    import requests
    
    url = f"https://restful-booker.herokuapp.com/booking"
    headers = {'User-Agent': 'schemathesis/4.3.15', 'Accept-Encoding': 'gzip, deflate, zstd', 'Accept': 'application/json', 'Connection': 'keep-alive', 'Authorization': 'Basic YWRtaW46cGFzc3dvcmQxMjM=', 'Content-Type': 'application/json', 'Content-Length': '246'}
    body = {'bookingdates': {'checkin': '5341-10-30', 'checkout': '4368-10-20'}, 'depositpaid': True, 'firstname': '\x03\U000de778ï𐕗ïsD\\(g!¢ç-\x0e\xa0å\U000aeefcy', 'lastname': 'null', 'totalprice': 45, '': {}}
    
    response = requests.post(url, headers=headers, json=body)
    
    check.equal(response.status_code, 200, f'Expected status 200, got {response.status_code}')
    check.equal(response.json(), {'bookingid': 1609, 'booking': {'firstname': '\x03\U000de778ï𐕗ïsD\\(g!¢ç-\x0e\xa0å\U000aeefcy', 'lastname': 'null', 'totalprice': 45, 'depositpaid': True, 'bookingdates': {'checkin': '5341-10-30', 'checkout': '4368-10-20'}}}, 'Response body mismatch')

def test_post_booking_113():
    """Test generated from Schemathesis VCR: zqKMAd
    Test: POST /booking
    Status: SUCCESS
    """
    import requests
    
    url = f"https://restful-booker.herokuapp.com/booking"
    headers = {'User-Agent': 'schemathesis/4.3.15', 'Accept-Encoding': 'gzip, deflate, zstd', 'Accept': 'application/json', 'Connection': 'keep-alive', 'Authorization': 'Basic YWRtaW46cGFzc3dvcmQxMjM=', 'Content-Type': 'application/json', 'Content-Length': '150'}
    body = {'bookingdates': {'checkin': '2945-10-07', 'checkout': '0300-11-14'}, 'depositpaid': True, 'firstname': '', 'lastname': 'â', 'totalprice': 13401}
    
    response = requests.post(url, headers=headers, json=body)
    
    check.equal(response.status_code, 200, f'Expected status 200, got {response.status_code}')
    check.equal(response.json(), {'bookingid': 1612, 'booking': {'firstname': '', 'lastname': 'â', 'totalprice': 13401, 'depositpaid': True, 'bookingdates': {'checkin': '2945-10-07', 'checkout': '0300-11-14'}}}, 'Response body mismatch')

def test_patch_booking_5_114():
    """Test generated from Schemathesis VCR: vmt2Pc
    Test: PATCH /booking/5%F0%A9%9C%BA%3C%C3%8B%C3%B8
    Status: FAILURE
    """
    import requests
    
    url = f"https://restful-booker.herokuapp.com/booking/5%F0%A9%9C%BA%3C%C3%8B%C3%B8"
    headers = {'User-Agent': 'schemathesis/4.3.15', 'Accept-Encoding': 'gzip, deflate, zstd', 'Accept': 'application/json', 'Connection': 'keep-alive', 'Authorization': 'Basic YWRtaW46cGFzc3dvcmQxMjM=', 'Content-Type': 'application/json', 'Content-Length': '150'}
    body = {'firstname': '', 'lastname': 'â', 'totalprice': 13401, 'depositpaid': True, 'bookingdates': {'checkin': '2945-10-07', 'checkout': '0300-11-14'}}
    
    response = requests.patch(url, headers=headers, json=body)
    
    check.equal(response.status_code, 200, f'Expected status 200, got {response.status_code}')
    # Original failed checks: negative_data_rejection

def test_post_booking_115():
    """Test generated from Schemathesis VCR: L5FHeM
    Test: POST /booking
    Status: SUCCESS
    """
    import requests
    
    url = f"https://restful-booker.herokuapp.com/booking"
    headers = {'User-Agent': 'schemathesis/4.3.15', 'Accept-Encoding': 'gzip, deflate, zstd', 'Accept': 'application/json', 'Connection': 'keep-alive', 'Authorization': 'Basic YWRtaW46cGFzc3dvcmQxMjM=', 'Content-Type': 'application/json', 'Content-Length': '150'}
    body = {'bookingdates': {'checkin': '2945-10-07', 'checkout': '0300-11-14'}, 'depositpaid': True, 'firstname': '', 'lastname': 'â', 'totalprice': 13401}
    
    response = requests.post(url, headers=headers, json=body)
    
    check.equal(response.status_code, 200, f'Expected status 200, got {response.status_code}')
    check.equal(response.json(), {'bookingid': 1615, 'booking': {'firstname': '', 'lastname': 'â', 'totalprice': 13401, 'depositpaid': True, 'bookingdates': {'checkin': '2945-10-07', 'checkout': '0300-11-14'}}}, 'Response body mismatch')

def test_patch_booking_5_116():
    """Test generated from Schemathesis VCR: JfnZax
    Test: PATCH /booking/5%F0%A9%9C%BA%3C%C3%8B%C3%B8
    Status: SUCCESS
    """
    import requests
    
    url = f"https://restful-booker.herokuapp.com/booking/5%F0%A9%9C%BA%3C%C3%8B%C3%B8"
    headers = {'User-Agent': 'schemathesis/4.3.15', 'Accept-Encoding': 'gzip, deflate, zstd', 'Accept': 'application/json', 'Connection': 'keep-alive', 'Authorization': 'Basic YWRtaW46cGFzc3dvcmQxMjM=', 'Content-Type': 'application/json', 'Content-Length': '150'}
    body = {'firstname': '', 'lastname': 'â', 'totalprice': 13401, 'depositpaid': True, 'bookingdates': {'checkin': '2945-10-07', 'checkout': '0300-11-14'}}
    
    response = requests.patch(url, headers=headers, json=body)
    
    check.equal(response.status_code, 200, f'Expected status 200, got {response.status_code}')
    check.equal(response.json(), {'firstname': '', 'lastname': 'â', 'totalprice': 13401, 'depositpaid': True, 'bookingdates': {'checkin': '2945-10-07', 'checkout': '0300-11-14'}}, 'Response body mismatch')

def test_put_booking_248224786_117():
    """Test generated from Schemathesis VCR: B7nr7V
    Test: PUT /booking/-248224786
    Status: FAILURE
    """
    import requests
    
    url = f"https://restful-booker.herokuapp.com/booking/-248224786"
    headers = {'User-Agent': 'schemathesis/4.3.15', 'Accept-Encoding': 'gzip, deflate, zstd', 'Accept': 'application/json', 'Connection': 'keep-alive', 'Authorization': 'Basic YWRtaW46cGFzc3dvcmQxMjM=', 'Content-Type': 'application/json', 'Content-Length': '150'}
    body = {'bookingdates': {'checkin': '2945-10-07', 'checkout': '0300-11-14'}, 'depositpaid': True, 'firstname': '', 'lastname': 'â', 'totalprice': 13401}
    
    response = requests.put(url, headers=headers, json=body)
    
    check.equal(response.status_code, 405, f'Expected status 405, got {response.status_code}')
    # Original failed checks: status_code_conformance, positive_data_acceptance

def test_post_booking_118():
    """Test generated from Schemathesis VCR: uAFF5l
    Test: POST /booking
    Status: SUCCESS
    """
    import requests
    
    url = f"https://restful-booker.herokuapp.com/booking"
    headers = {'User-Agent': 'schemathesis/4.3.15', 'Accept-Encoding': 'gzip, deflate, zstd', 'Accept': 'application/json', 'Connection': 'keep-alive', 'Authorization': 'Basic YWRtaW46cGFzc3dvcmQxMjM=', 'Content-Type': 'application/json', 'Content-Length': '150'}
    body = {'bookingdates': {'checkin': '2945-10-07', 'checkout': '0300-11-14'}, 'depositpaid': True, 'firstname': '', 'lastname': 'â', 'totalprice': 13401}
    
    response = requests.post(url, headers=headers, json=body)
    
    check.equal(response.status_code, 200, f'Expected status 200, got {response.status_code}')
    check.equal(response.json(), {'bookingid': 1621, 'booking': {'firstname': '', 'lastname': 'â', 'totalprice': 13401, 'depositpaid': True, 'bookingdates': {'checkin': '2945-10-07', 'checkout': '0300-11-14'}}}, 'Response body mismatch')

def test_patch_booking_5_119():
    """Test generated from Schemathesis VCR: HggOf6
    Test: PATCH /booking/5%F0%A9%9C%BA%3C%C3%8B%C3%B8
    Status: SUCCESS
    """
    import requests
    
    url = f"https://restful-booker.herokuapp.com/booking/5%F0%A9%9C%BA%3C%C3%8B%C3%B8"
    headers = {'User-Agent': 'schemathesis/4.3.15', 'Accept-Encoding': 'gzip, deflate, zstd', 'Accept': 'application/json', 'Connection': 'keep-alive', 'Authorization': 'Basic YWRtaW46cGFzc3dvcmQxMjM=', 'Content-Type': 'application/json', 'Content-Length': '150'}
    body = {'firstname': '', 'lastname': 'â', 'totalprice': 13401, 'depositpaid': True, 'bookingdates': {'checkin': '2945-10-07', 'checkout': '0300-11-14'}}
    
    response = requests.patch(url, headers=headers, json=body)
    
    check.equal(response.status_code, 200, f'Expected status 200, got {response.status_code}')
    check.equal(response.json(), {'firstname': '', 'lastname': 'â', 'totalprice': 13401, 'depositpaid': True, 'bookingdates': {'checkin': '2945-10-07', 'checkout': '0300-11-14'}}, 'Response body mismatch')

def test_post_booking_120():
    """Test generated from Schemathesis VCR: nuYDXc
    Test: POST /booking
    Status: SUCCESS
    """
    import requests
    
    url = f"https://restful-booker.herokuapp.com/booking"
    headers = {'User-Agent': 'schemathesis/4.3.15', 'Accept-Encoding': 'gzip, deflate, zstd', 'Accept': 'application/json', 'Connection': 'keep-alive', 'Authorization': 'Basic YWRtaW46cGFzc3dvcmQxMjM=', 'Content-Type': 'application/json', 'Content-Length': '150'}
    body = {'bookingdates': {'checkin': '2945-10-07', 'checkout': '0300-11-14'}, 'depositpaid': True, 'firstname': '', 'lastname': 'â', 'totalprice': 13401}
    
    response = requests.post(url, headers=headers, json=body)
    
    check.equal(response.status_code, 200, f'Expected status 200, got {response.status_code}')
    check.equal(response.json(), {'bookingid': 1626, 'booking': {'firstname': '', 'lastname': 'â', 'totalprice': 13401, 'depositpaid': True, 'bookingdates': {'checkin': '2945-10-07', 'checkout': '0300-11-14'}}}, 'Response body mismatch')

def test_patch_booking_5_121():
    """Test generated from Schemathesis VCR: lJThAi
    Test: PATCH /booking/5%F0%A9%9C%BA%3C%C3%8B%C3%B8
    Status: SUCCESS
    """
    import requests
    
    url = f"https://restful-booker.herokuapp.com/booking/5%F0%A9%9C%BA%3C%C3%8B%C3%B8"
    headers = {'User-Agent': 'schemathesis/4.3.15', 'Accept-Encoding': 'gzip, deflate, zstd', 'Accept': 'application/json', 'Connection': 'keep-alive', 'Authorization': 'Basic YWRtaW46cGFzc3dvcmQxMjM=', 'Content-Type': 'application/json', 'Content-Length': '150'}
    body = {'firstname': '', 'lastname': 'â', 'totalprice': 13401, 'depositpaid': True, 'bookingdates': {'checkin': '2945-10-07', 'checkout': '0300-11-14'}}
    
    response = requests.patch(url, headers=headers, json=body)
    
    check.equal(response.status_code, 200, f'Expected status 200, got {response.status_code}')
    check.equal(response.json(), {'firstname': '', 'lastname': 'â', 'totalprice': 13401, 'depositpaid': True, 'bookingdates': {'checkin': '2945-10-07', 'checkout': '0300-11-14'}}, 'Response body mismatch')

def test_put_booking_248224786_122():
    """Test generated from Schemathesis VCR: ek00gT
    Test: PUT /booking/-248224786
    Status: SUCCESS
    """
    import requests
    
    url = f"https://restful-booker.herokuapp.com/booking/-248224786"
    headers = {'User-Agent': 'schemathesis/4.3.15', 'Accept-Encoding': 'gzip, deflate, zstd', 'Accept': 'application/json', 'Connection': 'keep-alive', 'Authorization': 'Basic YWRtaW46cGFzc3dvcmQxMjM=', 'Content-Type': 'application/json', 'Content-Length': '150'}
    body = {'bookingdates': {'checkin': '2945-10-07', 'checkout': '0300-11-14'}, 'depositpaid': True, 'firstname': '', 'lastname': 'â', 'totalprice': 13401}
    
    response = requests.put(url, headers=headers, json=body)
    
    check.equal(response.status_code, 405, f'Expected status 405, got {response.status_code}')
    check.is_not_none(response.text, 'Response should have body')

def test_get_booking_null_123():
    """Test generated from Schemathesis VCR: o0JRki
    Test: GET /booking/null
    Status: SUCCESS
    """
    import requests
    
    url = f"https://restful-booker.herokuapp.com/booking/null"
    headers = {'User-Agent': 'schemathesis/4.3.15', 'Accept-Encoding': 'gzip, deflate, zstd', 'Accept': 'application/json', 'Connection': 'keep-alive', 'Authorization': 'Basic YWRtaW46cGFzc3dvcmQxMjM=', 'Content-Type': 'application/json'}
    
    response = requests.get(url, headers=headers)
    
    check.equal(response.status_code, 404, f'Expected status 404, got {response.status_code}')
    check.is_not_none(response.text, 'Response should have body')

def test_post_booking_124():
    """Test generated from Schemathesis VCR: n6IKPA
    Test: POST /booking
    Status: SUCCESS
    """
    import requests
    
    url = f"https://restful-booker.herokuapp.com/booking"
    headers = {'User-Agent': 'schemathesis/4.3.15', 'Accept-Encoding': 'gzip, deflate, zstd', 'Accept': 'application/json', 'Connection': 'keep-alive', 'Authorization': 'Basic YWRtaW46cGFzc3dvcmQxMjM=', 'Content-Type': 'application/json', 'Content-Length': '2'}
    body = []
    
    response = requests.post(url, headers=headers, json=body)
    
    check.equal(response.status_code, 500, f'Expected status 500, got {response.status_code}')
    check.is_not_none(response.text, 'Response should have body')

def test_post_booking_125():
    """Test generated from Schemathesis VCR: iydqiB
    Test: POST /booking
    Status: SUCCESS
    """
    import requests
    
    url = f"https://restful-booker.herokuapp.com/booking"
    headers = {'User-Agent': 'schemathesis/4.3.15', 'Accept-Encoding': 'gzip, deflate, zstd', 'Accept': 'application/json', 'Connection': 'keep-alive', 'Authorization': 'Basic YWRtaW46cGFzc3dvcmQxMjM=', 'Content-Type': 'application/json', 'Content-Length': '329'}
    body = {'bookingdates': {'checkin': '4077-07-10', 'checkout': '2772-04-13', 'Ï\U000b9b40\U000febfb\x9dt\x97\x9e\U000687e9\U00078896u\U000dbd53\U000aaf6f&\U000ad5a1n': {}, '÷[': []}, 'depositpaid': True, 'firstname': 'ãJ\x1dß<¡Õ$\x0e', 'lastname': '9\x12Ê', 'totalprice': -28}
    
    response = requests.post(url, headers=headers, json=body)
    
    check.equal(response.status_code, 200, f'Expected status 200, got {response.status_code}')
    check.equal(response.json(), {'bookingid': 1636, 'booking': {'firstname': 'ãJ\x1dß<¡Õ$\x0e', 'lastname': '9\x12Ê', 'totalprice': -28, 'depositpaid': True, 'bookingdates': {'checkin': '4077-07-10', 'checkout': '2772-04-13'}}}, 'Response body mismatch')

def test_get_booking_18976_126():
    """Test generated from Schemathesis VCR: rAFDfj
    Test: GET /booking/18976
    Status: SUCCESS
    """
    import requests
    
    url = f"https://restful-booker.herokuapp.com/booking/18976"
    headers = {'User-Agent': 'schemathesis/4.3.15', 'Accept-Encoding': 'gzip, deflate, zstd', 'Accept': 'application/json', 'Connection': 'keep-alive', 'Authorization': 'Basic YWRtaW46cGFzc3dvcmQxMjM=', 'Content-Type': 'application/json'}
    
    response = requests.get(url, headers=headers)
    
    check.equal(response.status_code, 404, f'Expected status 404, got {response.status_code}')
    check.is_not_none(response.text, 'Response should have body')

def test_put_booking_127():
    """Test generated from Schemathesis VCR: 9Q8UPb
    Test: PUT /booking/%C2%B4
    Status: SUCCESS
    """
    import requests
    
    url = f"https://restful-booker.herokuapp.com/booking/%C2%B4"
    headers = {'User-Agent': 'schemathesis/4.3.15', 'Accept-Encoding': 'gzip, deflate, zstd', 'Accept': 'application/json', 'Connection': 'keep-alive', 'Authorization': 'Basic YWRtaW46cGFzc3dvcmQxMjM=', 'Content-Type': 'application/json', 'Content-Length': '138'}
    body = {'lastname': '9\x12Ê', 'totalprice': -28, 'depositpaid': True, 'bookingdates': {'checkin': '4077-07-10', 'checkout': '2772-04-13'}}
    
    response = requests.put(url, headers=headers, json=body)
    
    check.equal(response.status_code, 400, f'Expected status 400, got {response.status_code}')
    check.is_not_none(response.text, 'Response should have body')

def test_post_booking_128():
    """Test generated from Schemathesis VCR: wnTi79
    Test: POST /booking
    Status: SUCCESS
    """
    import requests
    
    url = f"https://restful-booker.herokuapp.com/booking"
    headers = {'User-Agent': 'schemathesis/4.3.15', 'Accept-Encoding': 'gzip, deflate, zstd', 'Accept': 'application/json', 'Connection': 'keep-alive', 'Authorization': 'Basic YWRtaW46cGFzc3dvcmQxMjM=', 'Content-Type': 'application/json', 'Content-Length': '797'}
    body = {'bookingdates': {'checkin': '4024-10-17', 'checkout': '3496-12-09', 'ØÌ\x03¿': {'ì$\U00014b7eÙÏ\U000d45a9ÞÄa\U00049de0\U0008ba16kë\x98\x80\U0006e2cb': [None, 'ð\U000b2e7c\x81', 6.481196428081767e+16], '\x19\x8cË$\U0008d689\U0008c4ab!\U000f988c': {'òÝ[\xad\x81': None, '\U000a9881\x98\U0009717e\U000c3211\U000b9063𥼜𤗥\U0001fac7\U00062a90': {'': '\x05\x9e1\x01\U00072704\tíR\U000592cb%', '\U000e7687h\x8b\U000cdc34ýÏ': True, 'Ãè\U0004c1b8¿': True}, '': None}}}, 'depositpaid': False, 'firstname': '', 'lastname': '£ð\U0006711a]µ2', 'totalprice': 300, 'additionalneeds': '¶\r\x87À\x94'}
    
    response = requests.post(url, headers=headers, json=body)
    
    check.equal(response.status_code, 200, f'Expected status 200, got {response.status_code}')
    check.equal(response.json(), {'bookingid': 1641, 'booking': {'firstname': '', 'lastname': '£ð\U0006711a]µ2', 'totalprice': 300, 'depositpaid': False, 'bookingdates': {'checkin': '4024-10-17', 'checkout': '3496-12-09'}, 'additionalneeds': '¶\r\x87À\x94'}}, 'Response body mismatch')

def test_post_booking_129():
    """Test generated from Schemathesis VCR: hiiZ52
    Test: POST /booking
    Status: SUCCESS
    """
    import requests
    
    url = f"https://restful-booker.herokuapp.com/booking"
    headers = {'User-Agent': 'schemathesis/4.3.15', 'Accept-Encoding': 'gzip, deflate, zstd', 'Accept': 'application/json', 'Connection': 'keep-alive', 'Authorization': 'Basic YWRtaW46cGFzc3dvcmQxMjM=', 'Content-Type': 'application/json', 'Content-Length': '1807'}
    body = {'bookingdates': {'checkin': '1978-09-05', 'checkout': '2596-11-24', '\x84®¹': [{}], '¿\U000afcb2': [], '$i': {}, 'f': {'\x85\U000343fd\x97\x9d*\x01\U000cbb36\x97': []}, '\U000c0f45': [{'application/json': -3.964371776147052e-19, 'Ä|²\U00058c24ü': '\U000a55be\x01øG\U0008ea52\x7fó', 'u': False}, {}, [{',./;\'[]\\-=<>?:"{}|_+!@#$%^&*()`~': -1.7976931348623157e+308, 'n\U00058aeb\x00Ó\x00\x13\x8d': -1.7976931348623157e+308, '\U0006d018ï\x05ôR𐘤': ''}, [11364], [-11096]]], '__main__': [-6784920878579878.0, [], 2.9807954333166416e+16], '\U00106580m': '\U00061a11),', 'Àc\x0c': [[], None, {'µ': [False, -6787880805253401650, ['\U001008164', '\x16ò\x92T']], '__main__': [[]]}], '¶á\U000baec5\U000b56a4z\U0005d0ea': [{'¼ï': -5.7082905980845736e+16, '\U000a7a85â\x04𰑶': None, "éF\x12o«`\x92m\x99餆\x8ex\U000ab398Å'.": 5.005192738845096e+16}, [-28526, True, True]], '\x0c\x04\U000d4a3c\r&ªW³\U0005b37aß⠦²\x1f\x11Ç±\U0006183b𮶀ø': [], 'µ!\x8f\U00086879Þ\x1c¿\U00092a55¦': [7627339795381139587, 'Ø', 'ßÑË+\x0369\U0005746e\xa0:\U00071c14\U000cdbac´'], '': 4.291081679378629e+16, '\x98': {'\x86': True}, 'j㯷': {'\U0005a835\U000904d0\x9a>Æ&': '\U000b4a05\U0003dbea&þ]ÏshÇ\U0005a4a0¤¤Oá\x8bå\x8eÂ', '\U000dfff3\U000a3087ñ\x9fq': {}}, 'h': []}, 'depositpaid': False, 'firstname': 'ü\x81ÑR§\x81¬\x86', 'lastname': '\U000915f6', 'totalprice': 95917498721051772889914156421930684195}
    
    response = requests.post(url, headers=headers, json=body)
    
    check.equal(response.status_code, 500, f'Expected status 500, got {response.status_code}')
    check.is_not_none(response.text, 'Response should have body')

def test_post_booking_130():
    """Test generated from Schemathesis VCR: aboi8U
    Test: POST /booking
    Status: SUCCESS
    """
    import requests
    
    url = f"https://restful-booker.herokuapp.com/booking"
    headers = {'User-Agent': 'schemathesis/4.3.15', 'Accept-Encoding': 'gzip, deflate, zstd', 'Accept': 'application/json', 'Connection': 'keep-alive', 'Authorization': 'Basic YWRtaW46cGFzc3dvcmQxMjM=', 'Content-Type': 'application/json', 'Content-Length': '675'}
    body = {'bookingdates': {'checkin': '8216-01-11', 'checkout': '5729-11-02', '\U000394c4\x11õéq\x82ç\x9d\U000d8175I\U000acc8b': {}, ')': {}, 'W¦|\x03 ': [None, ['\x05ð\x7fÍ¿\x07'], {'x': ['\x04\x0b\x88\U0001b6f1q5Ã\U000a0e0b'], '2½': 38, 'ÓZù³y': '\U0010aadc\U000c9f48\x83×y¯𱞞m녜\U000531a4Q\U00035d89\x88Ëø'}], '': {'\U000965cf\r\U000ac1c2\U000747e6c': 2.00001}}, 'depositpaid': False, 'firstname': 'c', 'lastname': '¤\x9e\U0008d4abÝ\U00086fdf', 'totalprice': 68, 'additionalneeds': 'f´6𗙳𝙿\x8c'}
    
    response = requests.post(url, headers=headers, json=body)
    
    check.equal(response.status_code, 200, f'Expected status 200, got {response.status_code}')
    check.equal(response.json(), {'bookingid': 1645, 'booking': {'firstname': 'c', 'lastname': '¤\x9e\U0008d4abÝ\U00086fdf', 'totalprice': 68, 'depositpaid': False, 'bookingdates': {'checkin': '8216-01-11', 'checkout': '5729-11-02'}, 'additionalneeds': 'f´6𗙳𝙿\x8c'}}, 'Response body mismatch')

def test_patch_booking_NULL_131():
    """Test generated from Schemathesis VCR: ewj5aR
    Test: PATCH /booking/NULL
    Status: SUCCESS
    """
    import requests
    
    url = f"https://restful-booker.herokuapp.com/booking/NULL"
    headers = {'User-Agent': 'schemathesis/4.3.15', 'Accept-Encoding': 'gzip, deflate, zstd', 'Accept': 'application/json', 'Connection': 'keep-alive', 'Authorization': 'Basic YWRtaW46cGFzc3dvcmQxMjM=', 'Content-Type': 'application/json', 'Content-Length': '185'}
    body = {'firstname': 'c', 'lastname': '¤\x9e\U0008d4abÝ\U00086fdf', 'totalprice': 68, 'depositpaid': False, 'bookingdates': {'checkin': '8216-01-11', 'checkout': '5729-11-02'}}
    
    response = requests.patch(url, headers=headers, json=body)
    
    check.equal(response.status_code, 405, f'Expected status 405, got {response.status_code}')
    check.is_not_none(response.text, 'Response should have body')

def test_put_booking_null_132():
    """Test generated from Schemathesis VCR: 0ZzUYm
    Test: PUT /booking/null
    Status: FAILURE
    """
    import requests
    
    url = f"https://restful-booker.herokuapp.com/booking/null"
    headers = {'User-Agent': 'schemathesis/4.3.15', 'Accept-Encoding': 'gzip, deflate, zstd', 'Accept': 'application/json', 'Connection': 'keep-alive', 'Authorization': 'Basic YWRtaW46cGFzc3dvcmQxMjM=', 'Content-Type': 'application/json', 'Content-Length': '185'}
    body = {'firstname': 'c', 'lastname': '¤\x9e\U0008d4abÝ\U00086fdf', 'totalprice': 68, 'depositpaid': False, 'bookingdates': {'checkin': '8216-01-11', 'checkout': '5729-11-02'}}
    
    response = requests.put(url, headers=headers, json=body)
    
    check.equal(response.status_code, 405, f'Expected status 405, got {response.status_code}')
    # Original failed checks: negative_data_rejection

def test_post_booking_133():
    """Test generated from Schemathesis VCR: cg8tKL
    Test: POST /booking
    Status: SUCCESS
    """
    import requests
    
    url = f"https://restful-booker.herokuapp.com/booking"
    headers = {'User-Agent': 'schemathesis/4.3.15', 'Accept-Encoding': 'gzip, deflate, zstd', 'Accept': 'application/json', 'Connection': 'keep-alive', 'Authorization': 'Basic YWRtaW46cGFzc3dvcmQxMjM=', 'Content-Type': 'application/json', 'Content-Length': '675'}
    body = {'bookingdates': {'checkin': '8216-01-11', 'checkout': '5729-11-02', '\U000394c4\x11õéq\x82ç\x9d\U000d8175I\U000acc8b': {}, ')': {}, 'W¦|\x03 ': [None, ['\x05ð\x7fÍ¿\x07'], {'x': ['\x04\x0b\x88\U0001b6f1q5Ã\U000a0e0b'], '2½': 38, 'ÓZù³y': '\U0010aadc\U000c9f48\x83×y¯𱞞m녜\U000531a4Q\U00035d89\x88Ëø'}], '': {'\U000965cf\r\U000ac1c2\U000747e6c': 2.00001}}, 'depositpaid': False, 'firstname': 'c', 'lastname': '¤\x9e\U0008d4abÝ\U00086fdf', 'totalprice': 68, 'additionalneeds': 'f´6𗙳𝙿\x8c'}
    
    response = requests.post(url, headers=headers, json=body)
    
    check.equal(response.status_code, 200, f'Expected status 200, got {response.status_code}')
    check.equal(response.json(), {'bookingid': 1655, 'booking': {'firstname': 'c', 'lastname': '¤\x9e\U0008d4abÝ\U00086fdf', 'totalprice': 68, 'depositpaid': False, 'bookingdates': {'checkin': '8216-01-11', 'checkout': '5729-11-02'}, 'additionalneeds': 'f´6𗙳𝙿\x8c'}}, 'Response body mismatch')

def test_patch_booking_NULL_134():
    """Test generated from Schemathesis VCR: VPUyaC
    Test: PATCH /booking/NULL
    Status: SUCCESS
    """
    import requests
    
    url = f"https://restful-booker.herokuapp.com/booking/NULL"
    headers = {'User-Agent': 'schemathesis/4.3.15', 'Accept-Encoding': 'gzip, deflate, zstd', 'Accept': 'application/json', 'Connection': 'keep-alive', 'Authorization': 'Basic YWRtaW46cGFzc3dvcmQxMjM=', 'Content-Type': 'application/json', 'Content-Length': '185'}
    body = {'firstname': 'c', 'lastname': '¤\x9e\U0008d4abÝ\U00086fdf', 'totalprice': 68, 'depositpaid': False, 'bookingdates': {'checkin': '8216-01-11', 'checkout': '5729-11-02'}}
    
    response = requests.patch(url, headers=headers, json=body)
    
    check.equal(response.status_code, 405, f'Expected status 405, got {response.status_code}')
    check.is_not_none(response.text, 'Response should have body')

def test_put_booking_null_135():
    """Test generated from Schemathesis VCR: AUjBEI
    Test: PUT /booking/null
    Status: SUCCESS
    """
    import requests
    
    url = f"https://restful-booker.herokuapp.com/booking/null"
    headers = {'User-Agent': 'schemathesis/4.3.15', 'Accept-Encoding': 'gzip, deflate, zstd', 'Accept': 'application/json', 'Connection': 'keep-alive', 'Authorization': 'Basic YWRtaW46cGFzc3dvcmQxMjM=', 'Content-Type': 'application/json', 'Content-Length': '185'}
    body = {'firstname': 'c', 'lastname': '¤\x9e\U0008d4abÝ\U00086fdf', 'totalprice': 68, 'depositpaid': False, 'bookingdates': {'checkin': '8216-01-11', 'checkout': '5729-11-02'}}
    
    response = requests.put(url, headers=headers, json=body)
    
    check.equal(response.status_code, 405, f'Expected status 405, got {response.status_code}')
    check.is_not_none(response.text, 'Response should have body')

def test_put_booking_26905_136():
    """Test generated from Schemathesis VCR: pHANTO
    Test: PUT /booking/-26905
    Status: SUCCESS
    """
    import requests
    
    url = f"https://restful-booker.herokuapp.com/booking/-26905"
    headers = {'User-Agent': 'schemathesis/4.3.15', 'Accept-Encoding': 'gzip, deflate, zstd', 'Accept': 'application/json', 'Connection': 'keep-alive', 'Authorization': 'Basic YWRtaW46cGFzc3dvcmQxMjM=', 'Content-Type': 'application/json', 'Content-Length': '242'}
    body = {'bookingdates': {'checkin': '8216-01-11', 'checkout': '5729-11-02'}, 'depositpaid': False, 'firstname': 'c', 'lastname': '¤\x9e\U0008d4abÝ\U00086fdf', 'totalprice': 68, ',D\x14': {'\x93=WýÐ\U000e2c22': [-62]}}
    
    response = requests.put(url, headers=headers, json=body)
    
    check.equal(response.status_code, 405, f'Expected status 405, got {response.status_code}')
    check.is_not_none(response.text, 'Response should have body')

def test_post_booking_137():
    """Test generated from Schemathesis VCR: 3cF5TN
    Test: POST /booking
    Status: SUCCESS
    """
    import requests
    
    url = f"https://restful-booker.herokuapp.com/booking"
    headers = {'User-Agent': 'schemathesis/4.3.15', 'Accept-Encoding': 'gzip, deflate, zstd', 'Accept': 'application/json', 'Connection': 'keep-alive', 'Authorization': 'Basic YWRtaW46cGFzc3dvcmQxMjM=', 'Content-Type': 'application/json', 'Content-Length': '1625'}
    body = {'bookingdates': {'checkin': '0791-08-22', 'checkout': '9740-10-17', 'Z\U000b2eba': {'\x82': {'': False, 'Content-Type': True}}, '\x83¿\x97¶çl)': {'s¿\U000e5d97\x18\x86gTÎí\U000be1acu': [['\x0f', [True, 5.485194162894198e-202, -14132], {'«\U000873cc': [None, 24718, True]}]]}, 'm': {'\x06¢': {'0%å\x1f=': 4519, '\U00067345WÉêæf': 300, '': 26345}}, '@Ð#ÆL\x99\x8a£/¢\x15s\U00103d8b«': {'': {'\U000eaff0Ò\x07': -9.660522797894396e+248, '': None}}, '½': [[], None, []], '\x943\U0010ab92\U0006d722À®𥷧\U000400da\x89\U000575b3\U00097192Ý¤\x89\U000359b8Úð\U000de895H\x08': '\x0b', '\U000f8944\x07': {'🙠': [], '{öÌ': {}, '': [None, None]}, '': [[], [['Þ2\r\x08ZÆ', 6.795986535115418e+16, -14416], [None, None]], {'\U00092ab9\U000955ddÄO\U00108c0b\t\x7füj\U0010d186\U000c0492\U000eede5øï': ['µ\U000569de', -109, 86]}], '²': [True]}, 'depositpaid': False, 'firstname': '7\x7f𦲬Åh', 'lastname': '¿\U000d75a0', 'totalprice': -4450, '': [], 'r': {'': [['\x92®O', '\U0010c64a²', False], ['Ï\U00100789', [], None], {',𮇹\x06\x0e\x82\x1b': -4.6184906996751773e+67, '\U000f5d33>\x85/«D\U000b36f3': ['c\x9dC\x17tè', 79]}], 'w\U0005f12f𤐤¹Z\x1c³\x1c': [{'V': 'Ô\x90´'}, [-3.122364834036655e+16], True], 'â': [None]}, 'additionalneeds': '®'}
    
    response = requests.post(url, headers=headers, json=body)
    
    check.equal(response.status_code, 200, f'Expected status 200, got {response.status_code}')
    check.equal(response.json(), {'bookingid': 1661, 'booking': {'firstname': '7\x7f𦲬Åh', 'lastname': '¿\U000d75a0', 'totalprice': -4450, 'depositpaid': False, 'bookingdates': {'checkin': '0791-08-22', 'checkout': '9740-10-17'}, 'additionalneeds': '®'}}, 'Response body mismatch')

def test_patch_booking_y_138():
    """Test generated from Schemathesis VCR: LJPIJA
    Test: PATCH /booking/%26y%11%5B%C2%AD
    Status: SUCCESS
    """
    import requests
    
    url = f"https://restful-booker.herokuapp.com/booking/%26y%11%5B%C2%AD"
    headers = {'User-Agent': 'schemathesis/4.3.15', 'Accept-Encoding': 'gzip, deflate, zstd', 'Accept': 'application/json', 'Connection': 'keep-alive', 'Authorization': 'Basic YWRtaW46cGFzc3dvcmQxMjM=', 'Content-Type': 'application/json', 'Content-Length': '167'}
    body = {'firstname': '7\x7f𦲬Åh', 'lastname': '¿\U000d75a0', 'totalprice': -4450, 'bookingdates': {'checkin': '0791-08-22', 'checkout': '9740-10-17'}}
    
    response = requests.patch(url, headers=headers, json=body)
    
    check.equal(response.status_code, 405, f'Expected status 405, got {response.status_code}')
    check.is_not_none(response.text, 'Response should have body')

def test_post_booking_139():
    """Test generated from Schemathesis VCR: FzQX96
    Test: POST /booking
    Status: SUCCESS
    """
    import requests
    
    url = f"https://restful-booker.herokuapp.com/booking"
    headers = {'User-Agent': 'schemathesis/4.3.15', 'Accept-Encoding': 'gzip, deflate, zstd', 'Accept': 'application/json', 'Connection': 'keep-alive', 'Authorization': 'Basic YWRtaW46cGFzc3dvcmQxMjM=', 'Content-Type': 'application/json', 'Content-Length': '2'}
    body = []
    
    response = requests.post(url, headers=headers, json=body)
    
    check.equal(response.status_code, 500, f'Expected status 500, got {response.status_code}')
    check.is_not_none(response.text, 'Response should have body')

def test_post_booking_140():
    """Test generated from Schemathesis VCR: 9mGK7h
    Test: POST /booking
    Status: SUCCESS
    """
    import requests
    
    url = f"https://restful-booker.herokuapp.com/booking"
    headers = {'User-Agent': 'schemathesis/4.3.15', 'Accept-Encoding': 'gzip, deflate, zstd', 'Accept': 'application/json', 'Connection': 'keep-alive', 'Authorization': 'Basic YWRtaW46cGFzc3dvcmQxMjM=', 'Content-Type': 'application/json', 'Content-Length': '674'}
    body = {'bookingdates': {'checkin': '1730-01-08', 'checkout': '9678-04-10'}, 'depositpaid': True, 'firstname': '\x14\U0010e4071\U0009afc4\x94\x04\x9a½A\U00069714', 'lastname': '\x13\U000c1a19\x9ef\U0009085cÑ%å', 'totalprice': 52, 'å': {'application/json': {'\U00047bd4+𠂪÷c\U000f62d7Ù': [], '«\x1d': [-31, 43781811], 'Oy': {'\x92\ue419\t\x12\x95\x05-\x18G\x87': '\x11tí_6Á4£sº', '**𥦦\U000938a9': 29289, '\U000f9972?»Ix\n[4\U000d39b6\U000e89fa': 1189425965}}, '': [], '\x07Â÷²|\U000b549aÏ`C': []}, 'additionalneeds': 'H\x80'}
    
    response = requests.post(url, headers=headers, json=body)
    
    check.equal(response.status_code, 200, f'Expected status 200, got {response.status_code}')
    check.equal(response.json(), {'bookingid': 1664, 'booking': {'firstname': '\x14\U0010e4071\U0009afc4\x94\x04\x9a½A\U00069714', 'lastname': '\x13\U000c1a19\x9ef\U0009085cÑ%å', 'totalprice': 52, 'depositpaid': True, 'bookingdates': {'checkin': '1730-01-08', 'checkout': '9678-04-10'}, 'additionalneeds': 'H\x80'}}, 'Response body mismatch')

def test_delete_booking_81_141():
    """Test generated from Schemathesis VCR: IF8aQk
    Test: DELETE /booking/81
    Status: SUCCESS
    """
    import requests
    
    url = f"https://restful-booker.herokuapp.com/booking/81"
    headers = {'User-Agent': 'schemathesis/4.3.15', 'Accept-Encoding': 'gzip, deflate, zstd', 'Accept': 'application/json', 'Connection': 'keep-alive', 'Authorization': 'Basic YWRtaW46cGFzc3dvcmQxMjM=', 'Content-Type': 'application/json', 'Content-Length': '0'}
    
    response = requests.delete(url, headers=headers)
    
    check.equal(response.status_code, 201, f'Expected status 201, got {response.status_code}')
    check.is_not_none(response.text, 'Response should have body')

def test_get_booking_72_142():
    """Test generated from Schemathesis VCR: RKcSuk
    Test: GET /booking/72
    Status: SUCCESS
    """
    import requests
    
    url = f"https://restful-booker.herokuapp.com/booking/72"
    headers = {'User-Agent': 'schemathesis/4.3.15', 'Accept-Encoding': 'gzip, deflate, zstd', 'Accept': 'application/json', 'Connection': 'keep-alive', 'Authorization': 'Basic YWRtaW46cGFzc3dvcmQxMjM=', 'Content-Type': 'application/json'}
    
    response = requests.get(url, headers=headers)
    
    check.equal(response.status_code, 200, f'Expected status 200, got {response.status_code}')
    check.equal(response.json(), {'firstname': 'John', 'lastname': 'Smith', 'totalprice': 111, 'depositpaid': True, 'bookingdates': {'checkin': '2018-01-01', 'checkout': '2019-01-01'}, 'additionalneeds': 'Breakfast'}, 'Response body mismatch')

def test_get_booking_143():
    """Test generated from Schemathesis VCR: gMP44J
    Test: GET /booking/%F0%99%A8%AB%C3%9B%C3%92%F3%86%9B%AE%C2%A8
    Status: SUCCESS
    """
    import requests
    
    url = f"https://restful-booker.herokuapp.com/booking/%F0%99%A8%AB%C3%9B%C3%92%F3%86%9B%AE%C2%A8"
    headers = {'User-Agent': 'schemathesis/4.3.15', 'Accept-Encoding': 'gzip, deflate, zstd', 'Accept': 'application/json', 'Connection': 'keep-alive', 'Authorization': 'Basic YWRtaW46cGFzc3dvcmQxMjM=', 'Content-Type': 'application/json'}
    
    response = requests.get(url, headers=headers)
    
    check.equal(response.status_code, 404, f'Expected status 404, got {response.status_code}')
    check.is_not_none(response.text, 'Response should have body')

def test_delete_booking_144():
    """Test generated from Schemathesis VCR: zQ6QJo
    Test: DELETE /booking/%C2%BD
    Status: SUCCESS
    """
    import requests
    
    url = f"https://restful-booker.herokuapp.com/booking/%C2%BD"
    headers = {'User-Agent': 'schemathesis/4.3.15', 'Accept-Encoding': 'gzip, deflate, zstd', 'Accept': 'application/json', 'Connection': 'keep-alive', 'Authorization': 'Basic YWRtaW46cGFzc3dvcmQxMjM=', 'Content-Type': 'application/json', 'Content-Length': '0'}
    
    response = requests.delete(url, headers=headers)
    
    check.equal(response.status_code, 405, f'Expected status 405, got {response.status_code}')
    check.is_not_none(response.text, 'Response should have body')

def test_patch_booking_14870_145():
    """Test generated from Schemathesis VCR: Mjee3j
    Test: PATCH /booking/-14870
    Status: SUCCESS
    """
    import requests
    
    url = f"https://restful-booker.herokuapp.com/booking/-14870"
    headers = {'User-Agent': 'schemathesis/4.3.15', 'Accept-Encoding': 'gzip, deflate, zstd', 'Accept': 'application/json', 'Connection': 'keep-alive', 'Authorization': 'Basic YWRtaW46cGFzc3dvcmQxMjM=', 'Content-Type': 'application/json', 'Content-Length': '1074'}
    body = {'bookingdates': {'checkin': '6157-09-10', 'checkout': '7103-09-02', '': {'Ä': [True]}, '%"\x87Ç\U000b6608\U000922d4tc;': {'J\x97qì¾\x17\x94\x84\x0e\x813ü«\x9c,': True, '{ì\x1e': []}, '\U000d1485\U000dca87<ò\U000669dduõ\U000e684d\U000ea860\x99!à': 16828}, 'depositpaid': True, 'firstname': '\x03\x19`', 'lastname': '>ìíÜ|öZ𑣙©\U00050e82', 'totalprice': -8741, '9æ+Õ': [[[]], [-3.668617174026275e+16, False, 2064019328], {'\U000a61d9b': {}, '𫡕\U0007a428\U0007ee1fµD´': [[2067892000, '¿Ã𣸔H\x94츣𐂂\U00109831\U0005dd63%\U000d4ec7·²&'], {'³': 'ñ\U000b2648', 'ÁK': 1.9338488218509706e-115, 'FÞG\U000eda24\x80': False}, {'4ñ': True, '': -4.580607696759234e+16, "f'¢\xad³\x01": False}], '-\x07Ý\U000e8abb\U000dbb24Ç': [{'D\x12': '\x11Ù', 'Content-Type': True, 'True': -1.568224842317171e+16}]}]}
    
    response = requests.patch(url, headers=headers, json=body)
    
    check.equal(response.status_code, 405, f'Expected status 405, got {response.status_code}')
    check.is_not_none(response.text, 'Response should have body')

def test_post_booking_146():
    """Test generated from Schemathesis VCR: LecoPx
    Test: POST /booking
    Status: SUCCESS
    """
    import requests
    
    url = f"https://restful-booker.herokuapp.com/booking"
    headers = {'User-Agent': 'schemathesis/4.3.15', 'Accept-Encoding': 'gzip, deflate, zstd', 'Accept': 'application/json', 'Connection': 'keep-alive', 'Authorization': 'Basic YWRtaW46cGFzc3dvcmQxMjM=', 'Content-Type': 'application/json', 'Content-Length': '220'}
    body = {'bookingdates': {'checkin': '0489-10-06', 'checkout': '8592-05-25', '\x92\x01]': True}, 'depositpaid': False, 'firstname': '\U000fc1ad', 'lastname': 'nj\U000aa0f2³ËE\x8atº', 'totalprice': -5501}
    
    response = requests.post(url, headers=headers, json=body)
    
    check.equal(response.status_code, 200, f'Expected status 200, got {response.status_code}')
    check.equal(response.json(), {'bookingid': 1676, 'booking': {'firstname': '\U000fc1ad', 'lastname': 'nj\U000aa0f2³ËE\x8atº', 'totalprice': -5501, 'depositpaid': False, 'bookingdates': {'checkin': '0489-10-06', 'checkout': '8592-05-25'}}}, 'Response body mismatch')

def test_get_booking_r_147():
    """Test generated from Schemathesis VCR: drijDJ
    Test: GET /booking/%C2%84%C2%84%F0%93%82%B0r%C2%AE%C2%80%16%F0%B9%8B%8D
    Status: SUCCESS
    """
    import requests
    
    url = f"https://restful-booker.herokuapp.com/booking/%C2%84%C2%84%F0%93%82%B0r%C2%AE%C2%80%16%F0%B9%8B%8D"
    headers = {'User-Agent': 'schemathesis/4.3.15', 'Accept-Encoding': 'gzip, deflate, zstd', 'Accept': 'application/json', 'Connection': 'keep-alive', 'Authorization': 'Basic YWRtaW46cGFzc3dvcmQxMjM=', 'Content-Type': 'application/json'}
    
    response = requests.get(url, headers=headers)
    
    check.equal(response.status_code, 404, f'Expected status 404, got {response.status_code}')
    check.is_not_none(response.text, 'Response should have body')

def test_get_booking_13333_148():
    """Test generated from Schemathesis VCR: r6cq16
    Test: GET /booking/-13333
    Status: SUCCESS
    """
    import requests
    
    url = f"https://restful-booker.herokuapp.com/booking/-13333"
    headers = {'User-Agent': 'schemathesis/4.3.15', 'Accept-Encoding': 'gzip, deflate, zstd', 'Accept': 'application/json', 'Connection': 'keep-alive', 'Authorization': 'Basic YWRtaW46cGFzc3dvcmQxMjM=', 'Content-Type': 'application/json'}
    
    response = requests.get(url, headers=headers)
    
    check.equal(response.status_code, 404, f'Expected status 404, got {response.status_code}')
    check.is_not_none(response.text, 'Response should have body')

def test_post_booking_149():
    """Test generated from Schemathesis VCR: kXrdSM
    Test: POST /booking
    Status: SUCCESS
    """
    import requests
    
    url = f"https://restful-booker.herokuapp.com/booking"
    headers = {'User-Agent': 'schemathesis/4.3.15', 'Accept-Encoding': 'gzip, deflate, zstd', 'Accept': 'application/json', 'Connection': 'keep-alive', 'Authorization': 'Basic YWRtaW46cGFzc3dvcmQxMjM=', 'Content-Type': 'application/json', 'Content-Length': '402'}
    body = {'bookingdates': {'checkin': '1703-03-17', 'checkout': '2119-10-29', '\x01w¿;l\x83ó': [{'\x14¬': ['Ï', True, False], '': [], 'BwE\x8aÖ©': None}], '': {'z?': ')[ó\x15t-Üó', '\x95': 2.802429303167867e+214, 'Authorization': '6'}}, 'depositpaid': False, 'firstname': '\U00048c32£\U000195b3]', 'lastname': 'å\x87', 'totalprice': -108}
    
    response = requests.post(url, headers=headers, json=body)
    
    check.equal(response.status_code, 200, f'Expected status 200, got {response.status_code}')
    check.equal(response.json(), {'bookingid': 1680, 'booking': {'firstname': '\U00048c32£\U000195b3]', 'lastname': 'å\x87', 'totalprice': -108, 'depositpaid': False, 'bookingdates': {'checkin': '1703-03-17', 'checkout': '2119-10-29'}}}, 'Response body mismatch')

def test_post_booking_150():
    """Test generated from Schemathesis VCR: FWwSdg
    Test: POST /booking
    Status: SUCCESS
    """
    import requests
    
    url = f"https://restful-booker.herokuapp.com/booking"
    headers = {'User-Agent': 'schemathesis/4.3.15', 'Accept-Encoding': 'gzip, deflate, zstd', 'Accept': 'application/json', 'Connection': 'keep-alive', 'Authorization': 'Basic YWRtaW46cGFzc3dvcmQxMjM=', 'Content-Type': 'application/json', 'Content-Length': '5'}
    body = 30041
    
    response = requests.post(url, headers=headers, json=body)
    
    check.equal(response.status_code, 400, f'Expected status 400, got {response.status_code}')
    check.is_not_none(response.text, 'Response should have body')

def test_patch_booking_true_151():
    """Test generated from Schemathesis VCR: LKGL2k
    Test: PATCH /booking/true
    Status: SUCCESS
    """
    import requests
    
    url = f"https://restful-booker.herokuapp.com/booking/true"
    headers = {'User-Agent': 'schemathesis/4.3.15', 'Accept-Encoding': 'gzip, deflate, zstd', 'Accept': 'application/json', 'Connection': 'keep-alive', 'Authorization': 'Basic YWRtaW46cGFzc3dvcmQxMjM=', 'Content-Type': 'application/json', 'Content-Length': '96'}
    body = {'firstname': '\U00048c32£\U000195b3]', 'lastname': 'å\x87', 'totalprice': -108}
    
    response = requests.patch(url, headers=headers, json=body)
    
    check.equal(response.status_code, 405, f'Expected status 405, got {response.status_code}')
    check.is_not_none(response.text, 'Response should have body')

def test_delete_booking_78_152():
    """Test generated from Schemathesis VCR: yzOQE1
    Test: DELETE /booking/78
    Status: SUCCESS
    """
    import requests
    
    url = f"https://restful-booker.herokuapp.com/booking/78"
    headers = {'User-Agent': 'schemathesis/4.3.15', 'Accept-Encoding': 'gzip, deflate, zstd', 'Accept': 'application/json', 'Connection': 'keep-alive', 'Authorization': 'Basic YWRtaW46cGFzc3dvcmQxMjM=', 'Content-Type': 'application/json', 'Content-Length': '0'}
    
    response = requests.delete(url, headers=headers)
    
    check.equal(response.status_code, 405, f'Expected status 405, got {response.status_code}')
    check.is_not_none(response.text, 'Response should have body')

def test_get_booking_153():
    """Test generated from Schemathesis VCR: 1g8Bww
    Test: GET /booking/%04%C2%B3%F1%B0%BB%9A%F0%96%96%AD
    Status: SUCCESS
    """
    import requests
    
    url = f"https://restful-booker.herokuapp.com/booking/%04%C2%B3%F1%B0%BB%9A%F0%96%96%AD"
    headers = {'User-Agent': 'schemathesis/4.3.15', 'Accept-Encoding': 'gzip, deflate, zstd', 'Accept': 'application/json', 'Connection': 'keep-alive', 'Authorization': 'Basic YWRtaW46cGFzc3dvcmQxMjM=', 'Content-Type': 'application/json'}
    
    response = requests.get(url, headers=headers)
    
    check.equal(response.status_code, 404, f'Expected status 404, got {response.status_code}')
    check.is_not_none(response.text, 'Response should have body')

def test_put_booking_null_154():
    """Test generated from Schemathesis VCR: QbmqF4
    Test: PUT /booking/null
    Status: SUCCESS
    """
    import requests
    
    url = f"https://restful-booker.herokuapp.com/booking/null"
    headers = {'User-Agent': 'schemathesis/4.3.15', 'Accept-Encoding': 'gzip, deflate, zstd', 'Accept': 'application/json', 'Connection': 'keep-alive', 'Authorization': 'Basic YWRtaW46cGFzc3dvcmQxMjM=', 'Content-Type': 'application/json', 'Content-Length': '167'}
    body = {'firstname': '\U00048c32£\U000195b3]', 'lastname': 'å\x87', 'depositpaid': False, 'bookingdates': {'checkin': '1703-03-17', 'checkout': '2119-10-29'}}
    
    response = requests.put(url, headers=headers, json=body)
    
    check.equal(response.status_code, 400, f'Expected status 400, got {response.status_code}')
    check.is_not_none(response.text, 'Response should have body')

def test_post_booking_155():
    """Test generated from Schemathesis VCR: TNGsGa
    Test: POST /booking
    Status: SUCCESS
    """
    import requests
    
    url = f"https://restful-booker.herokuapp.com/booking"
    headers = {'User-Agent': 'schemathesis/4.3.15', 'Accept-Encoding': 'gzip, deflate, zstd', 'Accept': 'application/json', 'Connection': 'keep-alive', 'Authorization': 'Basic YWRtaW46cGFzc3dvcmQxMjM=', 'Content-Type': 'application/json', 'Content-Length': '1735'}
    body = {'bookingdates': {'checkin': '1400-12-13', 'checkout': '3987-02-21', 'Accept': {'À/2\U0007df21¡\x17': {'>6h¦\U000c9f23\x86\U000fc172ïD': [], '': [7.169944406253046e+47, 'Content-Type'], '\x1c': ''}, '\x83\U000d5d9e': {}}, '': [], '´\x87©|\x948\x1e\x86': {'': False, 'Y': None, '𪬳': None}, 'NULL': {}, '\x9a\U0005dda3iÔð\x1f\x93Y£¢\x90ý\x8e?': [False], '0..0': [], '`\U0004b9fb\x06\U000c1671\U0009ea3b': {'\x8c*×\x9b': {'À': '\x9a\x80\x97sÎ5(\U0006735e\x0f', '\x05¨~\x97õ\x93': None, 'ßÞëÜ붧·': "\x9c%'³\x9c"}, 'aº': []}, 'y\x8b£\xad\U000d31b7\x04\U000b5f8b\x81¾\x8bá×': {'\x05\U0009e348': [], 'Ჰ': False, '\x10\U0010f855\U000b09e3': [1.0991198446242456e+249]}, 'ãoø«\U000b2aac2\x8dB_ù': {'': {'Cz': {'zj': {'§': 5415912906728029.0, '\U000f5e6b': 3862}, '\x94': -6955, 'Authorization': False}, '': '\U0007c525', '|0á𓜧\r': {'\x12Ö': '§'}}, 'Authorization': {'': {'q\U000e331bKB\x06×\U00103b59>©': 1.0118514519640176e-244, '½<RX\U0005dfeb\x81\U000e27c9': 98637170253960450785360640315138850059, '\x95\x93#\U000fd74f': 61}, '\U0002f240\x12': [], 'ç': [False, 6.507936258134888e+16]}, 'ØC\x82p\x8f\x99': False}, '\r': [-2.7145268756135932e+16, -1786, -9.174976602212127e+34], '\U000b4454': []}, 'depositpaid': False, 'firstname': '', 'lastname': '?\U00103608E\U0004dca0\x0fÊÒsðm\x1aö', 'totalprice': -4235, '\U000a2129¤ýp\x99': None}
    
    response = requests.post(url, headers=headers, json=body)
    
    check.equal(response.status_code, 500, f'Expected status 500, got {response.status_code}')
    check.is_not_none(response.text, 'Response should have body')

def test_post_booking_156():
    """Test generated from Schemathesis VCR: KsQgwM
    Test: POST /booking
    Status: SUCCESS
    """
    import requests
    
    url = f"https://restful-booker.herokuapp.com/booking"
    headers = {'User-Agent': 'schemathesis/4.3.15', 'Accept-Encoding': 'gzip, deflate, zstd', 'Accept': 'application/json', 'Connection': 'keep-alive', 'Authorization': 'Basic YWRtaW46cGFzc3dvcmQxMjM=', 'Content-Type': 'application/json', 'Content-Length': '916'}
    body = {'bookingdates': {'checkin': '5140-08-15', 'checkout': '8651-08-16', 'æ}È\x99¸\U0010e8b0\U0008e702': [], 'PýB\x90\x1a\x19': [False, [None], {}], '\U000b25e8\U00091641ó': {}, 's;S\x93\U00010261¤\U00107d4a\x17\U000fcbedñrFP': {'\x9e\x86J𗗴Q': None, '0u𒆲Cwxu¸Aóª%\x91\x1b\x9b¸\x1f\x13': [{'¨\x12\U000e985b#½\x12': -2.00001, '\U000ca02a*': -6.751943287103031e-09, '\x7f\x96µ\x1d!': 13}], '': '\x1e'}, 'ö\U0005c551D\U000bab9a𝒌·\x06ù\x9b㎀{𤭾\U0001e1f7\U000910f7': {'â': True, '-Infinity': 'D\U00100c46M¿Æ\x10\U0009c970', '': None}}, 'depositpaid': False, 'firstname': ']\U001043fa\U000c62f0\x1e\U0009340bìÉ\U000891eeñú\x96à', 'lastname': 'c', 'totalprice': -23645}
    
    response = requests.post(url, headers=headers, json=body)
    
    check.equal(response.status_code, 200, f'Expected status 200, got {response.status_code}')
    check.equal(response.json(), {'bookingid': 1690, 'booking': {'firstname': ']\U001043fa\U000c62f0\x1e\U0009340bìÉ\U000891eeñú\x96à', 'lastname': 'c', 'totalprice': -23645, 'depositpaid': False, 'bookingdates': {'checkin': '5140-08-15', 'checkout': '8651-08-16'}}}, 'Response body mismatch')

def test_get_booking_69_157():
    """Test generated from Schemathesis VCR: z1eVfK
    Test: GET /booking/69
    Status: SUCCESS
    """
    import requests
    
    url = f"https://restful-booker.herokuapp.com/booking/69"
    headers = {'User-Agent': 'schemathesis/4.3.15', 'Accept-Encoding': 'gzip, deflate, zstd', 'Accept': 'application/json', 'Connection': 'keep-alive', 'Authorization': 'Basic YWRtaW46cGFzc3dvcmQxMjM=', 'Content-Type': 'application/json'}
    
    response = requests.get(url, headers=headers)
    
    check.equal(response.status_code, 404, f'Expected status 404, got {response.status_code}')
    check.is_not_none(response.text, 'Response should have body')

def test_get_booking_158():
    """Test generated from Schemathesis VCR: yuTpK2
    Test: GET /booking/%23%C3%93
    Status: SUCCESS
    """
    import requests
    
    url = f"https://restful-booker.herokuapp.com/booking/%23%C3%93"
    headers = {'User-Agent': 'schemathesis/4.3.15', 'Accept-Encoding': 'gzip, deflate, zstd', 'Accept': 'application/json', 'Connection': 'keep-alive', 'Authorization': 'Basic YWRtaW46cGFzc3dvcmQxMjM=', 'Content-Type': 'application/json'}
    
    response = requests.get(url, headers=headers)
    
    check.equal(response.status_code, 404, f'Expected status 404, got {response.status_code}')
    check.is_not_none(response.text, 'Response should have body')

def test_post_booking_159():
    """Test generated from Schemathesis VCR: OIunIa
    Test: POST /booking
    Status: SUCCESS
    """
    import requests
    
    url = f"https://restful-booker.herokuapp.com/booking"
    headers = {'User-Agent': 'schemathesis/4.3.15', 'Accept-Encoding': 'gzip, deflate, zstd', 'Accept': 'application/json', 'Connection': 'keep-alive', 'Authorization': 'Basic YWRtaW46cGFzc3dvcmQxMjM=', 'Content-Type': 'application/json', 'Content-Length': '1321'}
    body = {'bookingdates': {'checkin': '4003-02-04', 'checkout': '1959-09-23'}, 'depositpaid': False, 'firstname': '¢èz', 'lastname': '1', 'totalprice': -10976, ']\U000c988b\U000cc1f1\U0004975cF"𪭙¬\U000f7c19': {'': {'áÉ¨\x03¥W': {'F@E\U000a4921Ï_\x1f\xa0bÚú': 'Ä'}, '¶\x90\U00045c39Ô\U000e7965£F\x93\U000b41e1\U000aabbc\tL': {'\x12\U00086775×\x05\x8a\U000cefbd\U0007a128': '\x11³\U000af360`\uedbf\U00033648¸/ä', '\x03~N²»\U000becd5\x17\x07I': -22440, '': '\x96Íðåï\U00052f6d'}}, '<\U00082328\U0008e7c6àûEE\x93_\U000fa982': [], '\U00083845sÍý`': [[]]}, '': {'±©Ú#\U0009ee94': -4.819542170290848e+43, '': -60, '\x98¡¡': True}, 'additionalneeds': 'û𬟂\x83\U0001980cñ\x8d\x98¶\x01', '#=,ûâ\x06õ!ù%EØp𡿰è\x1c°}´\x11½': {'\U000a00faÖ\t': True, '': -1.7976931348623157e+308, 'FALSE': 21969}, 'Þ\U0006b1ee': {'°\x01<\x0f£¶7=æ\U0001c1a1\U000ca500¶': {'\U00060a1f': 'S', 'û': None, '\x18¶?õ\U0007e0e3': 6.764664716387419e-109}}}
    
    response = requests.post(url, headers=headers, json=body)
    
    check.equal(response.status_code, 200, f'Expected status 200, got {response.status_code}')
    check.equal(response.json(), {'bookingid': 1694, 'booking': {'firstname': '¢èz', 'lastname': '1', 'totalprice': -10976, 'depositpaid': False, 'bookingdates': {'checkin': '4003-02-04', 'checkout': '1959-09-23'}, 'additionalneeds': 'û𬟂\x83\U0001980cñ\x8d\x98¶\x01'}}, 'Response body mismatch')

def test_post_booking_160():
    """Test generated from Schemathesis VCR: hOJvvr
    Test: POST /booking
    Status: SUCCESS
    """
    import requests
    
    url = f"https://restful-booker.herokuapp.com/booking"
    headers = {'User-Agent': 'schemathesis/4.3.15', 'Accept-Encoding': 'gzip, deflate, zstd', 'Accept': 'application/json', 'Connection': 'keep-alive', 'Authorization': 'Basic YWRtaW46cGFzc3dvcmQxMjM=', 'Content-Type': 'application/json', 'Content-Length': '169'}
    body = {'bookingdates': {'checkin': '1950-06-20', 'checkout': '7838-01-16'}, 'depositpaid': True, 'firstname': '\x9e', 'lastname': '\U000b6d72V?', 'totalprice': -214988369}
    
    response = requests.post(url, headers=headers, json=body)
    
    check.equal(response.status_code, 200, f'Expected status 200, got {response.status_code}')
    check.equal(response.json(), {'bookingid': 1695, 'booking': {'firstname': '\x9e', 'lastname': '\U000b6d72V?', 'totalprice': -214988369, 'depositpaid': True, 'bookingdates': {'checkin': '1950-06-20', 'checkout': '7838-01-16'}}}, 'Response body mismatch')

def test_post_booking_161():
    """Test generated from Schemathesis VCR: wRNfXM
    Test: POST /booking
    Status: SUCCESS
    """
    import requests
    
    url = f"https://restful-booker.herokuapp.com/booking"
    headers = {'User-Agent': 'schemathesis/4.3.15', 'Accept-Encoding': 'gzip, deflate, zstd', 'Accept': 'application/json', 'Connection': 'keep-alive', 'Authorization': 'Basic YWRtaW46cGFzc3dvcmQxMjM=', 'Content-Type': 'application/json', 'Content-Length': '6177'}
    body = {'´ÇX}': {'G6C-*\x9d\U00083b47¯7\U0005fd0eg\U00103eb4\x10\x1d': -1.029582693357488e-126, 'í\U000a887a\x8c\x1b\x86\U000d7fefã': '\x00Ú\x00À\U0003b01cÆ%컐', '': None}, 's\U000b958c': [{}], 'totalprice': -23782, 'firstname': 'Ì', 'bookingdates': {'checkin': '2387-12-07', 'checkout': '4732-05-23', '\U000f6a51': {}, '5': {'TRUE': None, '[\x11\x99\x83âØ\U000fc435\U0009292b÷\U0006fb95\x99\x05\x18\x93\x8b¾ÿ¤Ñ': {'y|ÍÃ\x16ÓÌ\U000d5021¬\x02\U0001c7f0': None, 'M\x91\U0010de6e\x02u\x19': 1.0134766317486547e+275, '>\x03\x93:ß\U0003d4a7\x06\U0006e2ef\U000a52e5闺\x06': None}, '#𫒺\U000b0e59': 'ßÖ9,'}, '': [{}, {'\x96N\x9d)MÃ6Á': {' \x87\x1fNL>': -13035, '\U0008992eÀ°\x17k©q\\S\U000d6ad4Ýb': False, '': -4.43315520468328e+16}, '': [{}, {'ª\x9bÏ\x8b,𡕻': True, 'çÓ𭄉': '\x0f\U00101d2a+oÜ\U0005c6ad²Ý'}], 'H\x8d«\x8czÒ': -6.103515625e-05}, None], '\U00073e49𪑯¬é\x89\U000cd7ad\U000e2b02ª\x05ÜÈ': {'G\U0001083då\x1bv.¥\U000da6f7ÑûP\x8d': [{'\x1bg\U000b9777\U000f2f63\x00"𩸓ÒÒ\x9aþC\x9fóë\x1aºr\U0001637e\x81ï%¨è': [[[False], {'ã\U000abf07?\U0005693b\U0008d82dt\U00053cc8': False}, []]]}, {}], '\xad§òâ\x88ß}Ò\x8eK\x00\x1f\xa0-\U000ebbcf¯´': {'\x97\x9d\x95\U0008abc3': {}, '\x0b\t': [-18, True, '~\U000ff7de\x1e\t\x07®\x18ó\U00061903']}}, '😍': {'': [], 'Á¨': [None, None, 27796]}, 'Inf': [6.794311057690078e+248, 7.127911414273593e+16, '\U0003f44a\n\x82,[VFF\x10RVÈ\x99û·>\x93\U000b137d\U000d6fbcÍäß\U00035693\U000da4e9m鵡Ä\x93'], '\x94': {'9ÚÝ': {'º\x0cJ\U00065407ïK\x9e\U000ca05dO': True, 'Ía': False}, '\U000a6570£x¡\U000d13f8d': {'\x14Ø\x19r': {}}, '': None}, 'ñ\U0007486a/B\U0003636a\x04\x07': [[], {'M\x8b\U000f1b6b': -9384062745784684.0, '://\U000d7f63¾\U000b2224\x7f\U00055b1f': None, 'à𓞡áÅë\nÖ': 'ú\x83𩵤\x0c©`\x1d\U0010c412\x7f¯bEµ'}, {'|ð:': [], '\x90K\x1d\x0c\U000fd2a5«t¼æ\U000f177eÇój¨': ''}], '\U000993e6\U0001b5e0½&÷µ': [['\x95', 6424, 'pT\x1e\x91\U0010f6250L'], '\U000a8106\x80[*>JÊ\x90p\x1eª', []], '\U0005d48aØYì\x18\x1a\x8a': [[], [None], {'': '\x81Z\U000b60eeÕÌ', '2': -1}], '\x14\U0005ffc6\U00091ecf¤¹\n𗄋\U000a3d83#ÌÐ?P\U0001a473\x8c\U00106088Ûæi\U000cd509': {'q': [], 'Æ\x16': {'\x00\U00011ff5u\U000ce217': [None, -1465609449, True], 'CÊ;\x9b\U0007153cÓq¯\x82¿¯×': {'Q\x06\x9f/Ú\U000cb4a9nª¦g/EÁñ\x8d|\x1eÈ\U0010b4f5\x08\x00ǰ\x05': False}, '½\U000ec4dc£Ã¢': {'óB': {}}}}, '\U000fa6b23': {}, 't%\x8e\U000e7707Î\x19𝥚ÂNÉ\x1b1\x1a\x98¯': [{'{xK\U00068067\U001017e6\\\U000ca520\x8d\x7f\x03c\x80é\x1e\U0010da75%|': {}, '\x17r': {'ä²\U000a8fdcÐ': None, '\x10\x0c\x03\U000ef01b': [None, True], '¤]': 'H>'}, '\x82³\U001021a5fy½\U00034aceH¢\x06\U000809d8\U000c131cÂ': {'\U001027e4\U0006425c\x92\t': '\x89R\U000408d8\U000e18f8v\U0004be86\x985ç', '': False, 'F\x13Qädᛲ𗊍\U000ac0dbR\x90': -35}}, [14096, 'z'], {'4\U000d23af\U000c729b\x81\U000b1471\U000ffa70': 'ýN', '': {'\U000113f4z\t?æ': -0.99999, "\U000b1d42\U000a22e8\U00066a40\U000d526fíW'ÁêX\U000e3f1a": False, '': 3232}, 'Vy\U00041c5d3A\x1e\U0005a63as\x11E\x99Í\x0e\x11Û': 'v'}], '8\U0005f0bf(×\x99+\uea3e\U000ac40b×É¨\U0005526dR\U0004eaa2\U00104213': None, '§Ó\U000aa4e9': [], 'n¾\x15*¯': {}, '»\U0002fdbfs¥\x96': [{'"Õ\ufeff': 1.7976931348623157e+308, '\U00102d8a': -1.175494351e-38, 'òúvà𬿞\x8f': '\x06'}, {}, [{'\U0003a1a5x\x00': [49, 300, False]}, {'\x12Ó\U00014b25ä³': None, '{': 8.202142243266902e+260}]], '\U00080562\U000f416e\x91ÍÁ÷7': [{'\x9aÌ\U000b5138°': 1.1754943508222875e-38, '': {}, 'p\x80Å\U00091716éñ9°g': -7.125497496479826e+16}, [2703, 300, 95]], '¹o': [{'Ñ': True, 'Authorization': 14340, '\U000cbcd3\U000a8e69¸ÃÄB\x9c¤n\U00010737\x80£W': None}]}, '\U000d38b98Ùãí': [{}, [True], {' \x95\U0005a8ba\x82\U000bb9442\U00015d46': {'\x9d\x1a\x0cÝÉÍ´\x01\x15\U0005e05b\x99\U000b4c7a\x8eZ굗\U00065b31\x8d\x1aG': None, '\x83\U000b89526': {'': {'\x91Ö\x93x': 46, '¸w\x90\U000fc71c_ß': False, '\x80Q\x0c±': False}, 'Ó\x00': [False], '«\x91\U000a1bcf4måTáoL\x91=oú\U0005158f\x96\x97~': None}, '𝓣𝓱𝓮 𝓺𝓾𝓲𝓬𝓴 𝓫𝓻𝓸𝔀𝓷 𝓯𝓸𝔁 𝓳𝓾𝓶𝓹𝓼 𝓸𝓿𝓮𝓻 𝓽𝓱𝓮 𝓵𝓪𝔃𝔂 𝓭𝓸𝓰': [True, None, 112]}, 'É': {'\x11\U00037b97\U0003a40d': {'û\x02\x0c.\U000887ef\n\U000b4c1b': None}, 'true': True}, '': None}]}
    
    response = requests.post(url, headers=headers, json=body)
    
    check.equal(response.status_code, 500, f'Expected status 500, got {response.status_code}')
    check.is_not_none(response.text, 'Response should have body')

def test_post_booking_162():
    """Test generated from Schemathesis VCR: dqRIGC
    Test: POST /booking
    Status: SUCCESS
    """
    import requests
    
    url = f"https://restful-booker.herokuapp.com/booking"
    headers = {'User-Agent': 'schemathesis/4.3.15', 'Accept-Encoding': 'gzip, deflate, zstd', 'Accept': 'application/json', 'Connection': 'keep-alive', 'Authorization': 'Basic YWRtaW46cGFzc3dvcmQxMjM=', 'Content-Type': 'application/json', 'Content-Length': '720'}
    body = {'bookingdates': {'checkin': '7770-10-07', 'checkout': '6297-11-23', '\U0004ecc7ý\x14ZD\x7f': [{'': [True], 'ö1\t': {}, 'Æ\U000ddf99': [[{'ʇǝɯɐ ʇᴉs ɹolop ɯnsdᴉ ɯǝɹo˥': None, '': 3558}], {'¾ò³\x10\x99ðÇ\x02\x96\x05©TûqÅ': {'\U00045d90Ô¥_§': None, '[\x87': False}, '\x01\x86\U00104d56&': None, '\U000dfff8\x05Å': 57}]}]}, 'depositpaid': True, 'firstname': 'x,NïÇ¨', 'lastname': 'ÿè', 'totalprice': -29500187099952110599777076478723534628, 'additionalneeds': '', '¨P\U000dc9e2T\x88𑂭': {'\x93Á': []}}
    
    response = requests.post(url, headers=headers, json=body)
    
    check.equal(response.status_code, 200, f'Expected status 200, got {response.status_code}')
    check.equal(response.json(), {'bookingid': 1700, 'booking': {'firstname': 'x,NïÇ¨', 'lastname': 'ÿè', 'totalprice': -2, 'depositpaid': True, 'bookingdates': {'checkin': '7770-10-07', 'checkout': '6297-11-23'}, 'additionalneeds': ''}}, 'Response body mismatch')

def test_delete_booking_300_163():
    """Test generated from Schemathesis VCR: YaS3pW
    Test: DELETE /booking/300
    Status: SUCCESS
    """
    import requests
    
    url = f"https://restful-booker.herokuapp.com/booking/300"
    headers = {'User-Agent': 'schemathesis/4.3.15', 'Accept-Encoding': 'gzip, deflate, zstd', 'Accept': 'application/json', 'Connection': 'keep-alive', 'Authorization': 'Basic YWRtaW46cGFzc3dvcmQxMjM=', 'Content-Type': 'application/json', 'Content-Length': '0'}
    
    response = requests.delete(url, headers=headers)
    
    check.equal(response.status_code, 405, f'Expected status 405, got {response.status_code}')
    check.is_not_none(response.text, 'Response should have body')

def test_get_booking_10308_164():
    """Test generated from Schemathesis VCR: 59T9bz
    Test: GET /booking/-10308
    Status: SUCCESS
    """
    import requests
    
    url = f"https://restful-booker.herokuapp.com/booking/-10308"
    headers = {'User-Agent': 'schemathesis/4.3.15', 'Accept-Encoding': 'gzip, deflate, zstd', 'Accept': 'application/json', 'Connection': 'keep-alive', 'Authorization': 'Basic YWRtaW46cGFzc3dvcmQxMjM=', 'Content-Type': 'application/json'}
    
    response = requests.get(url, headers=headers)
    
    check.equal(response.status_code, 404, f'Expected status 404, got {response.status_code}')
    check.is_not_none(response.text, 'Response should have body')

def test_patch_booking_true_165():
    """Test generated from Schemathesis VCR: ekIx1O
    Test: PATCH /booking/true
    Status: SUCCESS
    """
    import requests
    
    url = f"https://restful-booker.herokuapp.com/booking/true"
    headers = {'User-Agent': 'schemathesis/4.3.15', 'Accept-Encoding': 'gzip, deflate, zstd', 'Accept': 'application/json', 'Connection': 'keep-alive', 'Authorization': 'Basic YWRtaW46cGFzc3dvcmQxMjM=', 'Content-Type': 'application/json', 'Content-Length': '269'}
    body = {'bookingdates': {'checkin': '7770-10-07', 'checkout': '6297-11-23'}, 'depositpaid': True, 'firstname': 'x,NïÇ¨', 'lastname': 'ÿè', 'totalprice': -2, 'Ð': [[False, 0.0, {'': 91}], [False, [], {'': '1'}], '__main__'], 'additionalneeds': ''}
    
    response = requests.patch(url, headers=headers, json=body)
    
    check.equal(response.status_code, 405, f'Expected status 405, got {response.status_code}')
    check.is_not_none(response.text, 'Response should have body')

def test_patch_booking_17209_166():
    """Test generated from Schemathesis VCR: bbWLcK
    Test: PATCH /booking/-17209
    Status: SUCCESS
    """
    import requests
    
    url = f"https://restful-booker.herokuapp.com/booking/-17209"
    headers = {'User-Agent': 'schemathesis/4.3.15', 'Accept-Encoding': 'gzip, deflate, zstd', 'Accept': 'application/json', 'Connection': 'keep-alive', 'Authorization': 'Basic YWRtaW46cGFzc3dvcmQxMjM=', 'Content-Type': 'application/json', 'Content-Length': '178'}
    body = {'bookingdates': {'checkin': '7770-10-07', 'checkout': '6297-11-23'}, 'depositpaid': True, 'firstname': 'x,NïÇ¨', 'lastname': 'ÿè', 'totalprice': -31286}
    
    response = requests.patch(url, headers=headers, json=body)
    
    check.equal(response.status_code, 405, f'Expected status 405, got {response.status_code}')
    check.is_not_none(response.text, 'Response should have body')
