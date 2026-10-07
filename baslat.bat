@echo off
chcp 65001 >nul
title Konulu Ayet ve Hadis Bilgi Portalı - Streamlit
echo Uygulama başlatılıyor, lütfen bekleyin...
cd /d "%~dp0"
streamlit run main.py
pause