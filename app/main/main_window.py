# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main.ui'
##
## Created by: Qt User Interface Compiler version 6.8.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QFrame,
    QGridLayout, QHBoxLayout, QLabel, QLayout,
    QLineEdit, QMainWindow, QMenu, QMenuBar,
    QProgressBar, QPushButton, QSizePolicy, QSpacerItem,
    QStatusBar, QTextBrowser, QWidget)
from app.model_management.model_management import Ui_ModelManagement

class Ui_Main(object):
    def setupUi(self, Main):
        if not Main.objectName():
            Main.setObjectName(u"Main")
        Main.resize(846, 586)
        self.main_widget = QWidget(Main)
        self.main_widget.setObjectName(u"main_widget")
        self.gridLayout = QGridLayout(self.main_widget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.combo_model = QComboBox(self.main_widget)
        self.combo_model.setObjectName(u"combo_model")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.combo_model.sizePolicy().hasHeightForWidth())
        self.combo_model.setSizePolicy(sizePolicy)

        self.gridLayout.addWidget(self.combo_model, 3, 1, 1, 1)

        self.check_timestamp = QCheckBox(self.main_widget)
        self.check_timestamp.setObjectName(u"check_timestamp")
        sizePolicy.setHeightForWidth(self.check_timestamp.sizePolicy().hasHeightForWidth())
        self.check_timestamp.setSizePolicy(sizePolicy)
        self.check_timestamp.setCheckable(True)
        self.check_timestamp.setChecked(False)

        self.gridLayout.addWidget(self.check_timestamp, 7, 0, 1, 2)

        self.button_file_selection = QPushButton(self.main_widget)
        self.button_file_selection.setObjectName(u"button_file_selection")
        sizePolicy.setHeightForWidth(self.button_file_selection.sizePolicy().hasHeightForWidth())
        self.button_file_selection.setSizePolicy(sizePolicy)

        self.gridLayout.addWidget(self.button_file_selection, 1, 1, 1, 1)

        self.button_stop = QPushButton(self.main_widget)
        self.button_stop.setObjectName(u"button_stop")

        self.gridLayout.addWidget(self.button_stop, 23, 3, 1, 1)

        self.label_language = QLabel(self.main_widget)
        self.label_language.setObjectName(u"label_language")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.label_language.sizePolicy().hasHeightForWidth())
        self.label_language.setSizePolicy(sizePolicy1)

        self.gridLayout.addWidget(self.label_language, 4, 0, 1, 1)

        self.label_quantization = QLabel(self.main_widget)
        self.label_quantization.setObjectName(u"label_quantization")
        sizePolicy1.setHeightForWidth(self.label_quantization.sizePolicy().hasHeightForWidth())
        self.label_quantization.setSizePolicy(sizePolicy1)

        self.gridLayout.addWidget(self.label_quantization, 6, 0, 1, 1)

        self.button_save = QPushButton(self.main_widget)
        self.button_save.setObjectName(u"button_save")

        self.gridLayout.addWidget(self.button_save, 24, 2, 1, 2)

        self.button_begin = QPushButton(self.main_widget)
        self.button_begin.setObjectName(u"button_begin")

        self.gridLayout.addWidget(self.button_begin, 23, 2, 1, 1)

        self.text_output = QTextBrowser(self.main_widget)
        self.text_output.setObjectName(u"text_output")

        self.gridLayout.addWidget(self.text_output, 1, 2, 21, 2)

        self.label_file_selection = QLabel(self.main_widget)
        self.label_file_selection.setObjectName(u"label_file_selection")
        sizePolicy1.setHeightForWidth(self.label_file_selection.sizePolicy().hasHeightForWidth())
        self.label_file_selection.setSizePolicy(sizePolicy1)
        font = QFont()
        font.setBold(True)
        self.label_file_selection.setFont(font)

        self.gridLayout.addWidget(self.label_file_selection, 0, 0, 1, 2)

        self.combo_quantization = QComboBox(self.main_widget)
        self.combo_quantization.setObjectName(u"combo_quantization")
        sizePolicy.setHeightForWidth(self.combo_quantization.sizePolicy().hasHeightForWidth())
        self.combo_quantization.setSizePolicy(sizePolicy)

        self.gridLayout.addWidget(self.combo_quantization, 6, 1, 1, 1)

        self.label_process_settings = QLabel(self.main_widget)
        self.label_process_settings.setObjectName(u"label_process_settings")
        sizePolicy1.setHeightForWidth(self.label_process_settings.sizePolicy().hasHeightForWidth())
        self.label_process_settings.setSizePolicy(sizePolicy1)
        font1 = QFont()
        font1.setBold(True)
        font1.setItalic(False)
        font1.setKerning(True)
        self.label_process_settings.setFont(font1)

        self.gridLayout.addWidget(self.label_process_settings, 2, 0, 1, 2)

        self.combo_device = QComboBox(self.main_widget)
        self.combo_device.setObjectName(u"combo_device")
        sizePolicy.setHeightForWidth(self.combo_device.sizePolicy().hasHeightForWidth())
        self.combo_device.setSizePolicy(sizePolicy)

        self.gridLayout.addWidget(self.combo_device, 5, 1, 1, 1)

        self.label_process_values = QLabel(self.main_widget)
        self.label_process_values.setObjectName(u"label_process_values")
        sizePolicy1.setHeightForWidth(self.label_process_values.sizePolicy().hasHeightForWidth())
        self.label_process_values.setSizePolicy(sizePolicy1)
        self.label_process_values.setFont(font)
        self.label_process_values.setFrameShape(QFrame.NoFrame)

        self.gridLayout.addWidget(self.label_process_values, 8, 0, 1, 2)

        self.label_model = QLabel(self.main_widget)
        self.label_model.setObjectName(u"label_model")
        sizePolicy1.setHeightForWidth(self.label_model.sizePolicy().hasHeightForWidth())
        self.label_model.setSizePolicy(sizePolicy1)

        self.gridLayout.addWidget(self.label_model, 3, 0, 1, 1)

        self.label_device = QLabel(self.main_widget)
        self.label_device.setObjectName(u"label_device")
        sizePolicy1.setHeightForWidth(self.label_device.sizePolicy().hasHeightForWidth())
        self.label_device.setSizePolicy(sizePolicy1)

        self.gridLayout.addWidget(self.label_device, 5, 0, 1, 1)

        self.label_output = QLabel(self.main_widget)
        self.label_output.setObjectName(u"label_output")
        sizePolicy1.setHeightForWidth(self.label_output.sizePolicy().hasHeightForWidth())
        self.label_output.setSizePolicy(sizePolicy1)
        self.label_output.setFont(font)

        self.gridLayout.addWidget(self.label_output, 0, 2, 1, 1)

        self.combo_language = QComboBox(self.main_widget)
        self.combo_language.setObjectName(u"combo_language")
        sizePolicy.setHeightForWidth(self.combo_language.sizePolicy().hasHeightForWidth())
        self.combo_language.setSizePolicy(sizePolicy)

        self.gridLayout.addWidget(self.combo_language, 4, 1, 1, 1)

        self.progressBar = QProgressBar(self.main_widget)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setValue(0)
        self.progressBar.setTextVisible(True)
        self.progressBar.setInvertedAppearance(False)
        self.progressBar.setTextDirection(QProgressBar.TopToBottom)

        self.gridLayout.addWidget(self.progressBar, 22, 2, 1, 2)

        self.line_file_selection = QLineEdit(self.main_widget)
        self.line_file_selection.setObjectName(u"line_file_selection")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.line_file_selection.sizePolicy().hasHeightForWidth())
        self.line_file_selection.setSizePolicy(sizePolicy2)

        self.gridLayout.addWidget(self.line_file_selection, 1, 0, 1, 1)

        self.horizontal_langauge = QWidget(self.main_widget)
        self.horizontal_langauge.setObjectName(u"horizontal_langauge")
        sizePolicy1.setHeightForWidth(self.horizontal_langauge.sizePolicy().hasHeightForWidth())
        self.horizontal_langauge.setSizePolicy(sizePolicy1)
        self.horizontalLayout = QHBoxLayout(self.horizontal_langauge)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setSizeConstraint(QLayout.SetFixedSize)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.label_selected_language = QLabel(self.horizontal_langauge)
        self.label_selected_language.setObjectName(u"label_selected_language")
        sizePolicy.setHeightForWidth(self.label_selected_language.sizePolicy().hasHeightForWidth())
        self.label_selected_language.setSizePolicy(sizePolicy)

        self.horizontalLayout.addWidget(self.label_selected_language)

        self.label_selected_language_value = QLabel(self.horizontal_langauge)
        self.label_selected_language_value.setObjectName(u"label_selected_language_value")
        sizePolicy1.setHeightForWidth(self.label_selected_language_value.sizePolicy().hasHeightForWidth())
        self.label_selected_language_value.setSizePolicy(sizePolicy1)

        self.horizontalLayout.addWidget(self.label_selected_language_value)


        self.gridLayout.addWidget(self.horizontal_langauge, 9, 0, 1, 2)

        self.horzontal_model = QWidget(self.main_widget)
        self.horzontal_model.setObjectName(u"horzontal_model")
        sizePolicy1.setHeightForWidth(self.horzontal_model.sizePolicy().hasHeightForWidth())
        self.horzontal_model.setSizePolicy(sizePolicy1)
        self.horizontalLayout_2 = QHBoxLayout(self.horzontal_model)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setSizeConstraint(QLayout.SetFixedSize)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.label_selected_model = QLabel(self.horzontal_model)
        self.label_selected_model.setObjectName(u"label_selected_model")
        sizePolicy.setHeightForWidth(self.label_selected_model.sizePolicy().hasHeightForWidth())
        self.label_selected_model.setSizePolicy(sizePolicy)

        self.horizontalLayout_2.addWidget(self.label_selected_model)

        self.label_selected_model_value = QLabel(self.horzontal_model)
        self.label_selected_model_value.setObjectName(u"label_selected_model_value")
        sizePolicy1.setHeightForWidth(self.label_selected_model_value.sizePolicy().hasHeightForWidth())
        self.label_selected_model_value.setSizePolicy(sizePolicy1)

        self.horizontalLayout_2.addWidget(self.label_selected_model_value)


        self.gridLayout.addWidget(self.horzontal_model, 10, 0, 1, 2)

        self.horizontal_quantization = QWidget(self.main_widget)
        self.horizontal_quantization.setObjectName(u"horizontal_quantization")
        self.horizontalLayout_4 = QHBoxLayout(self.horizontal_quantization)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setSizeConstraint(QLayout.SetFixedSize)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.label_selected_quantization = QLabel(self.horizontal_quantization)
        self.label_selected_quantization.setObjectName(u"label_selected_quantization")
        sizePolicy.setHeightForWidth(self.label_selected_quantization.sizePolicy().hasHeightForWidth())
        self.label_selected_quantization.setSizePolicy(sizePolicy)

        self.horizontalLayout_4.addWidget(self.label_selected_quantization)

        self.label_selected_quantization_value = QLabel(self.horizontal_quantization)
        self.label_selected_quantization_value.setObjectName(u"label_selected_quantization_value")
        sizePolicy1.setHeightForWidth(self.label_selected_quantization_value.sizePolicy().hasHeightForWidth())
        self.label_selected_quantization_value.setSizePolicy(sizePolicy1)

        self.horizontalLayout_4.addWidget(self.label_selected_quantization_value)


        self.gridLayout.addWidget(self.horizontal_quantization, 12, 0, 1, 2)

        self.horizontal_timestamp = QWidget(self.main_widget)
        self.horizontal_timestamp.setObjectName(u"horizontal_timestamp")
        self.horizontalLayout_5 = QHBoxLayout(self.horizontal_timestamp)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setSizeConstraint(QLayout.SetFixedSize)
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.label_selected_timestamp = QLabel(self.horizontal_timestamp)
        self.label_selected_timestamp.setObjectName(u"label_selected_timestamp")
        sizePolicy.setHeightForWidth(self.label_selected_timestamp.sizePolicy().hasHeightForWidth())
        self.label_selected_timestamp.setSizePolicy(sizePolicy)

        self.horizontalLayout_5.addWidget(self.label_selected_timestamp)

        self.label_selected_timestamp_value = QLabel(self.horizontal_timestamp)
        self.label_selected_timestamp_value.setObjectName(u"label_selected_timestamp_value")
        sizePolicy1.setHeightForWidth(self.label_selected_timestamp_value.sizePolicy().hasHeightForWidth())
        self.label_selected_timestamp_value.setSizePolicy(sizePolicy1)

        self.horizontalLayout_5.addWidget(self.label_selected_timestamp_value)


        self.gridLayout.addWidget(self.horizontal_timestamp, 13, 0, 1, 2)

        self.horizontal_ram_vram = QWidget(self.main_widget)
        self.horizontal_ram_vram.setObjectName(u"horizontal_ram_vram")
        self.horizontalLayout_6 = QHBoxLayout(self.horizontal_ram_vram)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setSizeConstraint(QLayout.SetFixedSize)
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.label_ram_vram = QLabel(self.horizontal_ram_vram)
        self.label_ram_vram.setObjectName(u"label_ram_vram")
        sizePolicy.setHeightForWidth(self.label_ram_vram.sizePolicy().hasHeightForWidth())
        self.label_ram_vram.setSizePolicy(sizePolicy)

        self.horizontalLayout_6.addWidget(self.label_ram_vram)

        self.label_ram_vram_value = QLabel(self.horizontal_ram_vram)
        self.label_ram_vram_value.setObjectName(u"label_ram_vram_value")
        sizePolicy1.setHeightForWidth(self.label_ram_vram_value.sizePolicy().hasHeightForWidth())
        self.label_ram_vram_value.setSizePolicy(sizePolicy1)

        self.horizontalLayout_6.addWidget(self.label_ram_vram_value)


        self.gridLayout.addWidget(self.horizontal_ram_vram, 14, 0, 1, 2)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer, 20, 0, 5, 2)

        self.horizontal_device = QWidget(self.main_widget)
        self.horizontal_device.setObjectName(u"horizontal_device")
        self.horizontalLayout_3 = QHBoxLayout(self.horizontal_device)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setSizeConstraint(QLayout.SetFixedSize)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.label_selected_device = QLabel(self.horizontal_device)
        self.label_selected_device.setObjectName(u"label_selected_device")
        sizePolicy.setHeightForWidth(self.label_selected_device.sizePolicy().hasHeightForWidth())
        self.label_selected_device.setSizePolicy(sizePolicy)

        self.horizontalLayout_3.addWidget(self.label_selected_device)

        self.label_selected_device_value = QLabel(self.horizontal_device)
        self.label_selected_device_value.setObjectName(u"label_selected_device_value")
        sizePolicy1.setHeightForWidth(self.label_selected_device_value.sizePolicy().hasHeightForWidth())
        self.label_selected_device_value.setSizePolicy(sizePolicy1)

        self.horizontalLayout_3.addWidget(self.label_selected_device_value)


        self.gridLayout.addWidget(self.horizontal_device, 11, 0, 1, 2)

        Main.setCentralWidget(self.main_widget)
        self.menubar = QMenuBar(Main)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 846, 24))
        self.menu_model_management = QMenu(self.menubar)
        self.menu_model_management.setObjectName(u"menu_model_management")
        self.menu_model_management.triggered.connect(self.show_model_management)
        self.menu_reference = QMenu(self.menubar)
        self.menu_reference.setObjectName(u"menu_reference")
        Main.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(Main)
        self.statusbar.setObjectName(u"statusbar")
        Main.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menu_model_management.menuAction())
        self.menubar.addAction(self.menu_reference.menuAction())

        self.retranslateUi(Main)

        QMetaObject.connectSlotsByName(Main)
    # setupUi

    def show_model_management(self):
        print("A")
        #model_management = Ui_ModelManagement()
        # model_management.exec()

    def retranslateUi(self, Main):
        Main.setWindowTitle(QCoreApplication.translate("Main", u"MainWindow", None))
        self.check_timestamp.setText(QCoreApplication.translate("Main", u"Insert timestamp beside string", None))
        self.button_file_selection.setText(QCoreApplication.translate("Main", u"Select File", None))
        self.button_stop.setText(QCoreApplication.translate("Main", u"Stop", None))
        self.label_language.setText(QCoreApplication.translate("Main", u"Language", None))
        self.label_quantization.setText(QCoreApplication.translate("Main", u"Quantization", None))
        self.button_save.setText(QCoreApplication.translate("Main", u"Save output", None))
        self.button_begin.setText(QCoreApplication.translate("Main", u"Begin", None))
        self.label_file_selection.setText(QCoreApplication.translate("Main", u"File selection", None))
        self.label_process_settings.setText(QCoreApplication.translate("Main", u"Process settings", None))
        self.label_process_values.setText(QCoreApplication.translate("Main", u"Process values", None))
        self.label_model.setText(QCoreApplication.translate("Main", u"Model", None))
        self.label_device.setText(QCoreApplication.translate("Main", u"Device", None))
        self.label_output.setText(QCoreApplication.translate("Main", u"Output", None))
        self.progressBar.setFormat(QCoreApplication.translate("Main", u"%p%", None))
        self.label_selected_language.setText(QCoreApplication.translate("Main", u"Selected language:", None))
        self.label_selected_language_value.setText(QCoreApplication.translate("Main", u"value", None))
        self.label_selected_model.setText(QCoreApplication.translate("Main", u"Selected model:", None))
        self.label_selected_model_value.setText(QCoreApplication.translate("Main", u"value", None))
        self.label_selected_quantization.setText(QCoreApplication.translate("Main", u"Selected quantization:", None))
        self.label_selected_quantization_value.setText(QCoreApplication.translate("Main", u"value", None))
        self.label_selected_timestamp.setText(QCoreApplication.translate("Main", u"Timestamp:", None))
        self.label_selected_timestamp_value.setText(QCoreApplication.translate("Main", u"value", None))
        self.label_ram_vram.setText(QCoreApplication.translate("Main", u"Available RAM/VRAM", None))
        self.label_ram_vram_value.setText(QCoreApplication.translate("Main", u"value", None))
        self.label_selected_device.setText(QCoreApplication.translate("Main", u"Selected device:", None))
        self.label_selected_device_value.setText(QCoreApplication.translate("Main", u"value", None))
        self.menu_model_management.setTitle(QCoreApplication.translate("Main", u"Model management", None))
        self.menu_reference.setTitle(QCoreApplication.translate("Main", u"Reference", None))
    # retranslateUi

