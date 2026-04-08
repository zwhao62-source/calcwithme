@echo off
chcp 65001 >nul
cd /d "C:\Users\Administrator\.qclaw\workspace\calcwithme-agent"
set PYTHONIOENCODING=utf-8
echo [%date% %time%] Running SEO Monitor...
python -X utf8 scripts/seo_monitor.py >> reports/seo_monitor.log 2>&1
echo [%date% %time%] SEO Monitor completed.
