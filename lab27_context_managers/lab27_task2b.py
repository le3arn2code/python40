# Task 2b: FileManager Context Manager

class FileManager:
    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode
    
    def __enter__(self):
        self.file = open(self.filename, self.mode)
        return self.file
    
    def __exit__(self, exc_type, exc_value, traceback):
        self.file.close()

# Using the FileManager to write to a file
with FileManager("sample.txt", "w") as f:
    f.write("Hello, World!")
