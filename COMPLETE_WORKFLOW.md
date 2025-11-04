# Complete Workflow: Schemathesis → VCR → Tests → AI Analysis

Complete command sequence from generating tests with Schemathesis to running extracted tests and analyzing failures with AI.

## ✨ Key Features

- **AI-Powered Test Filtering**: Intelligent test selection using Groq AI
- **AI-Generated Random Data**: Realistic random test values (actual values, not code)
- **Automated Conversion**: VCR cassettes to executable pytest tests
- **AI Failure Analysis**: Deep analysis with complete HTTP request details
- **⚠️ Manual Review Required**: Response assertions need manual fixes (critical limitation)

## Quick Start

```bash
# Run complete workflow (recommended)
python workflow.py

# Or run individual steps
python schemathesis/scripts/01_generate_schemathesis_tests.py
python schemathesis/scripts/02_analyze_vcr_with_ai.py schemathesis/reports/vcr-*.yaml
python schemathesis/scripts/03_convert_vcr_to_pytest.py
python schemathesis/scripts/04_copy_tests_to_openapi.py
# ⚠️ Step 4.5: Manual Review - Fix response assertions (see below)
python openapi-python/scripts/run_tests_with_ai_analysis.py openapi-python/test/test_schemathesis/ -v
```

## Prerequisites

```bash
# Install dependencies
pip install schemathesis pytest pyyaml groq pytest-check

# Set up Groq API key (optional, for AI analysis)
export GROQ_API_KEY='your-api-key-here'
# Or save it to a local file (ignored by git)
echo 'your-api-key-here' > .groq_api_key
```

## Complete Workflow

### Step 1: Generate Tests with Schemathesis (VCR Output)

```bash
python schemathesis/scripts/01_generate_schemathesis_tests.py
```

This generates:
- `schemathesis/reports/vcr-YYYYMMDDTHHMMSSZ.yaml` - VCR cassette with all HTTP interactions
- `schemathesis/reports/junit-YYYYMMDDTHHMMSSZ.xml` - JUnit XML results
- `schemathesis/reports/har-YYYYMMDDTHHMMSSZ.json` - HAR file
- `schemathesis/reports/tests_output.txt` - Terminal output

---

### Step 2: Analyze VCR with AI to Filter Tests & Generate Random Data

```bash
python schemathesis/scripts/02_analyze_vcr_with_ai.py schemathesis/reports/vcr-*.yaml
```

This generates:
- `schemathesis/reports/vcr-YYYYMMDDTHHMMSSZ_filtered.yaml` - Filtered VCR with only valuable tests
- `schemathesis/reports/vcr-YYYYMMDDTHHMMSSZ_analysis_report.txt` - Human-readable report
- `schemathesis/reports/vcr-YYYYMMDDTHHMMSSZ_analysis.json` - Machine-readable analysis with **randomized test data**

**AI Features:**
- Filters valuable tests (removes redundant/low-value tests)
- **Generates randomized test data** (actual values, not code)
  - Example: `{'firstname': 'Michael', 'totalprice': 378}` instead of hardcoded values
- **Flags response assertion issues** (critical limitation)

**Optional options:**
- `--max-tests N` - Limit number of tests analyzed
- `--no-filter` - Only generate report, don't create filtered VCR

**Note:** If you skip AI filtering, use the original VCR file in Step 3 (no randomized data will be available).

---

### Step 3: Convert VCR to pytest Tests

```bash
python schemathesis/scripts/03_convert_vcr_to_pytest.py [vcr_file]
```

**Note:** If `--analysis` is not provided, the script will auto-detect the analysis JSON file based on the VCR filename. For example, `vcr-20251107T000204Z_filtered.yaml` will look for `vcr-20251107T000204Z_analysis.json`.

This generates test files organized by phase:
- `schemathesis/test/test_schemathesis/test_phase_examples.py`
- `schemathesis/test/test_schemathesis/test_phase_coverage.py`
- `schemathesis/test/test_schemathesis/test_phase_fuzzing.py`
- `schemathesis/test/test_schemathesis/test_phase_stateful.py`

**Key Features:**
- **Uses AI-generated random values** (if analysis JSON is available)
- Example: `body = {'firstname': 'Michael', 'totalprice': 378}` (AI-generated)
- **No imports needed** (values are ready to use)
- **Response assertions still use VCR hardcoded values** (needs manual fix - see Step 4.5)

---

### Step 4: Copy Tests to OpenAPI-python Project

```bash
python schemathesis/scripts/04_copy_tests_to_openapi.py
```

This copies all generated tests to `openapi-python/test/test_schemathesis/`.

---

### Step 4.5: Manual Review - Fix Response Assertions (REQUIRED)

⚠️ **CRITICAL: This step is REQUIRED before running tests!**

**The Problem:**
- AI randomizes request data: `{'firstname': 'Michael', 'totalprice': 378}`
- But response assertions still use VCR hardcoded values: `{'firstname': 'Jim', 'totalprice': 111}`
- **Result**: Tests will FAIL until assertions are fixed

**What Needs Manual Fix:**
1. **Response Assertions** (CRITICAL - affects ALL randomized tests)
   - Update to verify server fields exist (not specific values)
   - Update to verify response echoes YOUR sent data
   - Example: Verify `bookingid` exists, verify `firstname` matches sent value

