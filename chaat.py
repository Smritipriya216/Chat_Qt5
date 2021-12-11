from datetime import datetime
from PyQt5.QtWidgets  import QMainWindow,QApplication, QLabel,QPushButton, QTextBrowser ,QTextEdit
from PyQt5 import uic
import sys
import datetime
import pyttsx3
import pywhatkit
import wikipedia
import pyjokes


class UI(QMainWindow):
    def __init__(self):
        super(UI, self).__init__()

     
        uic.loadUi("chat.ui", self)
        
        self.label = self.findChild(QLabel, "label")
        self.textbrowser = self.findChild(QTextBrowser,"textBrowser")
        self.button = self.findChild(QPushButton,"pushButton")
        self.clear_button = self.findChild(QPushButton,"pushButton_2")
        self.textedit = self.findChild(QTextEdit,"textEdit")
        
        self.button.clicked.connect(self.clicker)
        self.clear_button.clicked.connect(self.clearer)

        self.show()


    def clearer(self):
        self.textedit.setPlainText("")
        self.textbrowser.setText("Message Deleted!")
        self.textbrowser.setText("")

    def clicker(self):
        self.text = self.textedit.toPlainText()
        if 'alexa' in self.text:  
            self.textbrowser.append(f'<br><p align=\"left\"><b style="font-family:Trebuchet MS;color:white">User :</b> {self.textedit.toPlainText()}');
            if 'hey' in self.text or 'hello' in self.text or 'hi' in self.text:
                self.textbrowser.append('<br><p align=\"right\"><b style="font-family:Trebuchet MS;color:white">Assitant : </b>Hello there!!What can I do for you?')
                self.textedit.setPlainText("");

            elif 'how are you' in self.text:
                self.textbrowser.append('<br><p align=\"right\"><b style="font-family:Trebuchet MS;color:white">Assitant : </b>I am fine. Thanks for asking!!')
                self.textedit.setPlainText("");

            elif 'are you single' in self.text:
                self.textbrowser.append('<br><p align=\"right\"><b style="font-family:Trebuchet MS;color:white">Assitant : </b>No,I am in relationship with WIFI.')
                self.textedit.setPlainText("");
                
            elif 'time' in self.text:
                time=datetime.datetime.now().strftime('%I:%M %p') 
                self.textbrowser.append(f'<br><p align=\"right\"><b style="font-family:Trebuchet MS;color:white">Assitant :</b> The time is {time}.')
                self.textedit.setPlainText("");

            elif  'date' in self.text:
                date = datetime.datetime.today().strftime("%Y-%m-%d")
                self.textbrowser.append(f'<br><p align=\"right\"><b style="font-family:Trebuchet MS;color:white">Assitant :</b> The date is {date}.')
                self.textedit.setPlainText("");

            elif  'play' in self.text:
                song=self.text.replace('alexa play','')
                pywhatkit.playonyt(song)
                self.textbrowser.append(f'<br><p align=\"right\"><b style="font-family:Trebuchet MS;color:white">Assitant :</b> Playing {song}.')
                self.textedit.setPlainText("");
            
            elif  'who' in self.text:
                person = self.text.replace('alexa who is','')
                info=wikipedia.summary(person,1)
                self.textbrowser.append(f'<br><p align=\"right\"><b style="font-family:Trebuchet MS;color:white">Assitant :</b>{info}.')
                self.textedit.setPlainText("");
            
            elif  'tell me about' in self.text :
                person = self.text.replace('alexa tell me about','')
                info_1=wikipedia.summary(person,1)
                self.textbrowser.append(f'<br><p align=\"right\"><b style="font-family:Trebuchet MS;color:white">Assitant :</b>{info_1}.')
                self.textedit.setPlainText("");

            elif  'what' in self.text:
                person = self.text.replace('alexa what','')
                info=wikipedia.summary(person,1)
                self.textbrowser.append(f'<br><p align=\"right\"><b style="font-family:Trebuchet MS;color:white">Assitant :</b>{info}.')
                self.textedit.setPlainText("");

            elif  'do you love me' in self.text:
                self.textbrowser.append('<br><p align=\"right\"><b style="font-family:Trebuchet MS;color:white">Assitant : </b>Yeah!! You are an amazing person and I like you.')
                self.textedit.setPlainText("");

            elif  'joke' in self.text:
                fun=pyjokes.get_joke()
                self.textbrowser.append(f'<br><p align=\"right\"><b style="font-family:Trebuchet MS;color:white">Assitant :</b>{fun}.')
                self.textedit.setPlainText("");
            
            else:
                self.textbrowser.append('<br><p align=\"right\"><b style="font-family:Trebuchet MS;color:red">Assitant : </b>Sorry,I am not customized to perform above task.')
                self.textedit.setPlainText("");


       

        self.textedit.setPlainText("")


app = QApplication(sys.argv)
UIWindow = UI()
app.exec_()
