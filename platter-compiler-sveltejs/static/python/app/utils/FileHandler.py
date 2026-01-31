class FileHandler:
    def __init__(filename): pass

    def run_file(filename):
        filepath = filename
        with open(filepath, "r", encoding="utf-8") as f:
            source = f.read()
            return source