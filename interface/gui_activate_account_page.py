from tkinter import *
from tkinter import messagebox

from gui_frame_page import *
from gui_normalised_widgets import *
from gui_login_page import Login_page

from connect_db import *
from get_image_data import *
from mail_password_validity import *

##############################################################################

class Activate_account_page(Frame_page):

    def __init__(self, window):
        super().__init__(window)
        
        self.title()
        self.subtitle()
        self.activation_code_field()
        self.activation_code_button()
        self.back_button()

##############################################################################

    def title(self): # .grid row = 1
        Normalised.title_N(self.frame, "Activation compte",
            1, 1, 1, 2, sticky='we')

##############################################################################

    def subtitle(self): # .grid row = 2
        self.subtitle_label = Normalised.label_N(
            self.frame, "Veuillez entrer votre code d'activation",
            2 ,1 , 1, 2,
            pady= 20, sticky= 'we', color = "#8B9089", relief= 'flat'
            )

##############################################################################

    def activation_code_field(self): # .grid row = 3
        self.activation_code_label = Normalised.label_N(
            self.frame, "Code d'activation", 3, 1, sticky= 'we', width= 15)
        self.activation_code_entry = Normalised.entry_N(
            self.frame, 3, 2, width= 15)

    def activation_code_button(self): # .grid row = 4
        self.activate_button = Normalised.button_N(
            self.frame, "Soumettre", 4, 1, 1, 2, sticky= 'we', pady= 20,
            command= self.check_activation_code)

    def check_activation_code(self):

        # get entered activation code
        if self.activation_code_entry.get() == '':
            self.error("Veuillez entrer votre code d'activation")

        else:
            self.login_list = []
            self.login_list.append(self.activation_code_entry.get())     # [0]

            # connection to database for activation code checking
            self.activate = connect_db('activate', self.login_list)
            print('check_activation_code--------self.activate', self.activate)

            if self.activate == "Can't connect to MySQL server":
                self.error(f"{q}\nVeuillez contacter un administrateur")
                self.back_command()

            elif self.activate == "code error":
                self.error("Code d'activation invalide !")
                self.activation_code_entry.delete(0, END)

            else:
                # destroy first widgets layout
                self.subtitle_label.destroy()
                self.activation_code_label.destroy()
                self.activation_code_entry.destroy()
                self.activate_button.destroy()

                if self.activate == "new user":
                    # display activation widgets for new user
                    self.subtitle_activate()
                    self.pseudo_field()
                    self.password_field()
                    self.confirm_field()
                    self.activate_account_button()

                else:
                    # display re-activation widgets for existing user
                    self.subtitle_reactivate()
                    self.password_field()                
                    self.confirm_field()
                    self.check_box_password()
                    self.activate_account_button()


    def error(self, type_error):
        messagebox.showerror("Erreur", type_error)

##############################################################################

    def subtitle_activate(self): # .grid row = 2
        Normalised.label_N(
            self.frame, """Choisissez soigneusement vos Pseudo et Mot de pass,
            le choix du Pseudo est définitif.""",
            2 ,1 ,1 ,2, 
            pady= 20, sticky= 'we', color = "#8B9089", relief= 'flat')

##############################################################################

    def subtitle_reactivate(self): # .grid row = 2
        Normalised.label_N(
            self.frame, f"""Hello {self.activate} !
Cochez la case si vous souhaitez réinitialiser votre Mot de pass,
sinon pressez le bouton 'Activation'""",
             2 ,1 ,1 ,2, 
            pady= 20, sticky= 'we', color = "#8B9089", relief= 'flat')

##############################################################################

    def pseudo_field(self): # .grid row = 3
        Normalised.label_N(self.frame, "Pseudo", 3, 1, sticky= 'we', pady= 5)
        self.pseudo_entry = Normalised.entry_N(self.frame, 3, 2)
        
    def password_field(self): # .grid row = 4
        Normalised.label_N(self.frame, "Mot de pass", 4, 1, sticky= 'we')
        self.password_entry = Normalised.entry_N(self.frame, 4, 2, show= '*')

    def confirm_field(self): # .grid row = 5
        Normalised.label_N(self.frame, "Confirmation", 5, 1, sticky= 'we')
        self.confirm_entry = Normalised.entry_N(self.frame, 5, 2, show= '*')

