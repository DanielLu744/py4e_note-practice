# PY4E Practice (Python for Everybody)

This repository contains my personal practice while working through **Python for Everybody (PY4E)** by Dr. Charles Severance.  
It documents my progress from Python basics to working with files, data formats, networking, and databases.

---

## 📂 Repository Structure

Exercises are grouped by chapter/topic:


> ✅ More folders/exercises will be added as I continue the course.

---

## 🚀 Quick Start

### 1. Clone the repo
```bash
git clone https://github.com/DanielLu744/py4e-practice.git
cd py4e-practice

# macOS / Linux
python3 -m venv .venv
source .venv/bin/activate

# Windows (PowerShell)
py -3 -m venv .venv
.venv\Scripts\Activate.ps1

cd ex_6
python3 some_script.py

# Show Python version
python3 --version

# Format with black (if installed)
python3 -m pip install black
black ex_*/ *.py


---

### How to use it
1) Create/overwrite `README.md` at the repo root with the content above.  
2) Commit and push:
```bash
git add README.md
git commit -m "docs: refresh README with structure, progress, and usage"
git push origin main
