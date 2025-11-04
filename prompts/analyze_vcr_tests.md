# LLM Prompt: Analyze VCR Tests for Value

You are an expert API testing and quality assurance engineer. Analyze Schemathesis VCR test data to determine which tests bring value and should be kept vs which can be skipped. For tests that should be kept, provide randomized test data to avoid hardcoded values.

## Task

Analyze each test in the VCR data and determine:
1. **Should this test be kept?** (yes/no)
2. **Value level**: "high", "medium", or "low"
3. **Reason**: Brief explanation of why it should be kept or skipped
4. **Issues**: Any problems with the test (incorrect status codes, invalid expectations, etc.)
5. **Recommendations**: How to improve the test if kept
6. **Randomized data**: For tests that should be kept, provide Python code to generate random test data

## Analysis Approach

For each test, evaluate its value by considering:

- **Purpose and relevance**: What does this test validate? Is it testing meaningful API behavior?
- **Status code correctness**: Does the expected status code match HTTP standards and API contract?
- **Real-world applicability**: Would this scenario occur in actual API usage?
- **Bug detection potential**: Does this test catch real bugs or contract violations?
- **Redundancy**: Are there other tests that cover the same scenario more effectively?
- **API design alignment**: Does the test validate correct API behavior or document API design issues?
- **Test quality**: Is the test well-formed with appropriate expectations?

Make your own judgment about what makes a test valuable. Consider the context of the API endpoint, the test phase, and the overall test suite coverage.

## Data Randomization Guidelines

For tests that should be kept, analyze the request and response data and provide actual randomized values. This ensures tests don't rely on the same hardcoded data from VCR recordings and can catch more edge cases.

### What to Randomize

1. **Identifiers** (booking IDs, user IDs, etc.)
   - Use random numeric values
   - Examples: `4521`, `78392`, `15067` for numeric IDs
   - Examples: `"a3f8c9d1-4e2b-4c5d-9e8f-1a2b3c4d5e6f"` for UUID-style IDs

2. **Personal Information** (names, emails, etc.)
   - Generate realistic random values
   - Examples: `"michael.smith@example.com"`, `"user_4521"`, `"jennifer.wong@test.com"`

3. **Numeric Values** (prices, quantities, etc.)
   - Use reasonable random values
   - Examples: prices `245`, `387`, `156`; quantities `3`, `7`, `12`
   - Consider business logic (e.g., prices should be positive, quantities should be > 0)

4. **Boolean Values**
   - Randomly pick `true` or `false` if both values are valid
   - Use context-appropriate fixed value if the test requires specific behavior

5. **Dates and Times**
   - Use future dates in YYYY-MM-DD format
   - Examples: checkin `"2025-12-15"`, checkout `"2026-01-20"` (must be after checkin)
   - Ensure logical consistency (checkout after checkin, dates in appropriate ranges)

6. **String Fields** (descriptions, notes, etc.)
   - Use realistic descriptive values
   - Examples: `"Breakfast included"`, `"Late checkout"`, `"Extra towels"`
   - Keep length reasonable and within API constraints

### What NOT to Randomize

1. **Credentials** (username, password) - Keep static for non-authentication tests
2. **API Endpoints** - Keep exact paths as defined in the API
3. **Required Field Names** - Keep schema structure intact
4. **Test-Specific Values** - Values that are specifically being tested (e.g., testing edge case with price=0)
5. **Authentication Tests** - When testing auth failures, use specific invalid credentials

### Output Format for Randomized Data

**CRITICAL**: Provide actual random values (not code)!

Generate realistic random data and provide the **actual values** as JSON. Do NOT provide Python code or expressions.

**Correct format - Provide actual values:**
```json
{
  "firstname": "Michael",
  "lastname": "Rodriguez",
  "totalprice": 378,
  "depositpaid": true,
  "bookingdates": {
    "checkin": "2025-12-15",
    "checkout": "2026-01-20"
  },
  "additionalneeds": "Breakfast",
  "username": "admin",
  "password": "password123"
}
```

**WRONG - Do NOT provide code:**
```json
{
  "firstname": "faker.first_name()",  // ❌ NO! Provide actual value like "Michael"
  "totalprice": "random.randint(50, 500)",  // ❌ NO! Provide actual number like 378
  "depositpaid": "random.choice([True, False])"  // ❌ NO! Provide actual boolean like true
}
```

**Guidelines for generating values:**
- **Names**: Use realistic common names (not "Test User")
- **Numbers**: Generate reasonable random values (prices 50-500, IDs 1000-9999)
- **Dates**: Use future dates in YYYY-MM-DD format
- **Booleans**: Randomly pick true or false
- **Strings**: Generate realistic text (not "test" or "dummy")

## Output Format

