import json
from savefile import saveFile

class loginData(saveFile):
    def __init__(self):
        super(saveFile, self).__init__()

    def loginList(self):
        return self.loadData("login")

    def updateLogin(self, username, password):
        try: 
            self.fileRead()
        except json.decoder.JSONDecodeError:
            pass
        data = self.json_file
        data["login"][username] = password
        try: 
            self.fileWrite(data)
        except json.decoder.JSONDecodeError:
            pass