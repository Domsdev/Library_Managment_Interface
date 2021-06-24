from tkinter import *
from tkinter import messagebox

from gui_frame_page import *
from gui_normalised_widgets import *
from gui_search_reference_page import *

##############################################################################

class Administrator_page(Frame_page):

    def __init__(self, window):
        super().__init__(window)
        self.color = '#BDBCB5'
        
        self.title()
        self.search_reference()
        self.create_librarian_account()
        self.buy_new_reference()
        self.statistics()
        self.quit()

##############################################################################

    def title(self): # .grid row = 1
        Normalised.title_N(self.frame, "Welcome Administrator",
            1, 1, pady= 30, sticky='we')

##############################################################################

    def search_reference(self): # .grid row = 2
        self.search_button = Normalised.button_N(
            self.frame, "Search reference", 2, 1, sticky= 'we',
            command= Search_reference_top_page)

##############################################################################

    def create_librarian_account(self): # .grid row = 3
        self.search_button = Normalised.button_N(
            self.frame, "Create librarian account", 3, 1, sticky= 'we',
            command= self.librarian_command)

    def librarian_command(self):
        pass

##############################################################################

    def buy_new_reference(self): # .grid row = 4
        self.search_button = Normalised.button_N(
            self.frame, "Buy new reference", 4, 1, sticky= 'we',
            command= self.new_reference_command)

    def new_reference_command(self):
        pass

##############################################################################

    def statistics(self): # .grid row = 5
        self.statistic_button = Normalised.button_N(
            self.frame, "Statistics", 5, 1, sticky= 'we',
            command= self.statistics_command)

    def statistics_command(self):
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
