@echo off
echo Running EchoCert public MVP demo...
python echocert_mvp.py tamper-demo
python echocert_mvp.py verify receipts\original.json
python echocert_mvp.py report receipts\original.json --out reports\audit_report.html
echo.
echo Demo complete.
echo Open reports\audit_report.html in your browser.
pause
