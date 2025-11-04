#!/usr/bin/env python3
"""
Step 4: Copy Tests to OpenAPI-python Project

This script copies generated Schemathesis tests to the OpenAPI-python project.
"""

import sys
import shutil
import os
from pathlib import Path

# All scripts run from the SchemaSense project root
PROJECT_ROOT = Path(__file__).parent.parent.parent
os.chdir(PROJECT_ROOT)

# Add project root to path for imports
sys.path.insert(0, str(PROJECT_ROOT))

from config import (
    SCHEMATHESIS_TEST_DIR,
    OPENAPI_PYTHON_TEST_DIR,
)


def copy_tests():
    """Copy generated tests to OpenAPI-python project."""
    print("=" * 80)
    print("Step 4: Copying Tests to OpenAPI-python Project")
    print("=" * 80)
    
    if not SCHEMATHESIS_TEST_DIR.exists():
        print(f"Error: Source directory not found: {SCHEMATHESIS_TEST_DIR}")
        print("Run Step 3 first to generate tests.")
        sys.exit(1)
    
    # Ensure destination directory exists
    OPENAPI_PYTHON_TEST_DIR.mkdir(parents=True, exist_ok=True)
    
    # Copy test files
    test_files = list(SCHEMATHESIS_TEST_DIR.glob("test_phase_*.py"))
    if not test_files:
        print(f"Error: No test files found in {SCHEMATHESIS_TEST_DIR}")
        sys.exit(1)
    
    copied = 0
    for test_file in test_files:
        dest_file = OPENAPI_PYTHON_TEST_DIR / test_file.name
        shutil.copy2(test_file, dest_file)
        print(f"  ✓ Copied {test_file.name}")
        copied += 1
    
    # Ensure __init__.py exists
    init_file = OPENAPI_PYTHON_TEST_DIR / "__init__.py"
    if not init_file.exists():
        init_file.write_text("# Schemathesis generated tests organized by phase\n")
        print(f"  ✓ Created {init_file.name}")
    
    print(f"\n✅ Copied {copied} test file(s) to {OPENAPI_PYTHON_TEST_DIR}")
    print("\n📄 Next step: Review response assertions (see AI_RANDOMIZATION_LIMITATIONS.md)")


if __name__ == "__main__":
    copy_tests()

