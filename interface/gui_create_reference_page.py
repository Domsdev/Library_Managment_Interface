from tkinter import *
from gui_frame_page import Frame_page
from gui_normalised_widgets import Normalised
from connect_db import connect_db
from connect_classification_db import connect_classification_db
from get_image_data import *

##############################################################################

class Create_reference_top_page:

    def __init__(self):
        self.top_window = Toplevel()
        self.top_window.geometry("720x700")
        self.top_window.minsize(400,300)
        self.top_window.title("Domsdev Library")
        self.top_window.config(background= '#8B9089')
        Create_reference_page(self.top_window)

##############################################################################

class Create_reference_page(Frame_page):

    def __init__(self, window):
        super().__init__(window)
        self.color_1 = "#8B9089"
        self.reference_type = 'None'

        self.title_page()
        self.reference_type_choice()
        self.reference_title()
        self.reference_theme()
        self.reference_abstract()
        self.classification_selection()
        self.load_cover()
        self.buying_price()
        self.loan_permission_choice()
        self.create_new_ref()
        self.back_button()

##############################################################################

    def title_page(self): # .grid row = 0
        Normalised.title_N(self.frame, "Nouvelle référence", 0, 1, 1, 2,
            pady= 30, sticky='we')

##############################################################################
    """
    def reference_type_choice(self): # .grid row = 1, 2, 3
        Normalised.label_N(self.frame, "Type", 1, 1, 3, 1,
            sticky= 'nswe')

        self.reference_var = IntVar()
        self.reference_var.set(1) # initialize

        reference_type_dict = {1: "Livre", 2:"Bande dessinée", 3:"Magazine"}

        command_dict = {"Livre": self.book_type,
                        "Bande dessinée": self.comic_type,
                        "Magazine": self.magazine_type}

        for k in reference_type_dict:

            b = Radiobutton(self.frame, text= reference_type_dict[k],
                bg= self.color_1, font= ("Calibri", 12), fg = 'black',
                relief= 'flat', highlightthickness= 0,
                variable= self.reference_var, value= k,
                command= command_dict[reference_type_dict[k]])
            b.grid(row= k, column= 2, sticky= 'w')

        if self.reference_var.get() == 1: # initialise fields
            self.book_type()
    """
##############################################################################

    def reference_type_choice(self): # .grid row = 1, 2, 3
        Normalised.label_N(self.frame, "Type", 1, 1, 3, 1,
            sticky= 'nswe')

        # type_list = connect_db("fetch type list", None)

        def Poison():
            print('Poison')

        def Remede():
            print('Remède')

        mb = Menubutton(self.frame, text='Type',
            bg= '#BDBCB5', font= ("Calibri", 12), fg = 'black',
            relief= 'raised', highlightthickness= 0)
        

        mb.menu = Menu(mb, tearoff=0)
        mb['menu'] = mb.menu

        mb.menu.add_command(label='Poison', command= Poison)
        mb.menu.add_command(label='Remède contre le coronavirus', command= Remede)

        mb.grid(row= 1, column= 2, sticky= 'we')

##############################################################################

    def book_type(self):
        self.author()
        self.isbn()
        self.reference_type = "Book"

    def comic_type(self):
        self.author()
        self.album()
        self.reference_type = "Comic"

    def magazine_type(self):
        self.volume()
        self.publication()
        self.reference_type = "Magazine"

##############################################################################

    def reference_title(self): # .grid row = 4
        Normalised.label_N(self.frame, "Titre", 4,1,
            sticky= 'we', pady= 4)
        self.reference_title_entry = Normalised.entry_N(self.frame, 4, 2,
            width= 45)

