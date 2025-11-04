# Architecture Documentation

Technical architecture and component relationships for the **Schemathesis → Groq AI → pytest → Groq failure analysis** workflow.

## Overview

The current project implements a single automated flow:
- **Schemathesis** generates HTTP interactions from the OpenAPI specification.
- **Groq AI** filters valuable tests and produces randomized, production-like data.
- **pytest** executes the generated tests after a required manual response-assertion review.
- **Groq AI Failure Analysis** triages pytest failures with complete request context.

## System Architecture

```
┌─────────────────────────────────────────────────────────────┐
│                    API Under Test                           │
│     Restful-Booker (https://restful-booker.herokuapp.com)   │
└─────────────────────────────────────────────────────────────┘
                            ▲
                            │
                       Schemathesis
                            │
                            ▼
┌─────────────────────────────────────────────────────────────┐
│ Step 1: Schemathesis Run                                    │
│ • Script: schemathesis/scripts/01_generate_schemathesis_tests.py │
│ • Output: VCR + JUnit + HAR in schemathesis/reports/        │
└─────────────────────────────────────────────────────────────┘
                            │
                            ▼
┌─────────────────────────────────────────────────────────────┐
│ Step 2: Groq AI Analysis                                    │
│ • Script: schemathesis/scripts/02_analyze_vcr_with_ai.py     │
│ • Output: filtered VCR + analysis JSON (randomized values)  │
└─────────────────────────────────────────────────────────────┘
                            │
                            ▼
┌─────────────────────────────────────────────────────────────┐
│ Step 3: VCR → pytest Conversion                             │
│ • Script: schemathesis/scripts/03_convert_vcr_to_pytest.py   │
│ • Output: pytest tests with embedded random values           │
└─────────────────────────────────────────────────────────────┘
                            │
                            ▼
┌─────────────────────────────────────────────────────────────┐
│ Step 4: Copy to openapi-python                              │
│ • Script: schemathesis/scripts/04_copy_tests_to_openapi.py   │
│ • Output: openapi-python/test/test_schemathesis/*.py         │
└─────────────────────────────────────────────────────────────┘
                            │
                            ▼
┌─────────────────────────────────────────────────────────────┐
│ ⚠ Step 5: Manual Response-Assertion Review (Required)       │
│ • Update assertions to match randomized request data         │
│ • Checklist: AI_RANDOMIZATION_LIMITATIONS.md                 │
└─────────────────────────────────────────────────────────────┘
                            │
                            ▼
┌─────────────────────────────────────────────────────────────┐
│ Step 6: pytest + Groq Failure Analysis                      │
│ • Script: openapi-python/scripts/run_tests_with_ai_analysis.py │
│ • Output: JUnit XML + HTML report (full HTTP requests)      │
└─────────────────────────────────────────────────────────────┘
```

## Component Details

### 1. Schemathesis (Property-Based Testing)

**Purpose**: Automatically generate HTTP interactions from the OpenAPI specification.

**Components**:
- OpenAPI spec: `schemathesis/restful-booker-oas.yaml`
- Authentication hook: `schemathesis/restful_booker_basic_auth.py`
- Execution scripts: `schemathesis/scripts/01_generate_*.py`
- Groq analysis integration: `schemathesis/analyze_vcr_with_ai.py`
- Converter: `schemathesis/vcr_to_pytest.py`
- Reports: `schemathesis/reports/` (ignored by git)

**Key Features**:
- Generates Schemathesis phases (examples, coverage, fuzzing, stateful).
- Produces VCR/YAML, HAR, and JUnit XML outputs.
- Feeds Groq AI with test metadata to obtain randomized request data and value assessments.

**Integration**:
- Groq analysis JSON provides actual randomized values (e.g., `"firstname": "Michael"`).
- VCR converter injects those values into pytest tests.
- Tests are copied into `openapi-python/test/test_schemathesis/`.
- Manual response-assertion updates are required before running pytest.

### 2. Groq AI Failure Analyzer

**Purpose**: Deliver AI-assisted triage with complete request context and actionable fixes.

**Components**:
- Analyzer: `openapi-python/test/ai_failure_analyzer.py`
- Config: `openapi-python/test/ai_config.py`
- Runner: `openapi-python/scripts/run_tests_with_ai_analysis.py`
- Reports: `openapi-python/reports/` (HTML + JUnit XML, ignored by git)

**Key Features**:
- Parses pytest JUnit XML output.
- Extracts executed HTTP requests (method, URL, headers, body) for each failure.
- Calls Groq API for root cause, impact, suggested fix, and similar patterns.
- Renders HTML reports with complete request payloads and response summaries.
- Supports `--max-failures` and `--no-analysis` flags.

**Integration**:
- Designed for Schemathesis-generated tests in `openapi-python/test/test_schemathesis/`.
+- Relies on randomized request bodies embedded in tests during conversion.
- Highlights response-assertion issues in recommendations when randomized data and recorded responses diverge.

