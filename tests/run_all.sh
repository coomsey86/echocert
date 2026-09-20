#!/usr/bin/env bash
set -e

bash tests/test_smoke.sh
bash tests/test_tamper.sh
bash tests/test_commercial_docs.sh

echo "ALL TESTS PASSED"
