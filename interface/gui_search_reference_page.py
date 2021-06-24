from tkinter import *
from tkinter import messagebox

from gui_frame_page_multiple import *
from gui_normalised_widgets import *

from connect_db import *

##############################################################################

class Search_reference_top_page:

    def __init__(self):
        self.top_window = Toplevel()
        self.top_window.geometry("1105x560")
        self.top_window.minsize(1105, 560)
        self.top_window.title("Domsdev Library")
        self.top_window.config(background= '#8B9089')
        Search_reference_page(self.top_window)

##############################################################################

class Search_reference_page(Frame_page_multiple):

    def __init__(self, window):
        super().__init__(window)
        
        # frame 1 #############
        self.title_page()
        self.subtitle_result()
        self.subtitle_search()

        # frame 2 #############
        self.search_type()
        
        # frame 3 #############
        self.result_info()
        self.result_box()
        self.view_result()

        # frame 4 #############
        self.back_button()


# frame 1 ####################################################################

    def title_page(self): # .grid row = 1
        Normalised.title_N(
            self.frame1, "Rechercher une référence", 1, 1, 1, 2,
            sticky= 'we', pady= 20, width= 61)

    def subtitle_result(self): # .grid row = 2
        self.search_subtitle = Normalised.label_N(
            self.frame1, "Search results", 2, 2, sticky= 'e',
            color = "#8B9089", relief= 'flat', font= ("Calibri", 14))

    def subtitle_search(self): # .grid row = 2
        self.search_subtitle = Normalised.label_N(
            self.frame1, "Search type", 2, 1, sticky= 'w',
            color = "#8B9089", relief= 'flat', font= ("Calibri", 14))
        self.search_subtitle.bind("<Enter>", self.enter_info)
        self.search_subtitle.bind("<Leave>", self.leave_info)

    def enter_info(self, event):
        self.search_subtitle.unbind("<Enter>")
        self.info_popup_window = Toplevel()
        self.info_popup_window.geometry("+400+280")
        self.info_popup_window.title("Info")

        self.info_popup_label = Label(
            self.info_popup_window,
            font= ("Calibri", 10), justify= 'left',
            text= """\
Extented search:
   Enter whatever you want (words, names, titles, dates, numbers, etc...).
   This type of search will create multiple search keys with query elements
   (each element alone, combination of elements), and will try to find a
   correspondence with elements in tables of the database.

Custom search:
   This type of search is more specific.
   Select the type of ressource you are searching for (default type
   is book), enter a title, author name, isbn number, album title for a
   comic, publication date for a magazine, and add keywords if needed.
   These elements will be multiple searching keys to find a
   correspondence with elements in database according to each field
   respectively.

Note:
   Each element will be compared to nearby elements in database in order to 
   insure a result in case of orthographic mistake with given elements."""
   )
        
        self.info_popup_label.pack(ipadx= 10, ipady= 10)

    def leave_info(self, event):
        self.info_popup_window.destroy()
        self.search_subtitle.bind("<Enter>", self.enter_info)

# frame 2_1 ##################################################################

    def search_type(self): # .grid row = 3

        self.search_var = IntVar()
        self.search_var.set(1)
        # need self. to define variable Intvar inside class

        Radiobutton(self.frame2_1, text= "Extented search",
            bg= "#8B9089", font= ("Calibri", 12), fg= 'black',
            relief= 'flat', highlightthickness= 0,
            variable= self.search_var, value= 1,
            command= self.extented_search_display).grid(
            row= 3, column= 1, sticky= 'w')

        Radiobutton(self.frame2_1, text= "custom search",
            bg= "#8B9089", font= ("Calibri", 12), fg= 'black',
            relief= 'flat', highlightthickness = 0,
            variable= self.search_var, value= 2,
            command= self.custom_search_display).grid(
            row= 3, column= 2, sticky= 'w')

        if self.search_var.get() == 1: # initialise search fields
            self.extented_search_display()

# frame 2_2 ##################################################################

    def extented_search_display(self): # .grid row = 1
        for widget in self.frame2_2.winfo_children():
            widget.destroy()

        self.extented_search_entry = Text(self.frame2_2,
            width= 55, height= 4, wrap=WORD, font= ("Calibri", 12))
        self.extented_search_entry.grid(row= 1, column= 1, columnspan= 2)

        self.search_button()

