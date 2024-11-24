from PySide6.QtWidgets import (QDialog, QWidget,
    QGridLayout, QLabel, QPushButton,
    QProgressBar, QHBoxLayout, QListWidget, QApplication)
from PySide6.QtGui import QFont

class LeftSide(QWidget):
    def __init__(self):
        super().__init__()

        self.__grid_layout = QGridLayout(self)

        self.__label_models = QLabel("Models")
        font = QFont()
        font.setBold(True)
        self.__label_models.setFont(font)

        self.__list_models = QListWidget()

        self.__grid_layout.addWidget(self.__label_models, 0, 0)
        self.__grid_layout.addWidget(self.__list_models, 1, 0)


class RightSide(QWidget):
    def __init__(self):
        super().__init__()

        self.__grid_layout = QGridLayout(self)

        self.__label_model_info = QLabel("About model")
        font = QFont()
        font.setBold(True)
        self.__label_model_info.setFont(font)

        self.__model_name = Field("Model name:", "value")
        self.__memory_usage = Field("Memory usage:", "value")
        self.__storage_usage = Field("Storage usage:", "value")

        self.__field_list = (self.__model_name, 
                             self.__memory_usage, 
                             self.__storage_usage)
        
        self.__grid_layout.addWidget(self.__label_model_info)
        
        for i, field in enumerate(self.__field_list, start=1):
            self.__grid_layout.addWidget(field, i, 0)

        self.__progress_download = QProgressBar()
        self.__button_download = QPushButton("Download")
        self.__button_delete = QPushButton("Delete")

        self.__grid_layout.addWidget(self.__progress_download, int(self.__grid_layout.rowCount())+1, 0, 1, 2)
        self.__grid_layout.addWidget(self.__button_download, int(self.__grid_layout.rowCount())+1, 0)
        self.__grid_layout.addWidget(self.__button_delete, int(self.__grid_layout.rowCount())-1, 1)


class Field(QWidget):
    def __init__(self, name, value):
        super().__init__()

        self.__grid_layout = QHBoxLayout(self)

        self.__grid_layout.setContentsMargins(0, 0, 0, 0)

        self.__label_name = QLabel(name)
        self.__label_value_name = QLabel(value)

        self.__grid_layout.addWidget(self.__label_name, 0)
        self.__grid_layout.addWidget(self.__label_value_name, 1)

        
class DialogModelManagement(QDialog):
    def __init__(self):
        super().__init__()

        self.__central_widget = QGridLayout(self)
        
        self.__a = LeftSide()
        self.__b = RightSide()
        self.__central_widget.addWidget(self.__a, 0, 0)
        self.__central_widget.addWidget(self.__b, 0, 1)

def window():
    app2 = DialogModelManagement()
    app2.exec()
