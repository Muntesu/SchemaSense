# Workflows Documentation

Updated end-to-end workflows for the Schemathesis → Groq AI → pytest pipeline.

## 1. Initial Setup

### 1.1 Install Dependencies
```bash
cd SchemaSense
pip install -r requirements.txt  # installs schemathesis, pytest, groq, pytest-check, pyyaml
```

### 1.2 Configure Groq API Key
```bash
export GROQ_API_KEY="your-api-key"              # recommended

# or save it locally for tooling that reads .groq_api_key
echo "your-api-key" > .groq_api_key

# In CI, expose the secret via GitHub Actions:
# env:
#   GROQ_API_KEY: ${{ secrets.GROQ_API_KEY }}
```

### 1.3 Verify Environment
```bash
schemathesis --version
pytest --version
python - <<'PY'
from test.ai_config import AIConfig
print("Groq key available:", bool(AIConfig.get_api_key()))
PY
```

## 2. Core Workflow (Matches `workflow.py`)

### Step 1 – Schemathesis Run
```bash
python schemathesis/scripts/01_generate_schemathesis_tests.py
```
Output: `schemathesis/reports/vcr-*.yaml`, `junit-*.xml`, `har-*.json`, `tests_output.txt`.

### Step 2 – Groq AI Filtering & Randomization
```bash
python schemathesis/scripts/02_analyze_vcr_with_ai.py schemathesis/reports/vcr-*.yaml
```
Output:
- Filtered VCR (`*_filtered.yaml`)
- Analysis JSON (`*_analysis.json`) with randomized request data & recommendations
- Analysis report (`*_analysis_report.txt`)

### Step 3 – VCR → pytest Conversion
```bash
python schemathesis/scripts/03_convert_vcr_to_pytest.py schemathesis/reports/vcr-*-filtered.yaml
```
Behavior:
- Auto-detects corresponding analysis JSON.
- Embeds AI-supplied values directly into pytest request bodies.
- Writes tests to `schemathesis/test/test_schemathesis/test_phase_*.py`.

### Step 4 – Copy into openapi-python
```bash
python schemathesis/scripts/04_copy_tests_to_openapi.py
```
Copies generated tests to `openapi-python/test/test_schemathesis/`.

### Step 4.5 – Manual Response-Assertion Review (Required)
Actions:
1. Open each `test_phase_*.py` file.
2. Update assertions to:
   - Check server-generated fields exist (e.g., `bookingid`).
   - Ensure response echoes randomized request data (`response_data['firstname'] == body['firstname']`).
3. Fix GET filters & stateful dependencies to align with randomized data.
Reference: `AI_RANDOMIZATION_LIMITATIONS.md` checklist.

### Step 5 – pytest + Groq Failure Analysis
```bash
python openapi-python/scripts/run_tests_with_ai_analysis.py openapi-python/test/test_schemathesis/ -v
```
Output: `openapi-python/reports/junit-*.xml`, `ai-failure-analysis-*.html`.

## 3. Running Individual Steps

```bash
# Run only Schemathesis generation
python schemathesis/scripts/01_generate_schemathesis_tests.py

# AI analysis with limited tests
python schemathesis/scripts/02_analyze_vcr_with_ai.py schemathesis/reports/vcr-*.yaml --max-tests 50

# Convert without filtered VCR (skips randomization)
python schemathesis/scripts/03_convert_vcr_to_pytest.py schemathesis/reports/vcr-*.yaml --no-analysis

# Run pytest without AI analysis
python openapi-python/scripts/run_tests_with_ai_analysis.py openapi-python/test/test_schemathesis/ -v --no-analysis
```

## 4. Workflow Variants

### Quick Regression (Skip AI filtering)
```bash
python workflow.py --skip-ai-filter --skip-run
# Manual review still required
python openapi-python/scripts/run_tests_with_ai_analysis.py openapi-python/test/test_schemathesis/ -v
```

### Partial Failure Analysis
```bash
python openapi-python/scripts/run_tests_with_ai_analysis.py openapi-python/test/test_schemathesis/ -v --max-failures 5
```

### Rerun with Existing Reports
```bash
# Re-run Groq analysis using existing VCR
python schemathesis/scripts/02_analyze_vcr_with_ai.py schemathesis/reports/vcr-20250101T120000Z_filtered.yaml

# Rebuild tests from the latest analysis JSON
python schemathesis/scripts/03_convert_vcr_to_pytest.py schemathesis/reports/vcr-20250101T120000Z_filtered.yaml

# Copy + review + run as usual
```

## 5. Manual Review Checklist (Summary)

1. **Response assertions** – Replace hardcoded VCR snapshots with logic based on randomized request data.
2. **Server-generated IDs** – Assert presence, not specific values.
3. **GET filters / stateful flows** – Ensure filters reference existing randomized entities.
4. **DELETE/PUT/PATCH** – Create entities before modifying/deleting them.
5. **Error handling** – Preserve soft assertions and JSON parsing guards.
Detailed guidance: `AI_RANDOMIZATION_LIMITATIONS.md`.

## 6. Directory Hygiene

- Reports are ignored in git (`schemathesis/reports/`, `openapi-python/reports/`, root `reports/`).
- Randomized tests live in `openapi-python/test/test_schemathesis/`.
- Configuration centralised in `config.py`.

## 7. Related Resources

- [COMPLETE_WORKFLOW.md](../COMPLETE_WORKFLOW.md) – Command cheat sheet.
- [ARCHITECTURE.md](ARCHITECTURE.md) – Technical view of components.
- [CONFIGURATION.md](CONFIGURATION.md) – Groq, Schemathesis, pytest config reference.
- [AI_RANDOMIZATION_LIMITATIONS.md](../AI_RANDOMIZATION_LIMITATIONS.md) – Manual review checklist.


