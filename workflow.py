#!/usr/bin/env python3
"""
Main End-to-End Workflow Script

This script runs the complete Schemathesis test generation and AI analysis workflow:
1. Generate Schemathesis tests with VCR output
2. Analyze VCR with AI to filter tests (optional)
3. Convert VCR to pytest tests
4. Copy tests to the OpenAPI-python project
5. (Manual) Review and fix response assertions
6. Run tests with AI failure analysis

Usage:
    python workflow.py [--skip-ai-filter] [--skip-run]
"""

import sys
import argparse
import subprocess
import os
from pathlib import Path

# All scripts run from the SchemaSense project root
PROJECT_ROOT = Path(__file__).parent
os.chdir(PROJECT_ROOT)

# Add project root to path
sys.path.insert(0, str(PROJECT_ROOT))

from config import (
    PROJECT_ROOT,
    SCHEMATHESIS_DIR,
    SCHEMATHESIS_REPORTS_DIR,
    SCHEMATHESIS_TEST_DIR,
    OPENAPI_PYTHON_TEST_DIR,
    FILTERED_VCR_SUFFIX,
)


def run_step(step_name: str, script_path: Path, *args, cwd: Path = None):
    """Run a workflow step script."""
    print("\n" + "=" * 80)
    print(f"Running: {step_name}")
    print("=" * 80)
    
    # Resolve script path relative to project root
    if not script_path.is_absolute():
        script_path = PROJECT_ROOT / script_path
    else:
        script_path = Path(script_path)
    
    if not script_path.exists():
        print(f"Error: Script not found: {script_path}")
        return False
    
    cmd = [sys.executable, str(script_path)] + list(args)
    
    try:
        result = subprocess.run(
            cmd,
            cwd=cwd or PROJECT_ROOT,
            check=False,
            capture_output=False
        )
        result = subprocess.run(
            cmd,
            cwd=cwd or PROJECT_ROOT,
            check=False,
            capture_output=False
        )
        
        if result.returncode != 0:
            print(f"\n⚠️  Step '{step_name}' exited with code {result.returncode}")
            return False
        
        return True
    except Exception as e:
        print(f"Error running {step_name}: {e}")
        return False


def main():
    """Main workflow execution."""
    parser = argparse.ArgumentParser(
        description="Run complete Schemathesis test generation and AI analysis workflow"
    )
    parser.add_argument(
        "--skip-ai-filter",
        action="store_true",
        help="Skip AI filtering step (use original VCR)"
    )
    parser.add_argument(
        "--skip-run",
        action="store_true",
        help="Skip running tests with AI analysis"
    )
    parser.add_argument(
        "--max-tests",
        type=int,
        default=None,
        help="Maximum number of tests to analyze (for AI filtering)"
    )
    
    args = parser.parse_args()
    
    print("=" * 80)
    print("Schemathesis Test Generation and AI Analysis Workflow")
    print("=" * 80)
    
    steps = []
    
    # Step 1: Generate Schemathesis tests
    steps.append((
        "Step 1: Generate Schemathesis Tests",
        Path("schemathesis/scripts/01_generate_schemathesis_tests.py"),
        PROJECT_ROOT
    ))
    
    # Step 2: Analyze VCR with AI (optional)
    if not args.skip_ai_filter:
        analyze_args = []
        if args.max_tests:
            analyze_args.extend(["--max-tests", str(args.max_tests)])
        steps.append((
            "Step 2: Analyze VCR with AI",
            Path("schemathesis/scripts/02_analyze_vcr_with_ai.py"),
            PROJECT_ROOT,
            analyze_args
        ))
    else:
        print("\n⚠️  Skipping AI filtering step (using original VCR)")
    
    # Step 3: Convert VCR to pytest
    steps.append((
        "Step 3: Convert VCR to pytest",
        Path("schemathesis/scripts/03_convert_vcr_to_pytest.py"),
        PROJECT_ROOT
    ))
    
    # Step 4: Copy tests to OpenAPI-python
    steps.append((
        "Step 4: Copy Tests to OpenAPI-python",
        Path("schemathesis/scripts/04_copy_tests_to_openapi.py"),
        PROJECT_ROOT
    ))
    
    # Step 5: Run tests with AI analysis (optional)
    if not args.skip_run:
        steps.append((
            "Step 5: Run Tests with AI Analysis",
            Path("openapi-python/scripts/run_tests_with_ai_analysis.py"),
            PROJECT_ROOT,
            ["openapi-python/test/test_schemathesis/", "-v"]
        ))
    else:
        print("\n⚠️  Skipping test execution")
    
    # Execute all steps
    failed_steps = []
    for step_info in steps:
        if len(step_info) == 3:
            step_name, script_path, cwd = step_info
            step_args = []
        else:
            step_name, script_path, cwd, *step_args = step_info
            step_args = step_args[0] if step_args else []
        
        success = run_step(step_name, script_path, *step_args, cwd=cwd)
        
        if not success:
            failed_steps.append(step_name)
            print(f"\n❌ Step failed: {step_name}")
            response = input("Continue with remaining steps? (y/n): ")
            if response.lower() != 'y':
                print("\n❌ Workflow aborted by user")
                sys.exit(1)
        else:
            if step_name == "Step 4: Copy Tests to OpenAPI-python":
                print("\n" + "-" * 80)
                print("⚠️  Manual Review Required Before Running Tests")
                print("-" * 80)
                print(
                    "The generated tests now include AI-randomized request data, but response\n"
                    "assertions still reflect the original VCR recordings. Review and update\n"
                    "response assertions to verify:\n"
                    "  • Server-generated fields exist (e.g., booking IDs)\n"
                    "  • Responses echo the randomized request data you send\n"
                    "Skipping this manual review will cause test failures or false positives."
                )
                if not args.skip_run:
                    input("\nPress Enter once manual review is complete to continue...")
    
    # Summary
    print("\n" + "=" * 80)
    if failed_steps:
        print(f"⚠️  Workflow completed with {len(failed_steps)} failed step(s):")
        for step in failed_steps:
            print(f"  - {step}")
    else:
        print("✅ Workflow completed successfully!")
    print("=" * 80)
    
    # Show generated files
    print("\n📁 Generated Files:")
    
    # VCR files
    vcr_files = list(SCHEMATHESIS_REPORTS_DIR.glob("vcr-*.yaml"))
    if vcr_files:
        latest_vcr = max(vcr_files, key=lambda p: p.stat().st_mtime)
        print(f"  VCR: {latest_vcr}")
        
        filtered_vcr = latest_vcr.parent / f"{latest_vcr.stem}{FILTERED_VCR_SUFFIX}"
        if filtered_vcr.exists():
            print(f"  Filtered VCR: {filtered_vcr}")
    
    # Test files
    test_files = list(OPENAPI_PYTHON_TEST_DIR.glob("test_phase_*.py"))
    if test_files:
        print(f"  Tests: {len(test_files)} file(s) in {OPENAPI_PYTHON_TEST_DIR}")
    
    # Reports
    from config import OPENAPI_PYTHON_REPORTS_DIR
    html_reports = list(OPENAPI_PYTHON_REPORTS_DIR.glob("ai-failure-analysis-*.html"))
    if html_reports:
        latest_report = max(html_reports, key=lambda p: p.stat().st_mtime)
        print(f"  AI Report: {latest_report.relative_to(PROJECT_ROOT)}")


if __name__ == "__main__":
    main()

