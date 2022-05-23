import subprocess, sys
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
                self.sConsole.bash.stdin.write(tb.text())
                print("", file = self.sConsole.bash.stdin, flush = True)
                with open("log.txt", "r+") as temp:
                    sleep(0.01)
                    self.insertPlainText(f"\n{temp.read()}")
                    temp.truncate(0)
                return True
        return super().eventFilter(a0, a1)

    def runPressed(self, editor):
        self.clear()
        self.setTextInteractionFlags(Qt.TextEditorInteraction)
        self.filename = dir.joinpath("temp.py")
        self.fil = QFile(str(self.filename))
        if not self.fil.exists():
            self.filename.touch()
            self.fil = QFile(str(self.filename))
        if self.fil.open(QIODevice.ReadWrite):
            self.fil.resize(0)
            editor.write(self.fil)
        self.fil.close()

        self.consoleCursor = QTextCursor(self.consoleDoc)
        self.sConsole = startConsole()
        self.t1 = QThread()
        self.sConsole.moveToThread(self.t1)
        self.t1.started.connect(self.sConsole.startConsole)
        self.sConsole.finished.connect(self.t1.quit)
        self.sConsole.finished.connect(self.sConsole.deleteLater)
        self.sConsole.finished.connect(lambda: self.setTextInteractionFlags(Qt.NoTextInteraction))
        self.t1.finished.connect(self.t1.deleteLater)
        self.t1.start()

        sleep(0.1)
        with open("log.txt", "r+") as fo:
            self.append(fo.read())
            fo.truncate(0)

class startConsole(QObject):
    finished = pyqtSignal()

    def __init__(self):
        super().__init__()
        self.bash = None
        self.fi = None

    def startConsole(self):
        with open("log.txt", "w+") as self.fi:
            self.bash = subprocess.Popen(['python', str(dir.joinpath('temp.py'))], stdin = subprocess.PIPE, stdout = self.fi, stderr = subprocess.STDOUT, universal_newlines = True, bufsize = 0)
            self.bash.wait()
        self.finished.emit()