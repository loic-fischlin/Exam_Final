import sys
import traceback

from PyQt6.QtWidgets import QApplication

from model_ex2 import ModelEx2
from secondary_view_ex2 import SecViewEx2
from main_view_ex2 import MainViewEx2

#cette methode permet d'afficher les stack d'erreur sans devoir executer en mode debug
def qt_exception_hook(exctype, value, tb):
    traceback.print_exception(exctype, value, tb)


if __name__ == "__main__":
    # permet d'afficher les stack d'erreur sans devoir executer en mode debug
    sys.excepthook = qt_exception_hook
    app = QApplication(sys.argv)

    model=ModelEx2()
    main_window = MainViewEx2(model)
    sec_window = SecViewEx2(model)

    main_window.show()
    sec_window.show()
    sys.exit(app.exec())