##############################################################################
        
    def author(self): # .grid row = 5
        Normalised.label_N(self.frame, "Auteur", 5, 1,
            sticky= 'we', pady= 4)
        self.author_entry = Normalised.entry_N(self.frame, 5, 2,
            width= 45)

    def isbn(self): # .grid row = 6
        Normalised.label_N(self.frame, "N° Isbn", 6, 1,
            sticky= 'we', pady= 4)
        self.isbn_entry = Normalised.entry_N(self.frame, 6, 2,
            width= 45)

    def album(self): # .grid row = 6
        Normalised.label_N(self.frame, "Album", 6,1,
            sticky= 'we', pady= 4)
        self.album_entry = Normalised.entry_N(self.frame, 6, 2,
            width= 45)

    def volume(self): # .grid row = 5
        Normalised.label_N(self.frame, "Volume", 5,1,
            sticky= 'we', pady= 4)
        self.volume_entry = Normalised.entry_N(self.frame, 5, 2,
            width= 45)

    def publication(self): # .grid row = 6
        Normalised.label_N(self.frame, "Publication", 6,1,
            sticky= 'we', pady= 4)
        self.publication_entry = Normalised.entry_N(self.frame, 6, 2,
            width= 45)
        self.publication_entry.insert(0, 'yyyy-mm-dd')

##############################################################################

    def reference_theme(self): # .grid row = 7
        Normalised.button_N(self.frame, "Thème(s)", 7, 1,
            sticky= 'we', pady= 4,
            command= self.theme_top_window)

        self.theme_field_entry = Normalised.entry_N(self.frame, 7,2,
            width= 45)

    def theme_top_window(self):
        # create Toplevel window and associated frame
        self.top_window = Toplevel()
        self.top_window.geometry("500x180")
        self.top_frame = Frame(self.top_window)
        self.top_frame.pack(expand= YES)
        
        self.theme_text()
        self.theme_text_ok()

    def theme_text(self):
        Label(self.top_frame, text= 'Thème').grid(row= 1, column= 1)

        self.theme_text_box = Text(
            self.top_frame,
            height= 4, width= 50, wrap=WORD
            )
        self.theme_text_box.grid(row= 2, column= 1, sticky= 'w')

        # insert text from subject_field_entry in the Text box
        self.theme_text_box.insert(END, self.theme_field_entry.get())

    def theme_text_ok(self):
        Button(self.top_frame, 
               text= "Ok", 
               command= self.theme_text_command
               ).grid(row= 3, column= 1)

    def theme_text_command(self):
        self.entered_theme = self.theme_text_box.get(1.0, 'end-1c')
        self.theme_field_entry.delete(0, END)
        self.theme_field_entry.insert(0, self.entered_theme)
        self.top_window.destroy()

##############################################################################

    def reference_abstract(self): # .grid row = 8
        Normalised.button_N(self.frame, "Résumé", 8, 1,
            sticky= 'we', pady= 4,
            command= self.abstract_top_window)

        self.abstract_field_entry = Normalised.entry_N(self.frame, 8,2,
            width= 45)


    def abstract_top_window(self):
    	# create Toplevel window and associated frame
        self.top_window = Toplevel()
        self.top_window.geometry("500x280")
        self.top_frame = Frame(self.top_window)
        self.top_frame.pack(expand= YES)
        
        self.abstract_text()
        self.abstract_text_ok()

    def abstract_text(self):
        Label(self.top_frame, text= 'Résumé').grid(row= 1, column= 1)

        self.scrollbar = Scrollbar(self.top_frame)
        self.scrollbar.grid(row= 2, column= 2,sticky= 'ns')

        self.abstract_text_box = Text(
            self.top_frame,
            yscrollcommand= self.scrollbar.set, 
            height= 10, width= 50, wrap=WORD
            )
        self.abstract_text_box.grid(row= 2, column= 1, sticky= 'w')

        self.scrollbar.config(command= self.abstract_text_box.yview)

        # insert text from abstract_field_entry in the Text box
        self.abstract_text_box.insert(END, self.abstract_field_entry.get())

    def abstract_text_ok(self):
        Button(self.top_frame, 
               text= "Ok", 
               command= self.abstract_text_command
               ).grid(row= 3, column= 1)

    def abstract_text_command(self):
        self.entered_abstract = self.abstract_text_box.get(1.0, 'end-1c')
        self.abstract_field_entry.delete(0, END)
        self.abstract_field_entry.insert(0, self.entered_abstract)
        self.top_window.destroy()

