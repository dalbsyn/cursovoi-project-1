# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'reference.ui'
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
    QListWidgetItem, QMainWindow, QSizePolicy, QTextBrowser,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(766, 479)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.label_selected_element_information = QLabel(self.centralwidget)
        self.label_selected_element_information.setObjectName(u"label_selected_element_information")
        font = QFont()
        font.setBold(True)
        self.label_selected_element_information.setFont(font)

        self.gridLayout.addWidget(self.label_selected_element_information, 0, 1, 1, 1)

        self.label_ui_elements = QLabel(self.centralwidget)
        self.label_ui_elements.setObjectName(u"label_ui_elements")
        self.label_ui_elements.setFont(font)

        self.gridLayout.addWidget(self.label_ui_elements, 0, 0, 1, 1)

        self.area_element_information = QTextBrowser(self.centralwidget)
        self.area_element_information.setObjectName(u"area_element_information")

        self.gridLayout.addWidget(self.area_element_information, 1, 1, 1, 1)

        self.list_ui_elements = QListWidget(self.centralwidget)
        QListWidgetItem(self.list_ui_elements)
        QListWidgetItem(self.list_ui_elements)
        QListWidgetItem(self.list_ui_elements)
        QListWidgetItem(self.list_ui_elements)
        self.list_ui_elements.setObjectName(u"list_ui_elements")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.list_ui_elements.sizePolicy().hasHeightForWidth())
        self.list_ui_elements.setSizePolicy(sizePolicy)

        self.gridLayout.addWidget(self.list_ui_elements, 1, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        QWidget.setTabOrder(self.list_ui_elements, self.area_element_information)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"\u0421\u043f\u0440\u0430\u0432\u043a\u0430", None))
        self.label_selected_element_information.setText(QCoreApplication.translate("MainWindow", u"\u0418\u043d\u0444\u043e\u0440\u043c\u0430\u0446\u0438\u044f \u043e \u0432\u044b\u0431\u0440\u0430\u043d\u043d\u043e\u043c \u044d\u043b\u0435\u043c\u0435\u043d\u0442\u0435", None))
        self.label_ui_elements.setText(QCoreApplication.translate("MainWindow", u"\u042d\u043b\u0435\u043c\u0435\u043d\u0442\u044b \u0438\u043d\u0442\u0435\u0440\u0444\u0435\u0439\u0441\u0430", None))
        self.area_element_information.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u0412\u044b\u0431\u0435\u0440\u0438\u0442\u0435 \u044d\u043b\u0435\u043c\u0435\u043d\u0442 \u0438\u0437 \u043b\u0435\u0432\u043e\u0433\u043e \u043c\u0435\u043d\u044e, \u0447\u0442\u043e\u0431\u044b \u0442\u0443\u0442 \u043e\u0442\u043e\u0431\u0440\u0430\u0437\u0438\u043b\u0430\u0441\u044c \u0438\u043d\u0444\u043e\u0440\u043c\u0430\u0446\u0438\u044f \u043e\u0431 \u044d\u043b\u0435\u043c\u0435\u043d\u0442\u0435.", None))

        __sortingEnabled = self.list_ui_elements.isSortingEnabled()
        self.list_ui_elements.setSortingEnabled(False)
        ___qlistwidgetitem = self.list_ui_elements.item(0)
        ___qlistwidgetitem.setText(QCoreApplication.translate("MainWindow", u"\u041d\u043e\u0432\u044b\u0439 \u044d\u043b\u0435\u043c\u0435\u043d\u0442", None));
        ___qlistwidgetitem1 = self.list_ui_elements.item(1)
        ___qlistwidgetitem1.setText(QCoreApplication.translate("MainWindow", u"\u041d\u043e\u0432\u044b\u0439 \u044d\u043b\u0435\u043c\u0435\u043d\u0442", None));
        ___qlistwidgetitem2 = self.list_ui_elements.item(2)
        ___qlistwidgetitem2.setText(QCoreApplication.translate("MainWindow", u"\u041d\u043e\u0432\u044b\u0439 \u044d\u043b\u0435\u043c\u0435\u043d\u0442", None));
        ___qlistwidgetitem3 = self.list_ui_elements.item(3)
        ___qlistwidgetitem3.setText(QCoreApplication.translate("MainWindow", u"\u041d\u043e\u0432\u044b\u0439 \u044d\u043b\u0435\u043c\u0435\u043d\u0442", None));
        self.list_ui_elements.setSortingEnabled(__sortingEnabled)

    # retranslateUi

