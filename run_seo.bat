@echo off
chcp 65001 >nul
cd /d "C:\Users\Administrator\.qclaw\workspace\calcwithme-agent"
set PYTHONIOENCODING=utf-8
python -X utf8 scripts/seo_monitor.py
