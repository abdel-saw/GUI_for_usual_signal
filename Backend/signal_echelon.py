from math import *
from Backend.Visualisation import *
import numpy as np 

class signal_echelon(Visualisation):
    def __init__(self,ampli,temp_max,temp_debut) :
        self.amplitude=int(ampli)
        self.t=int(temp_max)
        self.t_debut=int(temp_debut)
        self.interval=np.linspace(-self.t,self.t,100)
        self.signal=np.piecewise(self.interval,[self.interval<self.t_debut,self.interval>=self.t_debut],[0,self.amplitude])