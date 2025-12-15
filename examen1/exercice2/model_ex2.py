import sympy as sp
from PyQt6.QtCore import QObject, pyqtSignal


class ModelEx2(QObject):

    __functions:list[str]
    __selected_function:str
    __value:float
    __exposant: int

    model_changed = pyqtSignal(object, float, int)
    
    def __init__(self):
        super().__init__()
        self.__variable = sp.symbols("x")
        self.__functions = ["sin(x)", "cos(x)", "log(x)", "exp(x)"]
        self.__selected_function: str = "sin(x)"
        self.__value = 0
        self.__exposant = 1


    @property
    def exposant(self):
        return self.__exposant

    @exposant.setter
    def exposant(self,value):
        self.__exposant = value
        self.emit_signal_modele_changed()

    @property
    def functions(self):
        return self.__functions

    @functions.setter
    def functions(self, value):
        self.__functions = value
        self.emit_signal_modele_changed()

    @property
    def selected_function(self):
        return self.__selected_function

    @selected_function.setter
    def selected_function(self, value):
        self.__selected_function = value
        # print(self.selected_function)
        self.emit_signal_modele_changed()

    @property
    def value(self):
        return self.__value
    
    @value.setter
    def value(self, value):
        self.__value= value
        # print(self.__value)
        self.emit_signal_modele_changed()


    def emit_signal_modele_changed(self):
        if self.selected_function is not None and self.value is not None and self.exposant is not None:
            valeur = self.value
            fonction_sp = sp.sympify(self.selected_function)
            fonction = sp.lambdify(self.__variable, fonction_sp, "numpy")
            exposant =self.exposant
            # print(valeur,fonction)

            self.model_changed.emit(fonction, valeur, exposant)
