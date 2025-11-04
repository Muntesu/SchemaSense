"""
Unified Configuration for Schemathesis Test Generation and AI Analysis Workflow

This file contains all configuration values used across the workflow.
Extract any hardcoded values to this file for easy maintenance.
"""

import os
from pathlib import Path
from typing import Optional

# Project Paths
# All scripts run from the SchemaSense project root
PROJECT_ROOT = Path(__file__).parent
SCHEMATHESIS_DIR = PROJECT_ROOT / "schemathesis"
OPENAPI_PYTHON_DIR = PROJECT_ROOT / "openapi-python"

# API Configuration
API_BASE_URL = "https://restful-booker.herokuapp.com"
API_USERNAME = os.getenv("API_USERNAME", "admin")
API_PASSWORD = os.getenv("API_PASSWORD", "password123")

# Schemathesis Configuration
SCHEMATHESIS_SPEC_FILE = SCHEMATHESIS_DIR / "restful-booker-oas.yaml"
SCHEMATHESIS_MAX_EXAMPLES = int(os.getenv("SCHEMATHESIS_MAX_EXAMPLES", "5"))
SCHEMATHESIS_WORKERS = int(os.getenv("SCHEMATHESIS_WORKERS", "5"))
SCHEMATHESIS_HOOKS = os.getenv("SCHEMATHESIS_HOOKS", "restful_booker_basic_auth")

# Report Directories
SCHEMATHESIS_REPORTS_DIR = SCHEMATHESIS_DIR / "reports"
OPENAPI_PYTHON_REPORTS_DIR = OPENAPI_PYTHON_DIR / "reports"

# Test Directories
SCHEMATHESIS_TEST_DIR = SCHEMATHESIS_DIR / "test" / "test_schemathesis"
OPENAPI_PYTHON_TEST_DIR = OPENAPI_PYTHON_DIR / "test" / "test_schemathesis"

# AI Configuration
AI_BATCH_SIZE = int(os.getenv("AI_BATCH_SIZE", "10"))  # Reduced from 20 to prevent response truncation with randomization data
AI_MAX_TOKENS_PER_REQUEST = int(os.getenv("AI_MAX_TOKENS_PER_REQUEST", "5000"))
AI_BODY_PREVIEW_LENGTH = int(os.getenv("AI_BODY_PREVIEW_LENGTH", "200"))

# VCR Analysis Configuration
VCR_ANALYSIS_MAX_TESTS = int(os.getenv("VCR_ANALYSIS_MAX_TESTS", "0"))  # 0 = all tests

# Test Generation Configuration
TEST_PHASES = {
    'examples': {
        'class_name': 'TestPhaseExamples',
        'description': 'Examples phase tests - basic functionality from OpenAPI spec',
    },
    'coverage': {
        'class_name': 'TestPhaseCoverage',
        'description': 'Coverage phase tests - edge cases and coverage expansion',
    },
    'fuzzing': {
        'class_name': 'TestPhaseFuzzing',
        'description': 'Fuzzing phase tests - property-based random inputs',
        'note': 'Note: Many tests may expect 500 errors or invalid responses',
    },
    'stateful': {
        'class_name': 'TestPhaseStateful',
        'description': 'Stateful phase tests - multi-step workflows',
    },
}

# File Patterns
VCR_FILE_PATTERN = "vcr-*.yaml"
FILTERED_VCR_SUFFIX = "_filtered.yaml"
ANALYSIS_REPORT_SUFFIX = "_analysis_report.txt"
ANALYSIS_JSON_SUFFIX = "_analysis.json"

# Output File Names
JUNIT_XML_PREFIX = "junit-"
AI_ANALYSIS_HTML_PREFIX = "ai-failure-analysis-"
TESTS_OUTPUT_FILE = "tests_output.txt"

