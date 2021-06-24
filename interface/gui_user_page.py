from tkinter import *
from tkinter import messagebox

from gui_frame_page_extented import Frame_page_extented
from gui_normalised_widgets import *
from gui_search_reference_page import *

##############################################################################

class User_page(Frame_page_extented):

    def __init__(self, window, login_list):
        super().__init__(window, login_list)
        self.color = '#BDBCB5'

        self.pseudo = login_list[0]
        
        self.title()
        self.search_reference()
        self.loan()
        self.loan_return()
        self.book_list()
        self.quit()

##############################################################################

    def title(self): # .grid row = 1
        Normalised.title_N(self.frame, "Welcome {}".format(self.pseudo),
            1, 1, pady= 30, sticky='we')

##############################################################################

    def search_reference(self): # .grid row = 2
        self.search_button = Normalised.button_N(
            self.frame, "Search reference", 2, 1, sticky= 'we',
            command= Search_reference_top_page)

##############################################################################

    def loan(self): # .grid row = 3
        self.search_button = Normalised.button_N(
            self.frame, "Loan", 3, 1, sticky= 'we',
            command= self.loan_command)

    def loan_command(self):
        pass

##############################################################################

    def loan_return(self): # .grid row = 4
        self.search_button = Normalised.button_N(
            self.frame, "Return", 4, 1, sticky= 'we',
            command= self.loan_return_command)

    def loan_return_command(self):
        pass

##############################################################################

    def book_list(self): # .grid row = 5
        self.search_button = Normalised.button_N(
            self.frame, "My book list", 5, 1, sticky= 'we',
            command= self.book_list_command)

    def book_list_command(self):
        pass

##############################################################################

    def quit(self): # .grid row = 6
        self.quit_button = Normalised.button_N(
            self.frame, "Logout", 6, 1, sticky= 'e', pady= 30,
            command= self.quit_command)

    def quit_command(self):
        answer = messagebox.askokcancel("Warning","Ready to logout ?")
        if answer == True:
            self.frame.destroy()
            from gui_welcome_page import Welcome_page
            Welcome_page(self.window)

