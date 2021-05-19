from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QPushButton, QAction, QLineEdit, QMessageBox,QDialog
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
import pyttsx3
import datetime
from PyQt5.QtCore import QObject, QThread, pyqtSignal
import os
import threading
from threading import *
import numpy as np
import cv2
import pyautogui
import speech_recognition as sr
import pyttsx3
import webbrowser
import wikipedia
from bs4 import BeautifulSoup
from scipy.io.wavfile import write
import wavio as wv
import wolframalpha
import mechanize
import pyjokes
import sounddevice as sd

r = sr.Recognizer()
engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
engine.setProperty("voice",voices[0].id)



class Uibot(Thread):

    def __init__(self):
        super(Uibot, self).__init__()
        self.human=False
        self.ms_list=[[None,False] for i in range(7) ]
        self.audio=""
        self.botimg=QPixmap('bot.png')
        self.humanimg=QPixmap('human.jpg')
        self.bot_img=self.botimg.scaled(21,21)
        self.human_img=self.humanimg.scaled(21,21)


        self.win=QMainWindow()
        self.win.setGeometry(500,50,400,600)
        self.win.setWindowIcon(QtGui.QIcon('logo.png'))
        self.win.setWindowTitle("Bajirao - Chat bot")
        self.win.setStyleSheet("background-color:#040808" )


        self.textbox=QLineEdit(self.win)
        self.textbox.move(35,550)
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
                                    "    border: 2px #040808;\n"
                                    "    border-radius: 10px;\n"
                                    "    padding: 0 8px;\n"
                                    "    background: Cyan ;\n"
                                    "}")

        self.pb.clicked.connect(self.clickme)

        self.voice =QPushButton(self.win)
        self.voice.move(5,547)
        self.voice.resize(21,26)
        self.voice.setStyleSheet(u"QPushButton {\n"
                                    "    border: 2px Blue;\n"
                                    "    border-radius: 10px;\n"
                                    "    background-image:url(mic.jpg)  ;\n"
                                    "}")

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


        self.status_label = QLabel(self.frame_7)
        self.status_label.setObjectName(u"label_status")
        self.status_label.setGeometry(QRect(110, 30, 200, 20))
        self.status_label.setStyleSheet(u"QLabel{  \n"
                                            "\n"
                                            "  border: 1px grey;\n"
                                            "    border-radius: 4px;\n"
                                            "    padding: 0 4px;\n"
                                            "    background: grey;\n"
                                            "    selection-background-color: darkgray;\n"
                                            "\n"
                                            "}")
        self.status_label.setText("Status:- Idle")



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

    def status_bot(self):
        pass

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
        self.Take_ss()
        self.Open_ss()

    def Take_ss(self):
        lenth = len(self.ms_list)
        if self.ms_list[lenth - 1][0] == "Take a ss" :
            self.Screen_shot()
            self.bottochat("SS Taken")
            self.speak("SS Taken")


    def Open_ss(self):
        lenth = len(self.ms_list)
        if self.ms_list[lenth - 1][0] == "Open ss":
            self.bottochat("SS Opened")
            self.speak("SS Opened")
            open("//'Screen Shot'//")

    def botsay(self):
        lenth = len(self.ms_list)
        print(self.ms_list[lenth - 1][0])
        if self.ms_list[lenth - 1][0] == "hello":
            self.bottochat("Hello Sir")
            self.speak("Hello Sir")

    def WishMe(self):
        hour=int(datetime.datetime.now().hour)
        if hour>=0 and hour<12:
            self.speak("good morning")
            self.bottochat("good morning")
        elif hour>=12 and hour<18:

            self.speak("good afternoon")
            self.bottochat("good afternoon   "  )
        else:
            self.speak("good Evening")
            self.bottochat("good Evening    ")
        self.speak("  I am Bajirao sir . Please tell me how may I help you ? ")
        self.bottochat(" I am Bajirao sir . Please tell me how may I help you ?   ")

    def speak(self,audio):
        self.status_label.setText("Status:- Speaking...")
        engine.say(audio)
        engine.runAndWait()
        self.status_label.setText("Status:- Idle")

    def Screen_shot(self):
        image = pyautogui.screenshot()

        image2 = cv2.cvtColor(np.array(image),
                             cv2.COLOR_RGB2BGR)

        cv2.imwrite("'Screen Shot'//image1.png", image2)

    def Command(self):
        while (1):

            # Exception handling to handle
            # exceptions at the runtime
            self.status_label.setText("Status:- Listening...")
            try:

                # use the microphone as source for input.
                with sr.Microphone() as source2:

                    # wait for a second to let the recognizer
                    # adjust the energy threshold based on
                    # the surrounding noise level
                    r.adjust_for_ambient_noise(source2, duration=0.2)

                    # listens for the user's input
                    audio2 = r.listen(source2)

                    # Using ggogle to recognize audio
                    MyText = r.recognize_google(audio2)
                    MyText = MyText.lower()
                    query=MyText
                    print("Did you say " + MyText)
                    self.speak(MyText)

                    if "wikipedia" in query:
                        self.speak("searching wikipedia")
                        query = query.replace("wikipedia", "")
                        results = wikipedia.summary(query, sentences=2)
                        self.speak("according to wikipedia")
                        print(results)
                        self.speak(results)
                    elif "record audio" in query:
                        print("sir,tell me how long do you want to record in seconds")
                        self.speak("sir,tell me how long do you want to record in seconds")
                        duration = 10

                        print("recording...")
                        self.speak("recording")
                        freq = 44100
                        recording = sd.rec(int(duration * freq), samplerate=freq, channels=2)
                        sd.wait()
                        write("Recording/recording0.wav", freq, recording)
                        wv.write("recording1.wav", recording, freq, sampwidth=2)
                        self.speak("recording is completed")

                    elif "open youtube" in query:
                        webbrowser.open("youtube.com")
                    elif "open google" in query:
                        webbrowser.open("google.com")
                    elif "open stackoverflow" in query:
                        webbrowser.open("stackoverflow.com")
                    elif "open facebook" in query:
                        webbrowser.open("facebook.com")
                    elif "open twitter" in query:
                        webbrowser.open("twitter.com")
                    elif "open yahoo" in query:
                        webbrowser.open("hahoo.com")
                    elif "open bing" in query:
                        webbrowser.open("bing.com")
                    elif "open instagram" in query:
                        webbrowser.open("instagram.com")
                    elif "play music " in query:
                        music_dir = "C:\\music"
                        songs = os.listdir(music_dir)
                        print(songs)
                        os.startfile(os.path.join(music_dir, songs[0]))
                    elif "the time" in query:
                        strTime = datetime.datetime.now().strftime("%H:%M:%S")
                        self.speak(f"sir,the time is {strTime}")





                    elif "send email" in query:
                        try:
                            d1 = {}
                            with open("emails.txt", mode='r', encoding='utf-8') as contacts_file:
                                for a_contact in contacts_file:
                                    key = a_contact.split()[0]
                                    value = a_contact.split()[1]
                                    d1[key] = value

                            speak("tell me the name to whome you want to send the message")

                            name = takeCommand().lower()
                            speak("what should I say?")
                            content = takeCommand()

                            if name in d1:
                                to = d1[name]
                                sendEmail(to, content)
                                speak("email has been sent")
                        except Exception as e:
                            print(e)
                            speak("sorry sir I am not able to send email")





                    elif "search for" in query:
                        speak("searching for results in google")
                        try:
                            from googlesearch import search
                        except ImportError:
                            print("No module named 'google' found")

                        # to search
                        query = query.replace("search for", "")

                        for j in search(query, tld="co.in", num=10, stop=10, pause=2):
                            print(j)
                        speak("sir, here are the results according to google")




                    elif "the calendar" in query:
                        speak("tell me the year")
                        print("tell me the year")
                        yy = int(takeCommand().lower())
                        speak("tell me the month in digit")
                        print("tell me the month in digit")
                        mm = int(takeCommand().lower())
                        print("sir,the calender is shown bellow:")
                        speak("sir,the calender is shown bellow:")
                        cal = calendar.month(yy, mm)
                        print(cal)

                    elif "open whatsapp" in query:
                        wppath = "C:\\Users\\vivek\\AppData\\Local\\WhatsApp\\WhatsApp.exe"
                        os.startfile(wppath)




                    elif "play music " in query:
                        music_dir = "C:\\music"
                        songs = os.listdir(music_dir)
                        print(songs)
                        os.startfile(os.path.join(music_dir, songs[0]))



                    elif "open code" in query:
                        print("visual studio code is opening")
                        speak("visual studio code is opening")
                        codpath = "C:\\Users\\vivek\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
                        os.startfile(codpath)




                    elif "send whatsapp message" in query:

                        print("to whome sir")
                        speak("to whome sir")
                        whome = takeCommand().lower()
                        cotactNo = return_contact(whome, "contacts.txt")
                        print("what should I say?")
                        speak("what shiuld I say?")
                        msg = takeCommand().lower()
                        print("tell me the hour in 24hr format")
                        speak("tell me the hour in 24hr format")
                        hr = int(takeCommand().lower())
                        print("tell me the minutes")
                        speak("tell me the minutes")
                        minutes = int(takeCommand().lower())

                        pywhatkit.sendwhatmsg("+919689758160", msg, hr, minutes)
                        print("whatsapp  message has been sent")
                        speak("whatsapp  message has been sent")




                    elif "trace number" in query:
                        mc = mechanize.Browser()
                        mc.set_handle_robots(False)

                        url = 'https://www.findandtrace.com/trace-mobile-number-location'
                        mc.open(url)

                        mc.select_form(name='trace')
                        speak("enter the mobile number which you want to trace")
                        mc['mobilenumber'] = str(
                            input("enter the mobile number which you want to trace"))  # Enter a mobile number
                        res = mc.submit().read()

                        soup = BeautifulSoup(res, 'html.parser')
                        tbl = soup.find_all('table', class_='shop_table')
                        # print(tbl)

                        data = tbl[0].find('tfoot')
                        c = 0
                        for i in data:
                            c += 1
                            if c in (1, 4, 6, 8):
                                continue
                            th = i.find('th')
                            td = i.find('td')
                            print(th.text, td.text)
                        data = tbl[1].find('tfoot')
                        c = 0
                        for i in data:
                            c += 1
                            if c in (2, 20, 22, 26):
                                th = i.find('th')
                                td = i.find('td')
                                print(th.text, td.text)



                    elif "joke" in query:
                        print(pyjokes.get_joke())
                        speak(pyjokes.get_joke())




                    elif "take a video" in query:
                        print("opening the camera")
                        speak("opening the camera")
                        speak("press q for closing the camera")







            except sr.RequestError as e:
                print("Could not request results; {0}".format(e))

            except sr.UnknownValueError:
                print("unknown error occured")


    def run(self):
        self.WishMe()
        self.Command()


if __name__ == '__main__':
    app=QApplication(sys.argv)
    ob=Uibot() 


    ob.start()


    sys.exit(app.exec_())
