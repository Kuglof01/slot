from PyQt5 import QtCore, QtGui, QtWidgets
import random
import time



def slot(n):
        if n == 7:
            return "👑"
        elif n <= 6:
            return "🍒"
        elif n <= 9:
            return "💎"
        elif n <= 18:
            return "🍋"
        elif n <= 27:
            return "🍉"
        elif n <= 30:
            return "🍀"
        elif n <= 32:
            return "⭐"
        elif n <= 38:
            return "🧨"
        elif n <= 45:
            return "🍎"
        else:
            return "🍊"

class Ui_PocsiSpin(object):
    def setupUi(self, PocsiSpin):
        PocsiSpin.setObjectName("PocsiSpin")
        PocsiSpin.resize(1180, 640)
        self.centralwidget = QtWidgets.QWidget(PocsiSpin)
        self.centralwidget.setObjectName("centralwidget")
        self.centralwidget.setStyleSheet("border-image: url(grass.jpg) 0 0 0 0 stretch stretch")
        
        
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(187, 360, 41, 41))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Emoji")
        font.setPointSize(16)
        self.label.setFont(font)
        self.label.setStyleSheet("border-image: none")
        self.label.setScaledContents(False)
        self.label.setObjectName("label")
        
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(242, 360, 41, 41))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Emoji")
        font.setPointSize(16)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("border-image: none")
        self.label_2.setObjectName("label_2")
        
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(296, 360, 41, 41))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Emoji")
        font.setPointSize(16)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("border-image: none")
        self.label_3.setObjectName("label_3")
        
        self.lcdNumber = QtWidgets.QLCDNumber(self.centralwidget)
        self.lcdNumber.setGeometry(QtCore.QRect(180, 260, 161, 41))
        self.lcdNumber.setStyleSheet("background-color: rgb(255, 255, 255);border-image: none")
        self.lcdNumber.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.lcdNumber.setFrameShadow(QtWidgets.QFrame.Plain)
        self.lcdNumber.setLineWidth(1)
        self.lcdNumber.setDigitCount(7)
        self.lcdNumber.setProperty("value", 10000)
        self.lcdNumber.setObjectName("lcdNumber")
        
        self.dollar = QtWidgets.QLabel(self.centralwidget)
        self.dollar.setGeometry(QtCore.QRect(330, 260, 21, 41))
        self.dollar.setStyleSheet("background-color: rgb(255, 255, 255);border-image: none")
        self.dollar.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.dollar.setText("")
        self.dollar.setPixmap(QtGui.QPixmap("dollar.png"))
        self.dollar.setScaledContents(True)
        self.dollar.setObjectName("dollar")
        
        self.spin1 = QtWidgets.QPushButton(self.centralwidget)
        self.spin1.setGeometry(QtCore.QRect(420, 260, 41, 41))
        self.spin1.setStyleSheet("border-image: none; background-color: rgba(0, 0, 0, 0)")
        self.spin1.setObjectName("spin")
        self.spin1.clicked.connect(self.clicked_button)
        
        self.lcdNumber_2 = QtWidgets.QLCDNumber(self.centralwidget)
        self.lcdNumber_2.setGeometry(QtCore.QRect(170, 420, 71, 31))
        self.lcdNumber_2.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.lcdNumber_2.setDigitCount(7)
        self.lcdNumber_2.setStyleSheet("border-image: none")
        self.lcdNumber_2.setProperty("value", 0)
        self.lcdNumber_2.setObjectName("lcdNumber_2")
        
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(130, 500, 271, 121))
        self.label_4.setText("")
        self.label_4.setStyleSheet("border-image: none")
        self.label_4.setPixmap(QtGui.QPixmap("711344_make_a_slot_machine_title__logo__titled__Pöcsi_Spi_xl-1024-v1-0-removebg.png"))
        self.label_4.setScaledContents(True)
        self.label_4.setObjectName("label_4")
        
        self.chip5 = QtWidgets.QLabel(self.centralwidget)
        self.chip5.setGeometry(QtCore.QRect(200, 445, 35, 35))
        self.chip5.setStyleSheet("border-image: none")
        self.chip5.setText("")
        self.chip5.setPixmap(QtGui.QPixmap("5chip-removebg-preview.png"))
        self.chip5.setScaledContents(True)
        self.chip5.setObjectName("chip5")
        
        self.c5 = QtWidgets.QPushButton(self.centralwidget)
        self.c5.setGeometry(QtCore.QRect(200, 445, 35, 35))
        self.c5.setStyleSheet("border-image: none; background-color: rgba(0, 0, 0, 0)")
        self.c5.setObjectName("c5")
        self.c5.clicked.connect(self.ch5)
        
        self.chip50 = QtWidgets.QLabel(self.centralwidget)
        self.chip50.setGeometry(QtCore.QRect(300, 445, 35, 35))
        self.chip50.setStyleSheet("border-image: none")
        self.chip50.setText("")
        self.chip50.setPixmap(QtGui.QPixmap("50chip-removebg-preview.png"))
        self.chip50.setScaledContents(True)
        self.chip50.setObjectName("chip50")
        
        self.c50 = QtWidgets.QPushButton(self.centralwidget)
        self.c50.setGeometry(QtCore.QRect(300, 445, 35, 35))
        self.c50.setStyleSheet("border-image: none; background-color: rgba(0, 0, 0, 0)")
        self.c50.setObjectName("c50")
        self.c50.clicked.connect(self.ch50)
        
        self.chip10 = QtWidgets.QLabel(self.centralwidget)
        self.chip10.setGeometry(QtCore.QRect(250, 445, 35, 35))
        self.chip10.setStyleSheet("border-image: none")
        self.chip10.setText("")
        self.chip10.setPixmap(QtGui.QPixmap("10chip-removebg-preview.png"))
        self.chip10.setScaledContents(True)
        self.chip10.setObjectName("chip10")
        
        self.c10 = QtWidgets.QPushButton(self.centralwidget)
        self.c10.setGeometry(QtCore.QRect(250, 450, 35, 35))
        self.c10.setStyleSheet("border-image: none; background-color: rgba(0, 0, 0, 0)")
        self.c10.setObjectName("c10")
        self.c10.clicked.connect(self.ch10)
        
        self.all1 = QtWidgets.QLabel(self.centralwidget)
        self.all1.setGeometry(QtCore.QRect(345, 330, 50, 50))
        self.all1.setStyleSheet("border-image: none; background-color: rgb(0, 0, 0); color: rgb(255, 255, 255)")
        self.all1.setText("ALL_IN")
        font.setPointSize(40)
        self.all1.setScaledContents(True)
        self.all1.setObjectName("reset")

        self.a1 = QtWidgets.QPushButton(self.centralwidget)
        self.a1.setGeometry(QtCore.QRect(345, 330, 50, 50))
        self.a1.setStyleSheet("border-image: none; background-color: rgba(0, 0, 0, 0)")
        self.a1.setObjectName("a1")
        self.a1.clicked.connect(self.allin)

        self.reset1 = QtWidgets.QLabel(self.centralwidget)
        self.reset1.setGeometry(QtCore.QRect(345, 380, 50, 50))
        self.reset1.setStyleSheet("border-image: none")
        self.reset1.setText("")
        self.reset1.setPixmap(QtGui.QPixmap("button.png"))
        self.reset1.setScaledContents(True)
        self.reset1.setObjectName("reset")

        self.r1 = QtWidgets.QPushButton(self.centralwidget)
        self.r1.setGeometry(QtCore.QRect(345, 380, 50, 50))
        self.r1.setStyleSheet("border-image: none; background-color: rgba(0, 0, 0, 0)")
        self.r1.setObjectName("r1")
        self.r1.clicked.connect(self.reset)

        self.chip100 = QtWidgets.QLabel(self.centralwidget)
        self.chip100.setGeometry(QtCore.QRect(350, 445, 35, 35))
        self.chip100.setStyleSheet("border-image: none")
        self.chip100.setText("")
        self.chip100.setPixmap(QtGui.QPixmap("100chip-removebg-preview.png"))
        self.chip100.setScaledContents(True)
        self.chip100.setObjectName("chip100")
        
        self.c100 = QtWidgets.QPushButton(self.centralwidget)
        self.c100.setGeometry(QtCore.QRect(350, 445, 35, 35))
        self.c100.setStyleSheet("border-image: none; background-color: rgba(0, 0, 0, 0)")
        self.c100.setObjectName("c100")
        self.c100.clicked.connect(self.ch100)
        
        self.chip1 = QtWidgets.QLabel(self.centralwidget)
        self.chip1.setGeometry(QtCore.QRect(150, 445, 35, 35))
        self.chip1.setStyleSheet("border-image: none")
        self.chip1.setText("")
        self.chip1.setPixmap(QtGui.QPixmap("1chip-removebg-preview.png"))
        self.chip1.setScaledContents(True)
        self.chip1.setObjectName("chip1")
        
        self.c1 = QtWidgets.QPushButton(self.centralwidget)
        self.c1.setGeometry(QtCore.QRect(150, 445, 35, 35))
        self.c1.setStyleSheet("border-image: none; background-color: rgba(0, 0, 0, 0)")
        self.c1.setObjectName("c1")
        self.c1.clicked.connect(self.ch1)
        
        self.machine = QtWidgets.QLabel(self.centralwidget)
        self.machine.setGeometry(QtCore.QRect(-150, 10, 941, 601))
        self.machine.setText("")
        self.machine.setPixmap(QtGui.QPixmap("machine-removebg.png"))
        self.machine.setStyleSheet("border-image: none")
        self.machine.setScaledContents(True)
        self.machine.setObjectName("label_5")
        
        
        self.machine.raise_()
        self.label.raise_()
        self.label_2.raise_()
        self.label_3.raise_()
        self.lcdNumber.raise_()
        self.dollar.raise_()
        self.spin1.raise_()
        self.lcdNumber_2.raise_()
        self.label_4.raise_()
        self.chip5.raise_()
        self.chip50.raise_()
        self.chip10.raise_()
        self.chip100.raise_()
        self.chip1.raise_()
        self.c1.raise_()
        self.c10.raise_()
        self.c100.raise_()
        self.c5.raise_()
        self.c50.raise_()
        self.reset1.raise_()
        self.r1.raise_()
        self.all1.raise_()
        self.a1.raise_()
        PocsiSpin.setCentralWidget(self.centralwidget)

        self.retranslateUi(PocsiSpin)
        QtCore.QMetaObject.connectSlotsByName(PocsiSpin)

    def retranslateUi(self, PocsiSpin):
        _translate = QtCore.QCoreApplication.translate
        PocsiSpin.setWindowTitle(_translate("PocsiSpin", "MainWindow"))
        self.label.setText(_translate("PocsiSpin", "⭐"))
        self.label_2.setText(_translate("PocsiSpin", "🍒"))
        self.label_3.setText(_translate("PocsiSpin", "🍀"))
        
    def ch1(self):
        bet = self.lcdNumber_2.value()
        bet += 1
        self.lcdNumber_2.setProperty("value", bet)
        
    def ch5(self):
        bet = self.lcdNumber_2.value()
        bet += 5
        self.lcdNumber_2.setProperty("value", bet)
        
    def ch50(self):
        bet = self.lcdNumber_2.value()
        bet += 50
        self.lcdNumber_2.setProperty("value", bet)
        
    def ch10(self):
        bet = self.lcdNumber_2.value()
        bet += 10
        self.lcdNumber_2.setProperty("value", bet)
        
    def ch100(self):
        bet = self.lcdNumber_2.value()
        bet += 100
        self.lcdNumber_2.setProperty("value", bet)

    def reset(self):
        bet = self.lcdNumber_2.value()
        
        self.lcdNumber_2.setProperty("value", bet)

    def allin(self):
        bet = self.lcdNumber_2.value()
        bal = self.lcdNumber.value()
        bet -= bet
        bet += bal
        self.lcdNumber_2.setProperty("value", bet)


    def clicked_button(self):
         
        try:
            bet = self.lcdNumber_2.value()
        except ValueError:
            bet = 0

        bal = self.lcdNumber.value()
        if bal < bet or bet < 0:
            return  

        bal -= bet
        self.lcdNumber.setProperty("value", bal)

        
        
        self.n1 = random.randint(1, 40)
        self.n2 = random.randint(1, 40)
        self.n3 = random.randint(1, 40)
        
        self.t1 = random.randint(7, 15)
        self.tt2 = random.randint(3, 6)
        self.tt3 = random.randint(10, 16)
        self.t2 = self.t1 + self.tt2
        self.t3 = self.t2 + self.tt3
        

        self.iteration = 0
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.spin)
        self.timer.start(200) 


    def spin(self):
        
        
        if self.iteration < self.t1:
            self.label.setText(slot(random.randint(1, 40)))
            
            
        if self.iteration < self.t2:
            self.label_2.setText(slot(random.randint(1, 40)))
            
            
        if self.iteration < self.t3:
            self.label_3.setText(slot(random.randint(1, 40)))

        self.iteration += 1

        if self.iteration >= max(self.t1, self.t2, self.t3):
            self.timer.stop()
            self.win()

    def win(self):

        bet = self.lcdNumber_2.value()
        bal = self.lcdNumber.value()
        
        
       
        self.s1 = self.label.text()
        self.s2 = self.label_2.text()
        self.s3 = self.label_3.text()
            
            
        if self.s1 == self.s2 == self.s3:
            if self.s1 == "👑":
                bal += bet * 100
            elif self.s1 == "🍒":
                bal += bet * 5
            elif self.s1 == "💎":
                bal += bet * 8
            elif self.s1 == "🍋":
                bal += bet * 3
            elif self.s1 == "🍉":
                bal += bet * 3
            elif self.s1 == "🍀":
                bal += bet * 8
            elif self.s1 == "⭐":
                bal += bet * 15
            elif self.s1 == "🧨":
                bal += bet * 3
            elif self.s1 == "🍎":
                bal += bet * 3
            else:  # 🍊
                bal += bet * 3
        elif self.s1 == self.s2 or self.s2 == self.s3 or self.s1 == self.s3:
            if "👑" in [self.s1, self.s2, self.s3]:
                bal += bet * 25  
            elif "🍒" in [self.s1, self.s2, self.s3]:
                bal += bet * 2
            elif "💎" in [self.s1, self.s2, self.s3]:
                bal += bet * 5
            elif "🍋" in [self.s1, self.s2, self.s3]:
                bal += bet * 2
            elif "🍉" in [self.s1, self.s2, self.s3]:
                bal += bet * 2
            elif "🍀" in [self.s1, self.s2, self.s3]:
                bal += bet * 5
            elif "⭐" in [self.s1, self.s2, self.s3]:
                bal += bet * 6
            elif "🧨" in [self.s1, self.s2, self.s3]:
                bal += bet * 2
            elif "🍎" in [self.s1, self.s2, self.s3]:
                bal += bet * 2
            else:  # 🍊
                bal += bet * 2
    
        print(f"{self.s1}{self.s2}{self.s3}")
        self.lcdNumber.setProperty("value", bal)
        
 

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    PocsiSpin = QtWidgets.QMainWindow()
    ui = Ui_PocsiSpin()
    ui.setupUi(PocsiSpin)
    PocsiSpin.show()
    sys.exit(app.exec_())
