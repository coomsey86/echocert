#!/usr/bin/env bash
set -e

./tests/test_smoke.sh
./tests/test_tamper.sh

echo "ALL TESTS PASSED"

