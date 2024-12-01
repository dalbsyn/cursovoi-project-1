from PySide6.QtWidgets import (QMainWindow, QWidget,
    QGridLayout, QLabel, QPushButton, QLineEdit, QComboBox, QCheckBox, QTextBrowser,
    QProgressBar, QHBoxLayout, QMenu)

import app.main.file_selection
import app.main.main_window
import app.main.process_settings
import app.main.process_values
import app.main.output

import app.model_management.main
import app.model_management.model_management


class LeftSide(QWidget):
    """В данном классе заполняется "левая" часть интерфейса, которая
    ответственна за настройки вводных данных для дальнейшей обработки.
    """

    def __init__(self):
        super().__init__()

        self.__grid_layout = QGridLayout(self)

        self.__file_select = app.main.file_selection.FileSelection()
        self.__process_settings = app.main.process_settings.ProcessSettings()
        self.__process_values = app.main.process_values.ProcessValues()

        self.__element_list = (self.__file_select,
                               self.__process_settings,
                               self.__process_values)

        for i in range(0, len(self.__element_list)):
            self.__grid_layout.addWidget(self.__element_list[i], i, 0)

        self.setLayout(self.__grid_layout)


class RightSide(QWidget):
    """В данном классе заполняется "правая" часть программы, которая
    ответсвенна за вывод данных, а также за управление текущим состоянием -
    начала или остановки. Показывается прогресс обработки.
    """
    def __init__(self):
        super().__init__()
        self.__grid_layout = QGridLayout(self)

        self.__output = app.main.output.Output()

        self.__grid_layout.addWidget(self.__output)
        self.setLayout(self.__grid_layout)

class WindowMain(QMainWindow):
    def __init__(self):
        super().__init__()
        
        self.__central_widget = QWidget()
        self.setCentralWidget(self.__central_widget)

        self.__main_layout = QHBoxLayout(self.__central_widget)

        self.__right_side = RightSide()
        self.__left_side = LeftSide()

        self.__main_layout.addWidget(self.__left_side, 0)
        self.__main_layout.addWidget(self.__right_side, 1)

        self.setWindowTitle("Transcriptor 9999")

        self.__menubar = self.menuBar()
        self.setMenuBar(self.__menubar)

        self.__menubar.addAction("Model management")
        self.__menubar.addAction("Reference")

        self.__menubar.triggered.connect(app.model_management.main.window)