# frame 2_2 ##################################################################

    def custom_search_display(self):
        for widget in self.frame2_2.winfo_children():
            widget.destroy()

        self.ressource_type_choice()
        self.title_search()
        self.category_search()
        self.keyword_search()
        self.search_button()


    def ressource_type_choice(self): # .grid row = 1
        Normalised.label_N(self.frame2_2, "Ressource\ntype",
            1, 1, 3, sticky= 'nswe')

        self.ressource_var = IntVar()
        self.ressource_var.set(1) # initialize

        ressource_type_dict = {1: "Book", 2:"Comic", 3:"Magazine"}

        command_dict = {"Book": self.book_type,
                        "Comic": self.comic_type,
                        "Magazine": self.magazine_type}

        for k in ressource_type_dict:

            b = Radiobutton(self.frame2_2, text= ressource_type_dict[k],
                bg= "#8B9089", font= ("Calibri", 12), fg = 'black',
                relief= 'flat', highlightthickness= 0,
                variable= self.ressource_var, value= k,
                command= command_dict[ressource_type_dict[k]])
            b.grid(row= k, column= 2, sticky= 'w')

        if self.ressource_var.get() == 1: # initialise fields
            self.book_type()


    def title_search(self): # .grid row = 4
        Normalised.label_N(self.frame2_2, "Title",
            4, 1, width= 9, sticky= 'we')
        self.title_search_entry = Normalised.entry_N(
            self.frame2_2, 4, 2, width= 45)

    def book_type(self):
        self.author()
        self.isbn()
        self.ressource_type = "Book"

    def comic_type(self):
        self.author()
        self.album()
        self.ressource_type = "Comic"

    def magazine_type(self):
        self.volume()
        self.publication()
        self.ressource_type = "Magazine"


    def author(self): # .grid row = 5
        Normalised.label_N(self.frame2_2, "Author", 5, 1, sticky= 'we')
        self.author_entry = Normalised.entry_N(self.frame2_2, 5, 2, width= 45)

    def isbn(self): # .grid row = 6
        Normalised.label_N(self.frame2_2, "ISBN", 6, 1, sticky= 'we')
        self.isbn_entry = Normalised.entry_N(self.frame2_2, 6, 2, width= 45)

    def album(self): # .grid row = 6
        Normalised.label_N(self.frame2_2, "Album", 6, 1, sticky= 'we')
        self.album_entry = Normalised.entry_N(self.frame2_2, 6, 2, width= 45)

    def volume(self): # .grid row = 5
        Normalised.label_N(self.frame2_2, "Volume", 5, 1, sticky= 'we')
        self.volume_entry = Normalised.entry_N(self.frame2_2, 5, 2, width= 45)

    def publication(self): # .grid row = 6
        Normalised.label_N(self.frame2_2, "Publication", 6, 1, sticky= 'we')
        self.publication_entry = Normalised.entry_N(self.frame2_2, 6, 2, width= 45)
        self.publication_entry.insert(0, 'yyyy-mm-dd')

