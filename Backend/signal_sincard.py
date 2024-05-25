from Backend.Visualisation import *
import numpy as np 
from math import * 

class signal_sincard(Visualisation):
    def __init__(self,t_repr_sincard) :
        self.t_max = int(t_repr_sincard)
        self.interv= np.linspace(-self.t_max,self.t_max,1000)
        self.sign_sinc= np.where(self.interv != 0,[(sin(self.k)/self.k )for self.k in self.interv],1)
        