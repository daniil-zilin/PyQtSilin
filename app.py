import sys
from PyQt5.QtCore import QPoint
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QWidget, QLabel, QTextEdit, QLineEdit, QGridLayout
from PyQt5.QtGui import QPainter, QColor, QBrush


class SnowmanWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Второе окно")
        self.setGeometry(100, 300, 450, 375)

        self.colorInput = QLineEdit(self)
        self.colorInput.setPlaceholderText("Цвет снеговика")

        self.hatWidthInput = QLineEdit(self)
        self.hatWidthInput.setPlaceholderText("Ширина шляпы")

        self.hatHeightInput = QLineEdit(self)
        self.hatHeightInput.setPlaceholderText("Высота шляпы")

        drawButton = QPushButton("Нарисовать снеговика")
        drawButton.clicked.connect(self.update)

        gridLayout = QGridLayout()

        gridLayout.addWidget(self.colorInput, 0, 0)
        gridLayout.addWidget(self.hatWidthInput, 0, 1)
        gridLayout.addWidget(self.hatHeightInput, 0, 2)
        gridLayout.addWidget(drawButton, 0, 3)

        gridLayout.setRowStretch(1, 1)

        container = QWidget()
        container.setLayout(gridLayout)
        self.setCentralWidget(container)

    def paintEvent(self, event):
        painter = QPainter(self)

        snowmanColor = self.colorInput.text() or "white"
        brush = QBrush(QColor(snowmanColor))
        painter.setBrush(brush)

        painter.drawEllipse(160, 220, 100, 100)
        painter.drawEllipse(180, 150, 70, 70)
        painter.drawEllipse(190, 100, 50, 50)

        painter.setBrush(QBrush(QColor(0, 0, 0)))
        painter.drawEllipse(205, 115, 5, 5)
        painter.drawEllipse(220, 115, 5, 5)

        painter.setBrush(QBrush(QColor(255, 165, 0)))
        painter.drawPolygon([QPoint(220, 125), QPoint(240, 120), QPoint(220, 130)])

        hatWidth = int(self.hatWidthInput.text()) if self.hatWidthInput.text().isdigit() else 40
        hatHeight = int(self.hatHeightInput.text()) if self.hatHeightInput.text().isdigit() else 10

        painter.setBrush(QBrush(QColor(0, 0, 0)))
        painter.drawRect(210 - hatWidth // 2, 80, hatWidth, hatHeight)
        painter.drawRect(200 - hatWidth // 2, 90, hatWidth + 20, 10)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Основное окно")
        self.setGeometry(100, 100, 400, 300)

        button = QPushButton("Открыть второе окно")
        button.clicked.connect(self.openSnowmanWindow)

        self.textEdit = QTextEdit(self)
        self.label = QLabel("Текст", self)

        changeLabelButton = QPushButton('Изменить Заголовок')
        changeLabelButton.clicked.connect(self.changeLabelText)

        gridLayout = QGridLayout()

        gridLayout.addWidget(self.label, 0, 0)
        gridLayout.addWidget(changeLabelButton, 1, 0)
        gridLayout.addWidget(self.textEdit, 2, 0)
        gridLayout.addWidget(button, 3, 0)

        gridLayout.setRowStretch(4, 1)

        container = QWidget()
        container.setLayout(gridLayout)
        self.setCentralWidget(container)

    def openSnowmanWindow(self):
        self.snowmanWindow = SnowmanWindow()
        self.snowmanWindow.show()

    def changeLabelText(self):
        text = self.textEdit.toPlainText()
        self.label.setText(text)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    mainWindow = MainWindow()
    mainWindow.show()
    sys.exit(app.exec_())
