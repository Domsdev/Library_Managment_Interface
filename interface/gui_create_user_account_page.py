from tkinter import *
from tkinter import messagebox

from gui_frame_page import *
from gui_normalised_widgets import *

from connect_db import *
from get_image_data import *
from mail_password_validity import *
from generate_activation_code import *

##############################################################################

class Create_user_account_top_page:

    def __init__(self):
        self.top_window = Toplevel()
        self.top_window.geometry("720x480")
        self.top_window.minsize(400,300)
        self.top_window.title("Domsdev Library")
        self.top_window.config(background= '#8B9089')
        Create_user_account_page(self.top_window)

##############################################################################

class Create_user_account_page(Frame_page):

    def __init__(self, window):
        super().__init__(window)
        
        self.title()
        self.first_name_field()
        self.last_name_field()
        self.phone_number_field()
        self.email_field()
        self.load_id_card()
        self.create_button()
        self.back_button()

##############################################################################

    def title(self): # .grid row = 1
        Normalised.title_N(self.frame, "Nouveau compte utilisateur", 1, 1, 1, 2,
            pady= 30, sticky='we')

    def first_name_field(self): # .grid row = 2
        Normalised.label_N(self.frame, "Prénom", 2, 1, sticky= 'we')
        self.first_name_entry = Normalised.entry_N(self.frame, 2, 2)

    def last_name_field(self): # .grid row = 3
        Normalised.label_N(self.frame, "Nom", 3, 1, sticky= 'we')
        self.last_name_entry = Normalised.entry_N(self.frame, 3, 2)

    def phone_number_field(self): # .grid row = 4
        Normalised.label_N(self.frame, "N° Téléphone", 4, 1, sticky= 'we')
        self.phone_number_entry = Normalised.entry_N(self.frame, 4, 2)

    def email_field(self): # .grid row = 5
        Normalised.label_N(self.frame, "e-Mail", 5, 1, sticky= 'we')
        self.email_entry = Normalised.entry_N(self.frame, 5, 2)

    ##########################################################################

    def load_id_card(self): # .grid row = 6
        
        # create load file button
        self.load_id_card = Normalised.button_N(
            self.frame, "Pièce d'identité", 6, 1,
            sticky= 'we', pady= 8,
            command= self.get_id_card_data)
        
        # create entry field to put in the name of loaded file
        self.id_card_file_name_entry = Normalised.entry_N(self.frame, 6, 2)
        

    def get_id_card_data(self):

        # clear entry field (if needed)
        self.id_card_file_name_entry.delete(0, END)
        
        # get binary data and file name from image file,
        # using filedialog in Get_image_data
        self.id_card_data, self.id_card_file_name = Get_image_data(
                                                                  self.window
                                                                  )
        # set name of file in entry field
        self.id_card_file_name_entry.insert(0, self.id_card_file_name)
        
##############################################################################

    def create_button(self): # .grid row = 7
        self.create_account = Normalised.button_N(
            self.frame, "Créer", 7, 1, 1, 2,
            sticky= 'we', pady= 15,
            command= self.register_command)

    def register_command(self):

        # check entered coordinates
        if self.first_name_entry.get() == '': 
            self.error("Veuillez entrer un Prénom")
        elif self.last_name_entry.get() == '': 
            self.error("Veuillez entrer un Nom")
        elif self.phone_number_entry.get() == '': 
            self.error("Veuillez entrer un N° de Téléphone")


        elif self.email_entry.get() == '': 
            self.error("Veuillez entrer une adresse e-Mail")
                # check if email format is valid
        elif mail_validity(self.email_entry.get()) == False:
            self.error(
"Adresse e-Mail invalide\
\nVeuillez entrer une adresse e-Mail valide")

        elif self.id_card_data == None:
            self.error("Veuillez charger une pièce d'identité")

        else:

            # enter coordinates in list
            self.account_data = []
            self.account_data.append(self.first_name_entry.get())     # [0]
            self.account_data.append(self.last_name_entry.get())      # [1]
            self.account_data.append(self.phone_number_entry.get())   # [2]
            self.account_data.append(self.email_entry.get())          # [3]
            self.account_data.append(self.id_card_data)               # [4]
            self.account_data.append(Generate_activation_code())      # [5]

            # formate data
            self.account_data[0] = self.account_data[0].strip()
            self.account_data[1] = self.account_data[1].strip()
            self.account_data[2] = self.account_data[2].strip()
            self.account_data[3] = self.account_data[3].strip()

            self.account_data[0] = self.account_data[0].capitalize()
            self.account_data[1] = self.account_data[1].capitalize()

            # connection to MySQL for registration in database
            q = connect_db('create user account', self.account_data)

            if q == True:
                self.frame.destroy()
                messagebox.showinfo("Info",
"Nouveau compte utilisateur crée !\
\nUn code d'activation est envoyé à l'utilisateur.",
parent= self.window)

                self.window.destroy()

            elif q == False:
                self.error(
"Une erreur est survenue lors de l'envoi du code d'activation !\
\nVeuillez contacter un administrateur.")

            elif q == "Can't connect to MySQL server":
                self.error("Can't connect to MySQL server\
                    \nVeuillez contacter un administrateur")


    def error(self, type_error):
        # message box for errors during registration
        messagebox.showerror("Erreur:", type_error, parent= self.window)

##############################################################################

    def back_button(self): # .grid row = 8
        Normalised.button_N(
            self.frame, "Retour", 8, 2, sticky= 'e',
            command= self.window.destroy)
