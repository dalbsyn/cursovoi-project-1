from PySide6.QtWidgets import (QMainWindow, QWidget,
    QGridLayout, QLabel, QPushButton, QLineEdit, QComboBox, QCheckBox, QTextBrowser,
    QProgressBar, QHBoxLayout, QMenu)

import app.model_management.main
import app.reference.main

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


class ProcessSettings(QWidget):
    """В данном классе определяются виджеты для настроек обработки - выбор
    модели, языка, устройства обработки (обычно ЦП или ГП), квантизации и
    варианта вывода распознанной речи - с временной меткой или без.
    """

    def __init__(self):
        super().__init__()

        self.__grid_layout = QGridLayout(self)

        # __label_process_settings = QLabel("Process settings")
        self.__label_model = QLabel("Model")
        self.__label_language = QLabel("Language")
        self.__label_device = QLabel("Device")
        self.__label_quantization = QLabel("Quantization")

        self.__combo_model = QComboBox()
        self.__combo_language = QComboBox()
        self.__combo_device = QComboBox()
        self.__combo_quantization = QComboBox()

        self.__check_timestamp = QCheckBox("Insert timestamp beside every line of output")

        self.__label_list = (self.__label_model,
                             self.__label_language,
                             self.__label_device,
                             self.__label_quantization)
        
        self.__combo_list = (self.__combo_model,
                             self.__combo_language,
                             self.__combo_device,
                             self.__combo_quantization)

        # grid_layout.addWidget(__label_process_settings)
        
        for i in range(0, len(self.__label_list)):
            self.__grid_layout.addWidget(self.__label_list[i], i, 0)
        
        for i in range(0, len(self.__combo_list)):
            self.__grid_layout.addWidget(self.__check_timestamp, len(self.__label_list)+1, 0)

        self.setLayout(self.__grid_layout)


class ProcessValues(QWidget):
    """В данном классе определяются виджеты, которые показывают выбранные
    значения в настройках, а также дополнительная характеристика в виде
    оперативной памяти.
    """

    def __init__(self):
        super().__init__()

        self.__grid_layout = QGridLayout(self)

        self.__label_selected_language = QLabel("Selected language:")
        self.__label_selected_model = QLabel("Selected model:")
        self.__label_selected_device = QLabel("Selected device:")
        self.__label_selected_quantization = QLabel("Selected quantization:")
        self.__label_selected_timestamp = QLabel("Timestamp:")
        self.__label_available_ram_vram = QLabel("Available RAM/VRAM:")

        self.__label_value_selected_language = QLabel("value")
        self.__label_value_selected_model = QLabel("value")
        self.__label_value_selected_device = QLabel("value")
        self.__label_value_selected_quantization = QLabel("value")
        self.__label_value_selected_timestamp = QLabel("value")
        self.__label_value_available_ram_vram = QLabel("value")

        __label_list = (self.__label_selected_language, 
                        self.__label_selected_model, 
                        self.__label_selected_device, 
                        self.__label_selected_quantization,
                        self.__label_selected_timestamp, 
                        self.__label_available_ram_vram)
        
        __label_value_list = (self.__label_value_selected_language,
                              self.__label_value_selected_model,
                              self.__label_value_selected_device,
                              self.__label_value_selected_quantization,
                              self.__label_value_selected_timestamp,
                              self.__label_value_available_ram_vram)
        
        for i in range(0, len(__label_list)):
            self.__grid_layout.addWidget(__label_list[i], i, 0)

        for i in range(0, len(__label_value_list)):
            self.__grid_layout.addWidget(__label_value_list[i], i, 1)

        self.setLayout(self.__grid_layout)


class LeftSide(QWidget):
    """В данном классе заполняется "левая" часть интерфейса, которая
    ответственна за настройки вводных данных для дальнейшей обработки.
    """

    def __init__(self):
        super().__init__()

        self.__grid_layout = QGridLayout(self)

        self.__file_select = FileSelection()
        self.__process_settings = ProcessSettings()
        self.__process_values = ProcessValues()

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

        self.__menu_model = self.__menubar.addAction("Model management")
        self.__menu_reference = self.__menubar.addAction("Reference")

        self.__menu_model.triggered.connect(app.model_management.main.window)
        self.__menu_reference.triggered.connect(app.reference.main.window)

