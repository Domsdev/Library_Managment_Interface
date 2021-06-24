from tkinter import *
from tkinter import messagebox

from gui_frame_page_extented import *
from gui_normalised_widgets import *
from gui_create_reference_page import *
from gui_search_reference_page import *
from gui_create_user_account_page import *
from gui_search_user_account_page import *

##############################################################################

class Librarian_page(Frame_page_extented):

    def __init__(self, window, login_list):
        super().__init__(window, login_list)

        self.pseudo = login_list[0]
        
        self.title()
        self.search_reference()
        self.create_reference()
        self.search_user_account()
        self.create_user_account()
        self.check_late_returns()
        self.quit()

##############################################################################

    def title(self): # .grid row = 1
        Normalised.title_N(self.frame, "Bienvenue {}".format(self.pseudo),
            1, 1, pady= 30, sticky='we')

##############################################################################

    def search_reference(self): # .grid row = 2
    	self.search_button = Normalised.button_N(
            self.frame, "Rechercher une référence", 2, 1, sticky= 'we',
            command= Search_reference_top_page)

##############################################################################

    def create_reference(self): # .grid row = 3
        self.new_refererence_button = Normalised.button_N(
            self.frame, "Créer une référence", 3, 1, sticky= 'we',
            command= Create_reference_top_page)

##############################################################################

    def search_user_account(self): # .grid row = 4
        self.search_button = Normalised.button_N(
            self.frame, "Rechercher un compte utilisateur", 4, 1, sticky= 'we',
            command= Search_user_account_top_page)

##############################################################################

    def create_user_account(self): # .grid row = 5
        self.verify_new_account_button = Normalised.button_N(
            self.frame, "Créer un compte utilisateur", 5, 1, sticky= 'we',
            command= Create_user_account_top_page)

##############################################################################

    def check_late_returns(self): # .grid row = 6
    	self.check_late_returns_button = Normalised.button_N(
            self.frame, "Vérifier les prêts", 6, 1, sticky= 'we',
            command= self.check_late_returns_command)

    def check_late_returns_command(self):
    	pass

##############################################################################

    def quit(self): # .grid row = 7
    	self.quit_button = Normalised.button_N(
            self.frame, "Déconnexion", 7, 1, sticky= 'e', pady= 30,
            command= self.quit_command)

    def quit_command(self):
        answer = messagebox.askokcancel("Attention",
                                        "Vous allez vous déconnecter !")
        if answer == True:
            self.frame.destroy()
            from gui_welcome_page import Welcome_page
            Welcome_page(self.window)
