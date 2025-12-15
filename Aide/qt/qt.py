import sys
import traceback

from PyQt6.QtCore import Qt, QStringListModel
from PyQt6.QtGui import QDoubleValidator, QColor
from PyQt6.QtWidgets import QMainWindow, QApplication, QLineEdit, QComboBox, QLCDNumber, QPushButton, QFrame, QSpinBox, \
    QSlider, QListView, QRadioButton, QCheckBox, QProgressBar, QMessageBox, QColorDialog
from PyQt6.uic import loadUi

from examen1.exercice3.exercice3 import MainViewEx3


class MainView(QMainWindow):
    lineEdit : QLineEdit
    comboBox : QComboBox
    lcdNumber : QLCDNumber
    pushButton : QPushButton
    frame : QFrame
    spinBox : QSpinBox
    horizontalSlider : QSlider
    listView : QListView
    radioButton : QRadioButton
    checkBox: QCheckBox
    progressBar: QProgressBar

    def __init__(self):
        super().__init__()
        loadUi("test.ui", self)

        #lineEdit
        self.lineEdit.setText("Bonjour")
        texte = self.lineEdit.text()
        self.lineEdit.textChanged.connect(self.ma_fonction)
        self.lineEdit.editingFinished.connect(self.ma_fonction)
        self.lineEdit.setPlaceholderText("Texte en fond")
        self.lineEdit.setEnabled(True)
        #validator: doit se faire appeler au changement de texte
        self.double_validator = QDoubleValidator(0.0, 100.0, 2, self)  # min=0, max=100
        self.lineEdit.setValidator(self.double_validator)
        etat, _, _ = self.double_validator.validate(texte, 0)
        if etat == QDoubleValidator.State.Acceptable:
            self.lineEdit.setStyleSheet("background-color: white;")  # valeur correcte → fond blanc
        else:
            self.lineEdit.setStyleSheet("background-color: red;")  # valeur incorrecte → fond rouge

        #comboBox
        self.comboBox.addItem("Rouge")
        self.comboBox.addItems(["Jaune", "Bleu", "Vert"])
        texte = self.comboBox.currentText()
        index = self.comboBox.currentIndex()
        self.comboBox.currentIndexChanged.connect(self.ma_fonction)
        self.comboBox.currentTextChanged.connect(self.ma_fonction)
        self.comboBox.setCurrentText("Vert") # valeur par défaut
        self.comboBox.setPlaceholderText("Choisissez une option")
        self.lineEdit.setEnabled(True)

        # lcdNumber
        self.lcdNumber.display(12.34)  # afficher une valeur
        self.lcdNumber.display("123")  # possible aussi avec une chaîne numérique
        valeur = self.lcdNumber.value()  # récupérer la valeur affichée
        self.lcdNumber.setDigitCount(6)  # nombre de chiffres affichés
        self.lcdNumber.setMode(QLCDNumber.Mode.Dec)  # Dec, Hex, Bin, Oct
        self.lcdNumber.setSegmentStyle(QLCDNumber.SegmentStyle.Filled) # autres styles : Flat, Outline
        self.lcdNumber.setEnabled(True)
        self.lineEdit.textChanged.connect(self.lcdNumber.display)

        # pushButton
        self.pushButton.setText("Valider")  # texte du bouton
        texte = self.pushButton.text()  # lire le texte
        self.pushButton.setEnabled(True)  # activer / désactiver
        self.pushButton.setCheckable(True)  # bouton à deux états (ON/OFF)
        etat = self.pushButton.isChecked()  # savoir si le bouton est coché
        self.pushButton.clicked.connect(self.ma_fonction)  # clic simple
        self.pushButton.pressed.connect(self.ma_fonction)  # bouton pressé
        self.pushButton.released.connect(self.ma_fonction)  # bouton relâché
        self.pushButton.toggled.connect(self.ma_fonction)  # si checkable

        # QFrame
        self.frame.setFrameShape(QFrame.Shape.Box)  # type de bordure : Box, Panel, HLine, VLine, StyledPanel
        self.frame.setFrameShadow(QFrame.Shadow.Raised)  # effet d’ombre : Raised, Sunken, Plain
        self.frame.setLineWidth(2)  # largeur de la bordure
        self.frame.setMidLineWidth(1)  # largeur de la ligne médiane (si applicable)
        self.frame.setEnabled(True)  # activer / désactiver
        self.frame.setVisible(True)  # afficher / cacher
        self.frame.setStyleSheet("background-color: lightgray; border: 2px solid black;")

        # QSpinBox
        self.spinBox.setValue(5)  # valeur initiale
        valeur = self.spinBox.value()  # récupérer la valeur
        self.spinBox.setRange(0, 100)  # définir min et max
        self.spinBox.setMinimum(0)  # minimum
        self.spinBox.setMaximum(100)  # maximum
        self.spinBox.setSingleStep(1)  # pas de variation à chaque clic
        self.spinBox.setEnabled(True)
        self.spinBox.valueChanged.connect(self.ma_fonction)  # déclenché à chaque changement
        self.spinBox.editingFinished.connect(self.ma_fonction)  # déclenché quand l’édition se termine

        # QSlider horizontal
        self.horizontalSlider.setOrientation(Qt.Orientation.Horizontal)  # orientation
        self.horizontalSlider.setMinimum(0)  # valeur minimum
        self.horizontalSlider.setMaximum(100)  # valeur maximum
        self.horizontalSlider.setValue(50)  # valeur initiale
        self.horizontalSlider.setSingleStep(1)  # incrément pour flèches clavier
        self.horizontalSlider.setPageStep(10)  # incrément pour clic dans la barre
        self.horizontalSlider.setEnabled(True)  # activer / désactiver
        self.horizontalSlider.setVisible(True)  # afficher / cacher
        self.horizontalSlider.valueChanged.connect(self.ma_fonction)  # déclenché à chaque changement de valeur
        self.horizontalSlider.sliderPressed.connect(self.ma_fonction)  # déclenché quand le curseur est pressé
        self.horizontalSlider.sliderReleased.connect(self.ma_fonction)  # déclenché quand le curseur est relâché

        # QListView
        self.listView.setEnabled(True)  # activer / désactiver
        self.listView.setVisible(True)  # afficher / cacher
        self.listView.setSelectionMode(
        self.listView.SelectionMode.SingleSelection)  # mode de sélection : Single, Multi, Extended
        self.model = QStringListModel()
        self.listView.setModel(self.model)
        self.model.setStringList(["Item 1", "Item 2", "Item 3"])  # remplir la liste
        index = self.listView.currentIndex()
        texte = index.data()
        self.listView.clicked.connect(self.ma_fonction)  # clic sur un élément
        self.listView.activated.connect(self.ma_fonction)  # double-clic ou Enter

        # QRadioButton
        self.radioButton.setText("Option 1")  # texte affiché
        texte = self.radioButton.text()  # lire le texte
        self.radioButton.setChecked(True)  # sélectionner le bouton
        etat = self.radioButton.isChecked()  # savoir si le bouton est sélectionné
        self.radioButton.setEnabled(True)  # activer / désactiver
        self.radioButton.setVisible(True)  # afficher / cacher
        self.radioButton.toggled.connect(self.ma_fonction)  # déclenché quand l’état change
        self.radioButton.clicked.connect(self.ma_fonction)  # déclenché à chaque clic

        # QCheckBox
        self.checkBox.setText("Option 1")  # texte affiché
        texte = self.checkBox.text()  # lire le texte
        self.checkBox.setChecked(True)  # cocher / décocher
        etat = self.checkBox.isChecked()  # savoir si coché
        self.checkBox.setEnabled(True)  # activer / désactiver
        self.checkBox.setVisible(True)  # afficher / cacher
        self.checkBox.toggled.connect(self.ma_fonction)  # déclenché quand l’état change
        self.checkBox.stateChanged.connect(self.ma_fonction)  # déclenché à chaque changement de l’état

        # QProgressBar
        self.progressBar.setMinimum(0)  # valeur minimum
        self.progressBar.setMaximum(100)  # valeur maximum
        self.progressBar.setValue(50)  # valeur actuelle
        valeur = self.progressBar.value()  # récupérer la valeur actuelle
        self.progressBar.setFormat("%p%")  # format affiché (ex: "50%")
        self.progressBar.setTextVisible(True)  # afficher ou cacher le texte
        self.progressBar.setEnabled(True)  # activer / désactiver
        self.progressBar.setVisible(True)  # afficher / cacher

        #MessageBox
        msg_box = QMessageBox()
        msg_box.setWindowTitle("Attention")
        msg_box.setText("Voulez-vous vraiment quitter ?")
        msg_box.setIcon(QMessageBox.Icon.Warning) #Icone de la boîte (Information, Warning, Critical, Question)
        msg_box.setStandardButtons(QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)
        msg_box.show()

        #QFileDialog
        # from PyQt6.QtWidgets import QFileDialog
        #
        # nom_fichier, _ = QFileDialog.getOpenFileName(
        #     self,
        #     "Ouvrir un fichier",
        #     "",
        #     "Fichiers texte (*.txt);;Tous les fichiers (*)"
        # )
        # if nom_fichier:
        #     print("Fichier choisi :", nom_fichier)
        #
        # nom_fichier, _ = QFileDialog.getSaveFileName(
        #     self,
        #     "Enregistrer sous",
        #     "",
        #     "Fichiers texte (*.txt);;Tous les fichiers (*)"
        # )
        # if nom_fichier:
        #     print("Fichier à enregistrer :", nom_fichier)

        #QColorDialog
        couleur = QColorDialog.getColor(initial=QColor(255, 0, 0), parent=self, title="Choisir une couleur")

        if couleur.isValid():
            print("Couleur choisie :", couleur.name())  # code hex, ex: "#ff0000"
            self.lineEdit.setStyleSheet(f"background-color: {couleur.name()}")

    def ma_fonction(self):
        return

    #@props pour créer getter et setter rapidement


if __name__ == "__main__":
    # permet d'afficher les stack d'erreur sans devoir executer en mode debug
    def qt_exception_hook(exctype, value, tb):
        traceback.print_exception(exctype, value, tb)

    app = QApplication(sys.argv)
    main_window = MainView()

    main_window.show()
    sys.exit(app.exec())