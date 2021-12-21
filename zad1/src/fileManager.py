import os


class FileManager:
    def readFile(self, file):
        with open(f"./{file}", 'r') as f:
            return f.read()

    def addLineToFile(self, file, newLine):
        with open(f"./{file}", 'r') as f:
            return f.write(newLine)

    def deleteFile(self, file):
        if os.path.exists(f"./{file}"):
            os.remove(f"./{file}")
        raise Exception("File doesn't exist.")
