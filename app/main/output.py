from PySide6.QtWidgets import (QGridLayout, QLabel, QWidget, QTextBrowser, QPushButton, QProgressBar)
from PySide6.QtGui import QFont

from faster_whisper import WhisperModel
from app.main.file_selection import FileSelection

class Output(QWidget):

    def __init__(self):
        super().__init__()

        self.__grid_layout = QGridLayout(self)

        self.__label_output = QLabel("Output")
        self.__text_output = QTextBrowser()
        self.__progress_process = QProgressBar()
        self.__button_begin = QPushButton("Begin")
        self.__button_stop = QPushButton("Stop")

        self.__grid_layout.addWidget(self.__label_output, 0, 0, 1, 2)
        self.__grid_layout.addWidget(self.__text_output, 1, 0, 1, 2)
        self.__grid_layout.addWidget(self.__progress_process, 2, 0, 1, 2)
        self.__grid_layout.addWidget(self.__button_begin, 3, 0)
        self.__grid_layout.addWidget(self.__button_stop, 3, 1)

        self.setLayout(self.__grid_layout)

        # Стилизация элементов
        self.__bold_font = QFont()
        self.__bold_font.setBold(True)
        self.__label_output.setFont(self.__bold_font)

        self.__button_begin.clicked.connect(self.transcribe)

    def transcribe(self):
        ass = FileSelection()
        print(ass.get_file())