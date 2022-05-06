from savefile import saveFile

class loginData(saveFile):
    def __init__(self):
        super(saveFile, self).__init__()

    def loginList(self):
        return self.loadData("login")
