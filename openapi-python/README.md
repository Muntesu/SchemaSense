# openapi-python Directory

This directory hosts the pytest execution environment, generated Schemathesis tests, and the Groq-powered failure analyzer.

## What's Here

- `test/test_schemathesis/` – Generated pytest modules grouped by Schemathesis phase (examples, coverage, fuzzing, stateful). These files are overwritten every time you run the workflow.
- `test/conftest.py` – Shared pytest fixtures (base URL, Basic Auth header generator).
- `test/ai_failure_analyzer.py` – Parses pytest JUnit XML, enriches failures with full HTTP request details, and calls Groq for analysis.
- `test/ai_config.py` – Groq API configuration (model ID, token limits, batch sizing).
- `scripts/run_tests_with_ai_analysis.py` – Wrapper script that runs pytest, writes JUnit XML, and invokes the analyzer.
- `reports/` – Output directory for JUnit XML and HTML analysis reports (ignored by git).

Legacy OpenAPI Generator artifacts may still exist in this folder, but they are no longer part of the active workflow.

## Running Tests with Groq Analysis

```bash
cd SchemaSense
python openapi-python/scripts/run_tests_with_ai_analysis.py openapi-python/test/test_schemathesis/ -v

# Optional: limit Groq analysis to the first N failures
python openapi-python/scripts/run_tests_with_ai_analysis.py openapi-python/test/test_schemathesis/ -v --max-failures 5

# Optional: run pytest only (skip Groq analysis)
python openapi-python/scripts/run_tests_with_ai_analysis.py openapi-python/test/test_schemathesis/ -v --no-analysis
```

Outputs:
- `openapi-python/reports/junit-YYYYMMDDTHHMMSS.xml`
- `openapi-python/reports/ai-failure-analysis-YYYYMMDDTHHMMSS.html`

## Configuration Tips

- Set `GROQ_API_KEY` in your environment (or save it to `.groq_api_key`) before running the analyzer.
- Adjust Groq settings (model, token limits, batch size) in `SchemaSense/config.py` or `test/ai_config.py`.
- After copying new tests into this directory, review response assertions per [AI_RANDOMIZATION_LIMITATIONS.md](../AI_RANDOMIZATION_LIMITATIONS.md) before executing pytest.

## Related Documentation

- [README.md](../README.md) – Full workflow overview.
- [ARCHITECTURE.md](../docs/ARCHITECTURE.md) – Component relationships.
- [WORKFLOWS.md](../docs/WORKFLOWS.md) – Step-by-step instructions.
- [CONFIGURATION.md](../docs/CONFIGURATION.md) – Groq and Schemathesis configuration reference.
- [AI_FAILURE_ANALYZER_README.md](test/AI_FAILURE_ANALYZER_README.md) – Analyzer behavior and setup.