##############################################################################

    def check_box_password(self): # .grid row = 4
        self.password_entry.config(state='disabled')
        self.confirm_entry.config(state='disabled')

        # check box
        self.password_var = StringVar()
        Normalised.check_N(
            self.frame, "", 4, 0,
            variable= self.password_var,
            command= self.config_password)

    # check box command
    def config_password(self):
        if self.password_var.get() == 'Ok':
            self.password_entry.config(state='normal')
            self.confirm_entry.config(state='normal')

        elif self.password_var.get() == 'Not Ok':
            self.password_entry.config(state='disabled')
            self.confirm_entry.config(state='disabled')

##############################################################################

    def activate_account_button(self): # .grid row = 6
        Normalised.button_N(
            self.frame, "Activation", 6, 1, 1, 2, sticky= 'we', pady= 20,
            command= self.activate_account)

##############################################################################

    def activate_account(self):

        ######### define checking functions
        def check_pseudo():
            if self.pseudo_entry.get() == '':
                self.error("Veuillez entre votre Pseudo")
            else:
                return True

        def check_password():
            if self.password_entry.get() == '':
                self.error("Veuillez entrer votre Mot de pass et confirmer")

            elif self.confirm_entry.get() == '':
                self.error("Veuillez confirmer votre Mot de pass")

            # check if password and confirmation are equal
            elif self.password_entry.get() != self.confirm_entry.get():
                print('check_password------------', self.password_entry.get())
                print('check_password-------------', self.confirm_entry.get())
                self.error("Erreur de confirmation de votre Mot de pass !\
                    \nEssayez de nouveau ou modifiez votre Mot de pass")

            # check validity of password format
            elif password_validity(self.password_entry.get()) == False:
                self.error("Mot de pass invalide\
                            \nVous ne pouvez utiliser d'espace\
                             dans votre Mot de pass")
                self.password_entry.delete(0, 'end')
                self.confirm_entry.delete(0, 'end')
            else:
                print('check_password------------------check password = True')
                return True

        ######### define activate connect to db function
        def activate_connect_db():
            q = connect_db('activate', self.login_list)
            print('activate_connect_db----------------------------------q', q)

            if q == True:
                self.frame.destroy()
                messagebox.showinfo("Info", "Votre compte est activé")
                Login_page(self.window)

            elif q == False:
                del self.login_list[-1]
                del self.login_list[-1]
                self.error("Pseudo already used\nTry another one")

            elif q == "Can't connect to MySQL server":
                self.error(f"{q}\nPlease contact administrator")


        ######### check validity of entered coordinates and connect to db
        if self.activate == 'new user':
            if check_pseudo():
                if check_password():
                    self.login_list.append(self.pseudo_entry.get())      # [1]
                    self.login_list.append(self.password_entry.get())    # [2]
                    print('activate_connect_db---login_list', self.login_list)
                    activate_connect_db()

        elif self.activate != 'new user' and self.password_var.get() == 'Ok':
            if check_password():
                self.login_list.append(self.activate)                    # [1]
                self.login_list.append(self.password_entry.get())        # [2]
                print('activate_connect_db-------login_list', self.login_list)
                activate_connect_db()

        else:
            self.login_list.append(self.activate)                        # [1]
            print('activate_connect_db-----------login_list', self.login_list)
            activate_connect_db()


##############################################################################

    def back_button(self): # .grid row = 7
        self.back_button = Normalised.button_N(
            self.frame, "Retour", 7, 2, sticky= 'e',
            command= self.back_command)

    def back_command(self):
        self.frame.destroy()
        from gui_welcome_page import Welcome_page
        # placed here because of circular dependancy
        Welcome_page(self.window)