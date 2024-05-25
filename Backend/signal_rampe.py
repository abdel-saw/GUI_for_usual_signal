from Backend.Visualisation import*
import numpy as np 

class signal_rampe(Visualisation):
    def __init__(self,t_deb,t_fin):
        self.t_debut = t_deb
        self.t_debut =int(self.t_debut)
        self.t_max = t_fin
        self.t_max = int (self.t_max)
        self.interv_r = np.linspace(-self.t_max,self.t_max,100)
        self.signal_r = np.where(self.interv_r>self.t_debut,self.interv_r-self.t_debut,0)