from gui import CodeforcesProblemFilterApp
from PyQt5.QtWidgets import QApplication
import sys


def main():
    app = QApplication(sys.argv)
    window = CodeforcesProblemFilterApp()
    window.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
