# Groq Analysis of Schemathesis VCR Files

`schemathesis/scripts/02_analyze_vcr_with_ai.py` uses Groq to evaluate Schemathesis interactions, keep the valuable ones, and provide randomized request data that replaces the hardcoded values recorded in the VCR cassette.

## What the Script Produces

For each VCR file (`vcr-YYYYMMDDTHHMMSSZ.yaml`) the script writes three artifacts to `schemathesis/reports/`:

1. `vcr-*_filtered.yaml` – The original VCR with only the retained interactions.
2. `vcr-*_analysis.json` – Machine-readable analysis containing:
   - `should_keep`, `value_level`, `reason`
   - `randomized_request_data` (actual values, no code)
   - `issues` / `recommendations` (response assertion guidance, edge cases)
3. `vcr-*_analysis_report.txt` – Human-readable summary.

## Running the Script

```bash
cd SchemaSense
python schemathesis/scripts/02_analyze_vcr_with_ai.py schemathesis/reports/vcr-*.yaml

# Limit the number of interactions analyzed
python schemathesis/scripts/02_analyze_vcr_with_ai.py schemathesis/reports/vcr-*.yaml --max-tests 50

# Generate report only (skip filtered VCR)
python schemathesis/scripts/02_analyze_vcr_with_ai.py schemathesis/reports/vcr-*.yaml --no-filter
```

The script auto-detects the analysis JSON when `03_convert_vcr_to_pytest.py` runs, so no extra wiring is needed.

## Why the Analysis Matters

- **Randomized data**: Eliminates hardcoded request bodies and gives each test realistic values (names, prices, dates).
- **Response assertion guidance**: Flags where assertions must be updated to avoid comparing against stale VCR responses (e.g., server-generated IDs).
- **Value scoring**: Enables smaller, higher-value test suites when desired.

## Downstream Usage

`03_convert_vcr_to_pytest.py` consumes the analysis JSON to:
- Embed the randomized request data into new pytest files.
- Group tests by phase (`test_phase_examples.py`, `test_phase_coverage.py`, etc.).
- Carry Groq recommendations forward as comments for manual review.

After copying the tests into `openapi-python/test/test_schemathesis/`, follow the manual review checklist in [AI_RANDOMIZATION_LIMITATIONS.md](../AI_RANDOMIZATION_LIMITATIONS.md) before executing pytest.

## Related Resources

- [vcr_to_pytest.py](vcr_to_pytest.py) – Conversion logic.
- [README.md](../README.md) – Full workflow overview.
- [COMPLETE_WORKFLOW.md](../COMPLETE_WORKFLOW.md) – Command-by-command reference.

