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
from PySide6.QtWidgets import (QApplication, QDialog, QGridLayout, QHBoxLayout,
    QLabel, QLayout, QListWidget, QListWidgetItem,
    QProgressBar, QPushButton, QSizePolicy, QWidget)

class Ui_ModelManagement(object):
    def setupUi(self, ModelManagement):
        if not ModelManagement.objectName():
            ModelManagement.setObjectName(u"ModelManagement")
        ModelManagement.setEnabled(True)
        ModelManagement.resize(760, 385)
        ModelManagement.setMinimumSize(QSize(0, 3))
        ModelManagement.setSizeGripEnabled(True)
        self.gridLayout = QGridLayout(ModelManagement)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setSizeConstraint(QLayout.SetFixedSize)
        self.horizontal_model = QWidget(ModelManagement)
        self.horizontal_model.setObjectName(u"horizontal_model")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.horizontal_model.sizePolicy().hasHeightForWidth())
        self.horizontal_model.setSizePolicy(sizePolicy)
        self.horizontalLayout_4 = QHBoxLayout(self.horizontal_model)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setSizeConstraint(QLayout.SetFixedSize)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.label_model_name = QLabel(self.horizontal_model)
        self.label_model_name.setObjectName(u"label_model_name")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.label_model_name.sizePolicy().hasHeightForWidth())
        self.label_model_name.setSizePolicy(sizePolicy1)

        self.horizontalLayout_4.addWidget(self.label_model_name)

        self.label_model_name_value = QLabel(self.horizontal_model)
        self.label_model_name_value.setObjectName(u"label_model_name_value")
        sizePolicy.setHeightForWidth(self.label_model_name_value.sizePolicy().hasHeightForWidth())
        self.label_model_name_value.setSizePolicy(sizePolicy)

        self.horizontalLayout_4.addWidget(self.label_model_name_value)


        self.gridLayout.addWidget(self.horizontal_model, 1, 1, 1, 2)

        self.horizontal_memory = QWidget(ModelManagement)
        self.horizontal_memory.setObjectName(u"horizontal_memory")
        sizePolicy.setHeightForWidth(self.horizontal_memory.sizePolicy().hasHeightForWidth())
        self.horizontal_memory.setSizePolicy(sizePolicy)
        self.horizontalLayout_3 = QHBoxLayout(self.horizontal_memory)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setSizeConstraint(QLayout.SetFixedSize)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.label_memory_usage = QLabel(self.horizontal_memory)
        self.label_memory_usage.setObjectName(u"label_memory_usage")
        sizePolicy1.setHeightForWidth(self.label_memory_usage.sizePolicy().hasHeightForWidth())
        self.label_memory_usage.setSizePolicy(sizePolicy1)

        self.horizontalLayout_3.addWidget(self.label_memory_usage)

        self.label_memory_usage_value = QLabel(self.horizontal_memory)
        self.label_memory_usage_value.setObjectName(u"label_memory_usage_value")
        sizePolicy.setHeightForWidth(self.label_memory_usage_value.sizePolicy().hasHeightForWidth())
        self.label_memory_usage_value.setSizePolicy(sizePolicy)

        self.horizontalLayout_3.addWidget(self.label_memory_usage_value)


        self.gridLayout.addWidget(self.horizontal_memory, 2, 1, 1, 2)

        self.listWidget = QListWidget(ModelManagement)
        QListWidgetItem(self.listWidget)
        QListWidgetItem(self.listWidget)
        QListWidgetItem(self.listWidget)
        QListWidgetItem(self.listWidget)
        self.listWidget.setObjectName(u"listWidget")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.listWidget.sizePolicy().hasHeightForWidth())
        self.listWidget.setSizePolicy(sizePolicy2)

        self.gridLayout.addWidget(self.listWidget, 1, 0, 8, 1)

        self.progress_download = QProgressBar(ModelManagement)
        self.progress_download.setObjectName(u"progress_download")
        self.progress_download.setValue(0)

        self.gridLayout.addWidget(self.progress_download, 4, 1, 1, 2)

        self.label_model_info = QLabel(ModelManagement)
        self.label_model_info.setObjectName(u"label_model_info")
        sizePolicy.setHeightForWidth(self.label_model_info.sizePolicy().hasHeightForWidth())
        self.label_model_info.setSizePolicy(sizePolicy)
        self.label_model_info.setMinimumSize(QSize(480, 0))
        font = QFont()
        font.setBold(True)
        self.label_model_info.setFont(font)

        self.gridLayout.addWidget(self.label_model_info, 0, 1, 1, 2)

        self.button_download = QPushButton(ModelManagement)
        self.button_download.setObjectName(u"button_download")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.button_download.sizePolicy().hasHeightForWidth())
        self.button_download.setSizePolicy(sizePolicy3)

        self.gridLayout.addWidget(self.button_download, 5, 1, 1, 1)

        self.button_delete = QPushButton(ModelManagement)
        self.button_delete.setObjectName(u"button_delete")
        sizePolicy3.setHeightForWidth(self.button_delete.sizePolicy().hasHeightForWidth())
        self.button_delete.setSizePolicy(sizePolicy3)

        self.gridLayout.addWidget(self.button_delete, 5, 2, 1, 1)

        self.label_models = QLabel(ModelManagement)
        self.label_models.setObjectName(u"label_models")
        sizePolicy.setHeightForWidth(self.label_models.sizePolicy().hasHeightForWidth())
        self.label_models.setSizePolicy(sizePolicy)
        self.label_models.setFont(font)

        self.gridLayout.addWidget(self.label_models, 0, 0, 1, 1)

        self.horizontal_storage = QWidget(ModelManagement)
        self.horizontal_storage.setObjectName(u"horizontal_storage")
        sizePolicy.setHeightForWidth(self.horizontal_storage.sizePolicy().hasHeightForWidth())
        self.horizontal_storage.setSizePolicy(sizePolicy)
        self.horizontalLayout_5 = QHBoxLayout(self.horizontal_storage)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setSizeConstraint(QLayout.SetFixedSize)
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.label_storage_usage = QLabel(self.horizontal_storage)
        self.label_storage_usage.setObjectName(u"label_storage_usage")
        sizePolicy1.setHeightForWidth(self.label_storage_usage.sizePolicy().hasHeightForWidth())
        self.label_storage_usage.setSizePolicy(sizePolicy1)

        self.horizontalLayout_5.addWidget(self.label_storage_usage)

        self.label_storage_usage_value = QLabel(self.horizontal_storage)
        self.label_storage_usage_value.setObjectName(u"label_storage_usage_value")
        sizePolicy.setHeightForWidth(self.label_storage_usage_value.sizePolicy().hasHeightForWidth())
        self.label_storage_usage_value.setSizePolicy(sizePolicy)

        self.horizontalLayout_5.addWidget(self.label_storage_usage_value)


        self.gridLayout.addWidget(self.horizontal_storage, 3, 1, 1, 2)

        self.horizontal_storage.raise_()
        self.label_models.raise_()
        self.label_model_info.raise_()
        self.listWidget.raise_()
        self.horizontal_memory.raise_()
        self.horizontal_model.raise_()
        self.progress_download.raise_()
        self.button_download.raise_()
        self.button_delete.raise_()

        self.retranslateUi(ModelManagement)

        QMetaObject.connectSlotsByName(ModelManagement)
    # setupUi

    def retranslateUi(self, ModelManagement):
        ModelManagement.setWindowTitle(QCoreApplication.translate("ModelManagement", u"Dialog", None))
        self.label_model_name.setText(QCoreApplication.translate("ModelManagement", u"Model name:", None))
        self.label_model_name_value.setText(QCoreApplication.translate("ModelManagement", u"value", None))
        self.label_memory_usage.setText(QCoreApplication.translate("ModelManagement", u"Memory usage:", None))
        self.label_memory_usage_value.setText(QCoreApplication.translate("ModelManagement", u"value", None))

        __sortingEnabled = self.listWidget.isSortingEnabled()
        self.listWidget.setSortingEnabled(False)
        ___qlistwidgetitem = self.listWidget.item(0)
        ___qlistwidgetitem.setText(QCoreApplication.translate("ModelManagement", u"New Item", None));
        ___qlistwidgetitem1 = self.listWidget.item(1)
        ___qlistwidgetitem1.setText(QCoreApplication.translate("ModelManagement", u"New Item", None));
        ___qlistwidgetitem2 = self.listWidget.item(2)
        ___qlistwidgetitem2.setText(QCoreApplication.translate("ModelManagement", u"New Item", None));
        ___qlistwidgetitem3 = self.listWidget.item(3)
        ___qlistwidgetitem3.setText(QCoreApplication.translate("ModelManagement", u"New Item", None));
        self.listWidget.setSortingEnabled(__sortingEnabled)

        self.label_model_info.setText(QCoreApplication.translate("ModelManagement", u"About model", None))
        self.button_download.setText(QCoreApplication.translate("ModelManagement", u"Download", None))
        self.button_delete.setText(QCoreApplication.translate("ModelManagement", u"Delete", None))
        self.label_models.setText(QCoreApplication.translate("ModelManagement", u"Models", None))
        self.label_storage_usage.setText(QCoreApplication.translate("ModelManagement", u"Storage usage:", None))
        self.label_storage_usage_value.setText(QCoreApplication.translate("ModelManagement", u"value", None))
    # retranslateUi

