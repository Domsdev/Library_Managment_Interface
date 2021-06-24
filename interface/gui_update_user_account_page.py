from tkinter import *
import PIL.Image, PIL.ImageTk
import os

from gui_frame_page_extented import Frame_page_extented
from gui_normalised_widgets import Normalised

from connect_db import connect_db
from connect_raw_db import connect_raw_db
from mail_password_validity import *
from generate_activation_code import *


##############################################################################

class Update_user_account_top_page:

    def __init__(self):
        self.top_window = Toplevel()
        self.top_window.geometry("910x480")
        self.top_window.minsize(400,300)
        self.top_window.title("Domsdev Library")
        self.top_window.config(background= '#8B9089')

# update user account page: ########################################################

class Update_user_account_page(Frame_page_extented):

    def __init__(self, window, selected_account):
        super().__init__(window, selected_account)
        self.color_1 = "#8B9089"

        self.selected_account = selected_account

        # get data of the selected account from dB
        self.account_data = connect_db(
            "fetch account data",self.selected_account)
        # self.account_data is a list of lists

        self.account_data = self.account_data[0]
        # self.account_data is now a simple list:
        # self.account_data == [id, pseudo, first_name, last_name, 
        #                       phone_number, email, active]

        self.title_page()
        self.subtitle()
        self.first_name_field()
        self.last_name_field()
        self.phone_number_field()
        self.email_field()
        self.identity_card_button()
        self.update_button()
        self.back_button()

##############################################################################

    def title_page(self): # .grid row = 1
        Normalised.title_N(
            self.frame, f"Compte utilisateur\n{self.account_data[1]}",
            1, 1, 1, 3,
            sticky= 'ew')

##############################################################################

    def subtitle(self): # .grid row = 2
        Normalised.label_N(
            self.frame, "Cochez les cases pour modifier les coordonnées",
            2 ,1 , 1, 2,
            pady= 20, sticky= 'we', color = "#8B9089", relief= 'flat'
            )

##############################################################################

    def first_name_field(self): # .grid row = 3
        Normalised.label_N(self.frame, "Prénom", 3, 1, sticky= 'ew')
        self.first_name_entry = Normalised.entry_N(self.frame, 3, 2)
        self.first_name_entry.insert(END, self.account_data[2])
        self.first_name_entry.config(state='disabled')

        # check box
        self.first_name_var = StringVar()
        Normalised.check_N(
            self.frame, "", 3, 0, 
            variable= self.first_name_var,
            command= self.config_first_name)

    # check box command
    def config_first_name(self):
        if self.first_name_var.get() == 'Ok':
            self.first_name_entry.config(state='normal')

        elif self.first_name_var.get() == 'Not Ok':
            self.first_name_entry.config(state='disabled')

##############################################################################

    def last_name_field(self): # .grid row = 4
        Normalised.label_N(self.frame, "Nom", 4, 1, sticky= 'ew')
        self.last_name_entry = Normalised.entry_N(self.frame, 4, 2)
        self.last_name_entry.insert(END, self.account_data[3])
        self.last_name_entry.config(state='disabled')

        # check box
        self.last_name_var = StringVar()
        Normalised.check_N(
            self.frame, "", 4, 0,
            variable= self.last_name_var,
            command= self.config_last_name)

    # check box command
    def config_last_name(self):
        if self.last_name_var.get() == 'Ok':
            self.last_name_entry.config(state='normal')

        elif self.last_name_var.get() == 'Not Ok':
            self.last_name_entry.config(state='disabled')

##############################################################################

    def phone_number_field(self): # .grid row = 5
        Normalised.label_N(self.frame, "N° Téléphone", 5, 1, sticky= 'ew')
        self.phone_number_entry = Normalised.entry_N(self.frame, 5, 2)
        self.phone_number_entry.insert(END, self.account_data[4])
        self.phone_number_entry.config(state='disabled')

        # check box
        self.phone_number_var = StringVar()
        Normalised.check_N(
            self.frame, "", 5, 0, 
            variable= self.phone_number_var,
            command= self.config_phone_number)

    # check box command
    def config_phone_number(self):
        if self.phone_number_var.get() == 'Ok':
            self.phone_number_entry.config(state='normal')

        elif self.phone_number_var.get() == 'Not Ok':
            self.phone_number_entry.config(state='disabled')

##############################################################################

    def email_field(self): # .grid row = 6
        Normalised.label_N(self.frame, "e-Mail", 6, 1, sticky= 'ew')
        self.email_entry = Normalised.entry_N(self.frame, 6, 2)
        self.email_entry.insert(END, self.account_data[5])
        self.email_entry.config(state='disabled')

        # check box
        self.email_var = StringVar()
        Normalised.check_N(
            self.frame, "", 6, 0,
            variable= self.email_var,
            command= self.config_email)

    # check box command
    def config_email(self):
        if self.email_var.get() == 'Ok':
            self.email_entry.config(state='normal')

        elif self.email_var.get() == 'Not Ok':
            self.email_entry.config(state='disabled')

