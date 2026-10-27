import sys

from PySide6.QtWidgets import QApplication, QLabel, QMainWindow


def main() -> int:
    app = QApplication(sys.argv)

    window = QMainWindow()
    window.setWindowTitle("My RPG")
    window.resize(1000, 700)

    label = QLabel("Welcome to your RPG!")
    label.setStyleSheet("font-size: 20px; padding: 20px;")

    window.setCentralWidget(label)
    window.show()

    return app.exec()


if __name__ == "__main__":
    sys.exit(main())