from tkinter import *
from tkinter import messagebox

from gui_frame_page import *
from gui_normalised_widgets import *
from gui_user_page import *
from gui_librarian_page import *
from gui_administrator_page import *

from connect_db import *

##############################################################################

class Login_page(Frame_page):

    def __init__(self, window):
        super().__init__(window)

        self.title()
        self.pseudo_field()
        self.password_field()
        self.login()
        self.back()

##############################################################################

    def title(self): # .grid row = 1
        Normalised.title_N(self.frame, "Connexion", 1, 1, 1, 2, 
            pady= 30, sticky='we')

##############################################################################

    def pseudo_field(self): # .grid row = 2
    	Normalised.label_N(self.frame, "Pseudo", 2, 1, sticky= 'we')
    	self.pseudo_entry = Normalised.entry_N(self.frame, 2, 2)

    def password_field(self): # .grid row = 3
    	Normalised.label_N(self.frame, "Mot de pass", 3, 1, sticky= 'we')
    	self.password_entry = Normalised.entry_N(self.frame, 3, 2, show= '*')

##############################################################################

    def login(self): # .grid row = 4

        self.login_button = Button(
            self.frame, text= "Entrer", 
            font= ("Calibri", 12), 
            bg= '#BDBCB5', fg='black')

        self.login_button.grid(row= 4, column= 1, columnspan= 2,
            sticky= 'we', pady= 20)

        self.login_button.bind("<ButtonRelease-1>",self.check_id)


    def check_id(self,event): # check (pseudo + password) for login

        login_list = []
        login_list.append(self.pseudo_entry.get())     # [0]
        login_list.append(self.password_entry.get())   # [1]

        # connection to database + login check (pseudo, password)
        q = connect_db('login', login_list)

        if q == "user": # pseudo + password + activation OK
            self.frame.destroy()
            messagebox.showinfo("Info","Connecté en tant qu'utilisateur")
            User_page(self.window, login_list)

        elif q == "activation":
            self.error(
"Le compte doit être activé avant connexion !\
\nVeuillez vérifier votre boite mail pour connaître votre code d'activation.")
            self.back_command()

        elif q == "librarian":
            self.frame.destroy()
            messagebox.showinfo("Info","Connecté en tant que bibliothécaire")
            Librarian_page(self.window, login_list)

        elif q == "administrator":
            self.frame.destroy()
            messagebox.showinfo("Info","Connecté en tant qu'administrateur")
            Administrator_page(self.window)

        elif q == "pseudo error": # pseudo error
            self.error("Pseudo introuvable")

        elif q == "password error": # password error
            self.error("Mot de pass invalide")
            self.password.delete(0, 'end')

        elif q == "Can't connect to MySQL server": 
            # connection to server failed
            self.error(f"{q}\nVeuillez contacter un administrateur")

    def error(self, type_error):
        messagebox.showerror("Error", type_error)

##############################################################################

    def back(self): # .grid row = 5
        self.back_button = Normalised.button_N(
            self.frame, "Retour", 5, 2, sticky= 'e',
            command= self.back_command)

    def back_command(self):
        self.frame.destroy()
        from gui_welcome_page import Welcome_page
        # placed here because of circular dependancy
        Welcome_page(self.window)