# Step 1
- Clone the repo to a directory
- cmd: git clone https://github.com/themariolinml/qbe_home.git

# Step 2
- Create python virtual environment in the clone repo
- cmd: python -m venv .venv

- Install Required packages
- cmd: pip install -r requirements.txt

# Step 3 
- Run test. Make sure you are in the qbe_home directory and run the tests
- cmd: pytest

# Step 4
- Experiement API interactively. Make sure you are in the qbe_home directory.
- cmd: uvicorn src.main:app --reload
- Go to http://127.0.0.1:8000/docs in your web browser and try.