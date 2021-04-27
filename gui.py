from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QPushButton, QAction, QLineEdit, QMessageBox
from PyQt5.QtWidgets import *
from PyQt5 import QtGui
from PyQt5 import QtCore
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot
from PyQt5 import QtCore, QtGui
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import sys
from PyQt5.QtGui import QMovie
from PyQt5.QtCore import Qt





class Uibot(object):
    def __init__(self):
        self.human=False
        self.ms_list=[[None,False] for i in range(7) ]
        self.botimg=QPixmap('bot.png')
        self.humanimg=QPixmap('human.jpg')
        self.bot_img=self.botimg.scaled(21,21)
        self.human_img=self.humanimg.scaled(21,21)

    def Main(self):

        self.win=QMainWindow()
        self.win.setGeometry(500,50,400,600)
        self.win.setWindowIcon(QtGui.QIcon('logo.png'))
        self.win.setWindowTitle("Bajirao - Chat bot")
        self.win.setStyleSheet("background-color:#040808" )


        self.textbox=QLineEdit(self.win)
        self.textbox.move(30,550)
        self.textbox.resize(300,25)
        self.textbox.setPlaceholderText("Type here")
        self.textbox.setStyleSheet(u"QLineEdit {\n"
                                    "    border: 2px solid gray;\n"
                                    "    border-radius: 10px;\n"
                                    "    padding: 0 8px;\n"
                                    "    background: white ;\n"
                                    "    selection-background-color: Cyan;\n"
                                    "}")

        self.pb = QPushButton(self.win)
        self.pb.move(340,550)
        self.pb.resize(40,25)
        self.pb.setText("Send")
        self.pb.setStyleSheet(u"QPushButton {\n"
                                    "    border: 2px Blue;\n"
                                    "    border-radius: 10px;\n"
                                    "    padding: 0 8px;\n"
                                    "    background: Cyan ;\n"
                                    "}")

        self.pb.clicked.connect(self.clickme)




        self.verticalLayoutWidget = QWidget(self.win)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(0, 150, 391, 391))
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)

        self.frame = QFrame(self.verticalLayoutWidget)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)


        self.frame_2 = QFrame(self.verticalLayoutWidget)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setGeometry(QRect(-10, 320, 391, 61))
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)


        self.label_20 = QLabel(self.frame_2)
        self.label_20.setObjectName(u"label_20")
        self.label_20.setGeometry(QRect(270, 30, 81, 21))

        self.label_21 = QLabel(self.frame_2)
        self.label_21.setObjectName(u"label_21")
        self.label_21.setGeometry(QRect(360, 30, 21, 21))

        self.label_22 = QLabel(self.frame_2)
        self.label_22.setObjectName(u"label_22")
        self.label_22.setGeometry(QRect(290, 10, 61, 16))


        self.frame_3 = QFrame(self.frame)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setGeometry(QRect(-10, 260, 391, 61))
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.label_23 = QLabel(self.frame_3)
        self.label_23.setObjectName(u"label_23")
        self.label_23.setGeometry(QRect(270, 30, 81, 21))
        self.label_24 = QLabel(self.frame_3)
        self.label_24.setObjectName(u"label_24")
        self.label_24.setGeometry(QRect(360, 30, 21, 21))
        self.label_25 = QLabel(self.frame_3)
        self.label_25.setObjectName(u"label_25")
        self.label_25.setGeometry(QRect(290, 10, 61, 16))


        self.frame_4 = QFrame(self.frame)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setGeometry(QRect(-10, 210, 391, 61))
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.label_26 = QLabel(self.frame_4)
        self.label_26.setObjectName(u"label_26")
        self.label_26.setGeometry(QRect(270, 30, 81, 21))
        self.label_27 = QLabel(self.frame_4)
        self.label_27.setObjectName(u"label_27")
        self.label_27.setGeometry(QRect(360, 30, 21, 21))
        self.label_28 = QLabel(self.frame_4)
        self.label_28.setObjectName(u"label_28")
        self.label_28.setGeometry(QRect(290, 10, 61, 16))


        self.frame_5 = QFrame(self.frame)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setGeometry(QRect(-10, 160, 391, 61))
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.label_29 = QLabel(self.frame_5)
        self.label_29.setObjectName(u"label_29")
        self.label_29.setGeometry(QRect(270, 30, 81, 21))
        self.label_30 = QLabel(self.frame_5)
        self.label_30.setObjectName(u"label_30")
        self.label_30.setGeometry(QRect(360, 30, 21, 21))
        self.label_31 = QLabel(self.frame_5)
        self.label_31.setObjectName(u"label_31")
        self.label_31.setGeometry(QRect(290, 10, 61, 16))


        self.frame_6 = QFrame(self.frame)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setGeometry(QRect(-10, 100, 391, 61))
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.label_32 = QLabel(self.frame_6)
        self.label_32.setObjectName(u"label_32")
        self.label_32.setGeometry(QRect(270, 30, 81, 21))
        self.label_33 = QLabel(self.frame_6)
        self.label_33.setObjectName(u"label_33")
        self.label_33.setGeometry(QRect(360, 30, 21, 21))
        self.label_34 = QLabel(self.frame_6)
        self.label_34.setObjectName(u"label_34")
        self.label_34.setGeometry(QRect(290, 10, 61, 16))


        self.frame_7 = QFrame(self.frame)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setGeometry(QRect(-10, 50, 391, 61))
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.label_35 = QLabel(self.frame_7)
        self.label_35.setObjectName(u"label_35")
        self.label_35.setGeometry(QRect(270, 30, 81, 21))
        self.label_36 = QLabel(self.frame_7)
        self.label_36.setObjectName(u"label_36")
        self.label_36.setGeometry(QRect(360, 30, 21, 21))
        self.label_37 = QLabel(self.frame_7)
        self.label_37.setObjectName(u"label_37")
        self.label_37.setGeometry(QRect(290, 10, 61, 16))



        self.verticalLayout.addWidget(self.frame)



        self.textbox.returnPressed.connect(self.clickme)

        self.label_2 = QLabel(self.win)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(100, 20, 200, 200))
        self.movie = QMovie("bot2.gif")
        self.label_2.setMovie(self.movie)
        self.movie.start()

        self.win.show()

    def msglog(self):


        lent=len(self.ms_list)

        if self.ms_list[lent - 5][0] != None:
            if self.ms_list[lent - 5][1] == True:
                self.label_34.setText("Human")
                self.label_33.setPixmap(self.human_img)
                self.label_32.setText(self.ms_list[lent - 5][0])
                self.label_34.move(290,10)
                self.label_33.move(360,30)
                self.label_32.move(270,30)
                self.label_32.adjustSize()
                self.label_32.setFixedHeight(20)
                self.label_33.setStyleSheet(u"QLabel{  \n"
                                            "\n"
                                            "  border: 1px Cyan;\n"
                                            "    border-radius: 4px;\n"
                                            "    padding: 0 4px;\n"
                                            "    background: White;\n"
                                            "    selection-background-color: darkgray;\n"
                                            "\n"
                                            "}")
            else:
                self.label_34.setText("Bajirao")
                self.label_33.setPixmap(self.bot_img)
                self.label_32.setText(self.ms_list[lent - 5][0])
                self.label_34.move(370-290,10)
                self.label_33.move(400-360,30)
                self.label_32.move(350-270,30)
                self.label_32.adjustSize()
                self.label_32.setFixedHeight(20)
                self.label_32.setStyleSheet(u"QLabel{  \n"
                                            "\n"
                                            "  border: 1px Cyan;\n"
                                            "    border-radius: 4px;\n"
                                            "    padding: 0 4px;\n"
                                            "    background: White;\n"
                                            "    selection-background-color: darkgray;\n"
                                            "\n"
                                            "}")

        if self.ms_list[lent - 4][0] != None:
            if self.ms_list[lent - 4][1] == True:
                self.label_31.setText("Human")
                self.label_30.setPixmap(self.human_img)
                self.label_29.setText(self.ms_list[lent - 4][0])
                self.label_31.move(290, 10)
                self.label_30.move(360, 30)
                self.label_29.move(270, 30)
                self.label_29.adjustSize()
                self.label_29.setFixedHeight(20)
                self.label_29.setStyleSheet(u"QLabel{  \n"
                                            "\n"
                                            "  border: 1px Cyan;\n"
                                            "    border-radius: 4px;\n"
                                            "    padding: 0 4px;\n"
                                            "    background: White;\n"
                                            "    selection-background-color: darkgray;\n"
                                            "\n"
                                            "}")
            else:
                self.label_31.setText("Bajirao")
                self.label_30.setPixmap(self.bot_img)
                self.label_29.setText(self.ms_list[lent - 4][0])
                self.label_31.move(370-290,10)
                self.label_30.move(400-360,30)
                self.label_29.move(350-270,30)
                self.label_29.adjustSize()
                self.label_29.setFixedHeight(20)
                self.label_29.setStyleSheet(u"QLabel{  \n"
                                            "\n"
                                            "  border: 1px Cyan;\n"
                                            "    border-radius: 4px;\n"
                                            "    padding: 0 4px;\n"
                                            "    background: White;\n"
                                            "    selection-background-color: darkgray;\n"
                                            "\n"
                                            "}")


        if self.ms_list[lent - 3][0] != None:
            if self.ms_list[lent - 3][1] == True:
                self.label_28.setText("Human")
                self.label_27.setPixmap(self.human_img)
                self.label_26.setText(self.ms_list[lent - 3][0])
                self.label_28.move(290, 10)
                self.label_27.move(360, 30)
                self.label_26.move(270, 30)
                self.label_26.adjustSize()
                self.label_26.setFixedHeight(20)
                self.label_26.setStyleSheet(u"QLabel{  \n"
                                            "\n"
                                            "  border: 1px Cyan;\n"
                                            "    border-radius: 4px;\n"
                                            "    padding: 0 4px;\n"
                                            "    background: White;\n"
                                            "    selection-background-color: darkgray;\n"
                                            "\n"
                                            "}")
            else:
                self.label_28.setText("Bajirao")
                self.label_27.setPixmap(self.bot_img)
                self.label_26.setText(self.ms_list[lent - 3][0])
                self.label_28.move(370-290,10)
                self.label_27.move(400-360,30)
                self.label_26.move(350-270,30)
                self.label_26.adjustSize()
                self.label_26.setFixedHeight(20)
                self.label_26.setStyleSheet(u"QLabel{  \n"
                                            "\n"
                                            "  border: 1px Cyan;\n"
                                            "    border-radius: 4px;\n"
                                            "    padding: 0 4px;\n"
                                            "    background: White;\n"
                                            "    selection-background-color: darkgray;\n"
                                            "\n"
                                            "}")

        if self.ms_list[lent - 2][0] != None:
            if self.ms_list[lent - 2][1] == True:
                self.label_25.setText("Human")
                self.label_24.setPixmap(self.human_img)
                self.label_23.setText(self.ms_list[lent - 2][0])
                self.label_25.move(290, 10)
                self.label_24.move(360, 30)
                self.label_23.move(270, 30)
                self.label_23.adjustSize()
                self.label_23.setFixedHeight(20)
                self.label_23.setStyleSheet(u"QLabel{  \n"
                                            "\n"
                                            "  border: 1px Cyan;\n"
                                            "    border-radius: 4px;\n"
                                            "    padding: 0 4px;\n"
                                            "    background: White;\n"
                                            "    selection-background-color: darkgray;\n"
                                            "\n"
                                            "}")
            else:
                self.label_25.setText("Bajirao")
                self.label_24.setPixmap(self.bot_img)
                self.label_23.setText(self.ms_list[lent - 2][0])
                self.label_25.move(370-290,10)
                self.label_24.move(400-360,30)
                self.label_23.move(350-270,30)
                self.label_23.adjustSize()
                self.label_23.setFixedHeight(20)
                self.label_23.setStyleSheet(u"QLabel{  \n"
                                            "\n"
                                            "  border: 1px Cyan;\n"
                                            "    border-radius: 4px;\n"
                                            "    padding: 0 4px;\n"
                                            "    background: White;\n"
                                            "    selection-background-color: darkgray;\n"
                                            "\n"
                                            "}")

        if self.ms_list[lent - 1][0] != None:
            if self.ms_list[lent - 1][1] == True:
                self.label_22.setText("Human")
                self.label_21.setPixmap(self.human_img)
                self.label_20.setText(self.ms_list[lent - 1][0])
                self.label_22.move(290, 10)
                self.label_21.move(360, 30)
                self.label_20.move(270, 30)
                self.label_20.adjustSize()
                self.label_20.setFixedHeight(20)
                self.label_20.setStyleSheet(u"QLabel{  \n"
                                            "\n"
                                            "  border: 1px Cyan;\n"
                                            "    border-radius: 4px;\n"
                                            "    padding: 0 4px;\n"
                                            "    background: White;\n"
                                            "    selection-background-color: darkgray;\n"
                                            "\n"
                                            "}")

            else:
                self.label_22.setText("Bajirao")
                self.label_21.setPixmap(self.bot_img)
                self.label_20.setText(self.ms_list[lent - 1][0])
                self.label_22.move(370-290,10)
                self.label_21.move(400-360,30)
                self.label_20.move(350-270,30)
                self.label_20.adjustSize()
                self.label_20.setFixedHeight(20)
                self.label_20.setStyleSheet(u"QLabel{  \n"
                                            "\n"
                                            "  border: 1px Cyan;\n"
                                            "    border-radius: 4px;\n"
                                            "    padding: 0 4px;\n"
                                            "    background: White;\n"
                                            "    selection-background-color: darkgray;\n"
                                            "\n"
                                            "}")


    def addtochat(self,text):
        self.human=True
        self.ms_list.append([text,True])


    def bottochat(self,text):
        self.human=False
        self.ms_list.append([text,False])
        self.msglog()

    def clickme(self):
        text=self.textbox.text()
        self.addtochat(text)
        self.textbox.setText("")
        self.botsay()

    def botsay(self):
        lenth = len(self.ms_list)
        if self.ms_list[lenth - 1][0] != " ":
            self.bottochat("Hello Friend")





if __name__ == '__main__':
    app=QApplication(sys.argv)
    ob=Uibot()
    ob.Main()


    sys.exit(app.exec_())
