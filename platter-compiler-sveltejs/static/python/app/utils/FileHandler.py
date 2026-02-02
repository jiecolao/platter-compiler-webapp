
import os

# Get the directory where this file is located (app/utils/)
samples_dir = os.path.dirname(os.path.abspath(__file__))

def run_file(filepath):
    # If filepath is just a filename, look for it in samples_dir
    if not os.path.isabs(filepath) and os.sep not in filepath:
        filepath = os.path.join(samples_dir, filepath)
    
    with open(filepath, "r", encoding="utf-8") as f:
        source = f.read()
        return source


class FileHandler:
    pass