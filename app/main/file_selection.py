from PySide6.QtWidgets import (QGridLayout, QLabel, QLineEdit, QPushButton,
                               QWidget, QFileDialog)
from PySide6.QtGui import QFont


class FileSelection(QWidget):
    """В данном классе определяются виджеты для реализации части выбора файла.
    """

    def __init__(self):
        super().__init__()

        self.__grid_layout = QGridLayout(self)

        # Определение элементов интерфейса
        self.__label_file_selection = QLabel("Select file")
        self.__line_file_selection = QLineEdit()
        self.__button_file_selection = QPushButton("Select file")
        
        # Добавление элементов интерфейса
        self.__grid_layout.addWidget(self.__label_file_selection, 0, 0)
        self.__grid_layout.addWidget(self.__line_file_selection, 1, 0)
        self.__grid_layout.addWidget(self.__button_file_selection, 1, 1)

        self.setLayout(self.__grid_layout)

        # Стилизация элементов
        self.__bold_font = QFont()
        self.__bold_font.setBold(True)
        self.__label_file_selection.setFont(self.__bold_font)

        self.__button_file_selection.clicked.connect(self.open_file)
    
    def open_file(self):
        self.__file_dialog = QFileDialog.getOpenFileName()
        self.__line_file_selection.setText(self.__file_dialog[0])
        print(self.__line_file_selection.displayText())
    
    def get_file(self):
        return self.__line_file_selection.displayText()

