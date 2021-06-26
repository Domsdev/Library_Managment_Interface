from tkinter import *
from tkinter import messagebox

from gui_frame_page import *
from gui_normalised_widgets import *
from gui_update_user_account_page import *

from connect_db import *

##############################################################################

class Search_user_account_top_page:

    def __init__(self):
        self.top_window = Toplevel()
        self.top_window.geometry("910x480")
        self.top_window.minsize(400,300)
        self.top_window.title("Domsdev Library")
        self.top_window.config(background= '#8B9089')
        Search_user_account_page(self.top_window)

##############################################################################

class Search_user_account_page(Frame_page):

    def __init__(self, window):
        super().__init__(window)
        
        self.title_page()
        self.subtitle_search()
        self.pseudo_field()
        self.first_name_field()
        self.last_name_field()
        self.phone_number_field()
        self.email_field()
        self.search_account_button()
        self.search_type()
        self.back_button()

        self.padx_column()

        self.subtitle_result()
        self.account_list()
        self.update_account_button()

##############################################################################

    def title_page(self): # .grid row = 1
        Normalised.title_N(
            self.frame, "Rechercher un compte utilisateur", 1, 1, 1, 4,
            sticky= 'we', pady= 15)

##############################################################################

    def subtitle_search(self): # .grid row = 2
        Normalised.label_N(
            self.frame, "Recherche par", 2, 1,
            pady= 5, color = "#8B9089", relief= 'flat')

##############################################################################

    def pseudo_field(self): # .grid row = 3
        Normalised.label_N(self.frame, "Pseudo", 3, 1, sticky= 'ew')
        self.pseudo_entry = Normalised.entry_N(self.frame, 3, 2)
        self.pseudo_entry.config(state='disabled')

        # check box
        self.pseudo_var = StringVar()
        Normalised.check_N(
            self.frame, "", 3, 0,
            variable= self.pseudo_var,
            command= self.config_pseudo)

    # check box command
    def config_pseudo(self):
        if self.pseudo_var.get() == 'Ok':
            self.pseudo_entry.config(state='normal')

        elif self.pseudo_var.get() == 'Not Ok':
            self.pseudo_entry.config(state='disabled')

##############################################################################

    def first_name_field(self): # .grid row = 4
        Normalised.label_N(self.frame, "Prénom", 4, 1, sticky= 'ew')
        self.first_name_entry = Normalised.entry_N(self.frame, 4, 2)
        self.first_name_entry.config(state='disabled')

        # check box
        self.first_name_var = StringVar()
        Normalised.check_N(
            self.frame, "", 4, 0,
            variable= self.first_name_var,
            command= self.config_first_name)

    # check box command
    def config_first_name(self):
        if self.first_name_var.get() == 'Ok':
            self.first_name_entry.config(state='normal')

        elif self.first_name_var.get() == 'Not Ok':
            self.first_name_entry.config(state='disabled')

##############################################################################

    def last_name_field(self): # .grid row = 5
        Normalised.label_N(self.frame, "Nom", 5, 1, sticky= 'ew')
        self.last_name_entry = Normalised.entry_N(self.frame, 5, 2)
        self.last_name_entry.config(state='disabled')

        # check box
        self.last_name_var = StringVar()
        Normalised.check_N(
            self.frame, "", 5, 0,
            variable= self.last_name_var,
            command= self.config_last_name)

    # check box command
    def config_last_name(self):
        if self.last_name_var.get() == 'Ok':
            self.last_name_entry.config(state='normal')
            
        elif self.last_name_var.get() == 'Not Ok':
            self.last_name_entry.config(state='disabled')

##############################################################################

    def phone_number_field(self): # .grid row = 6
        Normalised.label_N(self.frame, "N° Téléphone", 6, 1, sticky= 'ew')
        self.phone_number_entry = Normalised.entry_N(self.frame, 6, 2)
        self.phone_number_entry.config(state='disabled')

        # check box
        self.phone_number_var = StringVar()
        Normalised.check_N(
            self.frame, "", 6, 0,
            variable= self.phone_number_var,
            command= self.config_phone_number)

    # check box command
    def config_phone_number(self):
        if self.phone_number_var.get() == 'Ok':
            self.phone_number_entry.config(state='normal')
            
        elif self.phone_number_var.get() == 'Not Ok':
            self.phone_number_entry.config(state='disabled')

##############################################################################

    def email_field(self): # .grid row = 7
        Normalised.label_N(self.frame, "e-Mail", 7, 1, sticky= 'ew')
        self.email_entry = Normalised.entry_N(self.frame, 7, 2)
        self.email_entry.config(state='disabled')

        # check box
        self.email_var = StringVar()
        Normalised.check_N(
            self.frame, "", 7, 0,
            variable= self.email_var,
            command= self.config_email)

    # check box command
    def config_email(self):
        if self.email_var.get() == 'Ok':
            self.email_entry.config(state='normal')
            
        elif self.email_var.get() == 'Not Ok':
            self.email_entry.config(state='disabled')