##############################################################################
##############################################################################
##############################################################################

    def classification_selection(self): # .grid row = 9
        Normalised.button_N(self.frame, "Classification", 9, 1,
            sticky= 'nswe', pady= 4,
            command= self.classification_top_window)

        self.classification_entry = Text(self.frame,
            width= 56, height= 4, wrap=WORD,
            font= ("Calibri", 10),
            foreground= 'black', background= '#D9D9D9')
        self.classification_entry.grid(row= 9, column= 2)
        self.classification_entry.config(state='disabled')


    def classification_top_window(self):
        self.classification_entry.config(state='normal')

    	# create Toplevel window
        self.top_window = Toplevel()
        self.top_window.title("")
        x, y = self.window.winfo_x(), self.window.winfo_y()
        self.top_window.geometry("1200x700")

        # Frames definition:

        # global frame ####################################
        self.top_frame = Frame(self.top_window)
        self.top_frame.pack(expand= YES)
        

        # title frame #####################################
        self.top_frame_title = Frame(self.top_frame)
        self.top_frame_title.grid(
            row= 1, column= 1, columnspan= 4, pady= 20)

        Label(self.top_frame_title,
            text= 'Classification Selection',
            font= ("Calibri", 14)).grid(
            row= 1, column= 1, columnspan= 1, sticky= 'we')

        # validation frame ################################
        self.top_frame_validation = Frame(self.top_frame)
        self.top_frame_validation.grid(
            row= 3, column= 1, columnspan= 4, pady= 30)

        # textbox to display info on specific category
        self.classification_selection_entry = Text(self.top_frame_validation,
            width= 122, height= 5, wrap=WORD,
            font= ("Calibri", 10),
            foreground= 'black', background= '#CCCCCC')
        self.classification_selection_entry.grid(row= 1, column= 1)
        self.classification_selection_entry.config(state='disabled')

        # validation button
        Button(self.top_frame_validation,
            text= 'Valider', bg= '#8B9089', fg= 'black',
            font= ("Calibri", 14),
            command= self.classification_validation).grid(
            row= 1, column= 2, sticky= 'nswe')
        # >> see: def classification_validation(self):

        # class frame #####################################
        self.top_frame_class = Frame(self.top_frame,
            bd= 3, bg= '#8B9089')
        self.top_frame_class.grid(
            row= 2, column= 1, sticky= 'nw')

        # division frame ##################################
        self.top_frame_division = Frame(self.top_frame,
            bd= 3, bg= '#8B9089')
        self.top_frame_division.grid(
            row= 2, column= 2, sticky= 'nw')

        # section frame ###################################
        self.top_frame_section = Frame(self.top_frame,
            bd= 3, bg= '#8B9089')
        self.top_frame_section.grid(
            row= 2, column= 3, sticky= 'nw')

        # subsection frame ################################
        self.top_frame_subsection = Frame(self.top_frame,
            bd= 3, bg= '#8B9089')
        self.top_frame_subsection.grid(
            row= 2, column= 4, sticky= 'nw')

        # initialize categories display
        self.class_select()
        self.division_select()
        self.section_select()
        self.subsection_select()

        # initialize classification display
        self.initialize_classification_display = True
        self.classification_display()

