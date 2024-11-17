# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'model_management.ui'
##
## Created by: Qt User Interface Compiler version 6.8.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QGridLayout, QLabel, QListWidget,
    QListWidgetItem, QMainWindow, QProgressBar, QPushButton,
    QSizePolicy, QTextBrowser, QWidget)
from faster_whisper.utils import download_model, _MODELS

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(629, 501)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout_2 = QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.button_delete = QPushButton(self.centralwidget)
        self.button_delete.setObjectName(u"button_delete")

        self.gridLayout_2.addWidget(self.button_delete, 3, 2, 1, 1)

        self.button_download = QPushButton(self.centralwidget)
        self.button_download.setObjectName(u"button_download")

        self.gridLayout_2.addWidget(self.button_download, 3, 1, 1, 1)

        self.label_models = QLabel(self.centralwidget)
        self.label_models.setObjectName(u"label_models")
        font = QFont()
        font.setBold(True)
        self.label_models.setFont(font)

        self.gridLayout_2.addWidget(self.label_models, 0, 0, 1, 1)

        self.area_model_information = QTextBrowser(self.centralwidget)
        self.area_model_information.setObjectName(u"area_model_information")

        self.gridLayout_2.addWidget(self.area_model_information, 1, 1, 1, 2)

        self.progressbar_download = QProgressBar(self.centralwidget)
        self.progressbar_download.setObjectName(u"progressbar_download")
        self.progressbar_download.setValue(24)

        self.gridLayout_2.addWidget(self.progressbar_download, 2, 1, 1, 2)

        self.list_models = QListWidget(self.centralwidget)
        QListWidgetItem(self.list_models)
        QListWidgetItem(self.list_models)
        QListWidgetItem(self.list_models)
        QListWidgetItem(self.list_models)
        self.list_models.setObjectName(u"list_models")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.list_models.sizePolicy().hasHeightForWidth())
        self.list_models.setSizePolicy(sizePolicy)

        self.gridLayout_2.addWidget(self.list_models, 1, 0, 3, 1)

        self.label_model_information = QLabel(self.centralwidget)
        self.label_model_information.setObjectName(u"label_model_information")
        self.label_model_information.setFont(font)

        self.gridLayout_2.addWidget(self.label_model_information, 0, 1, 1, 2)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"\u0423\u043f\u0440\u0430\u0432\u043b\u0435\u043d\u0438\u0435 \u043c\u043e\u0434\u0435\u043b\u044f\u043c\u0438", None))
        self.button_delete.setText(QCoreApplication.translate("MainWindow", u"\u0423\u0434\u0430\u043b\u0438\u0442\u044c", None))
        self.button_download.setText(QCoreApplication.translate("MainWindow", u"\u0421\u043a\u0430\u0447\u0430\u0442\u044c", None))
        self.label_models.setText(QCoreApplication.translate("MainWindow", u"\u0414\u043e\u0441\u0442\u0443\u043f\u043d\u044b\u0435 \u043c\u043e\u0434\u0435\u043b\u0438", None))
        self.area_model_information.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Noto Sans'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.area_model_information.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u0412\u044b\u0431\u0435\u0440\u0438\u0442\u0435 \u044d\u043b\u0435\u043c\u0435\u043d\u0442 \u0438\u0437 \u043b\u0435\u0432\u043e\u0433\u043e \u043c\u0435\u043d\u044e, \u0447\u0442\u043e\u0431\u044b \u0442\u0443\u0442 \u043e\u0442\u043e\u0431\u0440\u0430\u0437\u0438\u043b\u0430\u0441\u044c \u0438\u043d\u0444\u043e\u0440\u043c\u0430\u0446\u0438\u044f \u043e\u0431 \u044d\u043b\u0435\u043c\u0435\u043d\u0442\u0435.", None))

        __sortingEnabled = self.list_models.isSortingEnabled()
        self.list_models.setSortingEnabled(False)
        ___qlistwidgetitem = self.list_models.item(0)
        ___qlistwidgetitem.setText(QCoreApplication.translate("MainWindow", u"\u041d\u043e\u0432\u044b\u0439 \u044d\u043b\u0435\u043c\u0435\u043d\u0442", None));
        ___qlistwidgetitem1 = self.list_models.item(1)
        ___qlistwidgetitem1.setText(QCoreApplication.translate("MainWindow", u"\u041d\u043e\u0432\u044b\u0439 \u044d\u043b\u0435\u043c\u0435\u043d\u0442", None));
        ___qlistwidgetitem2 = self.list_models.item(2)
        ___qlistwidgetitem2.setText(QCoreApplication.translate("MainWindow", u"\u041d\u043e\u0432\u044b\u0439 \u044d\u043b\u0435\u043c\u0435\u043d\u0442", None));
        ___qlistwidgetitem3 = self.list_models.item(3)
        ___qlistwidgetitem3.setText(QCoreApplication.translate("MainWindow", u"\u041d\u043e\u0432\u044b\u0439 \u044d\u043b\u0435\u043c\u0435\u043d\u0442", None));
        self.list_models.setSortingEnabled(__sortingEnabled)

        self.label_model_information.setText(QCoreApplication.translate("MainWindow", u"\u0414\u0430\u043d\u043d\u044b\u0435 \u043e \u043c\u043e\u0434\u0435\u043b\u0438", None))
    # retranslateUi

