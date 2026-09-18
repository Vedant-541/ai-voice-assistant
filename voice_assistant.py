from Brain.AIBrain import ReplyBrain
from Brain.QNA import QuestionAnswer
from Body.Speak import Speak
import sys
Speak("Starting Voice Assistant: please wait a few seconds.")
from Body.Listen import MicExecusion
from test import MaintaskExecution
from voice_assistant_ui import Ui_Dialog
from PyQt5 import QtGui
from PyQt5.QtGui import * # star to import everything under the specific package
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from time import sleep
Speak("Starting Voice Assistant")


class Mainthread(QThread):

    def __init__(self):
        super(Mainthread,self).__init__()

    def run(self):
        self.MainExecusion()

    def MainExecusion(self):

        Speak("Hello Sir")
        Speak("Voice Assistant is ready to assist you")

        while True:

            self.Data = MicExecusion()
            self.data = str(self.Data)

            self.ValueReturn = MaintaskExecution(self.data)#for open command
            if self.ValueReturn==True:
                sleep(2)
                pass

            elif len(self.data)<3:
                pass

            elif "what" in self.data or "where" in self.data:#if used what and where, answer will be saved in qna_log
                self.Reply = QuestionAnswer(self.data)
                Speak(self.Reply)
                sleep(2)

            else:
                self.Reply = ReplyBrain(self.data)#if nothing, answer will be saved in chat_log
                Speak(self.Reply)
                sleep(2)

startFunction = Mainthread()

class Gui_Start(QMainWindow):#To run gui

    def __init__(self):
        super().__init__()
        self.voice_assistant_ui = Ui_Dialog()
        self.voice_assistant_ui.setupUi(self)

        self.voice_assistant_ui.pushButton.clicked.connect(self.startFunc)# to start when clicked on start button

    def startFunc(self):
        self.voice_assistant_ui.movies= QtGui.QMovie("Qualt.gif")
        self.voice_assistant_ui.label.setMovie(self.voice_assistant_ui.movies)
        self.voice_assistant_ui.movies.start()

        timer = QTimer(self)
        timer.timeout.connect(self.showTimeLive)# To show current time
        timer.start(999)

        startFunction.start()
    
    def showTimeLive(self):
        timee = QTime.currentTime()
        time = timee.toString()
        label_time = "Time :" + time

        self.voice_assistant_ui.textBrowser.setText(label_time)

Gui_App = QApplication(sys.argv)
Gui_VoiceAssistant = Gui_Start()
Gui_VoiceAssistant.show()
exit(Gui_App.exec_())# to stop the code when clicked on cross button
