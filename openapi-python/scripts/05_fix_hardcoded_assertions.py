#!/usr/bin/env python3
"""
Step 5: Fix Hardcoded Assertions

This script fixes hardcoded data assertions in generated Schemathesis test files.
"""

import sys
import os
from pathlib import Path

# All scripts run from the SchemaSense project root
PROJECT_ROOT = Path(__file__).parent.parent.parent

# Change to project root first
os.chdir(PROJECT_ROOT)

# Add project root to path for imports (absolute path for consistency)
sys.path.insert(0, str(PROJECT_ROOT.resolve()))

try:
    from config import OPENAPI_PYTHON_TEST_DIR
except ImportError:
    # Fallback if config not available
    OPENAPI_PYTHON_TEST_DIR = PROJECT_ROOT / "openapi-python" / "test" / "test_schemathesis"

# Import from openapi-python directory
openapi_dir = Path(__file__).parent.parent
sys.path.insert(0, str(openapi_dir))
from fix_hardcoded_assertions import fix_hardcoded_assertions


def fix_assertions():
    """Fix hardcoded assertions in test files."""
    print("=" * 80)
    print("Step 5: Fixing Hardcoded Assertions")
    print("=" * 80)
    
    if not OPENAPI_PYTHON_TEST_DIR.exists():
        print(f"Error: Test directory not found: {OPENAPI_PYTHON_TEST_DIR}")
        sys.exit(1)
    
    test_files = list(OPENAPI_PYTHON_TEST_DIR.glob("test_phase_*.py"))
    if not test_files:
        print(f"No test files found in {OPENAPI_PYTHON_TEST_DIR}")
        sys.exit(1)
    
    total_changes = 0
    for test_file in test_files:
        print(f"Processing {test_file.name}...")
        try:
            content = test_file.read_text(encoding='utf-8')
            original = content
            content = fix_hardcoded_assertions(content)
            
            if content != original:
                test_file.write_text(content, encoding='utf-8')
                print(f"  ✓ Updated {test_file.name}")
                total_changes += 1
            else:
                print(f"  - No changes needed for {test_file.name}")
        except Exception as e:
            print(f"  ✗ Error processing {test_file.name}: {e}")
    
    print(f"\n✅ Processed {len(test_files)} file(s), updated {total_changes} file(s).")
    print(f"\n📄 Next step: Run tests with AI analysis")
    print(f"   python scripts/06_run_tests_with_ai_analysis.py test/test_schemathesis/ -v")


if __name__ == "__main__":
    fix_assertions()

