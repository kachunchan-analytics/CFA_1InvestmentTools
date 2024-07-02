@echo off
cd /d "C:\Users\Andy\Desktop\python_work_github\CFA_1InvestmentTools_GITHUB\CFA_1InvestmentTools"
rem cd /d %cd%
python change_TXT_to_PY.py
git add . 
git commit -m "Updated new modules for learning"
git push