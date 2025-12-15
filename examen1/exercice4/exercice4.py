import sys
import traceback
from abc import abstractclassmethod

from PyQt6.QtCore import QAbstractListModel, QModelIndex, Qt
from PyQt6.QtWidgets import QApplication, QMainWindow, QDoubleSpinBox, QPushButton, \
    QRadioButton, QListView, QFrame, QComboBox
from PyQt6.uic import loadUi

from examen1.exercice4.velo import Velo, VeloElectrique


#cette methode permet d'afficher les stack d'erreur sans devoir executer en mode debug
def qt_exception_hook(exctype, value, tb):
    traceback.print_exception(exctype, value, tb)

class MainViewEx4(QMainWindow):
    standardRadioButton: QRadioButton
    electriqueRadioButton: QRadioButton
    marqueLineEdit: QDoubleSpinBox
    electriqueComboBox:QComboBox
    electriqueParamFrame:QFrame
    addPushButton:QPushButton
    removePushButton:QPushButton
    veloListView:QListView


    def __init__(self):
        super().__init__()
        loadUi("ui/main_view_ex4.ui", self)

        self.electriqueParamFrame.setEnabled(False)
        self.electriqueParamFrame.setVisible(False)

        self.veloModele = VeloModele([])
        self.veloListView.setModel(self.veloModele)

        self.addPushButton.clicked.connect(self.add_velo)

        self.electriqueRadioButton.clicked.connect(self.manage_electrique)
        self.standardRadioButton.clicked.connect(self.manage_electrique)

    def manage_electrique(self):
        self.electriqueParamFrame.setVisible(self.electriqueRadioButton.isChecked())
        self.electriqueParamFrame.setEnabled(self.electriqueRadioButton.isChecked())


    def add_velo(self):
        marque = self.marqueLineEdit.text()
        nouveau = None

        if self.electriqueRadioButton.isChecked():
            type_assistance = self.electriqueComboBox.currentText()
            nouveau = VeloElectrique(marque, type_assistance)

        else :
            nouveau = Velo(marque)

        self.veloListView.model().add_item(nouveau)


class VeloModele(QAbstractListModel):
    __velos:list[Velo]
    def __init__(self, data):
        super().__init__()
        self.__velos = data

    def rowCount(self, parent = QModelIndex):
        return len(self.__velos)

    def data(self, index, role = 0):
        if not index.isValid():
            return None
        velo = self.__velos[index.row()]
        if role == Qt.ItemDataRole.DisplayRole:  # texte affiché
            return velo.__str__()
        elif role == Qt.ItemDataRole.UserRole:  # objet complet
            return velo
        elif role == Qt.ItemDataRole.ToolTipRole:
            return velo.marque
        return None

    def add_item(self, item):
        self.beginInsertRows(QModelIndex(), self.rowCount(),
        self.rowCount())
        self.__velos.append(item)
        self.endInsertRows()



if __name__ == "__main__":
    # permet d'afficher les stack d'erreur sans devoir executer en mode debug
    sys.excepthook = qt_exception_hook
    app = QApplication(sys.argv)
    main_window = MainViewEx4()

    main_window.show()
    sys.exit(app.exec())
