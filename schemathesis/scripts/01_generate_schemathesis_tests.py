#!/usr/bin/env python3
"""
Step 1: Generate Schemathesis Tests with VCR Output

This script runs Schemathesis to generate tests and save results as VCR YAML.
"""

import subprocess
import sys
import os
from pathlib import Path

# All scripts run from the SchemaSense project root
PROJECT_ROOT = Path(__file__).parent.parent.parent
os.chdir(PROJECT_ROOT)

# Add project root to path for config
sys.path.insert(0, str(PROJECT_ROOT))

from config import (
    SCHEMATHESIS_DIR,
    SCHEMATHESIS_SPEC_FILE,
    SCHEMATHESIS_REPORTS_DIR,
    API_BASE_URL,
    SCHEMATHESIS_MAX_EXAMPLES,
    SCHEMATHESIS_WORKERS,
    SCHEMATHESIS_HOOKS,
    TESTS_OUTPUT_FILE,
)


def generate_schemathesis_tests():
    """Run Schemathesis to generate tests with VCR output."""
    print("=" * 80)
    print("Step 1: Generating Schemathesis Tests with VCR Output")
    print("=" * 80)
    
    # Ensure reports directory exists
    SCHEMATHESIS_REPORTS_DIR.mkdir(parents=True, exist_ok=True)
    
    # Change to schemathesis directory
    original_cwd = Path.cwd()
    
    try:
        # Load environment from schemathesis.env if it exists (like the shell script does)
        env = os.environ.copy()
        env_file = SCHEMATHESIS_DIR / "schemathesis.env"
        if env_file.exists():
            # Read and parse env file (matching schemathesis_test.sh behavior)
            with open(env_file, 'r') as f:
                for line in f:
                    line = line.strip()
                    if line and not line.startswith('#') and '=' in line:
                        key, value = line.split('=', 1)
                        env[key.strip()] = value.strip()
        
        # Set hooks from env file or config (env file takes precedence)
        hook_value = env.get('SCHEMATHESIS_HOOKS', SCHEMATHESIS_HOOKS)
        if not hook_value:
            hook_value = SCHEMATHESIS_HOOKS
        
        # Remove :function suffix if present - schemathesis auto-detects before_call
        if ':' in hook_value:
            hook_value = hook_value.split(':')[0]
        
        env['SCHEMATHESIS_HOOKS'] = hook_value
        
        # Add schemathesis directory to PYTHONPATH so schemathesis can find the hook module
        pythonpath = env.get('PYTHONPATH', '')
        if pythonpath:
            pythonpath = f"{str(SCHEMATHESIS_DIR)}:{pythonpath}"
        else:
            pythonpath = str(SCHEMATHESIS_DIR)
        env['PYTHONPATH'] = pythonpath
        
        # Build schemathesis command with paths relative to the project root
        cmd = [
            "schemathesis", "run",
            "schemathesis/restful-booker-oas.yaml",
            "--url", API_BASE_URL,
            "--max-examples", str(SCHEMATHESIS_MAX_EXAMPLES),
            "--workers", str(SCHEMATHESIS_WORKERS),
            "--report", "junit,har,vcr",
            "--report-dir", "schemathesis/reports",
        ]
        
        print(f"Running: {' '.join(cmd)}")
        print(f"Spec file: {SCHEMATHESIS_SPEC_FILE}")
        print(f"Output directory: {SCHEMATHESIS_REPORTS_DIR}")
        print("-" * 80)
        
        # Run schemathesis and capture output
        output_file = SCHEMATHESIS_REPORTS_DIR / TESTS_OUTPUT_FILE
        
        # Run from the project root
        result = subprocess.run(
            cmd,
            env=env,
            cwd=PROJECT_ROOT,
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            text=True
        )
        
        # Write output to file and print to console
        output_file.write_text(result.stdout)
        print(result.stdout)
        
        print("-" * 80)
        
        if result.returncode != 0:
            print(f"Warning: Schemathesis exited with code {result.returncode}")
            print("This is normal if tests fail - check the reports for details.")
        
        # Find generated VCR file
        vcr_files = list(SCHEMATHESIS_REPORTS_DIR.glob("vcr-*.yaml"))
        if vcr_files:
            latest_vcr = max(vcr_files, key=lambda p: p.stat().st_mtime)
            print(f"\n✅ Generated VCR file: {latest_vcr}")
            return latest_vcr
        else:
            print("\n⚠️  No VCR file found. Check schemathesis output above.")
            return None
            
    except FileNotFoundError:
        print("Error: 'schemathesis' command not found.")
        print("Install with: pip install schemathesis")
        sys.exit(1)
    except Exception as e:
        print(f"Error: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)


if __name__ == "__main__":
    vcr_file = generate_schemathesis_tests()
    if vcr_file:
        print(f"\n📄 Next step: Analyze VCR with AI")
        print(f"   python schemathesis/scripts/02_analyze_vcr_with_ai.py {vcr_file.relative_to(PROJECT_ROOT)}")

