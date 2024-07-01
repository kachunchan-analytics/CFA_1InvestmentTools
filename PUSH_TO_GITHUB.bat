@echo off
cd /d %cd%
/min python change_TXT_to_PY.py
git add . > nul
if %errorlevel% NEQ 0 (
  echo "Error: Git add failed!"
  pause
)

git commit -m "Updated new modules for learning" > nul
if %errorlevel% NEQ 0 (
  echo "Error: Git commit failed!"
  pause
)

git push > nul
if %errorlevel% NEQ 0 (
  echo "Error: Git push failed!"
  pause
)