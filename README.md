# Schemathesis Test Generation and AI Analysis

Automated workflow that turns an OpenAPI specification into executable pytest tests with Groq-powered randomization and Groq-powered failure analysis.

## Overview

This project provides an end-to-end workflow for:
1. Generating property-based tests from the OpenAPI spec using Schemathesis.
2. Using Groq AI to keep valuable tests **and** produce realistic randomized data.
3. Converting the filtered interactions into pytest files with embedded random values.
4. Requiring a manual response-assertion review before executing tests.
5. Running pytest and analyzing failures with Groq to get complete HTTP request details and fixes.

## Quick Start

```bash
# Run complete workflow
python workflow.py

# Run with options
python workflow.py --skip-ai-filter --skip-run --max-tests 50
```

## Workflow Steps

1. **Generate Schemathesis Tests** – Produce VCR, JUnit, and HAR outputs.
2. **Analyze VCR with AI** – Filter tests and obtain randomized request data (actual values).
3. **Convert VCR to pytest** – Generate pytest files that embed the AI-provided data.
4. **Copy Tests to `openapi-python`** – Place generated tests where pytest will execute them.
5. **Manual Review (Required)** – Update response assertions to match the randomized data.
6. **Run Tests with AI Analysis** – Execute pytest and analyze failures with Groq.

### ✨ AI-Powered Data Randomization

The AI analysis provides randomized test data to eliminate hardcoded values:
- **Groq analyzes** each test and determines what data should be randomized
- **Smart decisions**: Randomizes user data (names, prices, dates), keeps credentials static
- **Actual values**: Generates realistic random data like `{'firstname': 'Michael', 'totalprice': 378}`
- **Flags issues**: Alerts you when response assertions need updating (critical!)

⚠️ **Important**: AI randomization generates request data but **cannot update response assertions**. Manual review is REQUIRED to fix response validation. See [AI_RANDOMIZATION_LIMITATIONS.md](AI_RANDOMIZATION_LIMITATIONS.md) for details.

## Individual Step Scripts

### Step 1: Generate Schemathesis Tests
```bash
python schemathesis/scripts/01_generate_schemathesis_tests.py
```

### Step 2: Analyze VCR with AI
```bash
python schemathesis/scripts/02_analyze_vcr_with_ai.py schemathesis/reports/vcr-*.yaml [--max-tests N]
```

### Step 3: Convert VCR to pytest
```bash
python schemathesis/scripts/03_convert_vcr_to_pytest.py [vcr_file] [--analysis analysis.json]
```

**Note**: If `--analysis` is not provided, the script will auto-detect the analysis JSON file based on the VCR filename. For example, `vcr-20251107T000204Z_filtered.yaml` will look for `vcr-20251107T000204Z_analysis.json`.

### Step 4: Copy Tests to OpenAPI-python
```bash
python schemathesis/scripts/04_copy_tests_to_openapi.py
```

### Step 4.5: Manual Review (Required)

⚠️ **Critical** – AI randomizes requests but cannot update response assertions.

- Replace hardcoded VCR comparisons with checks that confirm server-generated fields exist and responses echo the randomized values you sent.
- Align GET filters, IDs, and stateful flows with the data created earlier in the suite.
- Ensure DELETE/PUT/PATCH tests create or reuse valid resources before acting on them.

Use [AI_RANDOMIZATION_LIMITATIONS.md](AI_RANDOMIZATION_LIMITATIONS.md) for detailed examples, a review checklist, and best practices.

### Step 5: Run Tests with AI Analysis
```bash
python openapi-python/scripts/run_tests_with_ai_analysis.py openapi-python/test/test_schemathesis/ -v
```

## Configuration

All configuration is centralized in `config.py`:

- **API Configuration**: Base URL, username, password
- **Schemathesis Configuration**: Max examples, workers, hooks, spec file
- **AI Configuration**: Batch sizes, token limits, body preview length
- **Path Configuration**: All directories (reports, tests, etc.)
- **Test Phase Configuration**: Phase names, descriptions, class names

Environment variables can override config values:
```bash
export API_USERNAME="your-username"
export API_PASSWORD="your-password"
export SCHEMATHESIS_MAX_EXAMPLES="10"
export AI_BATCH_SIZE="30"
```

## Prerequisites

```bash
# Install dependencies
pip install schemathesis pytest pyyaml groq pytest-check

# Provide the Groq API key (required for AI analysis)
# Option A: export in your shell
export GROQ_API_KEY='your-api-key-here'

# Option B: save it to a local file (ignored by git)
echo 'your-api-key-here' > .groq_api_key
# In GitHub Actions, set GROQ_API_KEY as a repository secret.
```

## Output Files

### Schemathesis Directory (`schemathesis/reports/`)
- `vcr-*.yaml` - VCR cassette with HTTP interactions
- `vcr-*_filtered.yaml` - Filtered VCR (if AI filtering used)
- `vcr-*_analysis_report.txt` - AI analysis report
- `vcr-*_analysis.json` - Machine-readable analysis
- `junit-*.xml` - Test results
- `tests_output.txt` - Terminal output

### OpenAPI-python Directory (`openapi-python/`)
- `test/test_schemathesis/test_phase_*.py` - Generated test files
- `reports/ai-failure-analysis-*.html` - AI failure analysis report
- `reports/junit-*.xml` - Test results

## Configuration Files

- `config.py` - Main configuration (all settings)
- `schemathesis/schemathesis.toml` - Schemathesis settings
- `schemathesis/schemathesis.env` - Environment variables
- `openapi-python/test/ai_config.py` - AI API configuration

## Workflow Options

```bash
# Skip AI filtering (use original VCR without randomized data)
python workflow.py --skip-ai-filter

# Skip pytest + AI failure analysis
python workflow.py --skip-run

# Limit Groq analysis to N tests
python workflow.py --max-tests 50
```
