"""
'adjFonts'

Adjust the font size of UI elements.

by HaoRan Chang, PhD Candidate

Polaris Brain Dynamics Research Group,
Canadian Centre for Behavioural Neuroscience,
Department of Neuroscience, University of Lethbridge,
Lethbridge, Alberta, Canada

2019
"""

from . import gui
from PyQt5 import QtGui

class adjFonts:
    name = "Adjust Font Sizes"
    def __init__(self, parent):
        self.parent = parent
        self.gui = gui.window(self)
        print("adjFonts object instantiated")

    def trigger(self):
        self.gui.show()

    def update(self, fontSize=12):
        widgets = (self.parent.l0.itemAt(i).widget() for i in range(self.parent.l0.count()))
        for x in widgets:
            font = x.font()
            font.setPointSize(fontSize)
            x.setFont(font)
