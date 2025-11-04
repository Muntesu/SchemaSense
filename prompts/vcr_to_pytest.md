# LLM Prompt: Convert VCR to pytest Tests

You are an expert Python developer. Convert Schemathesis VCR YAML cassette files into pytest test modules that embed AI-provided randomized request data and keep tests organized by Schemathesis phase.

## Task

Create a Python script that parses Schemathesis VCR YAML files and generates pytest test functions for each HTTP interaction.

## Requirements

1. **Parse VCR YAML and Optional Analysis JSON**
   - Parse `http_interactions`.
   - Extract `id`, `components.phase.name`, HTTP request/response details, and checks.
   - Accept an optional AI analysis JSON that contains `randomized_request_data` for each test ID.
   - When analysis data exists, merge those values into the request body (actual literals, not faker expressions).

2. **Organize by Schemathesis Phase**
   - Group tests into files/classes per phase (examples, coverage, fuzzing, stateful).
   - Provide informative class docstrings (phase name, source VCR file, number of tests).

3. **Generate All Tests**
   - Emit a pytest function for every interaction (success and failure).
   - Include docstrings that capture method, path, original status, and test ID.
   - Preserve Groq recommendations (if any) as comments near the relevant test.

4. **Use Soft Assertions**
   - Import `pytest_check as check`.
   - Use `check.equal`, `check.is_not_none`, etc., so each test keeps running after individual assertion failures.

5. **Requests Construction**
   - Build `requests.{method}` calls with the URL, headers, and JSON payload.
   - Remove internal Schemathesis headers (`X-Schemathesis-*`).
   - When analysis data supplies randomized values, override the recorded body with those real values.

6. **Assertions**
   - Always assert the recorded status code.
   - For response bodies, keep lightweight checks (e.g., ensure JSON parsing succeeds, keys exist). Avoid full equality with the recorded response because manual review will update assertions later.
   - Add comments when the original VCR body is known so reviewers can adjust assertions manually.

7. **Naming & Hygiene**
   - Sanitize function names (URL decoded, non-alphanumeric → `_`, collapse multiple `_`, enforce `test_` prefix, truncate to avoid overly long names).
   - Keep the output Python files formatted and import-required modules at top level only once.

8. **CLI Expectations**
   - Provide a CLI similar to the current script:
     ```bash
     python vcr_to_pytest.py <input_vcr_file> [--analysis analysis.json] [--output-dir output_dir]
     ```
   - Auto-detect the analysis JSON when not provided (replace suffix `_filtered.yaml` → `_analysis.json`).

9. **Manual Review Reminder**
   - Add a file-level comment reminding users to review response assertions using `AI_RANDOMIZATION_LIMITATIONS.md`.

## Command Line Interface

```bash
python vcr_to_pytest.py <input_vcr_file> <output_pytest_file>
```

## Output

Provide complete Python script that:
- Parses VCR YAML files
- Generates pytest test functions
- Uses soft assertions (pytest-check)
- Handles all edge cases
- Produces executable test files
