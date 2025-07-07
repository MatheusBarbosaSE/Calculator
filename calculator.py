# Import PySide6 modules and standard libraries
from simpleeval import simple_eval
import sys
from PySide6.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QGridLayout,
    QPushButton, QLineEdit
)
from PySide6.QtGui import QFont, QColor, QPalette, QIcon
from PySide6.QtCore import Qt

# Main calculator class (inherits from QWidget)
class Calculator(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Calculator")
        self.setFixedSize(320, 480)
        self.setWindowIcon(QIcon("calculator.ico"))
        self.setStyleSheet(self.stylesheet())

        self.create_widgets()

# UI styling
    def stylesheet(self):
        return """
        QWidget {
            background-color: #121212;
            color: #FFFFFF;
            font-family: 'Segoe UI';
        }

        QLineEdit {
            background-color: #1E1E1E;
            color: #FFA500;
            border: none;
            padding: 15px;
            font-size: 28px;
            qproperty-alignment: 'AlignRight | AlignVCenter';
        }

        QPushButton {
            background-color: #1E1E1E;
            border: none;
            font-size: 20px;
            color: white;
            border-radius: 8px;
            padding: 20px;
        }

        QPushButton:hover {
            background-color: #333333;
        }

        QPushButton:pressed {
            background-color: #444444;
        }

        QPushButton.op {
            background-color: #FFA500;
            color: black;
        }

        QPushButton.equal {
            background-color: #FF8C00;
            color: black;
        }

        QPushButton.clear {
            color: #FF6347;
        }

        QPushButton.backspace {
            color: #FF6347;
        }
        """

# Create display, buttons and layout
    def create_widgets(self):
        layout = QVBoxLayout()
        self.display = QLineEdit()
        self.display.setReadOnly(True)
        layout.addWidget(self.display)

# Button layout configuration
        buttons = {
            'C': (0, 0, 'clear'),
            '◀': (0, 1, 'backspace'),
            '%': (0, 2, 'op'),
            '/': (0, 3, 'op'),
            '7': (1, 0),
            '8': (1, 1),
            '9': (1, 2),
            '*': (1, 3, 'op'),
            '4': (2, 0),
            '5': (2, 1),
            '6': (2, 2),
            '-': (2, 3, 'op'),
            '1': (3, 0),
            '2': (3, 1),
            '3': (3, 2),
            '+': (3, 3, 'op'),
            '0': (4, 0, '', 1, 2),
            '.': (4, 2),
            '=': (4, 3, 'equal'),
        }

# Add buttons to the grid
        grid = QGridLayout()
        for btn_text, pos in buttons.items():
            row, col = pos[0], pos[1]
            cls = pos[2] if len(pos) > 2 else ''
            rowspan = pos[3] if len(pos) > 3 else 1
            colspan = pos[4] if len(pos) > 4 else 1

            button = QPushButton(btn_text)
            if cls:
                button.setProperty("class", cls)
                button.setObjectName(cls)
                button.setStyleSheet("")
            grid.addWidget(button, row, col, rowspan, colspan)
            button.clicked.connect(self.on_button_clicked)

        layout.addLayout(grid)
        self.setLayout(layout)

# Handle button clicks and perform calculations
    def on_button_clicked(self):
        sender = self.sender()
        text = sender.text()

        if text == "C":
            self.display.clear()
        elif text == "◀":
            current = self.display.text()
            self.display.setText(current[:-1])
        elif text == "=":
            try:
                result = str(simple_eval(self.display.text()))
                self.display.setText(result)
            except Exception:
                self.display.setText("Invalid input")
        else:
            self.display.setText(self.display.text() + text)

# Start the application
if __name__ == "__main__":
    app = QApplication(sys.argv)
    calc = Calculator()
    calc.show()
    sys.exit(app.exec())