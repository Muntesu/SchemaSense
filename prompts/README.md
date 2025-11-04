# LLM Prompts

This directory contains the two prompts that support the Schemathesis → Groq → pytest workflow.

## Available Prompts

### 1. [analyze_vcr_tests.md](analyze_vcr_tests.md)
- **Goal**: Ask an LLM (or Groq) to evaluate Schemathesis VCR interactions, keep the valuable ones, and produce randomized request data plus recommendations.
- **Use it when**: You want to adjust or regenerate the Groq prompt used by `schemathesis/scripts/02_analyze_vcr_with_ai.py`.
- **Outputs**: JSON structure with `should_keep`, `randomized_request_data`, `issues`, and `recommendations`.

### 2. [vcr_to_pytest.md](vcr_to_pytest.md)
- **Goal**: Convert Schemathesis VCR cassettes into pytest files that group tests by phase, use soft assertions, and embed randomized data.
- **Use it when**: You need to modify or rebuild `schemathesis/vcr_to_pytest.py`.
- **Outputs**: Executable pytest code organized by Schemathesis phases.

## How to Use These Prompts

1. Copy the prompt file.
2. Provide current context (file paths, example snippets) to the LLM.
3. Review the generated code or changes.
4. Run the workflow scripts to verify everything still passes.

## Related Documentation

- [README.md](../README.md) – Project overview.
- [ARCHITECTURE.md](../docs/ARCHITECTURE.md) – Component relationships.
- [WORKFLOWS.md](../docs/WORKFLOWS.md) – Step-by-step workflow guide.
- [CONFIGURATION.md](../docs/CONFIGURATION.md) – Groq and Schemathesis configuration.
