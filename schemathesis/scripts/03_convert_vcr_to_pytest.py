#!/usr/bin/env python3
"""
Step 3: Convert VCR to pytest Tests

This script converts Schemathesis VCR YAML to pytest test files organized by phase.
"""

import sys
import argparse
import os
from pathlib import Path

# All scripts run from the SchemaSense project root
PROJECT_ROOT = Path(__file__).parent.parent.parent
os.chdir(PROJECT_ROOT)

# Add project root to path for imports
sys.path.insert(0, str(PROJECT_ROOT))

from config import (
    SCHEMATHESIS_DIR,
    SCHEMATHESIS_TEST_DIR,
    OPENAPI_PYTHON_TEST_DIR,
    TEST_PHASES,
)

# Import from parent directory
schemathesis_dir = Path(__file__).parent.parent
sys.path.insert(0, str(schemathesis_dir))
from vcr_to_pytest import convert_vcr_to_pytest


def convert_vcr(vcr_file: Path, output_dir: Path, analysis_file: Path = None):
    """Convert VCR file to pytest tests."""
    print("=" * 80)
    print("Step 3: Converting VCR to pytest Tests")
    print("=" * 80)
    
    # Resolve paths relative to the project root
    if not vcr_file.is_absolute():
        vcr_file = PROJECT_ROOT / vcr_file
    else:
        vcr_file = Path(vcr_file)
    
    if not output_dir.is_absolute():
        output_dir = PROJECT_ROOT / output_dir
    else:
        output_dir = Path(output_dir)
    
    if analysis_file and not analysis_file.is_absolute():
        analysis_file = PROJECT_ROOT / analysis_file
    
    if not vcr_file.exists():
        print(f"Error: VCR file not found: {vcr_file}")
        sys.exit(1)
    
    # Ensure output directory exists
    output_dir.mkdir(parents=True, exist_ok=True)
    
    # Convert VCR to pytest (with optional analysis data for randomization)
    convert_vcr_to_pytest(vcr_file, output_dir, analysis_file)
    
    print(f"\n✅ Conversion complete! Tests generated in: {output_dir}")
    print(f"\n📄 Next step: Copy tests to OpenAPI-python project")
    print(f"   python scripts/04_copy_tests_to_openapi.py")


def main():
    """CLI entry point."""
    parser = argparse.ArgumentParser(
        description="Convert Schemathesis VCR YAML to pytest test files"
    )
    parser.add_argument(
        'vcr_file',
        type=Path,
        nargs='?',
        help='Path to VCR YAML file (default: latest in reports/)'
    )
    parser.add_argument(
        '--output-dir',
        type=Path,
        default=SCHEMATHESIS_TEST_DIR,
        help=f'Output directory for test files (default: {SCHEMATHESIS_TEST_DIR})'
    )
    parser.add_argument(
        '--analysis',
        type=Path,
        help='Path to AI analysis JSON file (default: auto-detect based on VCR file)'
    )
    
    args = parser.parse_args()
    
    # Find VCR file if not provided
    vcr_file = args.vcr_file
    if not vcr_file:
        from config import SCHEMATHESIS_REPORTS_DIR, FILTERED_VCR_SUFFIX
        # Try to find filtered VCR first, then any VCR
        filtered_vcr = list(SCHEMATHESIS_REPORTS_DIR.glob(f"*{FILTERED_VCR_SUFFIX}"))
        if filtered_vcr:
            vcr_file = max(filtered_vcr, key=lambda p: p.stat().st_mtime)
            print(f"Using filtered VCR: {vcr_file.relative_to(PROJECT_ROOT)}")
        else:
            all_vcr = list(SCHEMATHESIS_REPORTS_DIR.glob("vcr-*.yaml"))
            if all_vcr:
                vcr_file = max(all_vcr, key=lambda p: p.stat().st_mtime)
                print(f"Using latest VCR: {vcr_file.relative_to(PROJECT_ROOT)}")
            else:
                print("Error: No VCR files found. Run Step 1 first.")
                sys.exit(1)
    else:
        # Resolve relative to the project root
        if not Path(vcr_file).is_absolute():
            vcr_file = PROJECT_ROOT / vcr_file
        else:
            vcr_file = Path(vcr_file)
    
    # Find analysis JSON if not provided
    analysis_file = args.analysis
    if not analysis_file:
        # Try to find analysis JSON matching the VCR file
        # Pattern: vcr-20251107T000204Z_filtered.yaml -> vcr-20251107T000204Z_analysis.json
        vcr_stem = vcr_file.stem.replace('_filtered', '')
        analysis_file = vcr_file.parent / f"{vcr_stem}_analysis.json"
        if analysis_file.exists():
            print(f"Found analysis JSON: {analysis_file.relative_to(PROJECT_ROOT)}")
        else:
            print("No analysis JSON found - using hardcoded VCR values")
            analysis_file = None
    else:
        if not analysis_file.is_absolute():
            analysis_file = PROJECT_ROOT / analysis_file
    
    convert_vcr(vcr_file, args.output_dir, analysis_file)


if __name__ == "__main__":
    main()