##############################################################################

    def search_account_button(self): # .grid row = 8
        Normalised.button_N(
            self.frame, "Recherche", 8, 1, 1, 2, sticky= 'we', pady= 20,
            command= self.search_account_command)

    def search_account_command(self):
        
        search_dict = {}

        search_dict['pseudo']       = (self.pseudo_var.get(),
                                       self.pseudo_entry.get().strip()
                                       )
        search_dict['first_name']   = (self.first_name_var.get(),
                                       self.first_name_entry.get().strip()
                                       )
        search_dict['last_name']    = (self.last_name_var.get(),
                                       self.last_name_entry.get().strip()
                                       )
        search_dict['phone_number'] = (self.phone_number_var.get(),
                                       self.phone_number_entry.get().strip()
                                       )
        search_dict['email']        = (self.email_var.get(),
                                       self.email_entry.get().strip()
                                       )

        result_dict = connect_db('search user account', search_dict)
        # return a dictionary when 'search_account' find results:
        # {'first_name': [(8,), (9,)], 'last_name': [(8,), (10,), (15,)]}

        if result_dict != {}:

            ###########################################
            # prepare list of sets of id before choosing search type:

            set_list = []

            for column_result in result_dict:
                result_list_tupl = result_dict[column_result]
                set_list.append(set([k[0] for k in result_list_tupl]))

                # [k[0] for k in result_list_tuple]
                # use list comprehension to transform list of tuple 
                # in list of id
                # set() create a set from the precedent list

            # now we have a list of sets of account id
            # print(set_list)
            # set_list == [{8, 9}, {8, 10, 15}]  (for exemple)

            ###########################################
            # define Intersection and Union functions
            # inside search_account_command function:
            def Intersection(set_list):
                for i in range(len(set_list)-1):
                    set_list[i+1] = set_list[i] & set_list[i+1]

                return set_list[-1]

            def Union(set_list):
                for i in range(len(set_list)-1):
                    set_list[i+1] = set_list[i] | set_list[i+1]

                return set_list[-1]

            ###########################################
            # finaly select search type:
            if self.search_var.get() == 1:
                search_result = list(Intersection(set_list))

            elif self.search_var.get() == 2:
                search_result = list(Union(set_list))

            # search result is now a basic list of id

            ###########################################
            # clear Listbox ...
            self.account_box.delete(0, END)

            # and display results in the Listbox:
            if search_result == []:
                self.account_box.insert(END, "Aucun résultat !")

            else:
                # connect to dB and retrieve accounts data...
                account_data_list = connect_db(
                    'fetch account data', search_result)

                # ... and display results
                for k in range(len(account_data_list)):
                    self.account_box.insert(END,
                        "Id: {} - Pseudo: {}  /  {}  {}\
                        ".format(str(account_data_list[k][0]),
                                 account_data_list[k][1],
                                 account_data_list[k][2],
                                 account_data_list[k][3])
                                )


##############################################################################

    def search_type(self): # .grid row = 9

        self.search_var = IntVar()
        self.search_var.set(1)
        # need self. to define variable Intvar inside class

        Radiobutton(self.frame, text= "Intersection",
            bg= "#8B9089", font= ("Calibri", 10), fg = 'black',
            relief= 'flat', highlightthickness = 0,
            variable= self.search_var, value= 1).grid(row= 9, column= 1, sticky= 'w')

        Radiobutton(self.frame, text= "Union",
            bg= "#8B9089", font= ("Calibri", 10), fg = 'black',
            relief= 'flat', highlightthickness = 0,
            variable= self.search_var, value= 2).grid(row= 9, column= 2, sticky= 'w')

##############################################################################

    # add a space in column display
    def padx_column(self): # .grid row = 2
        Label(self.frame, text="   ", bg= "#8B9089").grid(
            row= 2, column= 3, padx= 5)

##############################################################################

    def subtitle_result(self): # .grid row = 2
        Normalised.label_N(
            self.frame, "Résultats de recherche", 2, 4, sticky= 'w',
            pady= 5, color = "#8B9089", relief= 'flat')

##############################################################################

    def account_list(self): # .grid row = 3

        # create a Scrollbar + Listbox for selection of an account

        self.scrollbar = Scrollbar(self.frame)
        self.scrollbar.grid(row= 3, column= 5,rowspan= 5, sticky= 'wns')
        
        self.account_box = Listbox(self.frame, width= 40, height= 8,
                                   font= ("Calibri", 11),
                                   yscrollcommand = self.scrollbar.set)
        self.account_box.grid(row= 3, column= 4, rowspan= 5, sticky= 'e')

        self.scrollbar.config(command= self.account_box.yview)

##############################################################################

    def update_account_button(self): # .grid row = 8

        # create selection button for item selection in account_list
        Normalised.button_N(
            self.frame, "Vérifier / Modifier", 8, 4, 1, 1,
            sticky= 'we', pady= 20,
            command= self.update_account_command)

    def update_account_command(self):

        if self.account_box.curselection() == ():
            self.error("Veuillez selectionner un compte ou modifier votre recherche")

        # get the selected item from account_box
        selected_account_string = self.account_box.get(
            self.account_box.curselection()
            )

        # transform recovered string in list
        # a list of id is needed for fetching data of an account
        selected_account = selected_account_string.split(' ')
        # selected_account == ['Id:', '16', '-', 'Pseudo:', 'Inactive', .....]

        # Keep only selected account Id number
        del selected_account[0]
        del selected_account[1:]

        if selected_account != ["Aucun résultat !"]:
            Top = Update_user_account_top_page()
            Update_user_account_page(Top.top_window, selected_account)

##############################################################################
    def error(self, type_error):
        # message box for errors during account selection
        messagebox.showerror("Erreur:", type_error, parent= self.window)


    def back_button(self): # .grid row = 9
        Normalised.button_N(
            self.frame, "Retour", 9, 4, sticky= 'e', pady= 0,
            command= self.window.destroy)