##############################################################################

    def class_select(self):
        # create label for class selection
        Label(self.top_frame_class, 
            text= 'Classe', width= 20,
            font= ("Calibri", 12)).grid(
            row= 1, column= 1, ipady= 6, sticky= 'we')

        # fetch class data
        q = connect_classification_db('fetch class data', None)

        # formating data to display on buttons
        self.class_dict = {}
        for k in range(len(q)):
            self.class_dict[k] = [q[k][0] + ": " + q[k][1]]

        # create and display radiobutton for class selection
        self.class_var = IntVar()
        self.class_var.set(0) # initialize variable

        for k in self.class_dict:
            b = Radiobutton(self.top_frame_class,
                text= self.class_dict[k][0],
                height= 2, justify= 'left', anchor= 'nw', indicator= 0,
                wraplength= 250, width= 32, font= ("Calibri", 10),
                variable= self.class_var, value= k,
                foreground = 'black', background= '#CCCCCC',
                activeforeground= 'black', activebackground= '#DEDEDE',
                command= self.classification_display)
            b.grid(row= k+2, column= 1)


    def division_select(self):
        vlist = self.class_dict[self.class_var.get()][0].split(':', 1)
        v = vlist[0][0]
        # vlist[0] in {000, 100, ..., 900}

        # fetch division data according to selected class and its first digit
        q = connect_classification_db('fetch division data', v)

        # clear division display...
        for widget in self.top_frame_division.winfo_children():
            widget.destroy()

        # ... and create division label
        Label(self.top_frame_division, 
            text= 'Division', width= 20,
            font= ("Calibri", 12)).grid(
            row= 1, column= 1, ipady= 6, sticky= 'we')

        # formating data to display on buttons
        q0 = self.class_dict[self.class_var.get()][0].split(':', 1)
        q.insert(0, (vlist[0], q0[1]))

        self.division_dict = {}
        for k in range(len(q)):
            self.division_dict[k] = [q[k][0] + ": " + q[k][1]]

        # create and display radiobutton for division selection
        self.division_var = IntVar()
        self.division_var.set(0) # initialize variable

        for k in self.division_dict:
            b = Radiobutton(self.top_frame_division,
                text= self.division_dict[k][0],
                height= 2, justify= 'left', anchor= 'nw', indicator= 0,
                wraplength= 250, width= 32, font= ("Calibri", 10),
                variable= self.division_var, value= k,
                foreground = 'black', background= '#CCCCCC',
                activeforeground= 'black', activebackground= '#DEDEDE',
                command= self.classification_display)
            b.grid(row= k+2, column= 1)


    def section_select(self):
        vlist = self.division_dict[self.division_var.get()][0].split(':', 1)
        v = vlist[0][:2]
        # vlist[0] in {300, 310, ..., 390} if selected class is 300

        # fetch section data according to selected division
        # and its two first digits
        q = connect_classification_db('fetch section data', v)

        # clear section display...
        for widget in self.top_frame_section.winfo_children():
            widget.destroy()

        # ... and create section label
        Label(self.top_frame_section, 
            text= 'Section', width= 20,
            font= ("Calibri", 12)).grid(
            row= 1, column= 1, ipady= 6, sticky= 'we')

        # formating data to display on buttons
        q0 = self.division_dict[self.division_var.get()][0].split(':', 1)
        q.insert(0, (vlist[0], q0[1]))

        self.section_dict = {}
        for k in range(len(q)):
            self.section_dict[k] = [q[k][0] + ": " + q[k][1]]

        # create and display radiobutton for class selection
        self.section_var = IntVar()
        self.section_var.set(0) # initialize variable

        for k in self.section_dict:
            b = Radiobutton(self.top_frame_section,
                text= self.section_dict[k][0],
                height= 2, justify= 'left', anchor= 'nw', indicator= 0,
                wraplength= 250, width= 32, font= ("Calibri", 10),
                variable= self.section_var, value= k,
                foreground = 'black', background= '#CCCCCC',
                activeforeground= 'black', activebackground= '#DEDEDE',
                command= self.classification_display)
            b.grid(row= k+2, column= 1)


    def subsection_select(self):
        vlist = self.section_dict[self.section_var.get()][0].split(':', 1)
        v = vlist[0]
        # vlist[0] in {000, 100, ..., 999}

        # fetch subsection data according to selected section
        q = connect_classification_db('fetch subsection data', v)

        # clear subsection display
        for widget in self.top_frame_subsection.winfo_children():
            widget.destroy()

        # ... and create subsection label
        Label(self.top_frame_subsection, 
            text= 'Sous-section', width= 20,
            font= ("Calibri", 12)).grid(
            row= 1, column= 1, ipady= 6, sticky= 'we')

        # create scrollbar
        self.scrollbar = Scrollbar(self.top_frame_subsection, 
                                   orient=VERTICAL, width= 12)
        self.scrollbar.grid(row= 2, column= 2, sticky= 'wns')

        # create canvas
        self.canevas = Canvas(self.top_frame_subsection,
            width= 250, height= 398)
        self.canevas.grid(row= 2, column= 1)

        # formating data to display on buttons
        q0 = self.section_dict[self.section_var.get()][0].split(':', 1)
        q.insert(0, (vlist[0], q0[1]))

        self.subsection_dict = {}
        for k in range(len(q)):
            self.subsection_dict[k] = [q[k][0] + ": " + q[k][1]]

        # create and display radiobutton for subsection selection
        self.subsection_var = IntVar()
        # self.subsection_var.set(0) # initialize variable

        i=0
        for k in self.subsection_dict:
            b = Radiobutton(self.canevas,
                text= self.subsection_dict[k][0],
                height= 2, justify= 'left', anchor= 'nw', indicator= 0,
                wraplength= 250, width= 32, font= ("Calibri", 10),
                variable= self.subsection_var, value= k,
                foreground = 'black', background= '#CCCCCC',
                activeforeground= 'black', activebackground= '#DEDEDE',
                command= self.classification_display)
            b.grid(row= k+2, column= 1)

            self.canevas.create_window(0, 0+i, anchor= 'nw', window= b)
            i+=40

        # configure canevas: attach scrollbar and all created radiobuttons
        self.canevas.configure(
            scrollregion= self.canevas.bbox('all'),
            yscrollcommand= self.scrollbar.set)

        # configure scrollbar: scroll canevas in vertical direction
        self.scrollbar.config(command= self.canevas.yview)

