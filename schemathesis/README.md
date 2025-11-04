# Schemathesis Workflow

This folder contains everything required to run Schemathesis against the Restful-Booker OpenAPI specification, analyze the results with Groq, and convert them into pytest tests with randomized request data.

## Key Files

- `restful-booker-oas.yaml` – OpenAPI specification used by Schemathesis.
- `schemathesis.env` – Optional environment variables (Basic Auth credentials).
- `restful_booker_basic_auth.py` – Schemathesis hook that injects Basic Auth and default headers.
- `scripts/01_generate_schemathesis_tests.py` – Runs Schemathesis and writes VCR/JUnit/HAR outputs to `schemathesis/reports/`.
- `scripts/02_analyze_vcr_with_ai.py` – Uses Groq to keep valuable tests and provide randomized request data (`*_analysis.json`).
- `scripts/03_convert_vcr_to_pytest.py` – Converts the filtered VCR to pytest modules, embedding AI-supplied random values.
- `scripts/04_copy_tests_to_openapi.py` – Copies generated tests into `openapi-python/test/test_schemathesis/`.
- `vcr_to_pytest.py` – Conversion logic shared by the workflow and prompt.
- `analyze_vcr_with_ai.py` – Standalone module backing the AI filtering script.
- `reports/` – Raw Schemathesis outputs (ignored by git).

## How It Fits Together

1. Run `01_generate_schemathesis_tests.py` to produce VCR, JUnit, and HAR artifacts.
2. Run `02_analyze_vcr_with_ai.py` to:
   - Classify each interaction (keep/skip, value level).
   - Generate realistic randomized request data (`randomized_request_data`).
   - Flag response assertion issues in `issues` / `recommendations`.
3. Run `03_convert_vcr_to_pytest.py` to generate pytest modules (one per phase) that embed the randomized data.
4. Run `04_copy_tests_to_openapi.py` to move the generated files into the execution project.
5. Manually review the new tests and update response assertions per [AI_RANDOMIZATION_LIMITATIONS.md](../AI_RANDOMIZATION_LIMITATIONS.md).
6. Run pytest with Groq analysis (`openapi-python/scripts/run_tests_with_ai_analysis.py`).

## Configuration Tips

- Update global paths, Groq settings, and batch sizes in `SchemaSense/config.py`.
- Provide the Groq API key via `export GROQ_API_KEY=...` or by saving it to `.groq_api_key`.
- Adjust Schemathesis options (max examples, workers) directly inside `01_generate_schemathesis_tests.py`.
- The authentication hook will read credentials from `schemathesis.env` if present; otherwise it defaults to the public demo credentials.

## Related Documentation

- [README.md](../README.md) – Project overview and workflow summary.
- [ARCHITECTURE.md](../docs/ARCHITECTURE.md) – Component relationships.
- [WORKFLOWS.md](../docs/WORKFLOWS.md) – Step-by-step commands.
- [CONFIGURATION.md](../docs/CONFIGURATION.md) – Detailed configuration reference.
- [AI_RANDOMIZATION_LIMITATIONS.md](../AI_RANDOMIZATION_LIMITATIONS.md) – Manual review checklist.

