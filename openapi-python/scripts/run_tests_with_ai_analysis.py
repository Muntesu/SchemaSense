#!/usr/bin/env python3
"""
Run pytest tests and automatically analyze failures with AI.

Usage:
    python scripts/run_tests_with_ai_analysis.py [pytest args]
    
Example:
    python scripts/run_tests_with_ai_analysis.py test/ -v
    python scripts/run_tests_with_ai_analysis.py test/test_default_api.py -v
"""

import argparse
import subprocess
import sys
import os
from pathlib import Path
from datetime import datetime

# All scripts run from the SchemaSense project root
PROJECT_ROOT = Path(__file__).parent.parent.parent

# Change to project root first
os.chdir(PROJECT_ROOT)

# Add openapi-python directory to path for imports (test.* modules)
OPENAPI_PYTHON_DIR = PROJECT_ROOT / "openapi-python"
# Use absolute path to ensure it works regardless of where script is called from
sys.path.insert(0, str(OPENAPI_PYTHON_DIR.resolve()))

from test.ai_failure_analyzer import FailureAnalyzer
from test.ai_config import AIConfig


def run_pytest(args: list, junit_xml: Path) -> tuple[int, int]:
    """Run pytest with JUnit XML output and return (passed, total) counts."""
    pytest_cmd = [
        "pytest",
        *args,
        f"--junit-xml={junit_xml}",
        "--tb=short"
    ]
    
    print(f"Running: {' '.join(pytest_cmd)}")
    print("-" * 80)
    
    # Run pytest
    result = subprocess.run(pytest_cmd, capture_output=True, text=True)
    
    # Print pytest output
    print(result.stdout)
    if result.stderr:
        print(result.stderr, file=sys.stderr)
    
    # Parse summary from output
    passed = 0
    total = 0
    
    for line in result.stdout.split('\n'):
        if 'passed' in line.lower() and ('failed' in line.lower() or 'error' in line.lower()):
            # Parse line like: "142 passed, 25 failed in 45.67s"
            try:
                parts = line.split(',')
                for part in parts:
                    part = part.strip()
                    if 'passed' in part.lower():
                        passed = int(part.split()[0])
                    elif 'failed' in part.lower():
                        total = passed + int(part.split()[0])
                        break
                    elif 'error' in part.lower():
                        total = passed + int(part.split()[0])
                        break
            except (ValueError, IndexError):
                pass
    
    # If parsing failed, try to extract from JUnit XML
    if total == 0:
        import xml.etree.ElementTree as ET
        if junit_xml.exists():
            try:
                tree = ET.parse(junit_xml)
                root = tree.getroot()
                testsuites = root.findall('testsuite')
                if not testsuites:
                    testsuites = [root] if root.tag == 'testsuite' else []
                
                for testsuite in testsuites:
                    total = int(testsuite.get('tests', '0'))
                    passed = total - int(testsuite.get('failures', '0')) - int(testsuite.get('errors', '0'))
            except Exception:
                pass
    
    return passed, total


def main():
    """Main entry point."""
    parser = argparse.ArgumentParser(
        description="Run pytest tests and analyze failures with AI",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Run all tests
  python scripts/run_tests_with_ai_analysis.py test/ -v
  
  # Run specific test file
  python scripts/run_tests_with_ai_analysis.py test/test_default_api.py -v
  
  # Run with custom pytest options
  python scripts/run_tests_with_ai_analysis.py test/ -v -k "test_auth"
        """
    )
    
    parser.add_argument(
        "--no-analysis",
        action="store_true",
        help="Skip AI analysis (just run tests)"
    )
    
    parser.add_argument(
        "--report-dir",
        type=Path,
        default=PROJECT_ROOT / "openapi-python" / "reports",
        help="Directory for reports (default: openapi-python/reports/)"
    )
    
    parser.add_argument(
        "--max-failures",
        type=int,
        default=None,
        help="Maximum number of failures to analyze (default: all)"
    )
    
    # Parse known args - this allows pytest arguments to pass through
    args, pytest_args = parser.parse_known_args()
    
    # If no pytest args provided, use defaults
    if not pytest_args:
        pytest_args = ["openapi-python/test/", "-v"]
    else:
        # Adjust test paths to be relative to the project root
        adjusted_args = []
        for arg in pytest_args:
            if arg.startswith("test/") and not Path(arg).is_absolute():
                adjusted_args.append("openapi-python/" + arg)
            else:
                adjusted_args.append(arg)
        pytest_args = adjusted_args
    
    # Check API key if analysis is enabled
    if not args.no_analysis and not AIConfig.is_configured():
        print("Warning: GROQ_API_KEY not set. AI analysis will be skipped.")
        print("Get your free API key at: https://console.groq.com")
        print("Set it with: export GROQ_API_KEY='your-api-key'")
        args.no_analysis = True
    
    # Create reports directory
    args.report_dir.mkdir(parents=True, exist_ok=True)
    
    # Generate timestamped report files
    timestamp = datetime.now().strftime("%Y%m%dT%H%M%S")
    junit_xml = args.report_dir / f"junit-{timestamp}.xml"
    analysis_report = args.report_dir / f"ai-failure-analysis-{timestamp}.html"
    
    # Run tests
    print("=" * 80)
    print("🧪 Running pytest tests...")
    print("=" * 80)
    
    passed, total = run_pytest(pytest_args, junit_xml)
    failed = total - passed
    
    print("\n" + "=" * 80)
    print(f"📊 Test Results: {passed} passed, {failed} failed, {total} total")
    print("=" * 80)
    
    # Analyze failures if enabled
    if not args.no_analysis and failed > 0:
        if not junit_xml.exists():
            print(f"Error: JUnit XML file not found: {junit_xml}")
            print("Cannot analyze failures without JUnit XML output.")
            sys.exit(1)
        
        print("\n" + "=" * 80)
        print("🤖 Analyzing failures with AI...")
        print("=" * 80)
        
        try:
            analyzer = FailureAnalyzer()
            failures, analyses = analyzer.analyze_from_junit_xml(
                junit_xml,
                analysis_report,
                total,
                passed,
                max_failures=args.max_failures
            )
            
            print(f"\n✅ Analysis complete! Analyzed {len(failures)} failure(s).")
            print(f"📊 Report: {analysis_report}")
            print(f"📄 JUnit XML: {junit_xml}")
            
        except Exception as e:
            print(f"Error during AI analysis: {e}", file=sys.stderr)
            print("Tests completed, but analysis failed.", file=sys.stderr)
            sys.exit(1)
    
    elif failed > 0 and args.no_analysis:
        print(f"\n⚠️  {failed} test(s) failed. Enable AI analysis with --analysis flag.")
        print(f"📄 JUnit XML: {junit_xml}")
    
    elif failed == 0:
        print("\n✅ All tests passed! No failures to analyze.")
    
    # Exit with pytest exit code
    sys.exit(0 if failed == 0 else 1)


if __name__ == "__main__":
    main()

