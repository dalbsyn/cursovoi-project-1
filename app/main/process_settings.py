from PySide6.QtWidgets import (QGridLayout, QLabel, QLineEdit, QPushButton,
            QComboBox, QCheckBox, QWidget)

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
