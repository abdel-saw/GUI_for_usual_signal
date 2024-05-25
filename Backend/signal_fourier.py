import numpy as np
from numpy import fft 
from Backend.Visualisation import*

class signal_fourier(Visualisation):
    def __init__(self,fsignal):
        self.fsignal=np.fft.fft(fsignal)
        self.freq=np.fft.fftfreq(self.fsignal.size)
        