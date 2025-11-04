#!/bin/bash

# Load environment variables
source schemathesis.env

# Export environment variables
export SCHEMATHESIS_HOOKS
export USER
export PASSWORD

# Verify environment variables are loaded
echo "SCHEMATHESIS_HOOKS: $SCHEMATHESIS_HOOKS"
echo "USER: $USER"
echo "PASSWORD: $PASSWORD"

# Run Schemathesis CLI with authentication
echo "Running Schemathesis CLI with authentication..."
schemathesis run restful-booker-oas.yaml \
--url https://restful-booker.herokuapp.com \
--max-examples 5 --workers 5 \
--report junit,har,vcr --report-dir ./reports \
2>&1 | tee reports/tests_output.txt

# echo "Running Schemathesis CLI with authentication..."
# schemathesis run restful-booker-oas.yaml \
# --url https://restful-booker.herokuapp.com \
# --max-examples 5 --workers 5 \
# --report vcr \
# --report-dir ./reports \
# --report-vcr-path reports/cassette.yaml
