# AI Randomization – Manual Review Checklist

Groq supplies realistic randomized request data for Schemathesis-generated tests, but it cannot update the response assertions automatically. Use this checklist immediately after copying tests into `openapi-python/test/test_schemathesis/`.

## 0. Response Assertions (Critical)

- Replace any direct equality checks against the recorded VCR payload with logic that:
  - Verifies server-generated IDs/timestamps exist (`check.is_not_none(response_data.get("bookingid"))`).
  - Confirms the response echoes the randomized values you sent (`check.equal(response_data["booking"]["firstname"], body["firstname"])`).
- Remove hardcoded comparisons to VCR literals (e.g., `check.equal(response_data, {...'Jim'...})`).
- Ensure the response JSON is parsed inside a `try/except JSONDecodeError` block.

## 1. POST / PUT / PATCH (Create or Update)

- Confirm the request body uses the AI-provided values.
- Assert that server-generated fields exist, not that they match fixed values.
- Verify the response echoes your randomized fields (firstname, lastname, price, dates, etc.).
- Keep authentication static unless specifically testing credential failures.

## 2. GET Requests

- Align query parameters with data you actually created earlier in the suite.
- Avoid asserting entire response bodies; prefer structural checks (keys exist, list not empty).
- When testing GET by ID, ensure the ID comes from a create step in the same test or fixture.

## 3. DELETE Operations

- Create or reuse a valid resource before deleting it.
- Expect minimal responses (status code, optional message). Do not rely on body equality.

## 4. Stateful Workflows

- Consider grouping related requests in the same test class or fixture when the workflow depends on prior steps.
- Ensure IDs or tokens produced in earlier steps are stored and reused consistently.
- Document any limitations (e.g., read-after-write timing) in comments.

## 5. Error Handling & Soft Assertions

- Leave `pytest_check` assertions in place so all checks run even if one fails.
- Wrap JSON parsing in guarded blocks:
  ```python
  if response.status_code == expected_status:
      try:
          response_data = response.json()
      except JSONDecodeError:
          check.fail("Expected JSON response but received non-JSON payload")
          return
  ```
- Log the request/response in comments if additional context is needed during manual review.

## Recommended Workflow

1. Run the workflow scripts (`01` through `04`).
2. Open each generated file in `openapi-python/test/test_schemathesis/`.
3. Apply the checklist above, starting with response assertions.
4. Run pytest with Groq analysis:
   ```bash
   python openapi-python/scripts/run_tests_with_ai_analysis.py openapi-python/test/test_schemathesis/ -v
   ```
5. Address any failures flagged by Groq (the HTML report will include full HTTP requests).

## When in Doubt

- Favor assertions that confirm structure, existence, and echoing of randomized data over brittle equality checks.
- Leave short comments when manual intervention is still required so future maintainers understand the rationale.

