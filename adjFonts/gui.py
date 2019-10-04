import sys
from PyQt5.QtWidgets import *

class window(QWidget):
    def __init__(self, parent):
        super().__init__()
        self.fontSize = 12
        self.parent = parent
        self.init_ui()

    def init_ui(self):
        self.setGeometry(300, 300, 300, 200)
        self.setWindowTitle('Adjust font size for UI elements')

        grid = QGridLayout()
        self.setLayout(grid)

        label = QLabel('Font Size: ', self)
        grid.addWidget(label, *(1,1))

        font_txt = QLineEdit(self)
        font_txt.setText(str(self.fontSize))
        grid.addWidget(font_txt, *(1,2))

        font_txt.returnPressed.connect(lambda: self.parent.update(int(font_txt.text())))
