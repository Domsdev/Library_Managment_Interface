
from tkinter import *
from gui_frame_page import *
from gui_login_page import *
from gui_activate_account_page import *

##############################################################################

class Welcome_page(Frame_page):
	
    def __init__(self, window):
        super().__init__(window)
        
        self.color_1 = "#8B9089" # bg color of title & subtitles / same as bg
        self.color_2 = "#BDBCB5" # color for labels and buttons

        self.logo()
        self.title()
        self.subtitle()
        self.login_button()
        self.activate_account_button()
        self.quit_button()

##############################################################################

    def logo(self):
        w, h = 100, 100
        self.img =  PhotoImage(file= "Domsdev_library.png").subsample(8)
        canevas = Canvas(self.frame, width= w, height= h,
            bg= self.color_1, bd= 0, highlightthickness= 0)
        canevas.create_image(w/2, h/2, image= self.img)
        canevas.pack(side= 'top')

##############################################################################

    def title(self):
        Label(self.frame, text="Bienvenue à la \nDomsdev Library !",
              font=("Calibri", 26), bg=self.color_1, fg='white').pack()

##############################################################################

    def subtitle(self):
        Label(self.frame,
            text= "La Bibliothèque autodidacte",
            font= ("Calibri", 18),
            bg= self.color_1, fg= 'white').pack(pady= 15)

##############################################################################

    def login_button(self):
        login = Button(self.frame,
            text= "Connexion",
            font= ("Calibri", 14),
            bg= self.color_2, fg='black',
            command= self.login_command).pack(fill= X, pady= 10)
        # fill= X gives the same width than the largest displayed object

    def login_command(self):
        self.frame.destroy()
        Login_page(self.window)

##############################################################################

    def activate_account_button(self):
        login = Button(self.frame,
            text= "Activation compte",
            font= ("Calibri", 14),
            bg= self.color_2, fg='black',
            command= self.activate_account_command).pack(fill= X, pady= 10)
        # fill= X gives the same width than the largest displayed object

    def activate_account_command(self):
        self.frame.destroy()
        Activate_account_page(self.window)

##############################################################################

    def quit_button(self):
        self.quit_button = Button(self.frame, 
            text= "Quitter",
            font= ("Calibri", 10), 
            bg= self.color_2, 
            fg='black',
            command= self.window.destroy).pack(side= 'right', pady= 30)
