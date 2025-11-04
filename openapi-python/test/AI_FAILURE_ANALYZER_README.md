# AI Failure Analyzer

# AI Failure Analyzer

Analyze pytest failures with Groq to obtain root causes, impact, fixes, and the exact HTTP requests that triggered the errors.

## Setup

1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
2. Obtain a Groq API key (https://console.groq.com) and either export it or place it in `.groq_api_key` at the project root:
   ```bash
   export GROQ_API_KEY='your-api-key-here'
   # or
   echo 'your-api-key-here' > .groq_api_key
   ```
   Groq’s free tier currently allows 14,400 requests per day.
   In GitHub Actions, define `GROQ_API_KEY` as a repository secret and pass it via `env`.

## Usage

### Integrated Runner (Recommended)

```bash
cd SchemaSense
python openapi-python/scripts/run_tests_with_ai_analysis.py openapi-python/test/test_schemathesis/ -v

# Limit Groq analysis to the first N failures
python openapi-python/scripts/run_tests_with_ai_analysis.py openapi-python/test/test_schemathesis/ -v --max-failures 5

# Skip Groq analysis (pytest only)
python openapi-python/scripts/run_tests_with_ai_analysis.py openapi-python/test/test_schemathesis/ -v --no-analysis
```

Outputs:
- `openapi-python/reports/junit-YYYYMMDDTHHMMSS.xml`
- `openapi-python/reports/ai-failure-analysis-YYYYMMDDTHHMMSS.html`

## Report Format

Each failure entry includes:
1. Test metadata (module, class, function).
2. Error summary and traceback snippet.
3. Full HTTP request (method, URL, headers, body) reconstructed from the test.
4. Root cause, impact, and suggested fix from Groq.
5. Similar failure patterns detected in the suite.

## Configuration

Key settings (modifiable via `config.py` or `test/ai_config.py`):
- `GROQ_MODEL = "llama-3.1-8b-instant"`
- `MAX_TOKENS = 16000`
- `TEMPERATURE = 0.1`
- `AI_BATCH_SIZE = 10`
