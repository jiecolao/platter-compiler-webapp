class FileHandler:
    def __init__(filepath): pass

    def run_file(filepath):
        
        with open(filepath, "r", encoding="utf-8") as f:
            source = f.read()
            return source