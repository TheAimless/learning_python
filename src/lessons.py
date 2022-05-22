from concurrent.futures import thread
import subprocess, win32con, win32gui, win32process 
import appCore, psutil
from PyQt5.QtWidgets import * 
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.Qsci import *
from terminal import QConsole
import sys

class scintillaEditor(QsciScintilla):
    def __init__(self, *args):
        super(QsciScintilla, self).__init__(*args)

    def createEditor(self):
        self.setWrapMode(QsciScintilla.WrapWhitespace)
        self.setIndentationsUseTabs(True)
        self.setIndentationGuides(True)
        self.setAutoIndent(True)
        self.__lexer = QsciLexerPython(self)
        self.setLexer(self.__lexer)
        self.setIndentationGuides(True)
        self.setUtf8(True)  # Set encoding to UTF-8
        self.setMarginType(0, QsciScintilla.NumberMargin)
        self.setMarginWidth(0, "0000")

class learnWindow(appCore.windowClass):
    def __init__(self):
        super(appCore.windowClass, self).__init__()
        self.createNode()

    def setupWidget(self):
        self.setWindowTitle('Learn (placeholder)')
        self.setGeometry(0, 0, 1920, 1080)

        self.centralwidget = appCore.widgetClass(self)
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.widget = appCore.widgetClass(self.centralwidget)
        self.widget.setMaximumSize(QSize(16777215, 50))
        self.horizontalLayout = QHBoxLayout(self.widget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)

        self.line = QFrame(self.centralwidget)
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)
        self.verticalLayout.addWidget(self.line)
        self.widget.createBtn("node_3", "Home", False)
        self.widget.node_3_btn.setMaximumSize(QSize(50, 16777215))
        self.horizontalLayout.addWidget(self.widget.node_3_btn)
        spacerItem = QSpacerItem(40, 20, QSizePolicy.Preferred, QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.widget.createLabel("lesson", "Lesson")
        self.horizontalLayout.addWidget(self.widget.lesson_label)
        self.verticalLayout.addWidget(self.widget)
        self.widget_2 = appCore.widgetClass(self.centralwidget)
        self.horizontalLayout_3 = QHBoxLayout(self.widget_2)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setSpacing(0)

        self.splitter = QSplitter(self.widget_2)
        self.splitter.setOrientation(Qt.Horizontal)
        self.splitter.setOpaqueResize(True)
        self.splitter.setHandleWidth(0)
        self.splitter.setChildrenCollapsible(False)
        self.widget_4 = appCore.widgetClass(self.splitter)
        self.verticalLayout_2 = QVBoxLayout(self.widget_4)
        self.verticalLayout_2.setSizeConstraint(QLayout.SetMaximumSize)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setSpacing(0)
        self.scrollArea = QScrollArea(self.widget_4)
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = appCore.widgetClass()
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 118, 15516))

        self.verticalLayout_5 = QVBoxLayout(self.scrollAreaWidgetContents)
        self.scrollAreaWidgetContents.createLabel("content", "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Suspendisse sollicitudin massa sed pulvinar aliquam. Pellentesque porttitor tempus quam. Curabitur rhoncus orci tortor, blandit mollis odio auctor sed. Nunc non nunc ac mauris accumsan volutpat at ac quam. Mauris a lacus sed metus vehicula varius in eget turpis. Curabitur non magna quis mi tincidunt tempus. Sed fermentum tempus gravida. Cras pellentesque posuere arcu quis facilisis. Integer porttitor lacus sed justo hendrerit mattis. Proin et erat tempus, mattis dolor vitae, auctor nisl. Vivamus sagittis id tortor id sagittis. Interdum et malesuada fames ac ante ipsum primis in faucibus. Cras porttitor magna nec fermentum molestie. Suspendisse potenti. Donec vel ex tortor. Proin elit augue, elementum vel tincidunt ac, iaculis egestas mi. Nam congue, neque at posuere rhoncus, erat erat lobortis risus, rutrum imperdiet dui lacus sit amet quam. Donec et commodo felis. Integer eget urna non nibh finibus vehicula. Ut mollis quam est, a efficitur tellus tristique vitae. In vitae est ut ipsum laoreet rutrum. Donec blandit ipsum at convallis faucibus. Duis a turpis sit amet augue rutrum interdum. Orci varius natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Aliquam maximus enim id magna porta, vitae egestas leo pretium. In efficitur nisl nec mi auctor faucibus. Proin sodales condimentum ligula id interdum. Praesent eget auctor arcu, et consectetur nunc. Cras at lacus lacinia, pulvinar elit sed, tincidunt nisi. Vivamus hendrerit at nibh id finibus. Quisque eleifend hendrerit leo ac fermentum. Morbi tristique vitae dolor at pellentesque. Proin egestas purus vitae ipsum congue ultricies. Aenean vehicula ipsum sed est ultrices, ut congue orci sollicitudin. Aliquam vel turpis nibh. Vestibulum at efficitur turpis, ut egestas neque. Integer non erat tincidunt, elementum nunc quis, molestie mi. Fusce ut auctor urna, at imperdiet ligula. Vestibulum pharetra dignissim ex at congue. Phasellus nec nunc non lectus malesuada consectetur. Vivamus sem est, euismod at porta nec, aliquet id ex. Sed vel egestas magna. Mauris fringilla vel neque ut convallis. Quisque egestas laoreet lacinia. Nunc pulvinar porta magna, vitae dictum lacus. Etiam justo elit, ultrices sit amet tempus ac, bibendum non mauris. Quisque vitae augue ac erat vehicula ullamcorper. Vivamus aliquet luctus tortor, a egestas nunc interdum et. Aliquam accumsan lacus eu ante gravida, tincidunt molestie urna fringilla. Phasellus tincidunt vestibulum odio eget gravida. Ut nec mi nisi. Quisque non massa nec arcu lobortis vehicula eget a ipsum. Vivamus et tortor eu mauris blandit dignissim sed et massa. Curabitur et magna sollicitudin, dapibus nisl sagittis, tempor lorem. Cras gravida congue lorem, at luctus lacus pellentesque sed. Etiam tristique ultricies lacinia. Cras tellus mauris, vulputate nec purus nec, consectetur scelerisque libero. Praesent lorem orci, pharetra vel dolor at, mollis pellentesque turpis. Vestibulum vel enim eros. Nam ac dui sit amet purus elementum rutrum eu aliquam erat. Nulla consectetur urna vel posuere aliquet. Etiam a finibus nunc, at pharetra arcu. Nam et vestibulum turpis. Maecenas sed nibh sit amet mauris suscipit egestas vel pharetra risus. Nullam aliquet ac magna in pretium. Sed sollicitudin consectetur nibh et facilisis. Nullam lacinia accumsan magna, ut tincidunt eros porta ut. Aenean ac turpis feugiat nibh bibendum ullamcorper eu in nisl. Etiam tincidunt accumsan ultricies. Nulla porta sem magna, sit amet porttitor magna euismod id. Curabitur nec tincidunt neque. Ut orci magna, dictum nec ante vitae, vehicula interdum mi. Quisque sodales mollis lorem, id ullamcorper lacus commodo ac. Nullam porta ultrices est, quis vestibulum risus euismod eu. Sed eleifend efficitur tellus, non cursus est tempor et. Nulla facilisis convallis sem, id congue lacus dignissim blandit. Donec vitae neque magna. Maecenas eu est turpis. Nullam luctus lacinia tincidunt. Aliquam erat volutpat. Praesent ultricies orci tortor, ut tempus lorem tristique a. Suspendisse justo tortor, condimentum a nisi vitae, malesuada varius lorem. Fusce vel interdum felis, ut semper mauris. Proin orci tellus, semper ut porta id, imperdiet at augue. Suspendisse tincidunt sem eu sapien venenatis, in mattis erat consequat. Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. Morbi porta diam sed tellus elementum, et commodo nunc bibendum. Integer pharetra magna et venenatis ullamcorper. Quisque imperdiet et sem at semper. Quisque et velit tempor, vulputate odio sagittis, finibus mi. Morbi at elementum erat. Maecenas volutpat tellus ac quam blandit, sit amet mattis quam commodo. Nullam non feugiat enim. Nulla auctor tellus neque.Lorem ipsum dolor sit amet, consectetur adipiscing elit. Suspendisse sollicitudin massa sed pulvinar aliquam. Pellentesque porttitor tempus quam. Curabitur rhoncus orci tortor, blandit mollis odio auctor sed. Nunc non nunc ac mauris accumsan volutpat at ac quam. Mauris a lacus sed metus vehicula varius in eget turpis. Curabitur non magna quis mi tincidunt tempus. Sed fermentum tempus gravida. Cras pellentesque posuere arcu quis facilisis. Integer porttitor lacus sed justo hendrerit mattis. Proin et erat tempus, mattis dolor vitae, auctor nisl. Vivamus sagittis id tortor id sagittis. Interdum et malesuada fames ac ante ipsum primis in faucibus. Cras porttitor magna nec fermentum molestie. Suspendisse potenti. Donec vel ex tortor. Proin elit augue, elementum vel tincidunt ac, iaculis egestas mi. Nam congue, neque at posuere rhoncus, erat erat lobortis risus, rutrum imperdiet dui lacus sit amet quam. Donec et commodo felis. Integer eget urna non nibh finibus vehicula. Ut mollis quam est, a efficitur tellus tristique vitae. In vitae est ut ipsum laoreet rutrum. Donec blandit ipsum at convallis faucibus. Duis a turpis sit amet augue rutrum interdum. Orci varius natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Aliquam maximus enim id magna porta, vitae egestas leo pretium. In efficitur nisl nec mi auctor faucibus. Proin sodales condimentum ligula id interdum. Praesent eget auctor arcu, et consectetur nunc. Cras at lacus lacinia, pulvinar elit sed, tincidunt nisi. Vivamus hendrerit at nibh id finibus. Quisque eleifend hendrerit leo ac fermentum. Morbi tristique vitae dolor at pellentesque. Proin egestas purus vitae ipsum congue ultricies. Aenean vehicula ipsum sed est ultrices, ut congue orci sollicitudin. Aliquam vel turpis nibh. Vestibulum at efficitur turpis, ut egestas neque. Integer non erat tincidunt, elementum nunc quis, molestie mi. Fusce ut auctor urna, at imperdiet ligula. Vestibulum pharetra dignissim ex at congue. Phasellus nec nunc non lectus malesuada consectetur. Vivamus sem est, euismod at porta nec, aliquet id ex. Sed vel egestas magna. Mauris fringilla vel neque ut convallis. Quisque egestas laoreet lacinia. Nunc pulvinar porta magna, vitae dictum lacus. Etiam justo elit, ultrices sit amet tempus ac, bibendum non mauris. Quisque vitae augue ac erat vehicula ullamcorper. Vivamus aliquet luctus tortor, a egestas nunc interdum et. Aliquam accumsan lacus eu ante gravida, tincidunt molestie urna fringilla. Phasellus tincidunt vestibulum odio eget gravida. Ut nec mi nisi. Quisque non massa nec arcu lobortis vehicula eget a ipsum. Vivamus et tortor eu mauris blandit dignissim sed et massa. Curabitur et magna sollicitudin, dapibus nisl sagittis, tempor lorem. Cras gravida congue lorem, at luctus lacus pellentesque sed. Etiam tristique ultricies lacinia. Cras tellus mauris, vulputate nec purus nec, consectetur scelerisque libero. Praesent lorem orci, pharetra vel dolor at, mollis pellentesque turpis. Vestibulum vel enim eros. Nam ac dui sit amet purus elementum rutrum eu aliquam erat. Nulla consectetur urna vel posuere aliquet. Etiam a finibus nunc, at pharetra arcu. Nam et vestibulum turpis. Maecenas sed nibh sit amet mauris suscipit egestas vel pharetra risus. Nullam aliquet ac magna in pretium. Sed sollicitudin consectetur nibh et facilisis. Nullam lacinia accumsan magna, ut tincidunt eros porta ut. Aenean ac turpis feugiat nibh bibendum ullamcorper eu in nisl. Etiam tincidunt accumsan ultricies. Nulla porta sem magna, sit amet porttitor magna euismod id. Curabitur nec tincidunt neque. Ut orci magna, dictum nec ante vitae, vehicula interdum mi. Quisque sodales mollis lorem, id ullamcorper lacus commodo ac. Nullam porta ultrices est, quis vestibulum risus euismod eu. Sed eleifend efficitur tellus, non cursus est tempor et. Nulla facilisis convallis sem, id congue lacus dignissim blandit. Donec vitae neque magna. Maecenas eu est turpis. Nullam luctus lacinia tincidunt. Aliquam erat volutpat. Praesent ultricies orci tortor, ut tempus lorem tristique a. Suspendisse justo tortor, condimentum a nisi vitae, malesuada varius lorem. Fusce vel interdum felis, ut semper mauris. Proin orci tellus, semper ut porta id, imperdiet at augue. Suspendisse tincidunt sem eu sapien venenatis, in mattis erat consequat. Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. Morbi porta diam sed tellus elementum, et commodo nunc bibendum. Integer pharetra magna et venenatis ullamcorper. Quisque imperdiet et sem at semper. Quisque et velit tempor, vulputate odio sagittis, finibus mi. Morbi at elementum erat. Maecenas volutpat tellus ac quam blandit, sit amet mattis quam commodo. Nullam non feugiat enim. Nulla auctor tellus neque.Lorem ipsum dolor sit amet, consectetur adipiscing elit. Suspendisse sollicitudin massa sed pulvinar aliquam. Pellentesque porttitor tempus quam. Curabitur rhoncus orci tortor, blandit mollis odio auctor sed. Nunc non nunc ac mauris accumsan volutpat at ac quam. Mauris a lacus sed metus vehicula varius in eget turpis. Curabitur non magna quis mi tincidunt tempus. Sed fermentum tempus gravida. Cras pellentesque posuere arcu quis facilisis. Integer porttitor lacus sed justo hendrerit mattis. Proin et erat tempus, mattis dolor vitae, auctor nisl. Vivamus sagittis id tortor id sagittis. Interdum et malesuada fames ac ante ipsum primis in faucibus. Cras porttitor magna nec fermentum molestie. Suspendisse potenti. Donec vel ex tortor. Proin elit augue, elementum vel tincidunt ac, iaculis egestas mi. Nam congue, neque at posuere rhoncus, erat erat lobortis risus, rutrum imperdiet dui lacus sit amet quam. Donec et commodo felis. Integer eget urna non nibh finibus vehicula. Ut mollis quam est, a efficitur tellus tristique vitae. In vitae est ut ipsum laoreet rutrum. Donec blandit ipsum at convallis faucibus. Duis a turpis sit amet augue rutrum interdum. Orci varius natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Aliquam maximus enim id magna porta, vitae egestas leo pretium. In efficitur nisl nec mi auctor faucibus. Proin sodales condimentum ligula id interdum. Praesent eget auctor arcu, et consectetur nunc. Cras at lacus lacinia, pulvinar elit sed, tincidunt nisi. Vivamus hendrerit at nibh id finibus. Quisque eleifend hendrerit leo ac fermentum. Morbi tristique vitae dolor at pellentesque. Proin egestas purus vitae ipsum congue ultricies. Aenean vehicula ipsum sed est ultrices, ut congue orci sollicitudin. Aliquam vel turpis nibh. Vestibulum at efficitur turpis, ut egestas neque. Integer non erat tincidunt, elementum nunc quis, molestie mi. Fusce ut auctor urna, at imperdiet ligula. Vestibulum pharetra dignissim ex at congue. Phasellus nec nunc non lectus malesuada consectetur. Vivamus sem est, euismod at porta nec, aliquet id ex. Sed vel egestas magna. Mauris fringilla vel neque ut convallis. Quisque egestas laoreet lacinia. Nunc pulvinar porta magna, vitae dictum lacus. Etiam justo elit, ultrices sit amet tempus ac, bibendum non mauris. Quisque vitae augue ac erat vehicula ullamcorper. Vivamus aliquet luctus tortor, a egestas nunc interdum et. Aliquam accumsan lacus eu ante gravida, tincidunt molestie urna fringilla. Phasellus tincidunt vestibulum odio eget gravida. Ut nec mi nisi. Quisque non massa nec arcu lobortis vehicula eget a ipsum. Vivamus et tortor eu mauris blandit dignissim sed et massa. Curabitur et magna sollicitudin, dapibus nisl sagittis, tempor lorem. Cras gravida congue lorem, at luctus lacus pellentesque sed. Etiam tristique ultricies lacinia. Cras tellus mauris, vulputate nec purus nec, consectetur scelerisque libero. Praesent lorem orci, pharetra vel dolor at, mollis pellentesque turpis. Vestibulum vel enim eros. Nam ac dui sit amet purus elementum rutrum eu aliquam erat. Nulla consectetur urna vel posuere aliquet. Etiam a finibus nunc, at pharetra arcu. Nam et vestibulum turpis. Maecenas sed nibh sit amet mauris suscipit egestas vel pharetra risus. Nullam aliquet ac magna in pretium. Sed sollicitudin consectetur nibh et facilisis. Nullam lacinia accumsan magna, ut tincidunt eros porta ut. Aenean ac turpis feugiat nibh bibendum ullamcorper eu in nisl. Etiam tincidunt accumsan ultricies. Nulla porta sem magna, sit amet porttitor magna euismod id. Curabitur nec tincidunt neque. Ut orci magna, dictum nec ante vitae, vehicula interdum mi. Quisque sodales mollis lorem, id ullamcorper lacus commodo ac. Nullam porta ultrices est, quis vestibulum risus euismod eu. Sed eleifend efficitur tellus, non cursus est tempor et. Nulla facilisis convallis sem, id congue lacus dignissim blandit. Donec vitae neque magna. Maecenas eu est turpis. Nullam luctus lacinia tincidunt. Aliquam erat volutpat. Praesent ultricies orci tortor, ut tempus lorem tristique a. Suspendisse justo tortor, condimentum a nisi vitae, malesuada varius lorem. Fusce vel interdum felis, ut semper mauris. Proin orci tellus, semper ut porta id, imperdiet at augue. Suspendisse tincidunt sem eu sapien venenatis, in mattis erat consequat. Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. Morbi porta diam sed tellus elementum, et commodo nunc bibendum. Integer pharetra magna et venenatis ullamcorper. Quisque imperdiet et sem at semper. Quisque et velit tempor, vulputate odio sagittis, finibus mi. Morbi at elementum erat. Maecenas volutpat tellus ac quam blandit, sit amet mattis quam commodo. Nullam non feugiat enim. Nulla auctor tellus neque.")

        self.scrollAreaWidgetContents.content_label.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.scrollAreaWidgetContents.content_label.setWordWrap(True)
        self.verticalLayout_5.addWidget(self.scrollAreaWidgetContents.content_label)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayout_2.addWidget(self.scrollArea)
        self.widget_5 = appCore.widgetClass(self.splitter)
        self.verticalLayout_3 = QVBoxLayout(self.widget_5)
        self.verticalLayout_3.setSizeConstraint(QLayout.SetMaximumSize)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setSpacing(0)
        self.scrollArea_2 = QScrollArea(self.widget_5)
        self.scrollArea_2.setFrameShape(QFrame.NoFrame)
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollAreaWidgetContents_2 = appCore.widgetClass()
        #self.scrollAreaWidgetContents_2.setGeometry(QRect(0, 0, 127, 228))
        self.widget_7 = appCore.widgetClass(self.widget_5)
        self.horizontalLayout_4 = QHBoxLayout(self.widget_7)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setSpacing(0)

        self.widget_7.createBtn("run", "Run", False)
        self.widget_7.run_btn.setMaximumSize(QSize(50, 16777215))
        self.widget_7.run_btn.clicked.connect(lambda: self.scrollAreaWidgetContents_3.console.runPressed(self.qScintillaEditor))
        self.horizontalLayout_4.addWidget(self.widget_7.run_btn)
        self.widget_7.createBtn("a", "A", False)
        self.widget_7.a_btn.setMaximumSize(QSize(25, 16777215))
        self.horizontalLayout_4.addWidget(self.widget_7.a_btn)
        self.widget_7.createBtn("b", "B", False)
        self.widget_7.b_btn.setMaximumSize(QSize(25, 16777215))
        self.horizontalLayout_4.addWidget(self.widget_7.b_btn)
        spacerItem3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem3)

        self.verticalLayout_6 = QVBoxLayout(self.scrollAreaWidgetContents_2)
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_6.setSpacing(0)
        self.qScintillaEditor = scintillaEditor(self.scrollAreaWidgetContents_2)
        self.qScintillaEditor.createEditor()
        self.qScintillaEditor.setFrameShape(QFrame.NoFrame)
        self.qScintillaEditor.setLineWidth(0)
        self.verticalLayout_6.addWidget(self.qScintillaEditor)
        self.scrollArea_2.setWidget(self.scrollAreaWidgetContents_2)
        self.verticalLayout_3.addWidget(self.scrollArea_2)
        self.verticalLayout_3.addWidget(self.widget_7)
        self.widget_6 = appCore.widgetClass(self.splitter)
        self.splitter.setSizes([640, 640, 640])
        self.verticalLayout_4 = QVBoxLayout(self.widget_6)
        self.verticalLayout_4.setSizeConstraint(QLayout.SetMaximumSize)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setSpacing(0)
        self.scrollArea_3 = QScrollArea(self.widget_6)
        self.scrollArea_3.setFrameShape(QFrame.NoFrame)
        self.scrollArea_3.setWidgetResizable(True)
        self.scrollAreaWidgetContents_3 = appCore.widgetClass()
        self.scrollAreaWidgetContents_3.setGeometry(QRect(0, 0, 130, 230))

        self.verticalLayout_7 = QVBoxLayout(self.scrollAreaWidgetContents_3)
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_7.setSpacing(0)
#        self.wind = QWindow.fromWinId()
        for proc in psutil.process_iter():
            if process_name in proc.name():
                pid.append(proc.pid)

        print(pid)
        #print(self.find_window_for_pid())
        self.scrollAreaWidgetContents_3.console = QConsole()
        self.verticalLayout_7.addWidget(self.scrollAreaWidgetContents_3.console)
        self.scrollArea_3.setWidget(self.scrollAreaWidgetContents_3)
        self.verticalLayout_4.addWidget(self.scrollArea_3)
        self.horizontalLayout_3.addWidget(self.splitter)
        self.verticalLayout.addWidget(self.widget_2)
        self.widget_3 = appCore.widgetClass(self.centralwidget)
        self.widget_3.setMaximumSize(QSize(16777215, 50))
        self.horizontalLayout_2 = QHBoxLayout(self.widget_3)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setSpacing(0)
        spacerItem1 = QSpacerItem(148, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)

        self.widget_3.createLabel("temp4", "Temp4")
        self.horizontalLayout_2.addWidget(self.widget_3.temp4_label)
        spacerItem2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem2)
        self.widget_3.createBtn("temp2", "Back", False)
        self.widget_3.temp2_btn.setMaximumSize(QSize(100, 16777215))
        self.widget_3.temp2_btn.setEnabled(False)
        self.horizontalLayout_2.addWidget(self.widget_3.temp2_btn)
        self.widget_3.createBtn("temp3", "Next", False)
        self.widget_3.temp3_btn.setMaximumSize(QSize(100, 16777215))
        self.horizontalLayout_2.addWidget(self.widget_3.temp3_btn)
        self.verticalLayout.addWidget(self.widget_3)

        self.setCentralWidget(self.centralwidget)

    def resetWindow(self):
        pass

    def find_window_for_pid(self, pid):
        result = None
        def callback(hwnd, _):
            nonlocal result
            ctid, cpid = win32process.GetWindowThreadProcessId(hwnd)
            if cpid == pid:
                result = hwnd
                return False
            return True
        win32gui.EnumWindows(callback, None)
        return result