Provide a JSON object with a "tests" array, where each test has:
```json
{
  "test_id": "string (required)",
  "should_keep": boolean (required),
  "value_level": "high" | "medium" | "low" (required),
  "reason": "string explaining the decision (required)",
  "issues": ["list of issues found", "if any"],
  "recommendations": ["list of recommendations", "if any"],
  "randomized_request_data": {
    "description": "Actual random values for request data",
    "note": "Only include if should_keep is true and test has request body/params",
    "example": {
      "firstname": "John",
      "lastname": "Martinez",
      "totalprice": 425
    }
  }
}
```

**Notes:**
- `randomized_request_data`: Only include for tests with request bodies or parameters that need randomization
- Provide actual JSON values (strings, numbers, booleans, objects), NOT Python code
- For tests without request data (e.g., simple GET requests), omit `randomized_request_data`

## CRITICAL: Response Validation Guidelines

**Important**: When you randomize request data, the VCR-recorded response is NO LONGER VALID for assertion!

**The Problem:**
- VCR recorded: Request `{"firstname": "Jim"}` → Response `{"bookingid": 495, "booking": {"firstname": "Jim"}}`
- Your randomized data: `{"firstname": "Michael"}` → Response will be `{"bookingid": ???, "booking": {"firstname": "Michael"}}`
- Asserting against VCR response `{"firstname": "Jim"}` will FAIL!

**The Solution - Add guidance in `issues` or `recommendations` fields:**

For **POST/PUT/PATCH** (Create/Update operations):
1. **Server-generated fields** (IDs, timestamps): Don't assert specific values - just check they exist
   - ❌ BAD: `assert bookingid == 495`
   - ✅ GOOD: Add to `issues`: "Response assertion needs update: bookingid is server-generated, should only verify it exists (not specific value 495)"

2. **Echoed request data**: Should match what YOU sent (not VCR data)
   - ❌ BAD: `assert firstname == 'Jim'` (VCR value)
   - ✅ GOOD: Add to `recommendations`: "Response should echo back the sent data: firstname, lastname, totalprice, etc."

3. **Summary**: In `issues` or `recommendations`, note:
   - "Test needs response assertion update: verify bookingid exists, and response echoes sent data (not hardcoded VCR values)"

For **GET** requests:
- Response data is unpredictable (depends on what exists in DB)
- Note in `issues`: "GET response cannot be validated against hardcoded values - consider removing response body assertion"

For **DELETE** requests:
- Usually no body or simple confirmation message
- Response assertion may be acceptable as-is

## Understanding Request Context

Analyze each request to understand what it's testing and randomize accordingly:

### POST /booking (Create Booking)
- Randomize: firstname, lastname, totalprice, depositpaid, checkin/checkout dates, additionalneeds
- Keep static: none (all can be random)
- Ensure: checkout date > checkin date, totalprice > 0

### PUT/PATCH /booking/{id} (Update Booking)
- Randomize: firstname, lastname, totalprice, depositpaid, dates, additionalneeds
- Keep static: booking ID (comes from test setup/fixture)
- Keep static: credentials (unless testing auth failures)

### GET /booking (List Bookings)
- Usually no request body, might have query parameters
- Randomize: firstname, lastname, checkin, checkout filters if present
- Keep static: none

### GET /booking/{id} (Get Specific Booking)
- No request body
- Keep static: booking ID (should reference an existing booking)

### DELETE /booking/{id} (Delete Booking)
- No request body
- Keep static: booking ID (should reference an existing booking)
- Keep static: credentials (unless testing auth failures)

### POST /auth (Authentication)
- For valid auth tests: Keep static credentials (username="admin", password="password123")
- For invalid auth tests: Use specific invalid credentials to test (e.g., wrong password)
- Don't randomize credentials unless specifically testing auth validation with various inputs

## Important

- **Response Assertions**: For EVERY test with randomized data, add issue/recommendation noting that response assertions need updating (server-generated fields, echoed data)
- **Context Awareness**: Understand what each request does and why certain data should or shouldn't be randomized
- **Business Logic**: Ensure randomized data respects business constraints (e.g., dates in correct order, positive prices, valid data types)
- **Test Purpose**: Consider the test's purpose when deciding what to randomize (e.g., don't randomize the specific value being tested)
- **Realistic Values**: Generate realistic, varied random values (not generic "test" data)
- **Static When Necessary**: Keep credentials static for non-auth tests, keep IDs static when they reference existing resources
- Be specific and technical in your analysis
- Consider the test's purpose in the context of the phase it belongs to
- Use your expertise to determine what provides value for regression testing and API validation
- Provide clear reasoning for each decision
- Always include `randomized_request_data` with actual values for tests that should be kept and have request bodies
