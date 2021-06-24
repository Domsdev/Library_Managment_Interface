
##############################################################################
# PERSONAL EXERCICE : LIBRARY
##############################################################################
# > Create a system that manages loans and returns in a library.
# > The library manage books and magazines.
# > A book is characterised by its title, author and ISBN code.
# > A magazine is characterised by its title, volume number and release date.
# > Each copy is characterised by its library's bar code.
# > To borrow a book, a user must be registered.
# > A user can register by choosing a pseudo and password,
#       then, by entering his full name, telephone number, city
#       and make a money deposit.
# > Each book or magazine has a specific deposit.
# > A user can borrow a book only if
#       the deposit left on his account is greater to the deposit of the book.
# > The duration of the loan is fixed to 15 days.
# > One can not borrow more than one copy of the same ressource.
# > One can not borrow a new ressource if late to bring back other ressources.
# > The storage place of a book in the library is represented by
#       aisle, stand and shelf numbers.
# > All copies of the same ressource are stored at he same place.
##############################################################################

import smtplib, ssl
from tkinter import *
from gui_master_page import *


if __name__ == '__main__':
	library = Master_page()
	library.window.mainloop()