## End-to-End Flow

```
1. Schemathesis run (01_generate_schemathesis_tests.py)
   • Produces VCR/JUnit/HAR in schemathesis/reports/

2. Groq AI analysis (02_analyze_vcr_with_ai.py)
   • Generates filtered VCR + analysis JSON with actual randomized values

3. VCR → pytest conversion (03_convert_vcr_to_pytest.py)
   • Embeds AI-provided values directly into pytest tests

4. Copy tests (04_copy_tests_to_openapi.py)
   • Places tests in openapi-python/test/test_schemathesis/

5. Manual response-assertion review (required)
   • Update assertions to check server-generated IDs for existence
   • Ensure responses match randomized request data
   • Checklist: AI_RANDOMIZATION_LIMITATIONS.md

6. pytest + Groq failure analysis (run_tests_with_ai_analysis.py)
   • Runs tests, outputs JUnit XML, builds HTML report with full HTTP request details
```

## Shared Infrastructure

### Configuration (`config.py` & pytest fixtures)

- Global settings live in `SchemaSense/config.py`:
  - Path definitions (`SCHEMATHESIS_REPORTS_DIR`, `OPENAPI_PYTHON_TEST_DIR`, etc.).
  - Groq API configuration (`GROQ_API_URL`, `GROQ_MODEL`, `MAX_TOKENS`, `AI_BATCH_SIZE=10`).
  - Filename suffixes (`FILTERED_VCR_SUFFIX`, `ANALYSIS_SUFFIX`).
- `openapi-python/test/conftest.py` supplies pytest fixtures:
  - `base_url` – Base API endpoint (defaults to Restful-Booker).
  - `auth_basic_header` – Convenience fixture for Basic Auth.
  - Extendable for shared helpers.

### Manual Review Checklist

Documented in `AI_RANDOMIZATION_LIMITATIONS.md`:
1. **Response Assertions (Critical)** – Replace hard-coded VCR comparisons with checks against randomized data.
2. **Server-generated IDs** – Assert existence instead of specific values.
3. **GET filters** – Ensure filters use data created earlier in the suite.
4. **DELETE/PUT/PATCH** – Create prerequisite entities before deleting/updating.
5. **Stateful flows** – Note current limitation (AI treats tests independently).

## Project Structure (Relevant Paths)

```
SchemaSense/
├── config.py                        # Global configuration (Groq, paths, batch sizes)
├── workflow.py                      # Orchestrates the full workflow
├── schemathesis/
│   ├── scripts/01_generate_schemathesis_tests.py
│   ├── scripts/02_analyze_vcr_with_ai.py
│   ├── scripts/03_convert_vcr_to_pytest.py
│   ├── scripts/04_copy_tests_to_openapi.py
│   ├── analyze_vcr_with_ai.py       # Groq integration logic
│   ├── vcr_to_pytest.py             # VCR → pytest conversion
│   └── reports/                     # Schemathesis outputs (ignored by git)
├── openapi-python/
│   ├── test/
│   │   ├── test_schemathesis/       # Generated pytest files with random data
│   │   ├── conftest.py              # Shared fixtures/config
│   │   └── ai_failure_analyzer.py   # Groq-powered failure analysis
│   ├── scripts/run_tests_with_ai_analysis.py
│   └── reports/                     # JUnit + HTML reports (ignored by git)
├── docs/
│   ├── ARCHITECTURE.md              # (This file)
│   ├── WORKFLOWS.md                 # Detailed workflow guide
│   └── CONFIGURATION.md             # Configuration reference
└── AI_RANDOMIZATION_LIMITATIONS.md  # Manual review checklist & known limitations
```

## Technology Stack

### Testing & Automation
- **Schemathesis** – Generates scenarios across examples, coverage, fuzzing, stateful phases.
- **pytest** – Executes generated tests with soft assertions via `pytest-check`.

### AI/ML
- **Groq API** – High-throughput LLM inference used for:
  - Test value classification and filtering.
  - Randomized data generation (actual values, not code).
  - Highlighting response assertion risks in recommendations.
  - Failure analysis and complete request reconstruction.

### Python Libraries
- **requests** – Executes HTTP requests in generated pytest tests.
- **pytest-check** – Provides soft assertions to continue execution after failures.
- **pyyaml** – Parses VCR cassettes during conversion.
- **dataclasses/json** – Handles AI analysis payloads.

## Related Documentation

- [README.md](../README.md) – Project overview.
- [COMPLETE_WORKFLOW.md](../COMPLETE_WORKFLOW.md) – Step-by-step command guide.
- [WORKFLOWS.md](WORKFLOWS.md) – Detailed workflow walkthroughs.
- [CONFIGURATION.md](CONFIGURATION.md) – Configuration reference.
- [AI_RANDOMIZATION_LIMITATIONS.md](../AI_RANDOMIZATION_LIMITATIONS.md) – Manual review checklist & limitations.

