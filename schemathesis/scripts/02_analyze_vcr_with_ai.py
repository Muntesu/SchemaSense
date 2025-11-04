#!/usr/bin/env python3
"""
Step 2: Analyze VCR with AI to Filter Tests

This script analyzes Schemathesis VCR YAML using Groq AI to determine which tests
bring value and should be kept vs which can be skipped.
"""

import sys
import argparse
import os
from pathlib import Path
from typing import Optional

# All scripts run from the SchemaSense project root
PROJECT_ROOT = Path(__file__).parent.parent.parent
os.chdir(PROJECT_ROOT)

# Add project root to path for imports
schemathesis_dir = Path(__file__).parent.parent
sys.path.insert(0, str(PROJECT_ROOT / "openapi-python" / "test"))
sys.path.insert(0, str(PROJECT_ROOT))

from config import (
    SCHEMATHESIS_REPORTS_DIR,
    AI_BATCH_SIZE,
    VCR_ANALYSIS_MAX_TESTS,
    FILTERED_VCR_SUFFIX,
    ANALYSIS_REPORT_SUFFIX,
    ANALYSIS_JSON_SUFFIX,
)

# Import from parent directory
sys.path.insert(0, str(schemathesis_dir))
from analyze_vcr_with_ai import VCRAnalyzer


def analyze_vcr(vcr_file: Path, max_tests: Optional[int] = None, no_filter: bool = False):
    """Analyze VCR file with AI and generate filtered VCR."""
    print("=" * 80)
    print("Step 2: Analyzing VCR with AI")
    print("=" * 80)
    
    # Resolve path relative to project root
    if not vcr_file.is_absolute():
        vcr_file = PROJECT_ROOT / vcr_file
    else:
        vcr_file = Path(vcr_file)
    
    if not vcr_file.exists():
        print(f"Error: VCR file not found: {vcr_file}")
        sys.exit(1)
    
    # Default output paths
    output_file = vcr_file.parent / f"{vcr_file.stem}{FILTERED_VCR_SUFFIX}"
    report_file = vcr_file.parent / f"{vcr_file.stem}{ANALYSIS_REPORT_SUFFIX}"
    json_file = vcr_file.parent / f"{vcr_file.stem}{ANALYSIS_JSON_SUFFIX}"
    
    try:
        analyzer = VCRAnalyzer()
        
        # Load VCR
        vcr_data = analyzer.load_vcr_file(vcr_file)
        
        # Extract tests
        tests = analyzer.extract_tests_from_vcr(vcr_data)
        print(f"Extracted {len(tests)} tests from VCR")
        
        # Analyze with AI
        max_tests = max_tests or VCR_ANALYSIS_MAX_TESTS or None
        analyzer.analyze_tests(tests, max_tests=max_tests, verbose=True, batch_size=AI_BATCH_SIZE)
        
        # Generate report
        report = analyzer.generate_report(output_file=report_file)
        print("\n" + "=" * 80)
        print(report[:2000])  # Print first part of report
        print("...")
        print("=" * 80)
        
        # Save JSON
        analyzer.save_analysis_json(json_file)
        
        # Generate filtered VCR
        if not no_filter:
            analyzer.generate_filtered_vcr(vcr_data, output_file)
            print(f"\n✅ Analysis complete! Filtered VCR: {output_file}")
            return output_file
        else:
            print(f"\n✅ Analysis complete! Report: {report_file}")
            return vcr_file  # Return original if no filtering
            
    except Exception as e:
        print(f"Error: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)


def main():
    """CLI entry point."""
    parser = argparse.ArgumentParser(
        description="Analyze Schemathesis VCR YAML using Groq AI to filter tests"
    )
    parser.add_argument(
        'vcr_file',
        type=Path,
        help='Path to Schemathesis VCR YAML file'
    )
    parser.add_argument(
        '--max-tests',
        type=int,
        default=None,
        help='Maximum number of tests to analyze (default: all)'
    )
    parser.add_argument(
        '--no-filter',
        action='store_true',
        help='Only generate report, do not create filtered VCR'
    )
    parser.add_argument(
        '--batch-size',
        type=int,
        default=AI_BATCH_SIZE,
        help=f'Number of tests per batch (default: {AI_BATCH_SIZE})'
    )
    
    args = parser.parse_args()
    
    # Check if VCR file uses glob pattern
    vcr_file = args.vcr_file
    if '*' in str(vcr_file):
        # Find latest VCR file matching pattern
        pattern = Path(vcr_file).name
        vcr_files = list(SCHEMATHESIS_REPORTS_DIR.glob(pattern))
        if vcr_files:
            vcr_file = max(vcr_files, key=lambda p: p.stat().st_mtime)
            print(f"Using latest VCR file: {vcr_file.relative_to(PROJECT_ROOT)}")
        else:
            print(f"Error: No VCR files found matching pattern: {args.vcr_file}")
            sys.exit(1)
    else:
        # Resolve relative to the project root
        if not Path(vcr_file).is_absolute():
            vcr_file = PROJECT_ROOT / vcr_file
        else:
            vcr_file = Path(vcr_file)
    
    result_file = analyze_vcr(vcr_file, max_tests=args.max_tests, no_filter=args.no_filter)
    
    if result_file:
        print(f"\n📄 Next step: Convert VCR to pytest tests")
        print(f"   python scripts/03_convert_vcr_to_pytest.py {result_file}")


if __name__ == "__main__":
    from typing import Optional
    import os
    main()

