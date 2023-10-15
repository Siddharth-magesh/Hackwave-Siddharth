from PyQt5 import QtCore, QtGui, QtWidgets
import test1
import test2
from PyQt5.QtGui import QPixmap
global select_value
global zoom_address
global zoom_out_address
select_value = 1


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(418, 820)
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        MainWindow.setFont(font)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.main_map = QtWidgets.QLabel(self.centralwidget)
        self.main_map.setGeometry(QtCore.QRect(20, 60, 381, 211))
        self.main_map.setStyleSheet("")
        self.main_map.setText("")
        self.main_map.setPixmap(QtGui.QPixmap(
            "images/hospital_main_layout.jpeg"))
        self.main_map.setScaledContents(True)
        self.main_map.setObjectName("main_map")

        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(30, 320, 241, 51))
        self.textEdit.setMinimumSize(QtCore.QSize(34, 0))
        self.textEdit.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.textEdit.setFont(font)
        self.textEdit.setAcceptDrops(False)
        self.textEdit.setAutoFillBackground(False)
        self.textEdit.setStyleSheet("background-color: rgb(255, 237, 255);\n"
                                    "color: black;\n"
                                    "border-style: outset;\n"
                                    "border-radius: 10px;\n"
                                    "border-width: 2px;\n"
                                    "border-color: black;\n"
                                    "font:bold 20px;\n"
                                    "padding-left: 10px;\n"
                                    "padding-right: 10px;\n"
                                    "padding-top: 5px;\n"
                                    "min-width: 10px;")
        self.textEdit.setObjectName("textEdit")

        self.inst = QtWidgets.QLabel(self.centralwidget)
        self.inst.setGeometry(QtCore.QRect(20, 380, 371, 211))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.inst.setFont(font)
        self.inst.setTextFormat(QtCore.Qt.AutoText)
        self.inst.setAlignment(QtCore.Qt.AlignCenter)
        self.inst.setObjectName("inst")

        self.button1 = QtWidgets.QPushButton(self.centralwidget)
        self.button1.setGeometry(QtCore.QRect(280, 340, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.button1.setFont(font)
        self.button1.setStyleSheet("color: rgb(255, 255, 255);\n"
                                   "selection-color: rgb(192, 239, 255);\n"
                                   "background-color: rgb(0, 170, 255);")
        self.button1.setObjectName("button1")

        self.Emergency_exit = QtWidgets.QPushButton(self.centralwidget)
        self.Emergency_exit.setGeometry(QtCore.QRect(20, 600, 121, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.Emergency_exit.setFont(font)
        self.Emergency_exit.setStyleSheet("background-color: rgb(255, 70, 73);\n"
                                          "color: rgb(255, 255, 255);")
        self.Emergency_exit.setObjectName("Emergency_exit")

        self.elivator = QtWidgets.QPushButton(self.centralwidget)
        self.elivator.setGeometry(QtCore.QRect(150, 600, 121, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.elivator.setFont(font)
        self.elivator.setStyleSheet("background-color: rgb(255, 70, 73);\n"
                                    "color: rgb(255, 255, 255);")
        self.elivator.setObjectName("elivator")

        self.patient_rooms = QtWidgets.QPushButton(self.centralwidget)
        self.patient_rooms.setGeometry(QtCore.QRect(150, 720, 121, 41))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.patient_rooms.setFont(font)
        self.patient_rooms.setStyleSheet("background-color: rgb(255, 70, 73);\n"
                                         "color: rgb(255, 255, 255);")
        self.patient_rooms.setObjectName("patient_rooms")

        self.general_doc = QtWidgets.QPushButton(self.centralwidget)
        self.general_doc.setGeometry(QtCore.QRect(280, 600, 121, 41))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.general_doc.setFont(font)
        self.general_doc.setStyleSheet("background-color: rgb(255, 70, 73);\n"
                                       "color: rgb(255, 255, 255);")
        self.general_doc.setObjectName("general_doc")

        self.MRI = QtWidgets.QPushButton(self.centralwidget)
        self.MRI.setGeometry(QtCore.QRect(20, 660, 121, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.MRI.setFont(font)
        self.MRI.setStyleSheet("background-color: rgb(255, 70, 73);\n"
                               "color: rgb(255, 255, 255);")
        self.MRI.setObjectName("MRI")

        self.Gynacolagist = QtWidgets.QPushButton(self.centralwidget)
        self.Gynacolagist.setGeometry(QtCore.QRect(150, 660, 121, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.Gynacolagist.setFont(font)
        self.Gynacolagist.setStyleSheet("background-color: rgb(255, 70, 73);\n"
                                        "color: rgb(255, 255, 255);")
        self.Gynacolagist.setObjectName("Gynacolagist")

        self.vip_patients = QtWidgets.QPushButton(self.centralwidget)
        self.vip_patients.setGeometry(QtCore.QRect(280, 660, 121, 41))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.vip_patients.setFont(font)
        self.vip_patients.setStyleSheet("background-color: rgb(255, 70, 73);\n"
                                        "color: rgb(255, 255, 255);")
        self.vip_patients.setObjectName("vip_patients")

        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(20, 260, 251, 71))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_3.setFont(font)
        self.label_3.setScaledContents(False)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")

        self.Select_Hospital = QtWidgets.QPushButton(self.centralwidget)
        self.Select_Hospital.setGeometry(QtCore.QRect(20, 10, 111, 41))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.Select_Hospital.setFont(font)
        self.Select_Hospital.setStyleSheet("color: rgb(255, 255, 255);\n"
                                           "background-color: rgb(255, 0, 4);\n"
                                           "border-radius: 10px;\n"
                                           "\n"
                                           "")
        self.Select_Hospital.setObjectName("Select_Hospital")

        self.Select_mall = QtWidgets.QPushButton(self.centralwidget)
        self.Select_mall.setGeometry(QtCore.QRect(290, 10, 111, 41))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.Select_mall.setFont(font)
        self.Select_mall.setStyleSheet("background-color: rgb(255, 156, 34);\n"
                                       "color: rgb(255, 255, 255);\n"
                                       "border-radius: 10px;")
        self.Select_mall.setObjectName("Select_mall")

        self.Select_university = QtWidgets.QPushButton(self.centralwidget)
        self.Select_university.setGeometry(QtCore.QRect(150, 10, 111, 41))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.Select_university.setFont(font)
        self.Select_university.setStyleSheet("background-color: rgb(208, 65, 255);\n"
                                             "color: rgb(255, 255, 255);\n"
                                             "border-radius: 10px;")
        self.Select_university.setObjectName("Select_university")

        self.record_input = QtWidgets.QPushButton(self.centralwidget)
        self.record_input.setEnabled(True)
        self.record_input.setGeometry(QtCore.QRect(350, 710, 50, 50))
        self.record_input.setMinimumSize(QtCore.QSize(50, 50))
        self.record_input.setMaximumSize(QtCore.QSize(50, 50))
        self.record_input.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.record_input.setStyleSheet("QPushButton {\n"
                                        "    color: #333;\n"
                                        "    border: 2px solid #555;\n"
                                        "    border-radius: 25px;\n"
                                        "    border-style: outset;\n"
                                        "    background: qradialgradient(\n"
                                        "        cx: 0.3, cy: -0.4, fx: 0.3, fy: -0.4,\n"
                                        "        radius: 1.35, stop: 0 #fff, stop: 1 #888\n"
                                        "        );\n"
                                        "    padding: 5px;\n"
                                        "    }\n"
                                        "\n"
                                        "QPushButton:hover {\n"
                                        "    background: qradialgradient(\n"
                                        "        cx: 0.3, cy: -0.4, fx: 0.3, fy: -0.4,\n"
                                        "        radius: 1.35, stop: 0 #fff, stop: 1 #bbb\n"
                                        "        );\n"
                                        "    }\n"
                                        "\n"
                                        "QPushButton:pressed {\n"
                                        "    border-style: inset;\n"
                                        "    background: qradialgradient(\n"
                                        "        cx: 0.4, cy: -0.1, fx: 0.4, fy: -0.1,\n"
                                        "        radius: 1.35, stop: 0 #fff, stop: 1 #ddd\n"
                                        "        );\n"
                                        "    }\n"
                                        "")
        self.record_input.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(
            "images/icons/mic.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.record_input.setIcon(icon)
        self.record_input.setObjectName("record_input")

        self.sos_input = QtWidgets.QPushButton(self.centralwidget)
        self.sos_input.setEnabled(True)
        self.sos_input.setGeometry(QtCore.QRect(10, 710, 50, 50))
        self.sos_input.setMinimumSize(QtCore.QSize(50, 50))
        self.sos_input.setMaximumSize(QtCore.QSize(50, 50))
        self.sos_input.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.sos_input.setStyleSheet("QPushButton {\n"
                                     "    color: #333;\n"
                                     "    border: 2px solid #555;\n"
                                     "    border-radius: 25px;\n"
                                     "    border-style: outset;\n"
                                     "    background: qradialgradient(\n"
                                     "        cx: 0.3, cy: -0.4, fx: 0.3, fy: -0.4,\n"
                                     "        radius: 1.35, stop: 0 #fff, stop: 1 #888\n"
                                     "        );\n"
                                     "    padding: 5px;\n"
                                     "    }\n"
                                     "\n"
                                     "QPushButton:hover {\n"
                                     "    background: qradialgradient(\n"
                                     "        cx: 0.3, cy: -0.4, fx: 0.3, fy: -0.4,\n"
                                     "        radius: 1.35, stop: 0 #fff, stop: 1 #bbb\n"
                                     "        );\n"
                                     "    }\n"
                                     "\n"
                                     "QPushButton:pressed {\n"
                                     "    border-style: inset;\n"
                                     "    background: qradialgradient(\n"
                                     "        cx: 0.4, cy: -0.1, fx: 0.4, fy: -0.1,\n"
                                     "        radius: 1.35, stop: 0 #fff, stop: 1 #ddd\n"
                                     "        );\n"
                                     "    }\n"
                                     "")
        self.sos_input.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(
            "images/icons/sos.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.sos_input.setIcon(icon)
        self.sos_input.setObjectName("record_input")

        self.zoom_in = QtWidgets.QPushButton(self.centralwidget)
        self.zoom_in.setGeometry(QtCore.QRect(280, 280, 50, 50))
        self.zoom_in.setMinimumSize(QtCore.QSize(50, 50))
        self.zoom_in.setMaximumSize(QtCore.QSize(50, 50))
        self.zoom_in.setStyleSheet("QPushButton {\n"
                                   "    color: #333;\n"
                                   "    border: 2px solid #555;\n"
                                   "    border-radius: 25px;\n"
                                   "    border-style: outset;\n"
                                   "    background: qradialgradient(\n"
                                   "        cx: 0.3, cy: -0.4, fx: 0.3, fy: -0.4,\n"
                                   "        radius: 1.35, stop: 0 #fff, stop: 1 #888\n"
                                   "        );\n"
                                   "    padding: 5px;\n"
                                   "    }\n"
                                   "\n"
                                   "QPushButton:hover {\n"
                                   "    background: qradialgradient(\n"
                                   "        cx: 0.3, cy: -0.4, fx: 0.3, fy: -0.4,\n"
                                   "        radius: 1.35, stop: 0 #fff, stop: 1 #bbb\n"
                                   "        );\n"
                                   "    }\n"
                                   "\n"
                                   "QPushButton:pressed {\n"
                                   "    border-style: inset;\n"
                                   "    background: qradialgradient(\n"
                                   "        cx: 0.4, cy: -0.1, fx: 0.4, fy: -0.1,\n"
                                   "        radius: 1.35, stop: 0 #fff, stop: 1 #ddd\n"
                                   "        );\n"
                                   "    }\n"
                                   "")
        self.zoom_in.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("images/icons/plus.png"),
                        QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.zoom_in.setIcon(icon1)
        self.zoom_in.setIconSize(QtCore.QSize(52, 52))
        self.zoom_in.setObjectName("zoom_in")

        self.zoom_out = QtWidgets.QPushButton(self.centralwidget)
        self.zoom_out.setGeometry(QtCore.QRect(340, 280, 50, 50))
        self.zoom_out.setMinimumSize(QtCore.QSize(50, 50))
        self.zoom_out.setMaximumSize(QtCore.QSize(50, 50))
        self.zoom_out.setStyleSheet("QPushButton {\n"
                                    "    color: #333;\n"
                                    "    border: 2px solid #555;\n"
                                    "    border-radius: 25px;\n"
                                    "    border-style: outset;\n"
                                    "    background: qradialgradient(\n"
                                    "        cx: 0.3, cy: -0.4, fx: 0.3, fy: -0.4,\n"
                                    "        radius: 1.35, stop: 0 #fff, stop: 1 #888\n"
                                    "        );\n"
                                    "    padding: 5px;\n"
                                    "    }\n"
                                    "\n"
                                    "QPushButton:hover {\n"
                                    "    background: qradialgradient(\n"
                                    "        cx: 0.3, cy: -0.4, fx: 0.3, fy: -0.4,\n"
                                    "        radius: 1.35, stop: 0 #fff, stop: 1 #bbb\n"
                                    "        );\n"
                                    "    }\n"
                                    "\n"
                                    "QPushButton:pressed {\n"
                                    "    border-style: inset;\n"
                                    "    background: qradialgradient(\n"
                                    "        cx: 0.4, cy: -0.1, fx: 0.4, fy: -0.1,\n"
                                    "        radius: 1.35, stop: 0 #fff, stop: 1 #ddd\n"
                                    "        );\n"
                                    "    }\n"
                                    "")
        self.zoom_out.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("images/icons/minus.png"),
                        QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.zoom_out.setIcon(icon2)
        self.zoom_out.setIconSize(QtCore.QSize(46, 46))
        self.zoom_out.setObjectName("zoom_out")

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 418, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        # buttons clicking area
        self.button1.clicked.connect(self.get_dest)
        self.Emergency_exit.clicked.connect(self.get_dest_emergency_exit)
        self.elivator.clicked.connect(self.get_dest_elivator)
        self.patient_rooms.clicked.connect(self.get_dest_patient_room)
        self.general_doc.clicked.connect(self.get_dest_general_doc)
        self.MRI.clicked.connect(self.get_dest_MRI)
        self.Gynacolagist.clicked.connect(self.get_dest_gynacolagist)
        self.vip_patients.clicked.connect(self.get_dest_vip_patients)
        self.Select_Hospital.clicked.connect(self.hospital_code)
        self.Select_mall.clicked.connect(self.mall_code)
        self.Select_university.clicked.connect(self.university_code)
        self.record_input.clicked.connect(self.get_audio_input)
        self.zoom_in.clicked.connect(self.zoom_in_image)
        self.zoom_out.clicked.connect(self.zoom_out_image)
        self.sos_input.clicked.connect(self.reach_for_help)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.inst.setText(_translate(
            "MainWindow", "Destination Route Instructions"))
        self.button1.setText(_translate("MainWindow", "COMPUTE"))
        self.Emergency_exit.setText(_translate("MainWindow", "Emergency"))
        self.elivator.setText(_translate("MainWindow", "Elivator"))
        self.patient_rooms.setText(_translate("MainWindow", "Patient Rooms"))
        self.general_doc.setText(_translate("MainWindow", "General Doctor"))
        self.MRI.setText(_translate("MainWindow", "M R I Scan"))
        self.Gynacolagist.setText(_translate("MainWindow", "Gynacolagist"))
        self.vip_patients.setText(_translate(
            "MainWindow", "VIP Patient Rooms"))
        self.label_3.setText(_translate(
            "MainWindow", "Enter The Destination Below"))
        self.Select_Hospital.setText(_translate("MainWindow", "Hospital"))
        self.Select_mall.setText(_translate("MainWindow", "Mall"))
        self.Select_university.setText(_translate("MainWindow", "University"))

    def get_dest(self):
        global select_value
        global zoom_address
        global zoom_out_address
        if (select_value == 1):
            text = self.textEdit.toPlainText()
            result = test1.validate_text(text)
            self.inst.setText(result[0])
            self.inst.adjustSize()
            pixmap = QPixmap(result[1])
            self.main_map.setPixmap(pixmap)
            test2.talk(result[0])
            zoom_address = result[2]
            zoom_out_address = result[1]
        elif (select_value == 2):
            text = self.textEdit.toPlainText()
            result = test1.validate_text_university(text)
            self.inst.setText(result[0])
            self.inst.adjustSize()
            pixmap = QPixmap(result[1])
            self.main_map.setPixmap(pixmap)
            test2.talk(result[0])
            zoom_address = result[2]
            zoom_out_address = result[1]
        else:
            text = self.textEdit.toPlainText()
            result = test1.validate_text_mall(text)
            self.inst.setText(result[0])
            self.inst.adjustSize()
            pixmap = QPixmap(result[1])
            self.main_map.setPixmap(pixmap)
            test2.talk(result[0])
            zoom_address = result[2]
            zoom_out_address = result[1]

    def get_dest_emergency_exit(self):
        global select_value
        global zoom_address
        global zoom_out_address
        if (select_value == 1):
            self.main_map.setPixmap(QtGui.QPixmap(
                "images/hospital_emergency.jpeg"))
            result = test1.validate_text("emergency exit")
            self.inst.setText(result[0])
            self.inst.adjustSize()
            zoom_address = result[2]
            zoom_out_address = result[1]
            # test2.talk(result[0])
        elif (select_value == 2):
            self.main_map.setPixmap(QtGui.QPixmap(
                "images/university_img/university_emergency_exit.jpeg"))
            result = test1.validate_text_mall("emergency exit")
            self.inst.setText(result[0])
            self.inst.adjustSize()
            zoom_address = result[2]
            zoom_out_address = result[1]
            # test2.talk(result[0])
        else:
            self.main_map.setPixmap(QtGui.QPixmap(
                "images/mall_img/mall_emergency_exit.jpeg"))
            result = test1.validate_text_mall("emergency exit")
            self.inst.setText(result[0])
            self.inst.adjustSize()
            zoom_address = result[2]
            zoom_out_address = result[1]
            # test2.talk(result[0])

    def get_dest_elivator(self):
        global select_value
        global zoom_address
        global zoom_out_address
        if (select_value == 1):
            self.main_map.setPixmap(QtGui.QPixmap(
                "images/hospital_elevator.jpeg"))
            result = test1.validate_text("elevator")
            self.inst.setText(result[0])
            self.inst.adjustSize()
            zoom_address = result[2]
            zoom_out_address = result[1]
            # test2.talk(result[0])
        elif (select_value == 2):
            self.main_map.setPixmap(QtGui.QPixmap(
                "images/university_img/university_auditorium.jpeg"))
            result = test1.validate_text_university("auditorium")
            self.inst.setText(result[0])
            self.inst.adjustSize()
            zoom_address = result[2]
            zoom_out_address = result[1]
            # test2.talk(result[0])
        else:
            self.main_map.setPixmap(QtGui.QPixmap(
                "images/mall_img/mall_elevator.jpeg"))
            result = test1.validate_text_mall("elevator")
            self.inst.setText(result[0])
            self.inst.adjustSize()
            zoom_address = result[2]
            zoom_out_address = result[1]
            # test2.talk(result[0])

    def get_dest_patient_room(self):
        global select_value
        global zoom_address
        global zoom_out_address
        if (select_value == 1):
            self.main_map.setPixmap(QtGui.QPixmap(
                "images/hospital_patient_room.jpeg"))
            result = test1.validate_text("patient route")
            self.inst.setText(result[0])
            self.inst.adjustSize()
            zoom_address = result[2]
            zoom_out_address = result[1]
            # test2.talk(result[0])
        elif (select_value == 2):
            self.main_map.setPixmap(QtGui.QPixmap(
                "images/university_img/university_classes.jpeg"))
            result = test1.validate_text_university("classes")
            self.inst.setText(result[0])
            self.inst.adjustSize()
            zoom_address = result[2]
            zoom_out_address = result[1]
            # test2.talk(result[0])
        else:
            self.main_map.setPixmap(QtGui.QPixmap(
                "images/mall_img/mall_rest_area.jpeg"))
            result = test1.validate_text_mall("rest area")
            self.inst.setText(result[0])
            self.inst.adjustSize()
            zoom_address = result[2]
            zoom_out_address = result[1]
            # test2.talk(result[0])

    def get_dest_general_doc(self):
        global select_value
        global zoom_address
        global zoom_out_address
        if (select_value == 1):
            self.main_map.setPixmap(QtGui.QPixmap(
                "images/hospital_general_doc.jpeg"))
            result = test1.validate_text("general doctor")
            self.inst.setText(result[0])
            self.inst.adjustSize()
            zoom_address = result[2]
            zoom_out_address = result[1]
            # test2.talk(result[0])
        elif (select_value == 2):
            self.main_map.setPixmap(QtGui.QPixmap(
                "images/university_img/university_library.jpeg"))
            result = test1.validate_text_university("library")
            self.inst.setText(result[0])
            self.inst.adjustSize()
            zoom_address = result[2]
            zoom_out_address = result[1]
            # test2.talk(result[0])
        else:
            self.main_map.setPixmap(QtGui.QPixmap(
                "images/mall_img/mall_starbucks.jpeg"))
            result = test1.validate_text_mall("star bucks")
            self.inst.setText(result[0])
            self.inst.adjustSize()
            zoom_address = result[2]
            zoom_out_address = result[1]
            # test2.talk(result[0])

    def get_dest_MRI(self):
        global select_value
        global zoom_address
        global zoom_out_address
        if (select_value == 1):
            self.main_map.setPixmap(QtGui.QPixmap(
                "images/hospital_mri_scan.jpeg"))
            result = test1.validate_text("mri")
            self.inst.setText(result[0])
            self.inst.adjustSize()
            zoom_address = result[2]
            zoom_out_address = result[1]
            # test2.talk(result[0])
        elif (select_value == 2):
            self.main_map.setPixmap(QtGui.QPixmap(
                "images/university_img/university_seminar_hall.jpeg"))
            result = test1.validate_text_university("seminar hall")
            self.inst.setText(result[0])
            self.inst.adjustSize()
            zoom_address = result[2]
            zoom_out_address = result[1]
            # test2.talk(result[0])
        else:
            self.main_map.setPixmap(QtGui.QPixmap(
                "images/mall_img/mall_toilets.jpeg"))
            result = test1.validate_text_mall("toilets")
            self.inst.setText(result[0])
            self.inst.adjustSize()
            zoom_address = result[2]
            zoom_out_address = result[1]
            # test2.talk(result[0])

    def get_dest_gynacolagist(self):
        global select_value
        global zoom_address
        global zoom_out_address
        if (select_value == 1):
            self.main_map.setPixmap(QtGui.QPixmap(
                "images/hospital_gynacologist.jpeg"))
            result = test1.validate_text("gynacolagist")
            self.inst.setText(result[0])
            self.inst.adjustSize()
            zoom_address = result[2]
            zoom_out_address = result[1]
            # test2.talk(result[0])
        elif (select_value == 2):
            self.main_map.setPixmap(QtGui.QPixmap(
                "images/university_img/university_admin_office.jpeg"))
            result = test1.validate_text_university("admin office")
            self.inst.setText(result[0])
            self.inst.adjustSize()
            zoom_address = result[2]
            zoom_out_address = result[1]
            # test2.talk(result[0])
        else:
            self.main_map.setPixmap(QtGui.QPixmap(
                "images/mall_img/mall_westside.jpeg"))
            result = test1.validate_text_mall("west side")
            self.inst.setText(result[0])
            self.inst.adjustSize()
            zoom_address = result[2]
            zoom_out_address = result[1]
            # test2.talk(result[0])

    def get_dest_vip_patients(self):
        global select_value
        global zoom_address
        global zoom_out_address
        if (select_value == 1):
            self.main_map.setPixmap(QtGui.QPixmap(
                "images/hospital_vip_patient_room.jpeg"))
            result = test1.validate_text("vip patients")
            self.inst.setText(result[0])
            self.inst.adjustSize()
            zoom_address = result[2]
            zoom_out_address = result[1]
            # test2.talk(result[0])
        elif (select_value == 2):
            self.main_map.setPixmap(QtGui.QPixmap(
                "images/university_img/university_toilets.jpeg"))
            result = test1.validate_text_university("toilets")
            self.inst.setText(result[0])
            self.inst.adjustSize()
            zoom_address = result[2]
            zoom_out_address = result[1]
            # test2.talk(result[0])
        else:
            self.main_map.setPixmap(QtGui.QPixmap(
                "images/mall_img/mall_h&m.jpeg"))
            result = test1.validate_text_mall("H AND M")
            self.inst.setText(result[0])
            self.inst.adjustSize()
            zoom_address = result[2]
            zoom_out_address = result[1]
            # test2.talk(result[0])

    def hospital_code(self):
        global select_value
        _translate = QtCore.QCoreApplication.translate
        self.Emergency_exit.setText(_translate("MainWindow", "Emergency"))
        self.elivator.setText(_translate("MainWindow", "Elevator"))
        self.patient_rooms.setText(_translate(
            "MainWindow", "Patient room 1-4"))
        self.general_doc.setText(_translate("MainWindow", "General Doctor"))
        self.MRI.setText(_translate("MainWindow", "M R I Scan"))
        self.Gynacolagist.setText(_translate("MainWindow", "Gynacolagist"))
        self.vip_patients.setText(_translate(
            "MainWindow", "Vip Patient room 1-4"))
        self.main_map.setPixmap(QtGui.QPixmap(
            "images/hospital_main_layout.jpeg"))
        select_value = 1

    def mall_code(self):
        global select_value
        _translate = QtCore.QCoreApplication.translate
        self.Emergency_exit.setText(_translate("MainWindow", "Emergency"))
        self.elivator.setText(_translate("MainWindow", "Elevator"))
        self.patient_rooms.setText(_translate(
            "MainWindow", "Restarea"))
        self.general_doc.setText(_translate("MainWindow", "Star Bucks"))
        self.MRI.setText(_translate("MainWindow", "Toilets"))
        self.Gynacolagist.setText(_translate("MainWindow", "West side"))
        self.vip_patients.setText(_translate(
            "MainWindow", "H AND M"))
        self.main_map.setPixmap(QtGui.QPixmap(
            "images/mall_img/mall_general.jpg"))
        select_value = 3

    def university_code(self):
        global select_value
        _translate = QtCore.QCoreApplication.translate
        self.Emergency_exit.setText(_translate("MainWindow", "Emergency"))
        self.elivator.setText(_translate("MainWindow", "Auditorium"))
        self.patient_rooms.setText(_translate(
            "MainWindow", "classes 1-3"))
        self.general_doc.setText(_translate("MainWindow", "Library"))
        self.MRI.setText(_translate("MainWindow", "Seminar hall"))
        self.Gynacolagist.setText(_translate("MainWindow", "Admin office"))
        self.vip_patients.setText(_translate(
            "MainWindow", "toilet"))
        self.main_map.setPixmap(QtGui.QPixmap(
            "images/university_img/university_general.jpeg"))
        select_value = 2


# audio modules and functions


    def get_audio_input(self):
        global select_value
        user_command = test2.recognize_speech()
        if (select_value == 1):
            if (("emergency" in user_command) or ("exit" in user_command)):
                result = test1.validate_text("emergency exit")
                self.inst.setText(result[0])
                self.inst.adjustSize()
                pixmap = QPixmap(result[1])
                self.main_map.setPixmap(pixmap)
                test2.talk(result[0])
            elif ("elevator" in user_command):
                result = test1.validate_text("elevator")
                self.inst.setText(result[0])
                self.inst.adjustSize()
                pixmap = QPixmap(result[1])
                self.main_map.setPixmap(pixmap)
                test2.talk(result[0])
            elif ("patient" in user_command):
                result = test1.validate_text("patient route")
                self.inst.setText(result[0])
                self.inst.adjustSize()
                pixmap = QPixmap(result[1])
                self.main_map.setPixmap(pixmap)
                test2.talk(result[0])
            elif (("general" in user_command) or ("doctor" in user_command)):
                result = test1.validate_text("general doctor")
                self.inst.setText(result[0])
                self.inst.adjustSize()
                pixmap = QPixmap(result[1])
                self.main_map.setPixmap(pixmap)
                test2.talk(result[0])
            elif (("mri" in user_command) or ("scan" in user_command)):
                result = test1.validate_text("mri")
                self.inst.setText(result[0])
                self.inst.adjustSize()
                pixmap = QPixmap(result[1])
                self.main_map.setPixmap(pixmap)
                test2.talk(result[0])
            elif ("gynacolagist" in user_command):
                result = test1.validate_text("gynacolagist")
                self.inst.setText(result[0])
                self.inst.adjustSize()
                pixmap = QPixmap(result[1])
                self.main_map.setPixmap(pixmap)
                test2.talk(result[0])
            elif ("reception" in user_command):
                result = test1.validate_text("reception")
                self.inst.setText(result[0])
                self.inst.adjustSize()
                pixmap = QPixmap(result[1])
                self.main_map.setPixmap(pixmap)
                test2.talk(result[0])
            elif ("vip" in user_command):
                result = test1.validate_text("mri")
                self.inst.setText(result[0])
                self.inst.adjustSize()
                pixmap = QPixmap(result[1])
                self.main_map.setPixmap(pixmap)
                test2.talk(result[0])
            else:
                test2.talk("couldnt find that place")
        elif (select_value == 2):
            if (("emergency" in user_command) or ("exit" in user_command)):
                result = test1.validate_text_university("emergency exit")
                self.inst.setText(result[0])
                self.inst.adjustSize()
                pixmap = QPixmap(result[1])
                self.main_map.setPixmap(pixmap)
                test2.talk(result[0])
            elif ("auditorium" in user_command):
                result = test1.validate_text_university("auditorium")
                self.inst.setText(result[0])
                self.inst.adjustSize()
                pixmap = QPixmap(result[1])
                self.main_map.setPixmap(pixmap)
                test2.talk(result[0])
            elif ("class" in user_command):
                result = test1.validate_text_university("classes")
                self.inst.setText(result[0])
                self.inst.adjustSize()
                pixmap = QPixmap(result[1])
                self.main_map.setPixmap(pixmap)
                test2.talk(result[0])
            elif ("library" in user_command):
                result = test1.validate_text_university("library")
                self.inst.setText(result[0])
                self.inst.adjustSize()
                pixmap = QPixmap(result[1])
                self.main_map.setPixmap(pixmap)
                test2.talk(result[0])
            elif (("seminar" in user_command) or ("hall" in user_command)):
                result = test1.validate_text_university("seminar hall")
                self.inst.setText(result[0])
                self.inst.adjustSize()
                pixmap = QPixmap(result[1])
                self.main_map.setPixmap(pixmap)
                test2.talk(result[0])
            elif (("admin" in user_command) or ("office" in user_command)):
                result = test1.validate_text_university("admin office")
                self.inst.setText(result[0])
                self.inst.adjustSize()
                pixmap = QPixmap(result[1])
                self.main_map.setPixmap(pixmap)
                test2.talk(result[0])
            elif ("toilet" in user_command):
                result = test1.validate_text_university("toilet")
                self.inst.setText(result[0])
                self.inst.adjustSize()
                pixmap = QPixmap(result[1])
                self.main_map.setPixmap(pixmap)
                test2.talk(result[0])
            elif (("health" in user_command) or ("center" in user_command)):
                result = test1.validate_text_university("health center")
                self.inst.setText(result[0])
                self.inst.adjustSize()
                pixmap = QPixmap(result[1])
                self.main_map.setPixmap(pixmap)
                test2.talk(result[0])
            else:
                test2.talk("couldnt find that place")
        else:
            if (("emergency" in user_command) or ("exit" in user_command)):
                result = test1.validate_text_mall("emergency exit")
                self.inst.setText(result[0])
                self.inst.adjustSize()
                pixmap = QPixmap(result[1])
                self.main_map.setPixmap(pixmap)
                test2.talk(result[0])
            elif ("elevator" in user_command):
                result = test1.validate_text_mall("elevator")
                self.inst.setText(result[0])
                self.inst.adjustSize()
                pixmap = QPixmap(result[1])
                self.main_map.setPixmap(pixmap)
                test2.talk(result[0])
            elif (("rest" in user_command) or ("area" in user_command)):
                result = test1.validate_text_mall("rest area")
                self.inst.setText(result[0])
                self.inst.adjustSize()
                pixmap = QPixmap(result[1])
                self.main_map.setPixmap(pixmap)
                test2.talk(result[0])
            elif (("star" in user_command) or ("bucks" in user_command)):
                result = test1.validate_text_mall("star bucks")
                self.inst.setText(result[0])
                self.inst.adjustSize()
                pixmap = QPixmap(result[1])
                self.main_map.setPixmap(pixmap)
                test2.talk(result[0])
            elif ("toilets" in user_command):
                result = test1.validate_text_university("toilets")
                self.inst.setText(result[0])
                self.inst.adjustSize()
                pixmap = QPixmap(result[1])
                self.main_map.setPixmap(pixmap)
                test2.talk(result[0])
            elif (("west" in user_command) or ("side" in user_command)):
                result = test1.validate_text_mall("west side")
                self.inst.setText(result[0])
                self.inst.adjustSize()
                pixmap = QPixmap(result[1])
                self.main_map.setPixmap(pixmap)
                test2.talk(result[0])
            elif ("wildcraft" in user_command):
                result = test1.validate_text_mall("wildcraft")
                self.inst.setText(result[0])
                self.inst.adjustSize()
                pixmap = QPixmap(result[1])
                self.main_map.setPixmap(pixmap)
                test2.talk(result[0])
            elif ("nike" in user_command):
                result = test1.validate_text_mall("nike")
                self.inst.setText(result[0])
                self.inst.adjustSize()
                pixmap = QPixmap(result[1])
                self.main_map.setPixmap(pixmap)
                test2.talk(result[0])
            else:
                test2.talk("couldnt find that place")

    def zoom_in_image(self):
        global zoom_address
        self.main_map.setPixmap(QtGui.QPixmap(
            zoom_address))

    def zoom_out_image(self):
        global zoom_out_address
        self.main_map.setPixmap(QtGui.QPixmap(
            zoom_out_address))

    def reach_for_help(self):
        test2.talk(
            "kindly please assist the person near you, he or she is either physically or mentally challenged")
        print("emergency contact called")


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
