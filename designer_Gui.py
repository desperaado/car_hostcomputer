# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled.ui'
#
# Created by: PyQt5 UI code generator 5.8.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Win(object):
    def setupUi(self, Win):
        Win.setObjectName("Win")
        Win.resize(1200, 789)
        Win.setAutoFillBackground(True)
        self.centralwidget = QtWidgets.QWidget(Win)
        self.centralwidget.setObjectName("centralwidget")
        self.uart_set = QtWidgets.QGroupBox(self.centralwidget)
        self.uart_set.setGeometry(QtCore.QRect(10, 660, 781, 91))
        self.uart_set.setObjectName("uart_set")
        self.s1__lb_1 = QtWidgets.QLabel(self.uart_set)
        self.s1__lb_1.setGeometry(QtCore.QRect(0, 20, 60, 21))
        self.s1__lb_1.setObjectName("s1__lb_1")
        self.s1__box_1 = QtWidgets.QPushButton(self.uart_set)
        self.s1__box_1.setGeometry(QtCore.QRect(60, 20, 75, 23))
        self.s1__box_1.setAutoRepeatInterval(100)
        self.s1__box_1.setDefault(True)
        self.s1__box_1.setObjectName("s1__box_1")
        self.s1__box_2 = QtWidgets.QComboBox(self.uart_set)
        self.s1__box_2.setGeometry(QtCore.QRect(60, 50, 75, 20))
        self.s1__box_2.setObjectName("s1__box_2")
        self.s1__lb_2 = QtWidgets.QLabel(self.uart_set)
        self.s1__lb_2.setGeometry(QtCore.QRect(0, 50, 60, 20))
        self.s1__lb_2.setObjectName("s1__lb_2")
        self.open_button = QtWidgets.QPushButton(self.uart_set)
        self.open_button.setGeometry(QtCore.QRect(460, 20, 145, 23))
        self.open_button.setObjectName("open_button")
        self.close_button = QtWidgets.QPushButton(self.uart_set)
        self.close_button.setGeometry(QtCore.QRect(460, 50, 145, 23))
        self.close_button.setObjectName("close_button")
        self.s1__box_3 = QtWidgets.QComboBox(self.uart_set)
        self.s1__box_3.setGeometry(QtCore.QRect(220, 20, 75, 20))
        self.s1__box_3.setObjectName("s1__box_3")
        self.s1__box_3.addItem("")
        self.s1__box_3.addItem("")
        self.s1__box_3.addItem("")
        self.s1__box_3.addItem("")
        self.s1__box_3.addItem("")
        self.s1__box_3.addItem("")
        self.s1__box_3.addItem("")
        self.s1__box_3.addItem("")
        self.s1__box_3.addItem("")
        self.s1__box_3.addItem("")
        self.s1__box_3.addItem("")
        self.s1__box_3.addItem("")
        self.s1__lb_3 = QtWidgets.QLabel(self.uart_set)
        self.s1__lb_3.setGeometry(QtCore.QRect(150, 20, 48, 20))
        self.s1__lb_3.setObjectName("s1__lb_3")
        self.s1__box_4 = QtWidgets.QComboBox(self.uart_set)
        self.s1__box_4.setGeometry(QtCore.QRect(220, 50, 75, 20))
        self.s1__box_4.setObjectName("s1__box_4")
        self.s1__box_4.addItem("")
        self.s1__box_4.addItem("")
        self.s1__box_4.addItem("")
        self.s1__box_4.addItem("")
        self.s1__lb_4 = QtWidgets.QLabel(self.uart_set)
        self.s1__lb_4.setGeometry(QtCore.QRect(150, 50, 48, 20))
        self.s1__lb_4.setObjectName("s1__lb_4")
        self.s1__box_5 = QtWidgets.QComboBox(self.uart_set)
        self.s1__box_5.setGeometry(QtCore.QRect(380, 20, 75, 20))
        self.s1__box_5.setObjectName("s1__box_5")
        self.s1__box_5.addItem("")
        self.s1__lb_5 = QtWidgets.QLabel(self.uart_set)
        self.s1__lb_5.setGeometry(QtCore.QRect(310, 20, 48, 20))
        self.s1__lb_5.setObjectName("s1__lb_5")
        self.s1__box_6 = QtWidgets.QComboBox(self.uart_set)
        self.s1__box_6.setGeometry(QtCore.QRect(380, 50, 75, 20))
        self.s1__box_6.setObjectName("s1__box_6")
        self.s1__box_6.addItem("")
        self.s1__lb_6 = QtWidgets.QLabel(self.uart_set)
        self.s1__lb_6.setGeometry(QtCore.QRect(310, 50, 48, 20))
        self.s1__lb_6.setObjectName("s1__lb_6")
        self.uart_statusBox = QtWidgets.QGroupBox(self.uart_set)
        self.uart_statusBox.setGeometry(QtCore.QRect(610, 0, 171, 101))
        self.uart_statusBox.setObjectName("uart_statusBox")
        self.formLayout_2 = QtWidgets.QFormLayout(self.uart_statusBox)
        self.formLayout_2.setContentsMargins(10, 10, 10, 10)
        self.formLayout_2.setSpacing(10)
        self.formLayout_2.setObjectName("formLayout_2")
        self.label = QtWidgets.QLabel(self.uart_statusBox)
        self.label.setObjectName("label")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label)
        self.label_2 = QtWidgets.QLabel(self.uart_statusBox)
        self.label_2.setObjectName("label_2")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.lineEdit = QtWidgets.QLineEdit(self.uart_statusBox)
        self.lineEdit.setObjectName("lineEdit")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.lineEdit)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.uart_statusBox)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.lineEdit_2)
        self.state_label = QtWidgets.QLabel(self.uart_set)
        self.state_label.setGeometry(QtCore.QRect(0, 70, 145, 14))
        self.state_label.setText("")
        self.state_label.setTextFormat(QtCore.Qt.AutoText)
        self.state_label.setScaledContents(True)
        self.state_label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.state_label.setObjectName("state_label")
        self.imageBox = QtWidgets.QGroupBox(self.centralwidget)
        self.imageBox.setGeometry(QtCore.QRect(0, 0, 611, 461))
        font = QtGui.QFont()
        font.setFamily("SimSun-ExtB")
        font.setPointSize(11)
        self.imageBox.setFont(font)
        self.imageBox.setObjectName("imageBox")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.imageBox)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.dataBox = QtWidgets.QGroupBox(self.centralwidget)
        self.dataBox.setGeometry(QtCore.QRect(610, 0, 591, 311))
        font = QtGui.QFont()
        font.setFamily("SimSun-ExtB")
        font.setPointSize(11)
        self.dataBox.setFont(font)
        self.dataBox.setObjectName("dataBox")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.dataBox)
        self.horizontalLayout_2.setContentsMargins(9, -1, -1, -1)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.transmit = QtWidgets.QGroupBox(self.centralwidget)
        self.transmit.setGeometry(QtCore.QRect(30, 520, 401, 101))
        self.transmit.setObjectName("transmit")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.transmit)
        self.verticalLayout_2.setContentsMargins(10, 10, 10, 10)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.s3__send_text = QtWidgets.QTextEdit(self.transmit)
        self.s3__send_text.setObjectName("s3__send_text")
        self.verticalLayout_2.addWidget(self.s3__send_text)
        self.receive = QtWidgets.QGroupBox(self.centralwidget)
        self.receive.setGeometry(QtCore.QRect(530, 540, 561, 111))
        self.receive.setObjectName("receive")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.receive)
        self.verticalLayout.setContentsMargins(10, 10, 10, 10)
        self.verticalLayout.setObjectName("verticalLayout")
        self.s2__receive_text = QtWidgets.QTextBrowser(self.receive)
        self.s2__receive_text.setObjectName("s2__receive_text")
        self.verticalLayout.addWidget(self.s2__receive_text)
        self.motor_pid = QtWidgets.QGroupBox(self.centralwidget)
        self.motor_pid.setGeometry(QtCore.QRect(640, 460, 251, 48))
        self.motor_pid.setObjectName("motor_pid")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.motor_pid)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.MP = QtWidgets.QCheckBox(self.motor_pid)
        self.MP.setStyleSheet("color: rgb(0, 170, 255);")
        self.MP.setObjectName("MP")
        self.horizontalLayout_3.addWidget(self.MP)
        self.MI = QtWidgets.QCheckBox(self.motor_pid)
        self.MI.setStyleSheet("color: rgb(85, 170, 0);")
        self.MI.setObjectName("MI")
        self.horizontalLayout_3.addWidget(self.MI)
        self.MD = QtWidgets.QCheckBox(self.motor_pid)
        self.MD.setStyleSheet("color: rgb(255, 85, 127);")
        self.MD.setObjectName("MD")
        self.horizontalLayout_3.addWidget(self.MD)
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(900, 460, 291, 48))
        self.groupBox.setObjectName("groupBox")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.groupBox)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.SW = QtWidgets.QCheckBox(self.groupBox)
        self.SW.setStyleSheet("color: rgb(85, 170, 255);")
        self.SW.setObjectName("SW")
        self.horizontalLayout_4.addWidget(self.SW)
        self.SP = QtWidgets.QCheckBox(self.groupBox)
        self.SP.setStyleSheet("color: rgb(255, 189, 55);")
        self.SP.setObjectName("SP")
        self.horizontalLayout_4.addWidget(self.SP)
        self.SD = QtWidgets.QCheckBox(self.groupBox)
        self.SD.setStyleSheet("color: rgb(255, 213, 0);")
        self.SD.setObjectName("SD")
        self.horizontalLayout_4.addWidget(self.SD)
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_2.setGeometry(QtCore.QRect(180, 460, 241, 48))
        self.groupBox_2.setObjectName("groupBox_2")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.groupBox_2)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.midline = QtWidgets.QCheckBox(self.groupBox_2)
        self.midline.setStyleSheet("color: rgb(85, 170, 0);")
        self.midline.setObjectName("midline")
        self.horizontalLayout_5.addWidget(self.midline)
        self.Pixle = QtWidgets.QCheckBox(self.groupBox_2)
        self.Pixle.setObjectName("Pixle")
        self.horizontalLayout_5.addWidget(self.Pixle)
        self.sideline = QtWidgets.QCheckBox(self.groupBox_2)
        self.sideline.setStyleSheet("color: rgb(255, 213, 0);")
        self.sideline.setObjectName("sideline")
        self.horizontalLayout_5.addWidget(self.sideline)
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(430, 550, 77, 76))
        self.layoutWidget.setObjectName("layoutWidget")
        self.transmit_hex_clear_send = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.transmit_hex_clear_send.setContentsMargins(0, 0, 0, 0)
        self.transmit_hex_clear_send.setObjectName("transmit_hex_clear_send")
        self.hex_send = QtWidgets.QCheckBox(self.layoutWidget)
        self.hex_send.setObjectName("hex_send")
        self.transmit_hex_clear_send.addWidget(self.hex_send)
        self.s3__send_button = QtWidgets.QPushButton(self.layoutWidget)
        self.s3__send_button.setObjectName("s3__send_button")
        self.transmit_hex_clear_send.addWidget(self.s3__send_button)
        self.s3__clear_button = QtWidgets.QPushButton(self.layoutWidget)
        self.s3__clear_button.setObjectName("s3__clear_button")
        self.transmit_hex_clear_send.addWidget(self.s3__clear_button)
        self.layoutWidget1 = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget1.setGeometry(QtCore.QRect(80, 630, 181, 22))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.timer_send_layout = QtWidgets.QHBoxLayout(self.layoutWidget1)
        self.timer_send_layout.setContentsMargins(0, 0, 0, 0)
        self.timer_send_layout.setObjectName("timer_send_layout")
        self.timer_send_cb = QtWidgets.QCheckBox(self.layoutWidget1)
        self.timer_send_cb.setObjectName("timer_send_cb")
        self.timer_send_layout.addWidget(self.timer_send_cb)
        self.lineEdit_3 = QtWidgets.QLineEdit(self.layoutWidget1)
        self.lineEdit_3.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.timer_send_layout.addWidget(self.lineEdit_3)
        self.dw = QtWidgets.QLabel(self.layoutWidget1)
        self.dw.setObjectName("dw")
        self.timer_send_layout.addWidget(self.dw)
        self.layoutWidget2 = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget2.setGeometry(QtCore.QRect(1110, 540, 77, 47))
        self.layoutWidget2.setObjectName("layoutWidget2")
        self.receive_hex_clear = QtWidgets.QVBoxLayout(self.layoutWidget2)
        self.receive_hex_clear.setContentsMargins(0, 0, 0, 0)
        self.receive_hex_clear.setObjectName("receive_hex_clear")
        self.hex_receive = QtWidgets.QCheckBox(self.layoutWidget2)
        self.hex_receive.setObjectName("hex_receive")
        self.receive_hex_clear.addWidget(self.hex_receive)
        self.s2__clear_button = QtWidgets.QPushButton(self.layoutWidget2)
        self.s2__clear_button.setObjectName("s2__clear_button")
        self.receive_hex_clear.addWidget(self.s2__clear_button)
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(6, 404, 54, 12))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(6, 376, 54, 12))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(6, 344, 54, 12))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(6, 314, 54, 12))
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(6, 284, 54, 12))
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(6, 254, 54, 12))
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(6, 224, 54, 12))
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(6, 194, 54, 12))
        self.label_10.setObjectName("label_10")
        self.label_11 = QtWidgets.QLabel(self.centralwidget)
        self.label_11.setGeometry(QtCore.QRect(6, 164, 54, 12))
        self.label_11.setObjectName("label_11")
        self.label_12 = QtWidgets.QLabel(self.centralwidget)
        self.label_12.setGeometry(QtCore.QRect(6, 134, 54, 12))
        self.label_12.setObjectName("label_12")
        self.label_13 = QtWidgets.QLabel(self.centralwidget)
        self.label_13.setGeometry(QtCore.QRect(6, 104, 54, 12))
        self.label_13.setObjectName("label_13")
        self.label_14 = QtWidgets.QLabel(self.centralwidget)
        self.label_14.setGeometry(QtCore.QRect(8, 74, 54, 12))
        self.label_14.setObjectName("label_14")
        self.label_15 = QtWidgets.QLabel(self.centralwidget)
        self.label_15.setGeometry(QtCore.QRect(8, 52, 54, 12))
        self.label_15.setObjectName("label_15")
        self.label_16 = QtWidgets.QLabel(self.centralwidget)
        self.label_16.setGeometry(QtCore.QRect(23, 418, 54, 12))
        self.label_16.setObjectName("label_16")
        self.label_17 = QtWidgets.QLabel(self.centralwidget)
        self.label_17.setGeometry(QtCore.QRect(53, 418, 54, 12))
        self.label_17.setObjectName("label_17")
        self.label_18 = QtWidgets.QLabel(self.centralwidget)
        self.label_18.setGeometry(QtCore.QRect(83, 418, 54, 12))
        self.label_18.setObjectName("label_18")
        self.label_19 = QtWidgets.QLabel(self.centralwidget)
        self.label_19.setGeometry(QtCore.QRect(113, 418, 54, 12))
        self.label_19.setObjectName("label_19")
        self.label_20 = QtWidgets.QLabel(self.centralwidget)
        self.label_20.setGeometry(QtCore.QRect(141, 418, 54, 12))
        self.label_20.setObjectName("label_20")
        self.label_21 = QtWidgets.QLabel(self.centralwidget)
        self.label_21.setGeometry(QtCore.QRect(172, 418, 54, 12))
        self.label_21.setObjectName("label_21")
        self.label_22 = QtWidgets.QLabel(self.centralwidget)
        self.label_22.setGeometry(QtCore.QRect(202, 418, 54, 12))
        self.label_22.setObjectName("label_22")
        self.label_23 = QtWidgets.QLabel(self.centralwidget)
        self.label_23.setGeometry(QtCore.QRect(232, 418, 54, 12))
        self.label_23.setObjectName("label_23")
        self.label_24 = QtWidgets.QLabel(self.centralwidget)
        self.label_24.setGeometry(QtCore.QRect(262, 418, 54, 12))
        self.label_24.setObjectName("label_24")
        self.label_25 = QtWidgets.QLabel(self.centralwidget)
        self.label_25.setGeometry(QtCore.QRect(292, 418, 54, 12))
        self.label_25.setObjectName("label_25")
        self.label_26 = QtWidgets.QLabel(self.centralwidget)
        self.label_26.setGeometry(QtCore.QRect(322, 418, 54, 12))
        self.label_26.setObjectName("label_26")
        self.label_27 = QtWidgets.QLabel(self.centralwidget)
        self.label_27.setGeometry(QtCore.QRect(352, 418, 54, 12))
        self.label_27.setObjectName("label_27")
        self.label_28 = QtWidgets.QLabel(self.centralwidget)
        self.label_28.setGeometry(QtCore.QRect(382, 418, 54, 12))
        self.label_28.setObjectName("label_28")
        self.label_29 = QtWidgets.QLabel(self.centralwidget)
        self.label_29.setGeometry(QtCore.QRect(412, 418, 54, 12))
        self.label_29.setObjectName("label_29")
        self.label_30 = QtWidgets.QLabel(self.centralwidget)
        self.label_30.setGeometry(QtCore.QRect(442, 418, 54, 12))
        self.label_30.setObjectName("label_30")
        self.label_31 = QtWidgets.QLabel(self.centralwidget)
        self.label_31.setGeometry(QtCore.QRect(472, 418, 54, 12))
        self.label_31.setObjectName("label_31")
        self.label_32 = QtWidgets.QLabel(self.centralwidget)
        self.label_32.setGeometry(QtCore.QRect(502, 418, 54, 12))
        self.label_32.setObjectName("label_32")
        self.label_33 = QtWidgets.QLabel(self.centralwidget)
        self.label_33.setGeometry(QtCore.QRect(532, 418, 54, 12))
        self.label_33.setObjectName("label_33")
        self.label_34 = QtWidgets.QLabel(self.centralwidget)
        self.label_34.setGeometry(QtCore.QRect(562, 418, 54, 12))
        self.label_34.setObjectName("label_34")
        self.label_35 = QtWidgets.QLabel(self.centralwidget)
        self.label_35.setGeometry(QtCore.QRect(582, 418, 54, 12))
        self.label_35.setObjectName("label_35")
        self.dataBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        self.dataBox_2.setGeometry(QtCore.QRect(610, 310, 591, 151))
        font = QtGui.QFont()
        font.setFamily("SimSun-ExtB")
        font.setPointSize(11)
        self.dataBox_2.setFont(font)
        self.dataBox_2.setObjectName("dataBox_2")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.dataBox_2)
        self.horizontalLayout_6.setContentsMargins(9, -1, -1, -1)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.hc_help_button = QtWidgets.QPushButton(self.centralwidget)
        self.hc_help_button.setGeometry(QtCore.QRect(30, 470, 111, 31))
        self.hc_help_button.setObjectName("hc_help_button")
        self.label_36 = QtWidgets.QLabel(self.centralwidget)
        self.label_36.setGeometry(QtCore.QRect(1010, 700, 171, 41))
        self.label_36.setObjectName("label_36")
        self.am_button = QtWidgets.QPushButton(self.centralwidget)
        self.am_button.setGeometry(QtCore.QRect(810, 680, 131, 41))
        self.am_button.setObjectName("am_button")
        Win.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(Win)
        self.statusbar.setObjectName("statusbar")
        Win.setStatusBar(self.statusbar)

        self.retranslateUi(Win)
        QtCore.QMetaObject.connectSlotsByName(Win)

    def retranslateUi(self, Win):
        _translate = QtCore.QCoreApplication.translate
        Win.setWindowTitle(_translate("Win", "智能车调试助手"))
        self.uart_set.setTitle(_translate("Win", "串口设置"))
        self.s1__lb_1.setText(_translate("Win", "串口检测："))
        self.s1__box_1.setText(_translate("Win", "检测串口"))
        self.s1__lb_2.setText(_translate("Win", "串口选择："))
        self.open_button.setText(_translate("Win", "打开串口"))
        self.close_button.setText(_translate("Win", "关闭串口"))
        self.s1__box_3.setItemText(0, _translate("Win", "115200"))
        self.s1__box_3.setItemText(1, _translate("Win", "2400"))
        self.s1__box_3.setItemText(2, _translate("Win", "4800"))
        self.s1__box_3.setItemText(3, _translate("Win", "9600"))
        self.s1__box_3.setItemText(4, _translate("Win", "14400"))
        self.s1__box_3.setItemText(5, _translate("Win", "19200"))
        self.s1__box_3.setItemText(6, _translate("Win", "38400"))
        self.s1__box_3.setItemText(7, _translate("Win", "57600"))
        self.s1__box_3.setItemText(8, _translate("Win", "76800"))
        self.s1__box_3.setItemText(9, _translate("Win", "12800"))
        self.s1__box_3.setItemText(10, _translate("Win", "230400"))
        self.s1__box_3.setItemText(11, _translate("Win", "460800"))
        self.s1__lb_3.setText(_translate("Win", "波特率："))
        self.s1__box_4.setItemText(0, _translate("Win", "8"))
        self.s1__box_4.setItemText(1, _translate("Win", "7"))
        self.s1__box_4.setItemText(2, _translate("Win", "6"))
        self.s1__box_4.setItemText(3, _translate("Win", "5"))
        self.s1__lb_4.setText(_translate("Win", "数据位："))
        self.s1__box_5.setItemText(0, _translate("Win", "N"))
        self.s1__lb_5.setText(_translate("Win", "校验位："))
        self.s1__box_6.setItemText(0, _translate("Win", "1"))
        self.s1__lb_6.setText(_translate("Win", "停止位："))
        self.uart_statusBox.setTitle(_translate("Win", "串口状态"))
        self.label.setText(_translate("Win", "已接收："))
        self.label_2.setText(_translate("Win", "已发送："))
        self.imageBox.setTitle(_translate("Win", "实时图像"))
        self.dataBox.setTitle(_translate("Win", "PID"))
        self.transmit.setTitle(_translate("Win", "发送区"))
        self.s3__send_text.setHtml(_translate("Win", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">D</p></body></html>"))
        self.receive.setTitle(_translate("Win", "接收区"))
        self.motor_pid.setTitle(_translate("Win", "电机参数"))
        self.MP.setText(_translate("Win", "电机P(蓝)"))
        self.MI.setText(_translate("Win", "电机I(绿)"))
        self.MD.setText(_translate("Win", "电机D(红)"))
        self.groupBox.setTitle(_translate("Win", "舵机参数"))
        self.SW.setText(_translate("Win", "舵机PWM(蓝)"))
        self.SP.setText(_translate("Win", "舵机P(白)"))
        self.SD.setText(_translate("Win", "舵机D(黄)"))
        self.groupBox_2.setTitle(_translate("Win", "图像参数"))
        self.midline.setText(_translate("Win", "中线(绿)"))
        self.Pixle.setText(_translate("Win", "图像"))
        self.sideline.setText(_translate("Win", "边线(黄)"))
        self.hex_send.setText(_translate("Win", "Hex发送"))
        self.s3__send_button.setText(_translate("Win", "发送"))
        self.s3__clear_button.setText(_translate("Win", "清除"))
        self.timer_send_cb.setText(_translate("Win", "定时发送"))
        self.lineEdit_3.setText(_translate("Win", "1000"))
        self.dw.setText(_translate("Win", "ms/次"))
        self.hex_receive.setText(_translate("Win", "Hex接收"))
        self.s2__clear_button.setText(_translate("Win", "清除"))
        self.label_3.setText(_translate("Win", "<html><head/><body><p><span style=\" font-size:8pt;\">59</span></p></body></html>"))
        self.label_4.setText(_translate("Win", "<html><head/><body><p><span style=\" font-size:8pt;\">55</span></p></body></html>"))
        self.label_5.setText(_translate("Win", "<html><head/><body><p><span style=\" font-size:8pt;\">50</span></p></body></html>"))
        self.label_6.setText(_translate("Win", "<html><head/><body><p><span style=\" font-size:8pt;\">45</span></p></body></html>"))
        self.label_7.setText(_translate("Win", "<html><head/><body><p><span style=\" font-size:8pt;\">40</span></p></body></html>"))
        self.label_8.setText(_translate("Win", "<html><head/><body><p><span style=\" font-size:8pt;\">35</span></p></body></html>"))
        self.label_9.setText(_translate("Win", "<html><head/><body><p><span style=\" font-size:8pt;\">30</span></p></body></html>"))
        self.label_10.setText(_translate("Win", "<html><head/><body><p><span style=\" font-size:8pt;\">25</span></p></body></html>"))
        self.label_11.setText(_translate("Win", "<html><head/><body><p><span style=\" font-size:8pt;\">20</span></p></body></html>"))
        self.label_12.setText(_translate("Win", "<html><head/><body><p><span style=\" font-size:8pt;\">15</span></p></body></html>"))
        self.label_13.setText(_translate("Win", "<html><head/><body><p><span style=\" font-size:8pt;\">10</span></p></body></html>"))
        self.label_14.setText(_translate("Win", "<html><head/><body><p><span style=\" font-size:8pt;\">5</span></p></body></html>"))
        self.label_15.setText(_translate("Win", "<html><head/><body><p><span style=\" font-size:8pt;\">0</span></p></body></html>"))
        self.label_16.setText(_translate("Win", "0"))
        self.label_17.setText(_translate("Win", "5"))
        self.label_18.setText(_translate("Win", "10"))
        self.label_19.setText(_translate("Win", "15"))
        self.label_20.setText(_translate("Win", "20"))
        self.label_21.setText(_translate("Win", "25"))
        self.label_22.setText(_translate("Win", "30"))
        self.label_23.setText(_translate("Win", "35"))
        self.label_24.setText(_translate("Win", "40"))
        self.label_25.setText(_translate("Win", "45"))
        self.label_26.setText(_translate("Win", "50"))
        self.label_27.setText(_translate("Win", "55"))
        self.label_28.setText(_translate("Win", "60"))
        self.label_29.setText(_translate("Win", "65"))
        self.label_30.setText(_translate("Win", "70"))
        self.label_31.setText(_translate("Win", "75"))
        self.label_32.setText(_translate("Win", "80"))
        self.label_33.setText(_translate("Win", "85"))
        self.label_34.setText(_translate("Win", "90"))
        self.label_35.setText(_translate("Win", "93"))
        self.dataBox_2.setTitle(_translate("Win", "PWM"))
        self.hc_help_button.setText(_translate("Win", "上位机指令集"))
        self.label_36.setText(_translate("Win", "<html><head/><body><p><span style=\" font-size:14pt;\">@龙岩学院智能车队</span></p></body></html>"))
        self.am_button.setText(_translate("Win", "通信协议"))
