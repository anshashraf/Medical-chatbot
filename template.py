import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s')

list_of_files = [
    "src/__init__.py",
    "src/helper.py",
    "src/prompts.py",
    "env",  # This looks like a directory
    "setup.py",
    "app.py",
    "research/trials.ipynb"
]

for filepath in list_of_files:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)
    
    if filedir != "":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Created directory: {filedir} for the file: {filename}")
    
    # Check if path is directory (like 'env'), if so just create directory
    if filepath.suffix == "":
        # No extension means probably a directory
        if not filepath.exists():
            os.makedirs(filepath, exist_ok=True)
            logging.info(f"Created directory: {filepath}")
        else:
            logging.info(f"Directory {filepath} already exists")
        continue

    if not (filepath.exists()) or (os.path.getsize(filepath) == 0):
        with open(filepath, "w") as f:
            pass
        logging.info(f"Created new file: {filepath}")
    else:
        logging.info(f"{filename} already exists")