##############################################################################

    def classification_display(self):
        if self.initialize_classification_display == True:
            self.class_var_buffer = self.class_var.get()
            self.division_var_buffer = self.division_var.get()
            self.section_var_buffer = self.section_var.get()
            self.subsection_var_buffer = self.subsection_var.get()

            # writing selected classification info in
            # self.classification_selection_entry textbox
            self.classification_selection_entry.config(state='normal')
            self.classification_selection_entry.delete(1.0, END)
            self.classification_selection_entry.insert(1.0,
                self.class_dict[self.class_var.get()][0])
            self.classification_selection_entry.config(state='disabled')

        else:
            if self.class_var.get() != self.class_var_buffer:
                # after a clic on class button:
                # writing selected classification info in textbox
                self.classification_selection_entry.config(state='normal')
                self.classification_selection_entry.delete(1.0, END)
                self.classification_selection_entry.insert(1.0,
                self.class_dict[self.class_var.get()][0])
                self.classification_selection_entry.config(state='disabled')

                # updating child classifications and buffers
                self.division_select()
                self.section_select()
                self.subsection_select()
                self.class_var_buffer = self.class_var.get()
                self.division_var_buffer = self.division_var.get()
                self.section_var_buffer = self.section_var.get()
                self.subsection_var_buffer = self.subsection_var.get()
            
            elif self.division_var.get() != self.division_var_buffer:
                # after a clic on division button:
                # writing selected classification info in textbox
                self.classification_selection_entry.config(state='normal')
                self.classification_selection_entry.delete(1.0, END)
                self.classification_selection_entry.insert(1.0,
                self.division_dict[self.division_var.get()][0])
                self.classification_selection_entry.config(state='disabled')

                # updating child classifications and buffers
                self.section_select()
                self.subsection_select()
                self.division_var_buffer = self.division_var.get()
                self.section_var_buffer = self.section_var.get()
                self.subsection_var_buffer = self.subsection_var.get()

            elif self.section_var.get() != self.section_var_buffer:
                # after a clic on section button:
                # writing selected classification info in textbox
                self.classification_selection_entry.config(state='normal')
                self.classification_selection_entry.delete(1.0, END)
                self.classification_selection_entry.insert(1.0,
                self.section_dict[self.section_var.get()][0])
                self.classification_selection_entry.config(state='disabled')

                # updating child classifications and buffers
                self.subsection_select()
                self.section_var_buffer = self.section_var.get()
                self.subsection_var_buffer = self.subsection_var.get()

            elif self.subsection_var.get() != self.subsection_var_buffer:
                # after a clic on subsection button:
                # writing selected classification info in textbox
                self.classification_selection_entry.config(state='normal')
                self.classification_selection_entry.delete(1.0, END)
                self.classification_selection_entry.insert(1.0,
                self.subsection_dict[self.subsection_var.get()][0])
                self.classification_selection_entry.config(state='disabled')

                # updating buffer
                self.subsection_var_buffer = self.subsection_var.get()

        self.initialize_classification_display = False


    def classification_validation(self):
        # clear entry in new_reference_page
        self.classification_entry.delete(1.0, END)

        # write description of the selected category in new_reference_page
        c = self.classification_selection_entry.get(1.0, END)
        self.classification_entry.insert(1.0, c)
        self.classification_entry.config(state='disabled')
        self.top_window.destroy()