##############################################################################

    def identity_card_button(self): # .grid row = 7

        # create button for identity_card checking
        Normalised.button_N(
            self.frame, "Vérification pièce d'identité", 7, 1, 1, 2,
            sticky= 'we', pady= 10, command= self.check_identity_card
            )

    def check_identity_card(self):

        # create a toplevel window to display identity card
        self.id_top_window = Toplevel()
        self.id_top_window.title("Pièce d'identité utilisateur")
        self.id_top_window.config(background= '#8B9089')
        self.id_top_frame = Frame(self.id_top_window, bg= '#8B9089')
        self.id_top_frame.pack(expand= YES)


        # create back button on frame of toplevel window
        button = Button(self.id_top_frame,
                        text= " OK ", font= ("Calibri", 14),
                        command= self.quit_identity_card
                        )
        button.pack(side= 'bottom', fill= X)

        # get identity card binary data from dB
        self.id_card_data = connect_raw_db(self.selected_account[0])

        # write temporary the file in current folder
        with open("temp_image_file", "wb") as f:
        	f.write(self.id_card_data[0])

        # read the created file whith PIL.ImageTk.PhotoImage
        # and create PhotoImage data type
        # use PIL to read any image format (.png, .jpeg, etc ...)
        self.image =  PIL.ImageTk.PhotoImage(file= "temp_image_file")

        # create first a label that automatically fit the image size
        self.label_id_card = Label(self.id_top_frame, image= self.image)
        self.label_id_card.pack(fill=BOTH, expand=YES)

        self.id_top_window.update()
        # so we can get the optimised image size
        w = self.label_id_card.winfo_width()
        h = self.label_id_card.winfo_height()

        self.label_id_card.destroy()

        ############
        # scrollbar definition, in case of a picture bigger than the screen
        self.scrollbar = Scrollbar(self.id_top_frame, 
                                   orient=VERTICAL, width= 20
                                   )
        self.scrollbar.pack(side='right')
        ############

        # then create canvas with scrollbar to the dimensions of the label
        self.canevas = Canvas(self.id_top_frame, width= w, height= h,
        	bg= self.color_1, bd= 0, highlightthickness= 0,
        	yscrollcommand= self.scrollbar.set)
        self.canevas.create_image(0, 0, image= self.image, anchor= 'nw')
        self.canevas.pack()

        ############
        self.scrollbar.config(command= self.canevas.yview)
        ############


    def quit_identity_card(self):

        os.remove("temp_image_file")
        self.id_top_window.destroy()

##############################################################################

    def update_button(self): # .grid row = 8

        # create button account validation
        Normalised.button_N(
            self.frame, " Valider les modifications", 8, 1,
            sticky= 'w', pady= 20, command= self.update_command
            )

    def update_command(self):

        # check entered coordinates
        if self.first_name_entry.get() == '': 
            self.error("Veuillez entrer un Prénom")
        elif self.last_name_entry.get() == '': 
            self.error("Veuillez entrer un Nom")
        elif self.phone_number_entry.get() == '': 
            self.error("Veuillez entrer un N° de Téléphone")


        elif self.email_entry.get() == '': 
            self.error("Veuillez entrer un Prénom")
                # check if email format is valid
        elif mail_validity(self.email_entry.get()) == False:
            self.error(
"Adresse e-Mail invalide\
\nVeuillez entrer une adresse e-Mail valide")

        else:

            # enter coordinates in list
            self.account_data[2] = self.first_name_entry.get()
            self.account_data[3] = self.last_name_entry.get()
            self.account_data[4] = self.phone_number_entry.get()
            self.account_data[5] = self.email_entry.get()
            self.account_data[6] = Generate_activation_code()

            # formate data
            self.account_data[2] = self.account_data[2].strip()
            self.account_data[3] = self.account_data[3].strip()
            self.account_data[4] = self.account_data[4].strip()
            self.account_data[5] = self.account_data[5].strip()

            self.account_data[2] = self.account_data[2].capitalize()
            self.account_data[3] = self.account_data[3].capitalize()

            # connection to MySQL for registration in database
            q = connect_db('update', self.account_data)

            if q == True:
                self.frame.destroy()
                messagebox.showinfo("Info",
"Le compte utilisateur a été mis à jour !\
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
            self.frame, "Retour", 8, 2, sticky= 'e', pady= 20,
            command= self.window.destroy)
