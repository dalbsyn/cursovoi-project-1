from PySide6.QtWidgets import (QGridLayout, QLabel, QWidget)
from PySide6.QtGui import QFont

class ProcessValues(QWidget):
    """В данном классе определяются виджеты, которые показывают выбранные
    значения в настройках, а также дополнительная характеристика в виде
    оперативной памяти.
    """

    def __init__(self):
        super().__init__()

        self.__grid_layout = QGridLayout(self)

        self.__label_process_settings = QLabel("Process values")
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

        self.__label_list = (self.__label_process_settings,
                             self.__label_selected_language,
                             self.__label_selected_model,
                             self.__label_selected_device,
                             self.__label_selected_quantization,
                             self.__label_selected_timestamp,
                             self.__label_available_ram_vram)
        
        self.__label_value_list = (self.__label_value_selected_language,
                              self.__label_value_selected_model,
                              self.__label_value_selected_device,
                              self.__label_value_selected_quantization,
                              self.__label_value_selected_timestamp,
                              self.__label_value_available_ram_vram)
        
        for i in range(0, len(self.__label_list)):
            self.__grid_layout.addWidget(self.__label_list[i], i, 0)

        for i in range(0, len(self.__label_value_list)):
            self.__grid_layout.addWidget(self.__label_value_list[i], i+1, 1)

        self.setLayout(self.__grid_layout)

        # Стилизация элементов
        self.__bold_font = QFont()
        self.__bold_font.setBold(True)
        self.__label_process_settings.setFont(self.__bold_font)
