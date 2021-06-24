from tkinter import *

# frame page extented: #######################################################

class Frame_page_extented:

    def __init__(self, window, data_list):
        self.window = window

        self.frame = Frame(self.window, bg= '#8B9089') 
        # Same color as background
        
        self.frame.pack(expand= YES)
        self.data_list = data_list