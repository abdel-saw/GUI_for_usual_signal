import numpy as np 
from Backend.Visualisation import *

class signal_rect(Visualisation):
    def __init__(self,ampli,b_deb,b_fin,t_max):
        self.ampli= int(ampli)
        self.bornmin = int(b_deb)
        self.bornmax = int(b_fin)
        self.t_max =int(t_max)
        self.t_interv_rect = np.linspace(-self.t_max,self.t_max,100)
        self.s_rect = np.where((self.t_interv_rect>self.bornmin) & (self.t_interv_rect<self.bornmax),self.ampli,0)
        