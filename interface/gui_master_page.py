
from tkinter import *
from gui_welcome_page import *
from gui_search_reference_page import *
from gui_create_reference_page import *

# master page: ###############################################################

class Master_page:

    def __init__(self):
        self.window = Tk()
        self.window.geometry("720x480")
        self.window.minsize(720,480)
        self.window.title("Domsdev Library")
        self.window.config(background= '#8B9089') # background color
        Welcome_page(self.window)

