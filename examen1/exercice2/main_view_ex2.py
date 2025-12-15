
from PyQt6.QtWidgets import QMainWindow, QComboBox, QLineEdit, QSpinBox
from PyQt6.uic import loadUi

from model_ex2 import ModelEx2


class MainViewEx2(QMainWindow):
    __model:ModelEx2
    fonctionComboBox: QComboBox
    valeurLineEdit: QLineEdit
    exposantSpinBox : QSpinBox

    def __init__(self,model):
        super().__init__()
        loadUi("ui/main_view_ex2.ui", self)
        self.__model =model

        self.fonctionComboBox.addItems(self.__model.functions)

        self.exposantSpinBox.setMaximum(10)
        self.exposantSpinBox.setMinimum(-10)
        self.exposantSpinBox.setValue(1)

        self.valeurLineEdit.editingFinished.connect(self.on_value_changed)
        self.fonctionComboBox.currentTextChanged.connect(self.on_fonction_changed)
        self.exposantSpinBox.valueChanged.connect(self.on_exposant_changed)

    def on_value_changed(self):
        self.__model.value = float (self.valeurLineEdit.text())

    def on_fonction_changed(self,value):
        self.__model.selected_function = value

    def on_exposant_changed(self, value):
        self.__model.exposant = value
        # print("changement d'exposant!", value)




