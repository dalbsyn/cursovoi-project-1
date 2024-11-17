# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main.ui'
##
## Created by: Qt User Interface Compiler version 6.8.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale, QMetaObject, QObject, QPoint, QRect, QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QCursor, QFont, QFontDatabase, QIcon, QImage, QKeySequence, QPainter, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QFileDialog, QFrame, QGridLayout, QHBoxLayout, QLabel, QLineEdit, QMainWindow, QMenu, QMenuBar, QProgressBar, QPushButton, QSizePolicy, QSpacerItem, QTextEdit, QVBoxLayout, QWidget)
from faster_whisper.utils import _MODELS
from faster_whisper.tokenizer import _LANGUAGE_CODES
from faster_whisper import WhisperModel
from faster_whisper.transcribe import TranscriptionOptions
import ui_model_management
import sys

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(821, 451)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.MinimumExpanding, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setTabletTracking(False)
        MainWindow.setAcceptDrops(False)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout_2 = QHBoxLayout(self.centralwidget)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.gridFrame = QFrame(self.centralwidget)
        self.gridFrame.setObjectName(u"gridFrame")
        self.gridLayout_2 = QGridLayout(self.gridFrame)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.pushButton = QPushButton(self.gridFrame)
        self.pushButton.setObjectName(u"pushButton")

        self.pushButton.clicked.connect(self.select_file_dialog)

        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
        self.pushButton.setSizePolicy(sizePolicy1)

        self.gridLayout_2.addWidget(self.pushButton, 1, 1, 1, 1)

        self.label_devices = QLabel(self.gridFrame)
        self.label_devices.setObjectName(u"label_devices")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.label_devices.sizePolicy().hasHeightForWidth())
        self.label_devices.setSizePolicy(sizePolicy2)

        self.gridLayout_2.addWidget(self.label_devices, 5, 0, 1, 1)

        self.box_languages = QComboBox(self.gridFrame)
        for i in _LANGUAGE_CODES:
            self.box_languages.addItem(i)

        self.box_languages.setObjectName(u"box_languages")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Ignored, QSizePolicy.Policy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.box_languages.sizePolicy().hasHeightForWidth())
        self.box_languages.setSizePolicy(sizePolicy3)

        self.gridLayout_2.addWidget(self.box_languages, 4, 1, 1, 1)

        self.label_value_ram_available = QLabel(self.gridFrame)
        self.label_value_ram_available.setObjectName(u"label_value_ram_available")
        sizePolicy1.setHeightForWidth(self.label_value_ram_available.sizePolicy().hasHeightForWidth())
        self.label_value_ram_available.setSizePolicy(sizePolicy1)

        self.gridLayout_2.addWidget(self.label_value_ram_available, 7, 1, 1, 1)

        self.label_pc_info = QLabel(self.gridFrame)
        self.label_pc_info.setObjectName(u"label_pc_info")
        sizePolicy4 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.label_pc_info.sizePolicy().hasHeightForWidth())
        self.label_pc_info.setSizePolicy(sizePolicy4)
        font = QFont()
        font.setBold(True)
        self.label_pc_info.setFont(font)

        self.gridLayout_2.addWidget(self.label_pc_info, 6, 0, 1, 2)

        self.box_models = QComboBox(self.gridFrame)

        for i in _MODELS:
            self.box_models.addItem(i)

        self.box_models.setObjectName(u"box_models")
        sizePolicy3.setHeightForWidth(self.box_models.sizePolicy().hasHeightForWidth())
        self.box_models.setSizePolicy(sizePolicy3)

        self.gridLayout_2.addWidget(self.box_models, 3, 1, 1, 1)

        self.label_file_selection = QLabel(self.gridFrame)
        self.label_file_selection.setObjectName(u"label_file_selection")
        sizePolicy4.setHeightForWidth(self.label_file_selection.sizePolicy().hasHeightForWidth())
        self.label_file_selection.setSizePolicy(sizePolicy4)
        self.label_file_selection.setFont(font)

        self.gridLayout_2.addWidget(self.label_file_selection, 0, 0, 1, 2)

        self.label_process_settings = QLabel(self.gridFrame)
        self.label_process_settings.setObjectName(u"label_process_settings")
        sizePolicy4.setHeightForWidth(self.label_process_settings.sizePolicy().hasHeightForWidth())
        self.label_process_settings.setSizePolicy(sizePolicy4)
        self.label_process_settings.setFont(font)

        self.gridLayout_2.addWidget(self.label_process_settings, 2, 0, 1, 2)

        self.box_devices = QComboBox(self.gridFrame)
        self.box_devices.addItem("")
        self.box_devices.addItem("")
        self.box_devices.addItem("")
        self.box_devices.addItem("")
        self.box_devices.setObjectName(u"box_devices")
        sizePolicy3.setHeightForWidth(self.box_devices.sizePolicy().hasHeightForWidth())
        self.box_devices.setSizePolicy(sizePolicy3)

        self.gridLayout_2.addWidget(self.box_devices, 5, 1, 1, 1)

        self.label_ram_available = QLabel(self.gridFrame)
        self.label_ram_available.setObjectName(u"label_ram_available")
        sizePolicy1.setHeightForWidth(self.label_ram_available.sizePolicy().hasHeightForWidth())
        self.label_ram_available.setSizePolicy(sizePolicy1)

        self.gridLayout_2.addWidget(self.label_ram_available, 7, 0, 1, 1)

        self.label_model = QLabel(self.gridFrame)
        self.label_model.setObjectName(u"label_model")
        sizePolicy5 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.label_model.sizePolicy().hasHeightForWidth())
        self.label_model.setSizePolicy(sizePolicy5)

        self.gridLayout_2.addWidget(self.label_model, 3, 0, 1, 1)

        self.label_language = QLabel(self.gridFrame)
        self.label_language.setObjectName(u"label_language")
        sizePolicy5.setHeightForWidth(self.label_language.sizePolicy().hasHeightForWidth())
        self.label_language.setSizePolicy(sizePolicy5)

        self.gridLayout_2.addWidget(self.label_language, 4, 0, 1, 1)

        self.label_cpu_usage = QLabel(self.gridFrame)
        self.label_cpu_usage.setObjectName(u"label_cpu_usage")
        sizePolicy6 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Preferred)
        sizePolicy6.setHorizontalStretch(0)
        sizePolicy6.setVerticalStretch(0)
        sizePolicy6.setHeightForWidth(self.label_cpu_usage.sizePolicy().hasHeightForWidth())
        self.label_cpu_usage.setSizePolicy(sizePolicy6)

        self.gridLayout_2.addWidget(self.label_cpu_usage, 8, 0, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_2.addItem(self.verticalSpacer, 9, 0, 1, 1)

        self.label_value_cpu_usage_ = QLabel(self.gridFrame)
        self.label_value_cpu_usage_.setObjectName(u"label_value_cpu_usage_")
        sizePolicy4.setHeightForWidth(self.label_value_cpu_usage_.sizePolicy().hasHeightForWidth())
        self.label_value_cpu_usage_.setSizePolicy(sizePolicy4)

        self.gridLayout_2.addWidget(self.label_value_cpu_usage_, 8, 1, 1, 1)

        self.lineEdit = QLineEdit(self.gridFrame)
        self.lineEdit.setObjectName(u"lineEdit")
        sizePolicy1.setHeightForWidth(self.lineEdit.sizePolicy().hasHeightForWidth())
        self.lineEdit.setSizePolicy(sizePolicy1)

        self.gridLayout_2.addWidget(self.lineEdit, 1, 0, 1, 1)


        self.horizontalLayout_2.addWidget(self.gridFrame)

        self.verticalFrame = QFrame(self.centralwidget)
        self.verticalFrame.setObjectName(u"verticalFrame")
        self.verticalLayout_3 = QVBoxLayout(self.verticalFrame)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.label_output = QLabel(self.verticalFrame)
        self.label_output.setObjectName(u"label_output")
        self.label_output.setFont(font)

        self.verticalLayout_3.addWidget(self.label_output)

        self.area_output = QTextEdit(self.verticalFrame)
        self.area_output.setObjectName(u"area_output")

        self.verticalLayout_3.addWidget(self.area_output)

        self.progressbar_process = QProgressBar(self.verticalFrame)
        self.progressbar_process.setObjectName(u"progressbar_process")
        self.progressbar_process.setValue(24)

        self.verticalLayout_3.addWidget(self.progressbar_process)

        self.button_start = QPushButton(self.verticalFrame)
        self.button_start.setObjectName(u"button_start")

        self.verticalLayout_3.addWidget(self.button_start)
        self.button_start.clicked.connect(self.transcribe)

        self.button_stop = QPushButton(self.verticalFrame)
        self.button_stop.setObjectName(u"button_stop")

        self.verticalLayout_3.addWidget(self.button_stop)


        self.horizontalLayout_2.addWidget(self.verticalFrame)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 821, 26))
        self.menu_model_management = QMenu(self.menubar)
        self.menu_model_management.setObjectName(u"menu_model_management")
        self.menu_reference = QMenu(self.menubar)
        self.menu_reference.setObjectName(u"menu_reference")
        MainWindow.setMenuBar(self.menubar)
        QWidget.setTabOrder(self.lineEdit, self.pushButton)
        QWidget.setTabOrder(self.pushButton, self.box_models)
        QWidget.setTabOrder(self.box_models, self.box_languages)
        QWidget.setTabOrder(self.box_languages, self.box_devices)
        QWidget.setTabOrder(self.box_devices, self.area_output)
        QWidget.setTabOrder(self.area_output, self.button_start)
        QWidget.setTabOrder(self.button_start, self.button_stop)

        self.menubar.addAction(self.menu_model_management.menuAction())
        self.menubar.addAction(self.menu_reference.menuAction())

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi
    

    def select_file_dialog(self):
        filename = QFileDialog.getOpenFileName()
        self.lineEdit.setText(filename[0])

    def transcribe(self):
        model_size = self.box_models.currentText()
        model = WhisperModel(model_size, device="cpu", compute_type="int8")
        segments, info = model.transcribe(self.lineEdit.displayText(), self.box_languages.currentText(), beam_size=5)
        for segment in segments:
            temp = "[%.2fs -> %.2fs] %s" % (segment.start, segment.end, segment.text)
            print(temp)
            self.area_output.append(temp)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"\u0422\u0440\u0430\u043d\u0441\u043a\u0440\u0438\u043f\u0442\u043e\u0440 9999", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"\u0412\u044b\u0431\u0440\u0430\u0442\u044c \u0444\u0430\u0439\u043b", None))
        self.label_devices.setText(QCoreApplication.translate("MainWindow", u"\u0423\u0441\u0442\u0440\u043e\u0439\u0441\u0442\u0432\u043e \u043e\u0431\u0440\u0430\u0431\u043e\u0442\u043a\u0438", None))
        self.label_value_ram_available.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0417\u0423", None))
        self.label_pc_info.setText(QCoreApplication.translate("MainWindow", u"\u0414\u0430\u043d\u043d\u044b\u0435 \u043e\u0431 \u043a\u043e\u043c\u043f\u044c\u044e\u0442\u0435\u0440\u0435", None))
        self.label_file_selection.setText(QCoreApplication.translate("MainWindow", u"\u0412\u044b\u0431\u043e\u0440 \u0444\u0430\u0439\u043b\u0430", None))
        self.label_process_settings.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0430\u0441\u0442\u0440\u043e\u0439\u043a\u0438 \u043e\u0431\u0440\u0430\u0431\u043e\u0442\u043a\u0438", None))
        self.box_devices.setItemText(0, QCoreApplication.translate("MainWindow", u"\u041d\u043e\u0432\u044b\u0439 \u044d\u043b\u0435\u043c\u0435\u043d\u0442", None))
        self.box_devices.setItemText(1, QCoreApplication.translate("MainWindow", u"\u041d\u043e\u0432\u044b\u0439 \u044d\u043b\u0435\u043c\u0435\u043d\u0442", None))
        self.box_devices.setItemText(2, QCoreApplication.translate("MainWindow", u"\u041d\u043e\u0432\u044b\u0439 \u044d\u043b\u0435\u043c\u0435\u043d\u0442", None))
        self.box_devices.setItemText(3, QCoreApplication.translate("MainWindow", u"\u041d\u043e\u0432\u044b\u0439 \u044d\u043b\u0435\u043c\u0435\u043d\u0442", None))

