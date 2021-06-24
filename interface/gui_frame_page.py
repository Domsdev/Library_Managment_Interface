
from tkinter import *

# frame page: ###############################################################

class Frame_page:

    def __init__(self, window):
        self.window = window
        self.frame = Frame(self.window, bg= '#8B9089') # Same color as background
        self.frame.pack(expand= YES)