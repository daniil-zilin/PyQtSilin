import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget, QLabel, QTextEdit
from PyQt5.QtGui import QPainter, QColor, QBrush


class SecondWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Второе окно")
        self.setGeometry(100, 100, 400, 300)

    def paintEvent(self, event):
        painter = QPainter(self)
        brush = QBrush(QColor(255, 255, 255))
        painter.setBrush(brush)

        layout = QVBoxLayout()

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Основное окно")
        self.setGeometry(100, 100, 400, 300)

        button = QPushButton("Открыть второе окно")
        button.resize(50, 50)
        button.clicked.connect(self.openSecondWindow)

        self.textEdit = QTextEdit(self)
        self.label = QLabel("Текст", self)

        changeLabelButton = QPushButton('Изменить Заголовок')
        changeLabelButton.clicked.connect(self.changeLabelText)

        layout = QVBoxLayout()
        layout.addWidget(button)
        layout.addWidget(self.label)
        layout.addWidget(changeLabelButton)
        layout.addWidget(self.textEdit)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

    def openSecondWindow(self):
        self.second_window = SecondWindow()
        self.second_window.show()

    def changeLabelText(self):
        text = self.textEdit.toPlainText()
        self.label.setText(text)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec_())