##############################################################################
##############################################################################
##############################################################################

    def load_cover(self): # .grid row = 10
        self.load_cover = Normalised.button_N(self.frame, "Couverture:",10, 1,
            sticky= 'we', pady= 4)
        self.load_cover.bind("<ButtonRelease-1>",self.get_cover)
        
        self.cover_file_name_entry = Normalised.entry_N(
            self.frame, 10, 2, width= 45, disabledforeground= 'black')
        self.cover_file_name_entry.config(state='disabled')

        self.cover_data = 'None'

    def get_cover(self, event):
        self.cover_file_name_entry.config(state='normal')
        self.cover_file_name_entry.delete(0, END)
        self.cover_data, self.cover_file_name = Get_image_data(self.window)
        self.cover_file_name_entry.insert(0, self.cover_file_name)
        self.cover_file_name_entry.config(state='disabled')

##############################################################################

    def buying_price(self): # .grid row = 11
        Normalised.label_N(self.frame, "Prix d'achat", 11, 1,
            sticky= 'we', pady= 4)
        self.buying_price_entry = Normalised.entry_N(self.frame, 11, 2,
            width= 45)

##############################################################################

    def loan_permission_choice(self): # .grid row = 12, 13
        Normalised.label_N(self.frame, "Prêt:", 12, 1, 2, 1,
            sticky= 'nswe')
        self.loan_permission = 'None'

        self.loan_var = IntVar()
        self.loan_var.set(1) # initialize

        b1 = Radiobutton(self.frame, text= "Autorisé", bg= self.color_1, 
        	             font= ("Calibri", 12), fg = 'black', relief= 'flat',
        	             highlightthickness = 0,
        	             variable= self.loan_var, value= 1)
        b1.grid(row= 12, column= 2, sticky= 'w')

        b2 = Radiobutton(self.frame, text= "Non autorisé", bg= self.color_1,
        	             font= ("Calibri", 12), fg = 'black', relief= 'flat',
        	             highlightthickness = 0,
        	             variable= self.loan_var, value= 0)
        b2.grid(row= 13, column= 2, sticky= 'w')
        
