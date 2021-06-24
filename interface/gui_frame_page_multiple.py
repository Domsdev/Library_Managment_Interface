
from tkinter import *

# frame page: ################################################################

class Frame_page_multiple:

    def __init__(self, window):
        self.window = window

        # add a space column in display
        # padx frame on left side #######################
        self.padx_frame = Frame(self.window, bg= '#8B9089')
        self.padx_frame.pack(side= LEFT, fill= Y)
        Label(self.padx_frame, text="", bg= "#8B9089", width= 3).pack()

        # global frame ##################################
        self.frame = Frame(self.window,
        	                bg= '#8B9089')
        self.frame.pack(expand= YES, fill= 'both')

        # define widget frames inside global frame:
        # frame 1 #######################################
        self.frame1 = Frame(self.frame, bg= '#8B9089')
        self.frame1.grid(row= 1, column= 1, columnspan= 2, pady= 5)


        # frame 4 #######################################
        self.frame4 = Frame(self.frame, bg= '#8B9089')
        self.frame4.grid(row= 3, column= 1, columnspan= 2, sticky= 'e')


        # frame 2 #######################################
        self.frame2 = Frame(self.frame, bg= '#8B9089')
        self.frame2.grid(row= 2, column= 1, sticky= 'nw')


        self.frame2_1 = Frame(self.frame2, bg= '#8B9089')
        self.frame2_1.grid(row= 1, sticky= 'nw', pady= 10)


        self.frame2_2 = Frame(self.frame2, bg= '#8B9089')
        self.frame2_2.grid(row= 2, sticky= 'nw')


        # frame 3 #######################################
        self.frame3 = Frame(self.frame, bg= '#8B9089')
        self.frame3.grid(row= 2, column= 2, sticky= 'ne')


        self.frame3_1 = Frame(self.frame3, bg= '#8B9089')
        self.frame3_1.grid(row= 1, sticky= 'ne', pady= 10)


        self.frame3_2 = Frame(self.frame3, bg= '#8B9089')
        self.frame3_2.grid(row= 2, sticky= 'ne')