#if QT_CONFIG(statustip)
        self.box_devices.setStatusTip("")
#endif // QT_CONFIG(statustip)
        self.label_ram_available.setText(QCoreApplication.translate("MainWindow", u"\u0414\u043e\u0441\u0442\u0443\u043f\u043d\u043e \u043e\u043f\u0435\u0440\u0430\u0442\u0438\u0432\u043d\u043e\u0439 \u043f\u0430\u043c\u044f\u0442\u0438", None))
        self.label_model.setText(QCoreApplication.translate("MainWindow", u"\u041c\u043e\u0434\u0435\u043b\u044c", None))
        self.label_language.setText(QCoreApplication.translate("MainWindow", u"\u042f\u0437\u044b\u043a", None))
        self.label_cpu_usage.setText(QCoreApplication.translate("MainWindow", u"\u041f\u043e\u0442\u0440\u0435\u0431\u043b\u0435\u043d\u0438\u0435 \u0446\u0435\u043d\u0442\u0440\u0430\u043b\u044c\u043d\u043e\u0433\u043e \u043f\u0440\u043e\u0446\u0435\u0441\u0441\u043e\u0440\u0430", None))
        self.label_value_cpu_usage_.setText(QCoreApplication.translate("MainWindow", u"\u0426\u041f", None))
        self.label_output.setText(QCoreApplication.translate("MainWindow", u"\u0412\u044b\u0432\u043e\u0434 \u043e\u0431\u0440\u0430\u0431\u043e\u0442\u043a\u0438", None))
        self.button_start.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0430\u0447\u0430\u0442\u044c", None))
        self.button_stop.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0441\u0442\u0430\u043d\u043e\u0432\u0438\u0442\u044c", None))
        self.menu_model_management.setTitle(QCoreApplication.translate("MainWindow", u"\u0423\u043f\u0440\u0430\u0432\u043b\u0435\u043d\u0438\u0435 \u043c\u043e\u0434\u0435\u043b\u044f\u043c\u0438", None))
        self.menu_reference.setTitle(QCoreApplication.translate("MainWindow", u"\u0421\u043f\u0440\u0430\u0432\u043a\u0430", None))
    # retranslateUi

