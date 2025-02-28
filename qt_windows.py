import sys
from PyQt6.QtWidgets import QApplication

from qt_windows.main_window import MainWindow
from qt_windows.utils.logging_config import setup_logging

setup_logging()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
