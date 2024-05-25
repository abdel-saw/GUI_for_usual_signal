import matplotlib.pyplot as plt
class Visualisation():
    #cette classe récupère les paramètres pour afficher un signal
    def __init__(self) :
        pass
    def affichage_1(self,signal,interval):
        self.signal=signal
        self.interval=interval
        plt.figure()
        plt.plot(self.interval,self.signal)
        plt.title("Signal representation")
        plt.xlabel("interval")
        plt.ylabel("amplitude")
        plt.grid(True)
        plt.show()
     
    def affichage_2(self,partie_reel,partie_imag,freq):
        self.signal_img=partie_imag
        self.signal_reel=partie_reel
        self.freq=freq
        plt.figure()
        plt.plot(self.freq,self.signal_reel)
        plt.title("Signal representation")
        plt.xlabel("interval")
        plt.ylabel("amplitude")
        plt.grid(True)
        plt.show()    