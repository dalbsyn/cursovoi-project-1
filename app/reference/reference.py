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
from PySide6.QtWidgets import (QApplication, QDialog, QGridLayout, QLabel,
    QLayout, QListWidget, QListWidgetItem, QSizePolicy,
    QTextBrowser, QWidget)

class Ui_Reference(object):
    def setupUi(self, Reference):
        if not Reference.objectName():
            Reference.setObjectName(u"Reference")
        Reference.resize(760, 306)
        self.gridLayout_2 = QGridLayout(Reference)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setSizeConstraint(QLayout.SetFixedSize)
        self.text_information = QTextBrowser(Reference)
        self.text_information.setObjectName(u"text_information")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.text_information.sizePolicy().hasHeightForWidth())
        self.text_information.setSizePolicy(sizePolicy)
        self.text_information.setMinimumSize(QSize(480, 0))

        self.gridLayout_2.addWidget(self.text_information, 1, 1, 1, 2)

        self.label_elements = QLabel(Reference)
        self.label_elements.setObjectName(u"label_elements")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.label_elements.sizePolicy().hasHeightForWidth())
        self.label_elements.setSizePolicy(sizePolicy1)
        font = QFont()
        font.setBold(True)
        self.label_elements.setFont(font)

        self.gridLayout_2.addWidget(self.label_elements, 0, 0, 1, 1)

        self.list_elements = QListWidget(Reference)
        QListWidgetItem(self.list_elements)
        QListWidgetItem(self.list_elements)
        QListWidgetItem(self.list_elements)
        QListWidgetItem(self.list_elements)
        self.list_elements.setObjectName(u"list_elements")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.list_elements.sizePolicy().hasHeightForWidth())
        self.list_elements.setSizePolicy(sizePolicy2)

        self.gridLayout_2.addWidget(self.list_elements, 1, 0, 1, 1)

        self.label_element_info = QLabel(Reference)
        self.label_element_info.setObjectName(u"label_element_info")
        sizePolicy1.setHeightForWidth(self.label_element_info.sizePolicy().hasHeightForWidth())
        self.label_element_info.setSizePolicy(sizePolicy1)
        self.label_element_info.setFont(font)
        self.label_element_info.setWordWrap(False)

        self.gridLayout_2.addWidget(self.label_element_info, 0, 1, 1, 2)


        self.retranslateUi(Reference)

        QMetaObject.connectSlotsByName(Reference)
    # setupUi

    def retranslateUi(self, Reference):
        Reference.setWindowTitle(QCoreApplication.translate("Reference", u"Dialog", None))
        self.text_information.setPlaceholderText(QCoreApplication.translate("Reference", u"Select any element from left side menu to reveal information about it.", None))
        self.label_elements.setText(QCoreApplication.translate("Reference", u"Elements", None))

        __sortingEnabled = self.list_elements.isSortingEnabled()
        self.list_elements.setSortingEnabled(False)
        ___qlistwidgetitem = self.list_elements.item(0)
        ___qlistwidgetitem.setText(QCoreApplication.translate("Reference", u"New Item", None));
        ___qlistwidgetitem1 = self.list_elements.item(1)
        ___qlistwidgetitem1.setText(QCoreApplication.translate("Reference", u"New Item", None));
        ___qlistwidgetitem2 = self.list_elements.item(2)
        ___qlistwidgetitem2.setText(QCoreApplication.translate("Reference", u"New Item", None));
        ___qlistwidgetitem3 = self.list_elements.item(3)
        ___qlistwidgetitem3.setText(QCoreApplication.translate("Reference", u"New Item", None));
        self.list_elements.setSortingEnabled(__sortingEnabled)

        self.label_element_info.setText(QCoreApplication.translate("Reference", u"Information about selected element", None))
    # retranslateUi

