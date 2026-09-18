from Brain.AIBrain import ReplyBrain
from Brain.QNA import QuestionAnswer
from Body.Speak import Speak
import sys
Speak("Starting Jarvis : Wait For Few Seconds")
from Body.Listen import MicExecusion
from test import MaintaskExecution
from jarvisui import Ui_Dialog
from PyQt5 import QtGui
from PyQt5.QtGui import * # star to import everything under the specific package
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from time import sleep
Speak("Starting Jarvis")


class Mainthread(QThread):

    def __init__(self):
        super(Mainthread,self).__init__()

    def run(self):
        self.MainExecusion()

    def MainExecusion(self):

        Speak("Hello Sir")
        Speak("Jarvis is ready to assist you")

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
        self.Jarvis_ui = Ui_Dialog()
        self.Jarvis_ui.setupUi(self)

        self.Jarvis_ui.pushButton.clicked.connect(self.startFunc)# to start when clicked on start button

    def startFunc(self):
        self.Jarvis_ui.movies= QtGui.QMovie("Qualt.gif")
        self.Jarvis_ui.label.setMovie(self.Jarvis_ui.movies)
        self.Jarvis_ui.movies.start()

        timer = QTimer(self)
        timer.timeout.connect(self.showTimeLive)# To show current time
        timer.start(999)

        startFunction.start()
    
    def showTimeLive(self):
        timee = QTime.currentTime()
        time = timee.toString()
        label_time = "Time :" + time

        self.Jarvis_ui.textBrowser.setText(label_time)

Gui_App = QApplication(sys.argv)
Gui_Jarvis = Gui_Start()
Gui_Jarvis.show()
exit(Gui_App.exec_())# to stop the code when clicked on cross button
