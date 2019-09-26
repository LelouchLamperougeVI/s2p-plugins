import sys
from PyQt5.QtWidgets import *

class window(QWidget):
    black = '#000000'
    red = '#FF1100'
    fs_ph = 'framerate (Hz)'
    kernel_ph = 'kernel length (sec)'
    modes = {'smooth + dF/F': 0,
            'smooth': 1,
            'dF/F': 2}
    smooth_types = {'median': 'win = ',
                    'Gaussian': 'sigma = ',
                    'mean': 'win = '}
    dial_sstep = 1
    dial_pstep = 10 # this is also the multiplication factor
    dial_range = 500

    def __init__(self, parent):
        super().__init__()
        self.sigma = 0.0
        self.active = False
        self.mode = next(iter(window.modes))
        self.type = next(iter(window.smooth_types))
        self.parent = parent
        self.init_ui()

    def init_ui(self):
        self.setGeometry(300, 300, 300, 200)
        self.setWindowTitle('Smooth dF/F')

        grid = QGridLayout()
        self.setLayout(grid)

        label = QLabel('Mode: ', self)
        grid.addWidget(label, *(1,1))

        modes_list = QComboBox(self)
        modes_list.addItems(window.modes.keys())
        grid.addWidget(modes_list, *(1,2))

        label = QLabel('smoothing kernel: ', self)
        grid.addWidget(label, *(2,1))

        types_list = QComboBox(self)
        types_list.addItems(window.smooth_types.keys())
        grid.addWidget(types_list, *(2,2))

        Fs = QLineEdit(self)
        Fs.setPlaceholderText(window.fs_ph)
        grid.addWidget(Fs, *(3,1))

        win = QLineEdit(self)
        win.setPlaceholderText(window.kernel_ph)
        grid.addWidget(win, *(3,2))

        sig_disp = QLabel(window.smooth_types[types_list.currentText()] + str(self.sigma), self)
        grid.addWidget(sig_disp, *(4,1))

        dial = QDial(self)
        dial.setRange(0, window.dial_range)
        dial.setSingleStep(window.dial_sstep)
        dial.setPageStep(window.dial_pstep)
        dial.setSliderPosition(0)
        grid.addWidget(dial, *(4,2))

        on_button = QPushButton('status: Off', self)
        on_button.setCheckable(True)
        grid.addWidget(on_button, *(5,2))

        # signal/slots
        on_button.toggled[bool].connect(lambda state: on_button.setText('status: On') if state else on_button.setText('status: Off'))
        on_button.toggled[bool].connect(lambda state: self.set_status(state))
        on_button.toggled[bool].connect(lambda state: self.parent.activate() if state else self.parent.deactivate())
        modes_list.currentTextChanged[str].connect(lambda txt: self.set_mode(txt))
        types_list.currentTextChanged[str].connect(lambda txt: sig_disp.setText(window.smooth_types[txt] + str(self.sigma)))
        types_list.currentTextChanged[str].connect(lambda txt: self.set_type(txt))
        Fs.returnPressed.connect(lambda: win.setText(str( self.sigma / float(Fs.text()) )) if Fs.text() not in window.fs_ph else False)
        win.returnPressed.connect(lambda: dial.setValue(int( float(Fs.text()) * float(win.text()) ) * window.dial_pstep) if Fs.text() not in window.fs_ph else False)
        win.returnPressed.connect(lambda: sig_disp.setText(window.smooth_types[types_list.currentText()] + str(self.set_sigma(float(Fs.text()) * float(win.text())))) if Fs.text() not in window.fs_ph else False)
        dial.valueChanged[int].connect(lambda value: sig_disp.setText(window.smooth_types[types_list.currentText()] + str(self.set_sigma(value/10.0))))
        dial.valueChanged[int].connect(lambda value: win.setText(str( dial.value() / window.dial_pstep / float(Fs.text()) )) if Fs.text() not in window.fs_ph else False)

    def flip_colour(self, obj):
        obj.setStyleSheet('color: ' + window.black) if window.red in obj.styleSheet() else obj.setStyleSheet('color: ' + window.red)

    def set_sigma(self, sigma):
        self.sigma = sigma
        return self.sigma

    def set_mode(self, txt):
        self.mode = txt
        return self.mode

    def set_type(self, txt):
        self.type = txt
        return self.type

    def set_status(self, active):
        self.active = active
