from PySide6.QtWidgets import (QGridLayout, QLabel, QLineEdit, QPushButton,
            QComboBox, QCheckBox, QWidget)
from PySide6.QtGui import QFont

import faster_whisper.utils
import faster_whisper.tokenizer


class ProcessSettings(QWidget):
    """В данном классе определяются виджеты для настроек обработки - выбор
    модели, языка, устройства обработки (обычно ЦП или ГП), квантизации и
    варианта вывода распознанной речи - с временной меткой или без.
    """

    def __init__(self):
        super().__init__()

        self.__grid_layout = QGridLayout(self)

        self.__label_process_settings = QLabel("Process settings")
        self.__label_model = QLabel("Model")
        self.__label_language = QLabel("Language")
        self.__label_device = QLabel("Device")
        self.__label_quantization = QLabel("Quantization")

        self.combo_model = QComboBox()
        self.__combo_language = QComboBox()
        self.__combo_device = QComboBox()
        self.__combo_quantization = QComboBox()

        self.__check_timestamp = QCheckBox("Insert timestamp beside every line of output")

        self.__label_list = (self.__label_process_settings,
                             self.__label_model,
                             self.__label_language,
                             self.__label_device,
                             self.__label_quantization)
        
        self.__combo_list = (self.combo_model,
                             self.__combo_language,
                             self.__combo_device,
                             self.__combo_quantization)

        self.__grid_layout.addWidget(self.__label_process_settings)
        
        for i in range(0, len(self.__label_list)):
            self.__grid_layout.addWidget(self.__label_list[i], i, 0)
        
        for i in range(0, len(self.__combo_list)):
            self.__grid_layout.addWidget(self.__combo_list[i], i+1, 1)

        self.setLayout(self.__grid_layout)

        # Стилизация элементов
        self.__bold_font = QFont()
        self.__bold_font.setBold(True)
        self.__label_process_settings.setFont(self.__bold_font)

        for i in faster_whisper.utils._MODELS:
            self.combo_model.addItem(i)

        for i in faster_whisper.tokenizer._LANGUAGE_CODES:
            self.__combo_language.addItem(i)

    def get_model(self):
        a = self.combo_model.currentText()
        return a