# frame 2_2 ##################################################################

    def category_search(self): # .grid row = 7

        self.category_field = Normalised.button_N(
            self.frame2_2, "Category", 7, 1, pady= 6,
            command= self.category_top_window)

        self.category_field_entry = Normalised.entry_N(
            self.frame2_2, 7, 2, width= 45, disabledforeground= 'black')
        self.category_field_entry.config(state='disabled')

    def category_top_window(self):
        # create Toplevel window and associated frame
        self.top_window = Toplevel()
        self.top_window.title("")
        x, y = self.window.winfo_x(), self.window.winfo_y()
        self.top_window.geometry("320x420+{}+{}".format(x-200, y+100))
        self.top_frame = Frame(self.top_window)
        self.top_frame.pack(expand= YES)

        self.category_field_entry.config(state='normal')
        
        self.category_selection()
        self.category_action()

    def category_selection(self):

        # select category from list
        Label(self.top_frame, 
            text= 'Category selection',
            font= ("Calibri", 12)).grid(
            row= 1, column= 1, columnspan= 2, pady= 10, sticky= 'we')

        # fetch category list from database:
        category_list = connect_db('fetch category list', [])

        # create a Scrollbar + Listbox for selection of the category
        self.scrollbar = Scrollbar(self.top_frame)
        self.scrollbar.grid(
            row= 2, column= 3,sticky= 'ns')
        
        self.category_box = Listbox(self.top_frame, width= 35,
                                    yscrollcommand = self.scrollbar.set)
        self.category_box.grid(
            row= 2, column= 1, columnspan= 2,sticky= 'w')

        self.scrollbar.config(command= self.category_box.yview)

        for category in category_list:
            category = category[0]
            self.category_box.insert(END, category)

    def category_action(self):

        # insert a space in layout
        Label(self.top_frame).grid(
            row= 5, column= 1, columnspan= 2)

        # add button
        Button(self.top_frame, text= "Add", bg= "#424242",
            command= self.add_category_command).grid(
            row= 6, column= 1, sticky= 'we')

        # clear button
        Button(self.top_frame, text= "Clear", bg= "#424242",
            command= self.clear_category_command).grid(
            row= 6, column= 2, sticky= 'we')

        # ok button
        Button(self.top_frame, text= "Ok", bg= "#424242",
            command= self.validation_command).grid(
            row= 7, column= 1, columnspan= 2, sticky= 'we')

    def add_category_command(self):
        # add the selected item in 'self.category_field_entry'
        selected_category = self.category_box.get(
                                 self.category_box.curselection()
                                 )
        self.category_field_entry.insert("end", selected_category)
        self.category_field_entry.insert("end", ", ")

    def clear_category_command(self):
        self.category_field_entry.delete(0, END)

    def validation_command(self):
        self.top_window.destroy()
        self.category_field_entry.config(state='disabled')

# frame 2_2 ##################################################################

    def keyword_search(self): # .grid row = 8
        Normalised.label_N(self.frame2_2, "Keywords",
            8, 1, width= 9, sticky= 'we')
        self.title_search_entry = Normalised.entry_N(
            self.frame2_2, 8, 2, width= 45)

    def search_button(self): # .grid row = 9
        Normalised.button_N(
        self.frame2_2, "Search", 9, 1, 1, 2,
        sticky= 'we', pady= 20, width= 32,
        command= self.search_command
        )

# frame 2_2 ##################################################################

    def search_command(self):
        self.reference_box.delete(0, END)

        if self.search_var.get() == 1:
            self.extented_search_command()

        elif self.search_var.get() == 2:
            self.custom_search_command()


    def extented_search_command(self):

        search_query = self.extented_search_entry.get(0.0, 'end-1c')
        q = connect_db('extented search', search_query)

        if q == []:
            self.result_info_label['text'] = "No result found"

        else:
            if len(q) > 1:
                self.result_info_label['text'] = f"{len(q)} results found"
            elif len(q) == 1:
                self.result_info_label['text'] = "1 result found"

            for k in range(len(q)):
                self.reference_box.insert(END, f"{k+1}: " + q[k][1])


    def custom_search_command(self):
        search_list = []
        search_list.append(self.extented_search_entry.get())
        q = connect_db('custom search', search_list)


# frame 3_1 ##################################################################

    def result_info(self): # .grid row = 1
        self.result_info_label = Normalised.label_N(
            self.frame3_1, "", 1, 1, sticky= 'e',
            color = "#8B9089", relief= 'flat', font= ("Calibri", 12))

# frame 3_2 ##################################################################

    def result_box(self): # .grid row = 1

        # create Listbox + Scrollbar for selection of a reference

        self.scrollbar = Scrollbar(self.frame3_2)
        self.scrollbar.grid(row= 1, column= 2,rowspan= 5, sticky= 'wns')
        
        self.reference_box = Listbox(self.frame3_2, width= 50, height= 14,
                                   font= ("Calibri", 11),
                                   yscrollcommand = self.scrollbar.set)
        self.reference_box.grid(row= 1, column= 1, rowspan= 5, sticky= 'e')

        self.scrollbar.config(command= self.reference_box.yview)


    def view_result(self): # .grid row = 6
        Normalised.button_N(
        self.frame3_2, "View selected result", 6, 1, 1, 2,
        sticky= 'we', pady= 10,
        command= self.view_result_command
        )

    def view_result_command(self):
        pass

# frame 4 ####################################################################

    def back_button(self): # .grid row = 1
        Normalised.button_N(
            self.frame4, "Back", 1, 1, sticky= 'e', pady= 15,
            command= self.window.destroy)
