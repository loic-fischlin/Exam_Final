from PyQt6.QtWidgets import QWidget, QComboBox, QLineEdit, QLabel
from PyQt6.uic import loadUi


from model_ex2 import ModelEx2


class SecViewEx2(QWidget):
    resultLabel: QLabel

    def __init__(self,model:ModelEx2):
        super().__init__()
        loadUi("ui/sec_view_ex2.ui", self)

        model.model_changed.connect(self.on_model_changed)

    def on_model_changed(self,fonction: object, value: float, exposant: int):
        self.resultLabel.setText(str(fonction(value)**exposant))



