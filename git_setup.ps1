# git_setup.ps1 — one-time local Git setup for the PB_Writer repo.
# Run this once from the D:\Projects\Writer folder in PowerShell:
#     cd D:\Projects\Writer
#     powershell -ExecutionPolicy Bypass -File .\git_setup.ps1
#
# Why this script exists: the repo files were created from a sandboxed
# environment that could write to this drive but not run Git against it.
# This cleans up the partial init and creates a proper local commit.

Set-Location -Path $PSScriptRoot

# 1. Clean up the partial/broken git folder and any stray test file.
if (Test-Path .git)        { Remove-Item -Recurse -Force .git }
if (Test-Path ztest.txt)   { Remove-Item -Force ztest.txt }

# 2. Initialise a fresh repo and make the first commit.
git init
git branch -M main
git config user.name  "Prateek Bhatnagar"
git config user.email "prateek.bhatnagar89@gmail.com"
git add -A
git commit -m "Initial commit: PB_Writer plugin (pb-writer skill + references)"

Write-Host ""
Write-Host "Local commit done. Now connect your remote and push, e.g.:" -ForegroundColor Green
Write-Host "  git remote add origin https://github.com/<your-user>/Writer.git"
Write-Host "  git push -u origin main"
