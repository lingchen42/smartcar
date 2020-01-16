# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'F:/GUO/test/qss/Client_Ui.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtWidgets.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtWidgets.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtWidgets.QApplication.translate(context, text, disambig)

# grey appearance
GENERAL_COLOR = (72, 72, 72)
SIZE = (800, 850)
VIDEO_SIZE = (800, 450)

class Ui_Client(object):
    def setupUi(self, Client):
        Client.setObjectName(_fromUtf8("Client"))
        Client.resize(*SIZE)

        palette = QtGui.QPalette()
        for i in [QtGui.QPalette.Active, QtGui.QPalette.Inactive,
                  QtGui.QPalette.Disabled]:
            for j in [QtGui.QPalette.Button, QtGui.QPalette.Base,
                      QtGui.QPalette.Window]:
                      brush = QtGui.QBrush(QtGui.QColor(*GENERAL_COLOR))
                      brush.setStyle(QtCore.Qt.SolidPattern)
                      palette.setBrush(i, j, brush)

        Client.setPalette(palette)
        font = QtGui.QFont()
        font.setPointSize(14)
        Client.setFont(font)
        Client.setStyleSheet(_fromUtf8("QWidget{\n"
"background:#484848;\n"
"}\n"
"QAbstractButton{\n"
"border-style:none;\n"
"border-radius:0px;\n"
"padding:5px;\n"
"color:#DCDCDC;\n"
"background:qlineargradient(spread:pad,x1:0,y1:0,x2:0,y2:1,stop:0 #484848,stop:1 #383838);\n"
"}\n"
"QAbstractButton:hover{\n"
"color:#FFFFFF;\n"
"background-color:#00BB9E;\n"
"}\n"
"QAbstractButton:pressed{\n"
"color:#DCDCDC;\n"
"border-style:solid;\n"
"border-width:0px 0px 0px 2px;\n"
"padding:4px 4px 4px 2px;\n"
"border-color:#00BB9E;\n"
"background-color:#444444;\n"
"}\n"
"QLabel{\n"
"color:#DCDCDC;\n"
"border:1px solid #242424;\n"
"background:qlineargradient(spread:pad,x1:0,y1:0,x2:0,y2:1,stop:0 #484848,stop:1 #383838);\n"
"}\n"
"QLabel:focus{\n"
"border:1px solid #00BB9E;\n"
"background:qlineargradient(spread:pad,x1:0,y1:0,x2:0,y2:1,stop:0 #646464,stop:1 #525252);\n"
"}\n"
"QLineEdit{\n"
"border:1px solid #242424;\n"
"border-radius:3px;\n"
"padding:2px;\n"
"background:none;\n"
"selection-background-color:#484848;\n"
"selection-color:#DCDCDC;\n"
"}\n"
"QLineEdit:focus,QLineEdit:hover{\n"
"border:1px solid #242424;\n"
"}\n"
"QLineEdit{\n"
"border:1px solid #242424;\n"
"border-radius:3px;\n"
"padding:2px;\n"
"background:none;\n"
"selection-background-color:#484848;\n"
"selection-color:#DCDCDC;\n"
"}\n"
"\n"
"QLineEdit:focus,QLineEdit:hover{\n"
"border:1px solid #242424;\n"
"}\n"
"QLineEdit{\n"
"lineedit-password-character:9679;\n"
"}\n"
"QSlider::groove:horizontal,QSlider::add-page:horizontal{\n"
"height:3px;\n"
"border-radius:3px;\n"
"background:#18181a;\n"
"}\n"
"\n"
"\n"
"QSlider::sub-page:horizontal{\n"
"height:8px;\n"
"border-radius:3px;\n"
"background:#008aff;\n"
"}\n"
"\n"
"\n"
"QSlider::handle:horizontal{\n"
"width:12px;\n"
"margin-top:-5px;\n"
"margin-bottom:-4px;\n"
"border-radius:6px;\n"
"background:qradialgradient(spread:pad,cx:0.5,cy:0.5,radius:0.5,fx:0.5,fy:0.5,stop:0.6 #565656,stop:0.8 #565656);\n"
"}\n"
"\n"
"\n"
"QSlider::groove:vertical,QSlider::sub-page:vertical{\n"
"width:3px;\n"
"border-radius:3px;\n"
"background:#18181a;\n"
"}\n"
"\n"
"\n"
"QSlider::add-page:vertical{\n"
"width:8px;\n"
"border-radius:3px;\n"
"background:#008aff;\n"
"}\n"
"\n"
"\n"
"QSlider::handle:vertical{\n"
"height:12px;\n"
"margin-left:-5px;\n"
"margin-right:-4px;\n"
"border-radius:6px;\n"
"background:qradialgradient(spread:pad,cx:0.5,cy:0.5,radius:0.5,fx:0.5,fy:0.5,stop:0.6 #565656,stop:0.8 #565656);\n"
"}\n"
""))
        ################# Title ##############################################
        self.name = QtWidgets.QLabel(Client)
        self.name.setGeometry(QtCore.QRect(0, 1, SIZE[1], 30))
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(70)
        self.name.setFont(font)
        self.name.setStyleSheet(_fromUtf8(""))
        self.name.setObjectName(_fromUtf8("name"))

        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(20)
        self.Window_Min = QtWidgets.QPushButton(Client)
        self.Window_Min.setGeometry(QtCore.QRect(700, 1, 50, 30))
        self.Window_Min.setObjectName(_fromUtf8("Window_Min"))

        self.Window_Close = QtWidgets.QPushButton(Client)
        self.Window_Close.setGeometry(QtCore.QRect(750, 1, 50, 30))
        self.Window_Close.setObjectName(_fromUtf8("Window_Close"))

        ################## Video window #######################################
        self.label_Video = QtWidgets.QLabel(Client)
        self.label_Video.setGeometry(QtCore.QRect(1, 31, VIDEO_SIZE[0], VIDEO_SIZE[1]))
        self.label_Video.setText(_fromUtf8(""))
        self.label_Video.setObjectName(_fromUtf8("label_Video"))
        
        ################# Line 1 ##############################################
        # Line 1; y, 460 ; h, 25; w, 100
        y = 460 + 30
        w = 97
        h = 25
        x_base = 190
        # Video
        for i, b in enumerate(["Btn_Connect",
                               "Btn_Video",
                               "Btn_Recording",
                               "Btn_Tracking_Faces",
                               "Ultrasonic",
                               "Light"]):
            setattr(self, b, QtWidgets.QPushButton(Client))
            btn = getattr(self, b)
            x = x_base + 100*i
            btn.setGeometry(x, y, w, h)
            btn.setFont(font)
            btn.setObjectName(_fromUtf8(b))

        # Connection
        self.IP = QtWidgets.QLineEdit(Client)
        self.IP.setGeometry(QtCore.QRect(100, y, w, h))
        self.IP.setFont(font)
        self.IP.setStyleSheet(_fromUtf8(""))
        self.IP.setObjectName(_fromUtf8("IP"))

        # self.Btn_Connect = QtWidgets.QPushButton(Client)
        # self.Btn_Connect.setGeometry(QtCore.QRect(120, 580, 90, 30))
        # self.Btn_Connect.setFont(font)
        # self.Btn_Connect.setObjectName(_fromUtf8("Btn_Connect"))

        #################### Direction ########################################
        y_base = y + h*1.3
        h = 30
        w = 90
        for i, direction in enumerate(["ForWard", "Buzzer", "BackWard",
                                       "Turn_Left", "Turn_Right"]):
            setattr(self, "Btn_%s"%direction, QtWidgets.QPushButton(Client))
            d = getattr(self, "Btn_%s"%direction)
            if i < 3:
                x = 20 + w
                y = y_base + i*h*1.1
            else:
                x = 10 + (i-3)*w*1.1*2
                y = y_base + h*1.1
            d.setGeometry(QtCore.QRect(x, y, w, h))
            d.setFont(font)
            d.setStyleSheet(_fromUtf8(""))
            d.setObjectName(_fromUtf8("Btn_%s"%direction))

        ############# Mode #################################################
        h = 25
        for i in range(1, 5):
            setattr(self, "Btn_Mode%s"%i, QtWidgets.QRadioButton(Client))
            b = getattr(self, "Btn_Mode%s"%i)
            x = 330
            y = y_base + (i-1)*h*1.05
            b.setGeometry(QtCore.QRect(x, y, w, h))
            b.setFont(font)
            b.setObjectName(_fromUtf8("Btn_Mode%s"%i))

        #################### LED ###########################################
        y_base = 650
        self.Led_Module = QtWidgets.QLabel(Client)
        self.Led_Module.setGeometry(QtCore.QRect(120, y_base, 80, h))
        self.Led_Module.setObjectName(_fromUtf8("Led_Module"))

        y_base += 35
        self.Label_Named_Color = QtWidgets.QLabel(Client)
        self.Label_Named_Color.setGeometry(QtCore.QRect(10, y_base, 45, h))
        self.Label_Named_Color.setObjectName(_fromUtf8("Label_Named_Color"))

        self.Led_Named_Color = QtWidgets.QComboBox(self)
        self.Led_Named_Color.addItem("white")
        self.Led_Named_Color.addItem("red")
        self.Led_Named_Color.addItem("orange")
        self.Led_Named_Color.addItem("yello")
        self.Led_Named_Color.addItem("green")
        self.Led_Named_Color.addItem("blue")
        self.Led_Named_Color.addItem("purple")
        self.Led_Named_Color.addItem("black")
        #self.Led_Named_Color = QtWidgets.QLineEdit(Client)
        self.Led_Named_Color.setGeometry(QtCore.QRect(56, y_base, 80, h))
        self.Led_Named_Color.setFont(font)
        self.Led_Named_Color.setObjectName(_fromUtf8("Named_Color"))

        for i, color in enumerate(['R', 'G', 'B']):
            setattr(self, "Color_%s"%color, QtWidgets.QLineEdit(Client))
            c = getattr(self, "Color_%s"%color)
            x = 170 + 60*i
            c.setGeometry(QtCore.QRect(x, y_base, 30, h))
            c.setFont(font)
            c.setObjectName(_fromUtf8("Color_%s"%color))

            # label
            setattr(self, "%s"%color, QtWidgets.QLabel(Client))
            c = getattr(self, "%s"%color)
            x = 153 + 60*i
            c.setGeometry(QtCore.QRect(x, y_base, 16, h))
            c.setFont(font)
            c.setObjectName(_fromUtf8(color))

        for i in range(1, 5):
            setattr(self, "checkBox_Led_Mode%s"%i, QtWidgets.QCheckBox(Client))
            checkBox = getattr(self, "checkBox_Led_Mode%s"%i)
            x = 10 + 110 * (i-1)
            checkBox.setGeometry(QtCore.QRect(x, y_base+40, 100, h))
            checkBox.setFont(font)
            checkBox.setObjectName(_fromUtf8("checkBox_Led_Mode%s"%i))

        for i in range(1, 9):
            setattr(self, "checkBox_Led%s"%i, QtWidgets.QCheckBox(Client))
            checkBox = getattr(self, "checkBox_Led%s"%i)
            #checkBox = QtWidgets.QCheckBox(Client)
            x = 10 + 90 * ((i-1)%4)
            y = y_base + 20 + 30 * (i//5)
            checkBox.setGeometry(QtCore.QRect(x, y+60, 80, h))
            checkBox.setFont(font)
            checkBox.setObjectName(_fromUtf8("checkBox_Led%s"%i))

        #################### Servo ###########################################
        y_base = 530
        self.Servo_Module = QtWidgets.QLabel(Client)
        self.Servo_Module.setGeometry(QtCore.QRect(540, y_base, 100, h))
        self.Servo_Module.setObjectName(_fromUtf8("Servo_Module"))

        y_base = 570
        for i in [1, 2]:
            for j, b in enumerate(["HSlider_FineServo%s"%i,
                                   "Servo%s"%i, "label_FineServo%s"%i]):
                if b == "HSlider_FineServo%s"%i:
                    setattr(self, b, QtWidgets.QSlider(Client))
                    x = 510
                    y = y_base + (i-1)*40
                    w = 160
                    h = 22
                else:
                    setattr(self, b, QtWidgets.QLabel(Client))
                    x = 450 + (j-1)*(160*1.05 + 55)
                    y = y_base + (i-1)*30
                    w = 55
                    h = 25
                btn = getattr(self, b)
                btn.setGeometry(QtCore.QRect(x, y, w, h))
                try:
                    btn.setOrientation(QtCore.Qt.Horizontal)
                except:
                    pass
                btn.setObjectName(_fromUtf8(b))

        for i, direction in enumerate(["Up", "Home", "Down", "Left", "Right"]):
            setattr(self, "Btn_%s"%direction, QtWidgets.QPushButton(Client))
            d = getattr(self, "Btn_%s"%direction)
            if i < 3:
                x = 530
                y = y_base + 100 + i*30
            else:
                x = 460 + (i-3)*150
                y = y_base + 130
            d.setGeometry(QtCore.QRect(x, y, 90, 30))
            d.setFont(font)
            d.setStyleSheet(_fromUtf8(""))
            d.setObjectName(_fromUtf8("Btn_%s"%direction))

        self.HSlider_Servo1 = QtWidgets.QSlider(Client)
        self.HSlider_Servo1.setGeometry(QtCore.QRect(500, y_base+200, 160, 22))
        self.HSlider_Servo1.setStyleSheet(_fromUtf8(""))
        self.HSlider_Servo1.setOrientation(QtCore.Qt.Horizontal)
        self.HSlider_Servo1.setObjectName(_fromUtf8("HSlider_Servo1"))

        self.VSlider_Servo2 = QtWidgets.QSlider(Client)
        self.VSlider_Servo2.setGeometry(QtCore.QRect(710, y_base+80, 22, 160))
        self.VSlider_Servo2.setStyleSheet(_fromUtf8(""))
        self.VSlider_Servo2.setOrientation(QtCore.Qt.Vertical)
        self.VSlider_Servo2.setObjectName(_fromUtf8("VSlider_Servo2"))

        self.label_Servo1 = QtWidgets.QLabel(Client)
        self.label_Servo1.setGeometry(QtCore.QRect(560, y_base+230, 41, 25))
        self.label_Servo1.setFont(font)
        self.label_Servo1.setObjectName(_fromUtf8("label_Servo1"))

        self.label_Servo2 = QtWidgets.QLabel(Client)
        self.label_Servo2.setGeometry(QtCore.QRect(740, y_base+140, 41, 25))
        self.label_Servo2.setFont(font)
        self.label_Servo2.setObjectName(_fromUtf8("label_Servo2"))

        #################### Power ###########################################
        self.progress_Power = QtWidgets.QProgressBar(Client)
        self.progress_Power.setGeometry(QtCore.QRect(10, 490, 80, 25))
        self.progress_Power.setFont(font)
        self.progress_Power.setStyleSheet(_fromUtf8("QProgressBar {\n"
"border: 2px solid grey;\n"
"border-radius: 5px;\n"
"background-color: #FFFFFF;\n"
"}\n"
"\n"
"QProgressBar::chunk {\n"
"background-color:#696969;\n"
"width: 20px;\n"
"}\n"
"\n"
"QProgressBar {\n"
"text-align: center; \n"
"color: rgb(152,251,152);\n"
"}\n"
""))
        self.progress_Power.setProperty("value", 0)
        self.progress_Power.setObjectName(_fromUtf8("progress_Power"))

        self.retranslateUi(Client)
        QtCore.QMetaObject.connectSlotsByName(Client)

    def retranslateUi(self, Client):
        Client.setWindowTitle(_translate("Client", "Linda", None))
        self.Btn_ForWard.setText(_translate("Client", "ForWard", None))
        self.name.setText(_translate("Client", "Linda", None))
        self.Btn_Turn_Left.setText(_translate("Client", "Turn Left", None))
        self.Btn_BackWard.setText(_translate("Client", "BackWard", None))
        self.Btn_Turn_Right.setText(_translate("Client", "Turn Right", None))
        self.Btn_Video.setText(_translate("Client", "Open Video", None))
        self.Btn_Recording.setText(_translate("Client", "Start Recording", None))
        self.Btn_Tracking_Faces.setText(_translate("Client", "Tracing-On", None))
        self.Btn_Down.setText(_translate("Client", "Down", None))
        self.Btn_Left.setText(_translate("Client", "Left", None))
        self.Btn_Home.setText(_translate("Client", "Home", None))
        self.Btn_Up.setText(_translate("Client", "Up", None))
        self.Btn_Right.setText(_translate("Client", "Right", None))
        self.Window_Close.setText(_translate("Client", "×", None))
        self.IP.setText(_translate("Client", "192.168.1.26", None))
        self.Btn_Connect.setText(_translate("Client", "Connect", None))
        self.checkBox_Led1.setText(_translate("Client", "Led1", None))
        self.label_Servo2.setText(_translate("Client", "0", None))
        self.checkBox_Led2.setText(_translate("Client", "Led2", None))
        self.checkBox_Led3.setText(_translate("Client", "Led3", None))
        self.checkBox_Led4.setText(_translate("Client", "Led4", None))
        self.checkBox_Led5.setText(_translate("Client", "Led5", None))
        self.checkBox_Led6.setText(_translate("Client", "Led6", None))
        self.checkBox_Led7.setText(_translate("Client", "Led7", None))
        self.checkBox_Led8.setText(_translate("Client", "Led8", None))
        self.label_Servo1.setText(_translate("Client", "90", None))
        self.checkBox_Led_Mode2.setText(_translate("Client", "Led_Mode2", None))
        self.checkBox_Led_Mode3.setText(_translate("Client", "Led_Mode3", None))
        self.checkBox_Led_Mode4.setText(_translate("Client", "Led_Mode4", None))
        self.checkBox_Led_Mode1.setText(_translate("Client", "Led_Mode1", None))
        self.Color_R.setText(_translate("Client", "255", None))
        self.Color_G.setText(_translate("Client", "255", None))
        self.Color_B.setText(_translate("Client", "255", None))
        self.Servo_Module.setText(_translate("Client", "Servo Module", None))
        self.label_FineServo1.setText(_translate("Client", "0", None))
        self.label_FineServo2.setText(_translate("Client", "0", None))
        self.Window_Min.setText(_translate("Client", "-", None))
        self.Label_Named_Color.setText(_translate("Client", "Color", None))
       # self.Led_Named_Color.setText(_translate("Client", "red", None))
        self.R.setText(_translate("Client", "R", None))
        self.G.setText(_translate("Client", "G", None))
        self.B.setText(_translate("Client", "B", None))
        self.Led_Module.setText(_translate("Client", "Led Module", None))
        self.Servo1.setText(_translate("Client", "Servo 1", None))
        self.Servo2.setText(_translate("Client", "Servo 2", None))
        self.Btn_Buzzer.setText(_translate("Client", "Buzzer", None))
        self.Ultrasonic.setText(_translate("Client", "Ultrasonic", None))
        self.Light.setText(_translate("Client", "Light", None))
        self.Btn_Mode1.setText(_translate("Client", "M-Free", None))
        self.Btn_Mode2.setText(_translate("Client", "M-Light", None))
        self.Btn_Mode3.setText(_translate("Client", "M-Sonic", None))
        self.Btn_Mode4.setText(_translate("Client", "M-Line", None))