# PY4E Practice (Python for Everybody)

Personal practice repo while I work through **Python for Everybody (PY4E)** — building from fundamentals to working with files, data formats, networking, and databases.

> 🗓️ Ongoing study log. I’ll keep pushing exercises and notes as I progress.

## Repository Structure

Exercises are grouped by chapter/topic:

ex_1/ # Variables, expressions, & user input
ex_2/ # Conditional code
ex_3/ # Functions
ex_4/ # Loops / iteration
ex_5/ # Strings
ex_6/ # Files
ex_7/ # Lists
ex_8/ # Dictionaries
ex_9/ # Tuples
ex_10/ # Regular expressions
ex_11/ # Networked programs (HTTP)
ex_12/ # Web services / XML
ex_13/ # JSON & APIs
ex_14/ # Databases / SQLite

bash
Copy code

> Folder names exist up to `ex_14` in this repo; I’ll add more as I go.

## Quick Start

### 1) Clone

```bash
git clone https://github.com/DanielLu744/py4e-practice.git
cd py4e-practice
2) (Optional) Create a virtual environment
bash
Copy code
# macOS / Linux
python3 -m venv .venv
source .venv/bin/activate

# Windows (PowerShell)
py -3 -m venv .venv
.venv\Scripts\Activate.ps1
3) Run any exercise
bash
Copy code
cd ex_6
python3 some_script.py
If an exercise needs a data file (e.g., mbox.txt), place it in the same folder or update the script path accordingly.

Progress Tracker
 Ch 1–2: Basics & Conditionals

 Ch 3: Functions

 Ch 4: Loops

 Ch 5–6: Strings & Files

 Ch 7: Lists

 Ch 8: Dictionaries

 Ch 9: Tuples

 Ch 10: Regular Expressions

 Ch 11: Networked Programs (HTTP)

 Ch 12: XML

 Ch 13: JSON

 Ch 14: Databases / SQLite

 Ch 15+: (If applicable) Visualizations / extras

I’ll tick items as I finalize and commit each exercise set.

Notes
Scripts that read files default to UTF-8.

Database exercises use sqlite3 and create local .sqlite files in the exercise folder.

Networking/API exercises may require an internet connection or API keys (when applicable). Keys are never committed.

Useful Commands
bash
Copy code
# Show Python version
python3 --version

# Format a file with black (if installed)
python3 -m pip install black
black ex_*/ *.py
Learning Resources
Python for Everybody (Dr. Charles Severance) — course & textbook

Python docs: https://docs.python.org/3/

Roadmap / Next Steps
Add sample outputs to each folder’s README where helpful.

Add lightweight tests for text-parsing exercises.

(Optional) Add requirements.txt if any third-party libs are introduced.

If you spot mistakes or have suggestions, feel free to open an issue or PR. Happy coding! 🐍

yaml
Copy code

---

### How to use it
1) Create/overwrite `README.md` at the repo root with the content above.  
2) Commit and push:
```bash
git add README.md
git commit -m "docs: refresh README with structure, progress, and usage"
git push origin main
