from Backend.Visualisation import *
from math import*
import numpy as np
class signal_sinuso(Visualisation):
    #cette classe récupère les paramètres pour représenter un signal sinusoïdal
    def __init__(self,amplitude,tmax,freq):
        self.amplitude=amplitude
        self.amplitude=int(self.amplitude)
        self.Tmax=tmax
        self.Tmax=int(self.Tmax)
        self.freq=freq
        self.freq=int(self.freq)
        self.interval=np.linspace(0,self.Tmax,200)
        self.signal=[(self.amplitude*cos(2*pi*self.freq*t))for t in self.interval]
    