2. **GET by ID**: Ensure IDs exist or create them first
3. **GET with filters**: Ensure filter values match created data
4. **DELETE operations**: Create resources before deleting

**Example Fix:**
```python
# ❌ BEFORE (will fail):
check.equal(response_data, {
    'bookingid': 495,  # Server-generated, will be different!
    'booking': {'firstname': 'Jim'}  # VCR value, we sent 'Michael'!
})

# ✅ AFTER (correct):
response_data = response.json()
check.is_not_none(response_data.get('bookingid'))  # Verify exists
check.equal(response_data['booking']['firstname'], body['firstname'])  # Match sent data
```

**AI Flags Issues:**
- Check the AI analysis JSON for `issues` and `recommendations` fields
- AI flags response assertion problems in recommendations

**See [AI_RANDOMIZATION_LIMITATIONS.md](AI_RANDOMIZATION_LIMITATIONS.md) for:**
- Detailed examples with fixes
- Complete review checklist
- Best practices

---

### Step 5: Run Tests with AI Failure Analysis

```bash
python openapi-python/scripts/run_tests_with_ai_analysis.py openapi-python/test/test_schemathesis/ -v
```

This generates:
- `openapi-python/reports/junit-YYYYMMDDTHHMMSS.xml` - JUnit XML results
- `openapi-python/reports/ai-failure-analysis-YYYYMMDDTHHMMSS.html` - AI analysis report

**AI Failure Analysis Includes:**
- Root cause identification
- **Complete HTTP request details** (method, URL, headers, body with randomized values)
- Similar failure patterns
- Suggested fixes
- Impact assessment

**Optional options:**
- `--max-failures N` - Limit number of failures analyzed
- `--no-analysis` - Skip AI analysis (just run tests)

---

## Complete One-Line Workflow

```bash
# Run complete workflow
python workflow.py

# With options
python workflow.py --skip-ai-filter --skip-run --max-tests 50
```

**Note:** Manual review (Step 4.5) is always required before running tests.

---

## Quick Reference: File Locations

### Configuration
- `config.py` - Main configuration file (all settings)

### Schemathesis Directory
- `schemathesis/restful-booker-oas.yaml` - OpenAPI spec
- `schemathesis/restful_booker_basic_auth.py` - Auth hook
- `schemathesis/reports/vcr-*.yaml` - Generated VCR
- `schemathesis/vcr_to_pytest.py` - VCR converter
- `schemathesis/analyze_vcr_with_ai.py` - AI VCR analyzer
- `schemathesis/scripts/` - Individual workflow step scripts

### OpenAPI-python Directory
- `openapi-python/test/test_schemathesis/` - Generated tests (with AI-generated random values)
- `openapi-python/test/conftest.py` - Shared fixtures
- `openapi-python/test/ai_failure_analyzer.py` - AI failure analyzer
- `openapi-python/test/ai_config.py` - AI config
- `openapi-python/scripts/run_tests_with_ai_analysis.py` - Test runner with AI analysis
- `openapi-python/reports/` - Test reports and analysis

### Main Workflow Script
- `workflow.py` - End-to-end workflow script

---

## Quick Checks

### Schemathesis: Authentication Errors
```bash
# Verify authentication hook is set
echo $SCHEMATHESIS_HOOKS
# Should output: restful_booker_basic_auth

# Check auth hook file exists
ls -la schemathesis/restful_booker_basic_auth.py
```

### VCR Conversion: Module Import Errors
```bash
# Ensure test directory structure exists
mkdir -p openapi-python/test/test_schemathesis
touch openapi-python/test/test_schemathesis/__init__.py
```

### AI Analysis: API Key Issues
```bash
# Check AI config
cat openapi-python/test/ai_config.py | grep GROQ_API_KEY

# Or set environment variable / local file
export GROQ_API_KEY='your-api-key-here'
echo 'your-api-key-here' > .groq_api_key
```

### Test Execution: pytest-check Not Found
```bash
pip install pytest-check
```

---

## Expected Output

After running the complete workflow, you should see:

1. **Schemathesis Output**: Terminal output with test results
2. **VCR File**: `schemathesis/reports/vcr-YYYYMMDDTHHMMSSZ.yaml` with HTTP interactions
3. **AI Analysis Report**: `schemathesis/reports/vcr-YYYYMMDDTHHMMSSZ_analysis_report.txt` (if filtering)
4. **AI Analysis JSON**: `schemathesis/reports/vcr-YYYYMMDDTHHMMSSZ_analysis.json` with:
   - Test filtering decisions
   - **Randomized test data** (actual values)
   - **Response assertion issues** (flagged in recommendations)
5. **Generated Tests**: `openapi-python/test/test_schemathesis/test_phase_*.py` files
   - Tests use **AI-generated random values** (not hardcoded)
   - Example: `body = {'firstname': 'Michael', 'totalprice': 378}`
   - **Response assertions still need manual fixes** (see Step 4.5)
6. **Manual Review**: Fix response assertions before running tests
7. **Test Execution**: pytest output with pass/fail results
8. **AI Failure Analysis**: `openapi-python/reports/ai-failure-analysis-YYYYMMDDTHHMMSS.html` with:
   - Root cause analysis
   - Impact assessment
   - Suggested fixes
   - **Complete HTTP request details** (method, URL, headers, body with randomized values)
   - Similar patterns