##############################################################################

    def create_new_ref(self): # .grid row = 17
        self.create_new_ref = Normalised.button_5(self.frame, "Créer", 17,1)
        self.create_new_ref.bind(
        	"<ButtonRelease-1>", self.create_new_reference_command)


    def create_new_reference_command(self,event):

        # define function to verify if given price is a float number
        def valid_buying_price():
            try:
                valid_price = float(self.buying_price_entry.get())
                return True
            except:
                return False

        new_reference_data = []

        # check if data has been entered correctly
        if self.reference_title_entry.get() == '':
        	self.error("Veuillez entrer un titre")

        elif (self.reference_type == "Book"
            and (self.author_entry.get() == ''
                 and self.isbn_entry.get() == '')):
            self.error("Veuillez entrer un auteur\
                (et le N° ISBN si existant)")

        elif (self.reference_type == "Comic"
            and (self.author_entry.get() == ''
                 and self.album_entry.get() == '')):
            self.error("Veuillez entrer un auteur\
                (et l'album si existant)")

        elif (self.reference_type == "Magazine"
        	  and (self.volume_entry.get == ''
                   or self.publication_entry.get() == 'yyyy-mm-dd')):
        	self.error("Veuillez entrer les informations sur le volume et la date de publication")

        elif self.classification_entry.get(1.0, "end-1c") =='':
            self.error("Veuillez choisir une classification")

        elif (self.buying_price_entry.get() == ''
              or not valid_buying_price()):
            self.error("\
Le prix d'achat doit être un nombre décimal (ou zéro)")


        else: # enter data in list
            new_reference_data.append(self.reference_type)               # [0]
            new_reference_data.append(self.reference_title_entry.get())  # [1]

            if self.reference_type == "Book":
                new_reference_data.append(self.author_entry.get())       # [2]
                new_reference_data.append(self.isbn_entry.get())         # [3]

            elif self.reference_type == "Comic":
                new_reference_data.append(self.author_entry.get())       # [2]
                new_reference_data.append(self.album_entry.get())        # [3]

            elif self.reference_type == "Magazine":
                new_reference_data.append(self.volume_entry.get())       # [2]
                new_reference_data.append(self.publication_entry.get())  # [3]

            if self.theme_field_entry.get() == '':
                new_reference_data.append('None')
            else:
                new_reference_data.append(
                self.theme_field_entry.get()
                )                                                        # [4]

            if self.abstract_field_entry.get() == '':
                new_reference_data.append('None')
            else:
                new_reference_data.append(
                self.abstract_field_entry.get()
                )                                                        # [5]

            c = self.classification_entry.get(1.0, "end-1c").split(':', 1)
            new_reference_data.append(c[0])                              # [6]

            new_reference_data.append(self.cover_data)                   # [7]

            new_reference_data.append(
                float(self.buying_price_entry.get())
                )                                                        # [8]

            new_reference_data.append(self.loan_var.get())               # [9]
            
            # formate data
            new_reference_data[1] = new_reference_data[1].strip()
            new_reference_data[2] = new_reference_data[2].strip()
            new_reference_data[3] = new_reference_data[3].strip()
            new_reference_data[4] = new_reference_data[4].strip()
            new_reference_data[5] = new_reference_data[5].strip()

            new_reference_data[1] = new_reference_data[1].capitalize()
            new_reference_data[2] = new_reference_data[2].capitalize()
            new_reference_data[3] = new_reference_data[3].capitalize()

            
            # connection to MySQL for registration in dB
            q,reference_id = connect_db('check reference', new_reference_data)

            if q == 'new': # create new reference in dB
                new_reference_data.append('new')                         #[10]
                # connection to MySQL for new reference creation in dB
                p = connect_db('new reference', new_reference_data)

                messagebox.showinfo("Info",
	        		"Nouvelle référence crée avec succès !\
\nVeuillez noter le code-barres pour cet exemplaire : \
{:08d}".format(p), parent= self.window)

                self.window.destroy()

            elif q == 'copy': # create copy reference in dB
                new_reference_data.append('copy')                        #[10]
                new_reference_data.append(reference_id)                  #[11]

                answer = messagebox.askokcancel(
	        		"Attention","La référence existe déjà\
	        		\nVoulez-vous enregistrer un nouvel exemplaire ?",
	        		parent= self.window)

                if answer == True:
                    # connection to MySQL for copy reference creation in dB
                    p = connect_db('new reference', new_reference_data)

                    messagebox.showinfo("Info",
	        		"Nouvel exemplaire crée avec succès !\
	        		\nVeuillez noter le code-barres \
                    pour cet exemplaire : {:08d} \
	        		\nLa classification pour cet exemplaire \
	        		est identique à sa référence.\
                    ".format(p), parent= self.window)

                    self.window.destroy()

            elif q == "Can't connect to MySQL server":
                self.error(f"{q}\nVeuillez contacter un administrateur")


    def error(self, type_error): # message box for errors during registration
        messagebox.showerror("Error:", type_error, parent= self.window)

##############################################################################

    def back_button(self): # .grid row = 18
        Normalised.button_N(self.frame, "Retour", 18, 2, sticky= 'e',
            command= self.window.destroy)
