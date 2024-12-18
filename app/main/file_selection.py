from PySide6.QtWidgets import (QGridLayout, QLabel, QLineEdit, QPushButton, QWidget)

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