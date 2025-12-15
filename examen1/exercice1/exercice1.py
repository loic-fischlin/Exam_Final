import sys
import traceback

from PyQt6.QtWidgets import QApplication, QMainWindow
from PyQt6.uic import loadUi

#cette methode permet d'afficher les stack d'erreur sans devoir executer en mode debug
def qt_exception_hook(exctype, value, tb):
    traceback.print_exception(exctype, value, tb)


class MainViewEx1(QMainWindow):

    def __init__(self):
        super().__init__()
        loadUi("ui/main_view_ex1.ui", self)

if __name__ == "__main__":
    # permet d'afficher les stack d'erreur sans devoir executer en mode debug
    sys.excepthook = qt_exception_hook
    app = QApplication(sys.argv)
    window = MainViewEx1()
    window.show()
    sys.exit(app.exec())