# QE Foundations
#### A library containing utility fuctions for working with strings, numbers, dates, and data generation

##### Project 1 milestone - Week 2, Monday

Currently, the project contains the foundational library, split into separate modules. It also has requirement files for copying the virtual environment, some documentation, and a small file to test the functionality of the utilities.
In the rest of the week, the data and tests folders will be filled with relevant work.

### Setup

1. Create venv: `python -m venv .venv`
2. Activate:
-Powershell: `.venv\Scripts\Activate.ps1`
-bash: `source .venv/bin/activate`
-Git Bash: `source .venv/Scripts/Activate`
3. Install: `python -m pip install -r requirements.txt`
4. Verify: `python smoke_utils.py`
5. Usage: For example, `python -c "from qe_foundations.utils import slugify; print(slugify('  Hello World  '))"`, will format string and print it as hello-world