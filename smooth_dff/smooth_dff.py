"""
'smooth_dff'

This is my first attempt at making a plugin for MouseLand/suite2p.
Tool for plotting smooth fluorescent traces (as in old MATLAB version).

by HaoRan Chang, PhD Candidate

Polaris Brain Dynamics Research Group,
Canadian Centre for Behavioural Neuroscience,
Department of Neuroscience, University of Lethbridge,
Lethbridge, Alberta, Canada

2019
"""

from . import gui
from scipy.signal import medfilt
from scipy.ndimage import gaussian_filter1d as gaussfilt
import numpy as np

modes = gui.window.modes.keys()
types = gui.window.smooth_types.keys()

class smooth_dff:
    name = "Smooth dF/F" # name displayed in plugin menu sub-item
    def __init__(self, parent):
        self.parent = parent # keep parent
        self.gui = gui.window(self)
        print("smooth_dff object instantiated")

    def trigger(self):
        self.gui.show()

    def smooth(self, signal):
        if self.gui.type == 'median':
            return medfilt(signal, (1, round(self.gui.sigma) + round(self.gui.sigma + 1) % 2))
        elif self.gui.type == 'Gaussian':
            return gaussfilt(signal, self.gui.sigma)
        else:
            return np.convolve(signal, np.ones(round(self.gui.sigma))/round(self.gui.sigma), mode='same')

    def activate(self):
        self.original_Fcell = self.parent.Fcell
        self.original_Fneu = self.parent.Fneu
        self.original_Spks = self.parent.Spks

        self.parent.Fcell = self.smooth(self.parent.Fcell)
        self.parent.Fneu = self.smooth(self.parent.Fneu)
        self.parent.Spks = self.smooth(self.parent.Spks)

    def deactivate(self):
        self.parent.Fcell = self.original_Fcell
        self.parent.Fneu = self.original_Fneu
        self.parent.Spks = self.original_Spks
