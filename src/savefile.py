import json, pathlib
dir = pathlib.Path.home().joinpath("Appdata/Local/learning_python")

class saveFile:
    def __init__(self):
        if not dir.exists():
            dir.mkdir()

    def fileRead(self):
        self.filename = dir.joinpath("data.json")
        try:
            self.file = open(self.filename, 'r+')
        except:
            self.filename.touch()
            self.file = open(self.filename, 'r+')
        self.json_file = json.load(self.file)

    def fileWrite(self, data):
        self.filename = dir.joinpath("data.json")
        try:
            self.file = open(self.filename, 'w')
        finally:
            json.dump(data, self.file, indent = 4)
            self.file.close()

    def loadData(self, data):
        try: 
            self.fileRead()
        except json.decoder.JSONDecodeError:
            pass
        return self.json_file[data]
