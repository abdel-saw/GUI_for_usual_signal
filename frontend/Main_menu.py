from Backend.signal_sinuso import *
from Backend.Visualisation import*
from Backend.signal_fourier import*
from Backend.signal_echelon import *
from Backend.signal_rampe import * 
from Backend.signal_rect import *
from Backend.signal_sincard import *
import tkinter as tk

class Main_menu (signal_sinuso):
    def __init__(self) :
        self.fenetre_principal= tk.Tk()
        self.fenetre_secondaire=tk.Frame(self.fenetre_principal)
        self.fenetre_secondaire.grid()
        self.fenetre_principal.title("Signal Processing ")
        self.screen_x= int(self.fenetre_principal.winfo_screenwidth())
        self.screen_y=int(self.fenetre_principal.winfo_screenheight())
        self.fenetre_principal_x=800
        self.fenetre_principal_y=700
        self.posx=(self.screen_x//2)-(self.fenetre_principal_x//2)
        self.posy=(self.screen_y//2)-(self.fenetre_principal_y//2)
        self.geo = "{}x{}+{}+{}".format(self.fenetre_principal_x,self.fenetre_principal_y,self.posx,self.posy)
        self.fenetre_principal.geometry(self.geo)
        self.welcome_label=tk.Label(self.fenetre_secondaire,text=" WELCOME TO THE BEST APP FOR SIGNAL PROCESSING ",font=25,bg='blue')
        self.welcome_label.grid(row=0,column=0)
        self.btn_sign_sinu=tk.Button(self.fenetre_secondaire,text="creer un signal sinusoidal",width=30,command=self.menu_signal_sinusoidal)
        self.btn_sign_sinu.grid(row=1,column=0)
        self.btn_sign_usuel=tk.Button(self.fenetre_secondaire,text="creer un signal usuel",width=30,command=self.choix_signaux_usuels)
        self.btn_sign_usuel.grid(row=2,column=0)
        self.btn_sign_fourier_usuel=tk.Button(self.fenetre_secondaire,text="creer une representation de fourier \n d'un signal usuel",width=30,command=self.choix_signaux_usuels_fourier)
        self.btn_sign_fourier_usuel.grid(row=3,column=0)
        self.btn_sign_fourier_sinus=tk.Button(self.fenetre_secondaire,text="creer une representation de fourier \n d'un signal sinusoidal",width=30,command=self.menu_four_sinus)
        self.btn_sign_fourier_sinus.grid(row=4,column=0)
        self.fenetre_principal.mainloop()

    def choix_signaux_usuels(self):
        # ask the user to make a choice after he cliked on the button "creer un signal usuel"
        self.fen_princip2=tk.Tk()
        self.fen_princip2.title("CHOISIR LE SIGNAL ")
        self.fen_second2=tk.Frame(self.fen_princip2)
        self.fen_second2.grid()
        self.btn_echelon=tk.Button(self.fen_second2,text="SIGNAL ECHELON ",command=self.sign_echelon_menu)
        self.btn_echelon.grid(row=0,column=0)
        self.btn_rampe=tk.Button(self.fen_second2,text="SIGNAL RAMPE ",command=self.menu_sign_rampe)
        self.btn_rampe.grid(row=1,column=0)
        self.btn_rect=tk.Button(self.fen_second2,text="SIGNAL RECTANGLE ",command=self.sign_rect_menu)
        self.btn_rect.grid(row=2,column=0)
        self.btn_sincard=tk.Button(self.fen_second2,text="SIGNAL SINUS CARDINAL ",command=self.menu_sign_sincard)
        self.btn_sincard.grid(row=3,column=0)
        self.fen_princip2.mainloop()
    
    def menu_sign_rampe(self):
        #menu that appears when the user click on the button "signal rampe " from the menu "signaux usuels"
        self.fen_princip4=tk.Tk()
        self.fen_princip4.title("signal rampe ")
        self.label_giveparameter=tk.Label(self.fen_princip4,text=" Entrer les parametres ")
        self.label_giveparameter.grid(row=0,column=0)
        self.label_t_deb=tk.Label(self.fen_princip4,text="entrer le temps de debut: ")
        self.label_t_deb.grid(row=1,column=0)
        self.ent_t_deb=tk.Entry(self.fen_princip4)
        self.ent_t_deb.grid(row=1,column=1)
        self.label_tmax=tk.Label(self.fen_princip4,text="entrer le temps max pour la representation : ")
        self.label_tmax.grid(row=2,column=0)
        self.ent_tmax=tk.Entry(self.fen_princip4)
        self.ent_tmax.grid(row=2,column=1)
        self.btn_para_rampe=tk.Button(self.fen_princip4,text="OK",command=self.appel_sign_rampe)
        self.btn_para_rampe.grid(row=3,column=0)
        self.fen_princip4.mainloop()
        
    def appel_sign_rampe(self):
        #function called after the user click the "OK"button from signal ranpe menu
        self.sign_rampe_obj=signal_rampe(self.ent_t_deb.get(),self.ent_tmax.get())
        self.sign_rampe_obj.affichage_1(self.sign_rampe_obj.signal_r,self.sign_rampe_obj.interv_r)   
        
        
    def sign_rect_menu(self):
        #menu that appears when the user click on the button "signal rectangle " from the menu "signaux usuels"
        self.fen_princip4=tk.Tk()
        self.fen_princip4.title("signal rectangle ")
        self.label_giveparameter=tk.Label(self.fen_princip4,text=" Entrer les parametres ")
        self.label_giveparameter.grid(row=0,column=0)
        self.label_amp_rect=tk.Label(self.fen_princip4,text="entrer l'amplitude : ")
        self.label_amp_rect.grid(row=1,column=0)
        self.ent_amp_rect=tk.Entry(self.fen_princip4)
        self.ent_amp_rect.grid(row=1,column=1)
        self.label_t_deb_rect=tk.Label(self.fen_princip4,text="entrer la borne de debut : ")
        self.label_t_deb_rect.grid(row=2,column=0)
        self.ent_t_deb_rect=tk.Entry(self.fen_princip4)
        self.ent_t_deb_rect.grid(row=2,column=1)
        self.label_t_fin_rect=tk.Label(self.fen_princip4,text="entrer la borne de fin : ")
        self.label_t_fin_rect.grid(row=3,column=0)
        self.ent_t_fin_rect=tk.Entry(self.fen_princip4)
        self.ent_t_fin_rect.grid(row=3,column=1)
        self.label_tmax_rect=tk.Label(self.fen_princip4,text="entrer le t_max pour la representation")
        self.label_tmax_rect.grid(row=4,column=0)
        self.t_max_rect_ent=tk.Entry(self.fen_princip4)
        self.t_max_rect_ent.grid(row=4,column=1)
        self.btn_para_rect=tk.Button(self.fen_princip4,text="OK",command=self.appel_sign_rect)
        self.btn_para_rect.grid(row=5,column=0)
        self.fen_princip4.mainloop()
    
    def appel_sign_rect(self):
        #function called after the user click the "OK"button from signal rectangle  menu
        self.sign_rect_obj=signal_rect(self.ent_amp_rect.get(),self.ent_t_deb_rect.get(),self.ent_t_fin_rect.get(),self.t_max_rect_ent.get())
        self.sign_rect_obj.affichage_1(self.sign_rect_obj.s_rect,self.sign_rect_obj.t_interv_rect)
        
        
    def menu_sign_sincard(self):
        #menu that appears when the user click on the button "signal sinus cardinal " from the menu "signaux usuels"
        self.fen_princip4=tk.Tk()
        self.fen_princip4.title("signal sinus cardinal ")
        self.label_giveparameter=tk.Label(self.fen_princip4,text=" Entrer les parametres ")
        self.label_giveparameter.grid(row=0,column=0)
        self.label_t_sincard=tk.Label(self.fen_princip4,text="entrer le temps pour la representation  ")
        self.label_t_sincard.grid(row=1,column=0)
        self.ent_t_sincard=tk.Entry(self.fen_princip4)
        self.ent_t_sincard.grid(row=1,column=1) 
        self.btn_para_sinus=tk.Button(self.fen_princip4,text="OK",command=self.appel_sincard)
        self.btn_para_sinus.grid(row=2,column=0)  
        self.fen_princip4.mainloop() 
    
    def appel_sincard(self):
         #function called after the user click the "OK"button from signal sinus cardinal menu
        self.sincard_obj=signal_sincard(int(self.ent_t_sincard.get()))
        self.sincard_obj.affichage_1(self.sincard_obj.sign_sinc,self.sincard_obj.interv)
    
    def sign_echelon_menu(self):
        self.fen_princip4=tk.Tk()
        self.fen_princip4.title("signal echelon ")
        self.label_giveparameter=tk.Label(self.fen_princip4,text=" Entrer les parametres ")
        self.label_giveparameter.grid(row=0,column=0)
        self.label_amp_eche=tk.Label(self.fen_princip4,text="entrer l'amplitude : ")
        self.label_amp_eche.grid(row=1,column=0)
        self.ent_amp_eche=tk.Entry(self.fen_princip4)
        self.ent_amp_eche.grid(row=1,column=1)
        self.label_t_max_eche=tk.Label(self.fen_princip4,text="entrer le temps max pour la representation : ")
        self.label_t_max_eche.grid(row=2,column=0)
        self.ent_t_max_eche=tk.Entry(self.fen_princip4)
        self.ent_t_max_eche.grid(row=2,column=1)
        self.label_t_deb_eche=tk.Label(self.fen_princip4,text="entrer le temps de debut: ")
        self.label_t_deb_eche.grid(row=3,column=0)
        self.ent_t_deb_eche=tk.Entry(self.fen_princip4)
        self.ent_t_deb_eche.grid(row=3,column=1)
        self.btn_para_eche=tk.Button(self.fen_princip4,text="OK",command=self.appel_sign_echelon)
        self.btn_para_eche.grid(row=4,column=0)
        self.fen_princip4.mainloop()
        
    def appel_sign_echelon(self):
        self.sign_eche_obj=signal_echelon(self.ent_amp_eche.get(),self.ent_t_max_eche.get(),self.ent_t_deb_eche.get())
        self.sign_eche_obj.affichage_1 (self.sign_eche_obj.signal,self.sign_eche_obj.interval)    
            
        
             
    def choix_signaux_usuels_fourier(self):
         # ask the user to make a choice after he cliked on the button "creer une representation de fourier d'un signal usuel"
        self.fen_princip3=tk.Tk()
        self.fen_princip3.title("CHOISIR LE SIGNAL ")
        self.fen_second3=tk.Frame(self.fen_princip3)
        self.fen_second3.grid()
        self.btn_echelon_four=tk.Button(self.fen_second3,text="SIGNAL ECHELON ")
        self.btn_echelon_four.grid(row=0,column=0)
        self.btn_rampe_four=tk.Button(self.fen_second3,text="SIGNAL RAMPE ")
        self.btn_rampe_four.grid(row=1,column=0)
        self.btn_rect_four=tk.Button(self.fen_second3,text="SIGNAL RECTANGLE ",command=self.menu_sign_rect_four)
        self.btn_rect_four.grid(row=2,column=0)
        self.btn_sincard_four=tk.Button(self.fen_second3,text="SIGNAL SINUS CARDINAL ",command=self.menu_sincard_fourier)
        self.btn_sincard_four.grid(row=3,column=0)
        self.fen_princip3.mainloop()
        
    def menu_sign_rect_four(self):
         #menu that appears when the user click on the button "signal rectangle " from the menu "representation de fourier de signaux usuels"
        self.fen_princip4=tk.Tk()
        self.fen_princip4.title("signal rectangle ")
        self.label_giveparameter=tk.Label(self.fen_princip4,text=" Entrer les parametres ")
        self.label_giveparameter.grid(row=0,column=0)
        self.label_amp_rect=tk.Label(self.fen_princip4,text="entrer l'amplitude : ")
        self.label_amp_rect.grid(row=1,column=0)
        self.ent_amp_rect=tk.Entry(self.fen_princip4)
        self.ent_amp_rect.grid(row=1,column=1)
        self.label_t_deb_rect=tk.Label(self.fen_princip4,text="entrer la borne de debut : ")
        self.label_t_deb_rect.grid(row=2,column=0)
        self.ent_t_deb_rect=tk.Entry(self.fen_princip4)
        self.ent_t_deb_rect.grid(row=2,column=1)
        self.label_t_fin_rect=tk.Label(self.fen_princip4,text="entrer la borne de fin : ")
        self.label_t_fin_rect.grid(row=3,column=0)
        self.ent_t_fin_rect=tk.Entry(self.fen_princip4)
        self.ent_t_fin_rect.grid(row=3,column=1)
        self.label_tmax_rect=tk.Label(self.fen_princip4,text="entrer le t_max pour la representation")
        self.label_tmax_rect.grid(row=4,column=0)
        self.t_max_rect_ent=tk.Entry(self.fen_princip4)
        self.t_max_rect_ent.grid(row=4,column=1)
        self.btn_para_rect=tk.Button(self.fen_princip4,text="OK",command=self.appel_sign_rect_four)
        self.btn_para_rect.grid(row=5,column=0)
        self.fen_princip4.mainloop()
        
    def appel_sign_rect_four(self):
        self.sign_rect_obj=signal_rect(self.ent_amp_rect.get(),self.ent_t_deb_rect.get(),self.ent_t_fin_rect.get(),self.t_max_rect_ent.get())
        self.sign_rect_obj_four=signal_fourier(self.sign_rect_obj.s_rect)
        self.sign_rect_obj_four.affichage_2(self.sign_rect_obj_four.fsignal.real,self.sign_rect_obj_four.fsignal.imag,self.sign_rect_obj_four.freq)
      
        
        
    def menu_sincard_fourier(self):
         #menu that appears when the user click on the button "signal sinus cardinal" from the menu "representation usuels d'un signal de fourier"
        self.fen_princip4=tk.Tk()
        self.fen_princip4.title("representation de fourier d'un signal sinus cardinal ")
        self.label_giveparameter=tk.Label(self.fen_princip4,text=" Entrer les parametres ")
        self.label_giveparameter.grid(row=0,column=0)
        self.label_t_sincard=tk.Label(self.fen_princip4,text="entrer le temps pour la representation  ")
        self.label_t_sincard.grid(row=1,column=0)
        self.ent_t_sincard=tk.Entry(self.fen_princip4)
        self.ent_t_sincard.grid(row=1,column=1) 
        self.btn_para_sincard=tk.Button(self.fen_princip4,text="OK",command=self.appel_sincard_four)
        self.btn_para_sincard.grid(row=2,column=0)  
        self.fen_princip4.mainloop()  
        
    def appel_sincard_four(self):
        #function called after the user click the "OK"button from signal sinus cardinal from fourier usuels menu
        self.sincard_obj=signal_sincard(int(self.ent_t_sincard.get())) 
        self.sincard_obj_four=signal_fourier(self.sincard_obj.sign_sinc)
        self.sincard_obj_four.affichage_2(self.sincard_obj_four.fsignal.real,self.sincard_obj_four.fsignal.imag,self.sincard_obj_four.freq)      
   
    
    def menu_signal_sinusoidal(self):
        # collect parameters to show siusoidal signal after clicking on the button "Signal sinusoidal"
        self.fen_princip4=tk.Tk()
        self.fen_princip4.title("signal sinusoidal ")
        self.label_giveparameter=tk.Label(self.fen_princip4,text=" Entrer les parametres ")
        self.label_giveparameter.grid(row=0,column=0)
        self.label_amp=tk.Label(self.fen_princip4,text="entrer l'amplitude : ")
        self.label_amp.grid(row=1,column=0)
        self.ent_amp=tk.Entry(self.fen_princip4)
        self.ent_amp.grid(row=1,column=1)
        self.label_tmax=tk.Label(self.fen_princip4,text="entrer le temps max pour la representation : ")
        self.label_tmax.grid(row=2,column=0)
        self.ent_tmax=tk.Entry(self.fen_princip4)
        self.ent_tmax.grid(row=2,column=1)
        self.label_freq=tk.Label(self.fen_princip4,text="entrer la frequence du signal : ")
        self.label_freq.grid(row=3,column=0)
        self.ent_freq=tk.Entry(self.fen_princip4)
        self.ent_freq.grid(row=3,column=1)
        self.btn_para_sinus=tk.Button(self.fen_princip4,text="OK",command=self.appel_signal_sinus)
        self.btn_para_sinus.grid(row=4,column=0)
        self.fen_princip4.mainloop()
        
    def appel_signal_sinus(self):
     #appel la fonction sinusoidal avec les parametre de representation
        self.signal_sinu_obj=signal_sinuso(int(self.ent_amp.get()),int(self.ent_tmax.get()),int(self.ent_freq.get()))
        self.signal_sinu_obj.affichage_1(self.signal_sinu_obj.signal,self.signal_sinu_obj.interval)
        
    def menu_four_sinus(self):
        #menu shown when user click on representation de fourier d'un signal sinusoidal 
        self.fen_princip4=tk.Tk()
        self.fen_princip4.title("representation de fourier d'un signal sinusoidal ")
        self.label_giveparameter=tk.Label(self.fen_princip4,text=" Entrer les parametres ")
        self.label_giveparameter.grid(row=0,column=0)
        self.label_amp=tk.Label(self.fen_princip4,text="entrer l'amplitude : ")
        self.label_amp.grid(row=1,column=0)
        self.ent_amp=tk.Entry(self.fen_princip4)
        self.ent_amp.grid(row=1,column=1)
        self.label_tmax=tk.Label(self.fen_princip4,text="entrer le temps max pour la representation : ")
        self.label_tmax.grid(row=2,column=0)
        self.ent_tmax=tk.Entry(self.fen_princip4)
        self.ent_tmax.grid(row=2,column=1)
        self.label_freq=tk.Label(self.fen_princip4,text="entrer la frequence du signal : ")
        self.label_freq.grid(row=3,column=0)
        self.ent_freq=tk.Entry(self.fen_princip4)
        self.ent_freq.grid(row=3,column=1)
        self.btn_para_sinus=tk.Button(self.fen_princip4,text="OK",command=self.appel_signal_fourier_sinus)
        self.btn_para_sinus.grid(row=4,column=0)
        self.fen_princip4.mainloop()    
        
    def appel_signal_fourier_sinus(self):
      #function called when user click on the ok button from menu fourier sinusoidal  
        self.sign_sinu_obj=signal_sinuso(int(self.ent_amp.get()),int(self.ent_tmax.get()),int(self.ent_freq.get()))
        self.sign_four_sinu_obj=signal_fourier(self.sign_sinu_obj.signal)
        self.sign_four_sinu_obj.affichage_2(self.sign_four_sinu_obj.fsignal.real,self.sign_four_sinu_obj.fsignal.imag,self.sign_four_sinu_obj.freq)
        
                

