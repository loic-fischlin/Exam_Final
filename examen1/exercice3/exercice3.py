import sys
import traceback

from PyQt6.QtCore import QLocale, Qt
from PyQt6.QtGui import QDoubleValidator
from PyQt6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QPushButton, \
    QLineEdit
from PyQt6.uic import loadUi
from matplotlib import pyplot as plt
from matplotlib.backends.backend_qtagg import FigureCanvasQTAgg


#cette methode permet d'afficher les stack d'erreur sans devoir executer en mode debug
def qt_exception_hook(exctype, value, tb):
    traceback.print_exception(exctype, value, tb)

class MPLCanvas(FigureCanvasQTAgg):

    is_dirty : bool = False

    def __init__(self):
        # Création de la figure matplotlib
        self.__fig, self.__ax = plt.subplots()
        self.__ax.set_aspect('equal')
        self.__ax.set_xlim(-100, 100)
        self.__ax.set_ylim(-100, 100)
        #appel du constructeur de FigureCanvas avec la fig créée en parametre
        super().__init__(self.__fig)

    def dessinerCarre(self,x,y,taille):
        carre = plt.Rectangle((x,y),taille, taille)
        print("carré imprié:", carre)
        self.__ax.add_patch(carre)
        self.draw()
        self.is_dirty = True


    def effacer(self):
        self.__ax.clear()
        self.__ax.set_aspect('equal')
        self.__ax.set_xlim(-100, 100)
        self.__ax.set_ylim(-100, 100)
        self.draw()



class MainViewEx3(QMainWindow):
    xLineEdit: QLineEdit
    yLineEdit: QLineEdit
    tailleLineEdit: QLineEdit
    matplotlibVerticalLayout: QVBoxLayout
    dessinerCarrePushButton: QPushButton
    effacerPushButton: QPushButton

    def __init__(self):
        super().__init__()
        loadUi("ui/main_view_ex3.ui", self)

        self.canvas = MPLCanvas()
        self.matplotlibVerticalLayout.addWidget(self.canvas)

        self.effacerPushButton.clicked.connect(self.effacer)
        self.dessinerCarrePushButton.clicked.connect(self.dessiner)

        self.validator = QDoubleValidator(0,10,1,self)
        self.tailleLineEdit.setValidator(self.validator)

        self.tailleLineEdit.textChanged.connect(self.update_button_states)
        self.tailleLineEdit.textChanged.connect(self.verifier_taille)


        self.update_button_states()

        self.tailleLineEdit.editingFinished.connect(self.update_button_states)
        self.xLineEdit.editingFinished.connect(self.update_button_states)
        self.yLineEdit.editingFinished.connect(self.update_button_states)
        self.dessinerCarrePushButton.clicked.connect(self.update_button_states)

    def verifier_taille(self,texte):

        etat, _, _ = self.validator.validate(texte, 0)
        if etat == QDoubleValidator.State.Acceptable:
            self.tailleLineEdit.setStyleSheet("background-color: white")
        else:
            self.dessinerCarrePushButton.setEnabled(False)
            self.tailleLineEdit.setStyleSheet("background-color: red;")




    def dessiner(self):
        # print("Je vais dessiner un carré")
        x= float(self.xLineEdit.text())
        y= float(self.yLineEdit.text())
        locale = QLocale()
        taille, _ = locale.toDouble(self.tailleLineEdit.text())
        self.canvas.dessinerCarre(x,y,taille)

    def effacer(self):
        self.canvas.effacer()

    def update_button_states(self):
        if self.xLineEdit.text() !="" and self.yLineEdit.text() !="" and self.tailleLineEdit.text() !="" :
            self.dessinerCarrePushButton.setEnabled(True)

        else:
            self.dessinerCarrePushButton.setEnabled(False)

        self.effacerPushButton.setEnabled(self.canvas.is_dirty)


if __name__ == "__main__":
    # permet d'afficher les stack d'erreur sans devoir executer en mode debug
    sys.excepthook = qt_exception_hook
    app = QApplication(sys.argv)
    main_window = MainViewEx3()

    main_window.show()
    sys.exit(app.exec())
