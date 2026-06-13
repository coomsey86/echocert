@echo off
echo Running EchoCert demo...
python echocert.py init-demo
python echocert.py record --from-files --prompt examples/prompt.txt --output examples/output.txt --receipt receipts/receipt.json --label Demo
python echocert.py verify receipts/receipt.json
python echocert_report.py receipts/receipt.json --out reports/audit_report.html
echo.
echo Demo complete.
echo Open reports\audit_report.html in your browser.
pause
