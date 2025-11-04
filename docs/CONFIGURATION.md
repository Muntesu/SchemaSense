# Configuration Reference

Complete configuration reference for the Schemathesis → Groq AI → pytest workflow.

## 1. Global Configuration (`config.py`)

**Location:** `SchemaSense/config.py`

| Setting | Description |
|---------|-------------|
| `PROJECT_ROOT` | Repository root for relative path resolution. |
| `SCHEMATHESIS_DIR` / `SCHEMATHESIS_REPORTS_DIR` | Source directory and reports output for Schemathesis. |
| `OPENAPI_PYTHON_DIR` / `OPENAPI_PYTHON_TEST_DIR` | Destination for generated pytest tests. |
| `OPENAPI_PYTHON_REPORTS_DIR` | Location for pytest + AI analysis reports. |
| `FILTERED_VCR_SUFFIX` | Suffix appended to AI-filtered VCR files (default `_filtered`). |
| `ANALYSIS_REPORT_SUFFIX` / `ANALYSIS_JSON_SUFFIX` | Filenames for AI report (`_analysis_report.txt`) and JSON (`_analysis.json`). |
| `AI_BATCH_SIZE` | Max tests sent to Groq per batch (default `10`). |
| `AI_MAX_TOKENS_PER_REQUEST` | Groq `max_tokens` limit (default `16000`). |
| `GROQ_MODEL` | Model ID used for analysis (e.g., `"llama-3.1-8b-instant"`). |

> Update `config.py` instead of editing individual scripts whenever paths or Groq settings change.

## 2. Groq API Configuration

### 2.1 API Key
```bash
export GROQ_API_KEY="your-api-key"    # preferred
```
Or place the key in a local file (ignored by git):
```bash
echo "your-api-key" > .groq_api_key
```

For GitHub Actions, add `GROQ_API_KEY` as a repository secret and expose it in workflow steps:
```yaml
env:
  GROQ_API_KEY: ${{ secrets.GROQ_API_KEY }}
```

### 2.2 Model & Request Settings (`openapi-python/test/ai_config.py`)
Key defaults:
```python
class AIConfig:
    GROQ_MODEL = "llama-3.1-8b-instant"
    GROQ_API_URL = "https://api.groq.com/openai/v1/chat/completions"
    MAX_TOKENS = 16000
    TEMPERATURE = 0.1
```
- `MAX_TOKENS` matches `MAX_ANALYSIS_TOKENS` in `config.py`.
- Adjust `TEMPERATURE` if responses need more variability (higher) or consistency (lower).

### 2.3 Batch Size
Controlled by `AI_BATCH_SIZE` (default `10`) in `config.py`. AI analysis script dynamically adjusts when responses are truncated.

## 3. Schemathesis Configuration

### 3.1 Environment Variables / Hooks
```bash
export SCHEMATHESIS_HOOKS="restful_booker_basic_auth:before_call"
```
Optional `.env` file: `schemathesis/schemathesis.env`
```
USER=admin
PASSWORD=password123
```

### 3.2 Auth Hook (`schemathesis/restful_booker_basic_auth.py`)
```python
USERNAME = os.getenv("USER", "admin")
PASSWORD = os.getenv("PASSWORD", "password123")
```
Customize credentials by updating environment variables or editing the hook file.

### 3.3 Command Options
Schemathesis run options are defined inside `schemathesis/scripts/01_generate_schemathesis_tests.py`:
- `--max-examples` (default 5)
- `--workers` (default 5)
- `--report junit,har,vcr`
- `--report-dir schemathesis/reports`

Adjust these in the script if different test coverage or execution profiles are required.

## 4. pytest & Test Execution

### 4.1 Fixtures (`openapi-python/test/conftest.py`)
```python
BASE_URL = "https://restful-booker.herokuapp.com"

@pytest.fixture(scope="session")
def base_url():
    return BASE_URL

@pytest.fixture(scope="session")
def auth_basic_header():
    return get_auth_basic_header()
```
- Override `BASE_URL` by editing the constant or making it environment-driven:
  ```python
  BASE_URL = os.getenv("API_BASE_URL", "https://restful-booker.herokuapp.com")
  ```
- Extend with project-specific fixtures (e.g., JWT tokens) in the same file.

### 4.2 pytest Configuration (`openapi-python/pyproject.toml`)
```toml
[tool.pytest.ini_options]
testpaths = ["test"]
addopts = "-v"
```
Adjust `addopts` or plugins here (e.g., `-s`, `--tb=short`).

## 5. AI Failure Analysis Runner

**Script:** `openapi-python/scripts/run_tests_with_ai_analysis.py`

Key CLI flags:
```bash
--max-failures N    # Limit failures sent to Groq
--no-analysis       # Run pytest only (skip Groq)
--junit-xml PATH    # Override XML output path
```
Defaults:
- JUnit XML: `openapi-python/reports/junit-YYYYMMDDTHHMMSS.xml`
- HTML report: `openapi-python/reports/ai-failure-analysis-YYYYMMDDTHHMMSS.html`

## 6. Manual Review Configuration

`AI_RANDOMIZATION_LIMITATIONS.md` documents required manual adjustments:
- Response assertions must reflect randomized request bodies.
- GET filters/IDs must align with created data.
- DELETE/PUT/PATCH tests must create prerequisites.
- Use this checklist after running `04_copy_tests_to_openapi.py`.

## 7. Ignored Artifacts

`.gitignore` entries ensure generated reports stay out of version control:
- `schemathesis/reports/`
- `openapi-python/reports/`
- Root `reports/`

## 8. Configuration Best Practices

1. **Centralize changes**  – Prefer updating `config.py` over editing individual scripts.
2. **Use environment variables** – For API keys and environment-specific URLs.
3. **Keep reports out of git** – Run `git status` to verify only source files are tracked.
4. **Validate Groq connectivity** – Run a small batch (`--max-tests 5`) after changes.
5. **Document overrides** – Note custom paths or credentials in team documentation.

## 9. Related Documentation

- [ARCHITECTURE.md](ARCHITECTURE.md) – Component relationships.
- [WORKFLOWS.md](WORKFLOWS.md) – Detailed step-by-step instructions.
- [COMPLETE_WORKFLOW.md](../COMPLETE_WORKFLOW.md) – Command checklist.
- [AI_RANDOMIZATION_LIMITATIONS.md](../AI_RANDOMIZATION_LIMITATIONS.md) – Manual review requirements.

