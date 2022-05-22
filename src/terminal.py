import subprocess
from time import sleep
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from savefile import dir

class QConsole(QTextEdit):
    def __init__(self):
        super().__init__()
        self.setTextInteractionFlags(Qt.NoTextInteraction)
        self.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.consoleDoc = QTextDocument()
        self.setDocument(self.consoleDoc)
        self.installEventFilter(self)
#        pal = self.scrollAreaWidgetContents_3.temp3_textedit.palette()
#        pal.setColor(QPalette.Base, QColor('black'))
        #pal.setColor(QPalette.WindowText, QColor('white'))
#        self.scrollAreaWidgetContents_3.temp3_textedit.setPalette(pal)
#        self.scrollAreaWidgetContents_3.temp3_textedit.setStyleSheet("background-color: black")

    def eventFilter(self, a0: 'QObject', a1: 'QEvent') -> bool:
        if a1.type() == QEvent.KeyPress and a0 is self:
            if a1.key() == Qt.Key_Return and self.hasFocus():
                curLine = self.consoleDoc.lineCount()
                tb = self.consoleDoc.findBlockByLineNumber(curLine - 1)
                print(tb.text())
                print(self.sConsole.bash)
                self.sConsole.bash.communicate(tb.text())
        return super().eventFilter(a0, a1)

    def runPressed(self, editor):
        self.clear()
        self.setTextInteractionFlags(Qt.TextEditorInteraction)
        #self.scrollAreaWidgetContents_3.temp3_textedit.setReadOnly(False)
        self.filename = dir.joinpath("temp.py")
        self.fil = QFile(str(self.filename))
        if not self.fil.exists():
            self.filename.touch()
            self.fil = QFile(str(self.filename))
        if self.fil.open(QIODevice.ReadWrite):
            self.fil.resize(0)
            editor.write(self.fil)
        self.fil.close()
#        self.parse(self.filename)

        self.consoleCursor = QTextCursor(self.consoleDoc)
#        self.consoleCursor.insertText("Text")
        self.sConsole = startConsole()
        #print(self.console.bash.poll())
        self.t1 = QThread()
        self.sConsole.moveToThread(self.t1)
        self.t1.started.connect(self.sConsole.startConsole)
        self.sConsole.finished.connect(self.t1.quit)
        self.sConsole.finished.connect(self.sConsole.deleteLater)
        self.t1.finished.connect(self.t1.deleteLater)
        self.t1.start()
        self.getStatus()
        #print(self.sConsole.bash)

#        t1 = threading.Thread(target = self.console.checkFinished)
#        t1.start()
        #print(1)

    def getStatus(self):
        sleep(0.1)
        self.console = consoleIO(self.sConsole.bash, self)
        self.t2 = QThread()
        self.console.moveToThread(self.t2)
        self.t2.started.connect(self.console.checkFinished)
        self.console.finished.connect(self.t2.quit)
        self.console.finished.connect(self.console.deleteLater)
        self.t2.finished.connect(self.t2.deleteLater)
        self.t2.start()

class startConsole(QObject):
    finished = pyqtSignal()

    def __init__(self):
        super().__init__()
        self.bash = None

    def startConsole(self):
        f = open("log.txt", "w")
        self.bash = subprocess.Popen(['python', str(dir.joinpath('temp.py'))], stdin = subprocess.PIPE, stdout = f, stderr = subprocess.STDOUT, universal_newlines = True)
        #print(self.bash)
        self.bash.wait()

class consoleIO(QObject):
    finished = pyqtSignal()
    updateText = pyqtSignal(str)

    def __init__(self, bash, console):
        super().__init__()
        self.bash = bash
        self.console = console
    
    def update(self, s):
        self.updateText.emit(s)
        self.updateText.connect(self.console.append)

    def checkFinished(self):
        while self.bash.poll() is None:
            pass
        #print(x)
        pass
