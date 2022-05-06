import json, pathlib
dir = pathlib.Path.home().joinpath("Appdata/Local/learning_python")

class saveFile:
    def __init__(self):
        if not dir.exists():
            dir.mkdir()

    def fileRead(self):
        self.filename = dir.joinpath("data.json")
        try:
            self.file = self.filename.open(mode = 'r+')
        except:
            self.filename.touch()
            self.file = self.filename.open(mode = 'r+')
        self.json_file = json.load(self.file)

    def loadData(self, data):
        try: 
            self.fileRead()
        except json.decoder.JSONDecodeError:
            pass
        return self.json_file[data]
