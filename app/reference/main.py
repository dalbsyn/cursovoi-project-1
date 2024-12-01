from PySide6.QtWidgets import (QDialog, QWidget,
    QGridLayout, QLabel, QTextBrowser, QListWidget)


class Leftside(QWidget):
    def __init__(self):
        super().__init__()

        self.__grid_layout = QGridLayout(self)

        self.__label_elements = QLabel("Elements")
       
        self.__list_elements = QListWidget()

        self.__grid_layout.addWidget(self.__label_elements, 0, 0)
        self.__grid_layout.addWidget(self.__list_elements, 1, 0)

class RightSide(QWidget):
    def __init__(self):
        super().__init__()
        self.__grid_layout = QGridLayout(self)
        
        self.__label_element_info = QLabel("Information about selected element")
        self.__text_element_information = QTextBrowser()

        self.__grid_layout.addWidget(self.__label_element_info, 0, 0)
        self.__grid_layout.addWidget(self.__text_element_information, 1, 0)

class DialogReference(QDialog):
    def __init__(self):
        super().__init__()

        self.__central_widget = QGridLayout(self)

        self.__left_side = Leftside()
        self.__right_side = RightSide()

        self.__central_widget.addWidget(self.__left_side, 0, 0)
        self.__central_widget.addWidget(self.__right_side, 0, 1)

def window():
    app = DialogReference()
    app.exec()

    