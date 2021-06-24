from tkinter import *

# Normalised Widgets: ########################################################

class Normalised:

    def title_N(frame_name, field_name, 
                row, column, 
                rs= 1, cs= 1,
                sticky= None,
                color = '#BDBCB5',
                relief= 'sunken',
                pady= 0,
                width= 0
                ):
                Label(
                    frame_name, text= field_name,
                    fg= 'black', font= ("Calibri", 20),
                    bg= color, relief= relief, width= width
                    ).grid(row= row, column= column,
                             rowspan= rs, columnspan= cs,
                             sticky= sticky, pady= pady
                             )

    def label_N(frame_name, text, 
                row, column, 
                rs= 1, cs= 1,
                sticky= None, pady= 0,
                color = '#BDBCB5',
                relief= 'groove',
                font= ("Calibri", 12),
                width= None
                ):
                label = Label(
                    frame_name, text= text,
                    fg= 'black', font= font,
                    bg= color, relief= relief, width= width
                    )
                label.grid(row= row, column= column,
                           rowspan= rs, columnspan= cs,
                           sticky= sticky, pady= pady
                           )
                return label

    def entry_N(frame_name, 
                row, column, 
                rs= 1, cs= 1,
                sticky= None, pady= 0,
                width=30,
                show= None,
                disabledbackground= None,
                disabledforeground= 'grey'
                ):
                entry_field = Entry(
                    frame_name,
                    font= ("Calibri", 12),
                    width= width, show= show,
                    disabledbackground= disabledbackground,
                    disabledforeground= disabledforeground
                    )
                entry_field.grid(row= row, column= column,
                                 rowspan= rs, columnspan= cs,
                                 sticky= sticky, pady= pady
                                 )
                return entry_field

    def button_N(frame_name, field_name, 
                 row, column, 
                 rs= 1, cs= 1,
                 sticky= None, pady= 0, width= 0,
                 color = '#BDBCB5',
                 relief= 'groove',
                 command= None
                 ):
                 button= Button(
                    frame_name, text= field_name,
                    fg= 'black', font= ("Calibri", 12), width= width,
                    bg= color, relief= relief, command= command
                    )
                 button.grid(row= row, column= column,
                             rowspan= rs, columnspan= cs,
                             sticky= sticky, pady= pady
                             )
                 return button

    def check_N(frame_name, field_name,
                row, column,
                rs= 1, cs= 1,
                variable= None,
                color = '#8B9089',
                relief= 'flat',
                sticky= None, pady= 0,
                width= 0,
                command= None
                ):
                check_button = Checkbutton(
                    frame_name, text= field_name,
                    variable= variable,
                    font= ("Calibri", 12), fg= 'black',
                    bg= color, relief= relief,
                    highlightthickness = 0,
                    width= width,
                    onvalue = "Ok", offvalue= "Not Ok",
                    command= command
                    )
                check_button.grid(row= row, column= column,
                                 rowspan= rs, columnspan= cs,
                                 sticky= sticky, pady= pady
                                 )
                check_button.deselect()
                return check_button


    def title_page(frame_name, field_name, r, c, color = '#BDBCB5'):
        Label(frame_name, text= field_name,
            fg= 'Black', font= ("Calibri", 20), bg= color, relief= 'sunken'
            ).grid(row= r, column= c, columnspan= 3, sticky= 'we', pady= 30)

    def label(frame_name, field_name, r, color = '#BDBCB5'):
        Label(frame_name, text= field_name, 
            fg= 'black', font= ("Calibri", 12), bg= color, relief= 'groove'
            ).grid(row= r, column= 0, sticky= 'we')

    def label_2(frame_name, field_name, r, c, color = '#BDBCB5'):
        Label(frame_name, text= field_name, 
            fg= 'black', font= ("Calibri", 12), bg= color, relief= 'groove'
            ).grid(row= r, column= c, sticky= 'we')

    def label_3(frame_name, field_name, r, c, color = '#BDBCB5'):
        Label(frame_name, text= field_name, 
            fg= 'black', font= ("Calibri", 12), bg= color, relief= 'groove'
            ).grid(row= r, column= c, rowspan= 3, sticky= 'nswe')

    def label_4(frame_name, field_name, r, c, color = '#BDBCB5'):
        Label(frame_name, text= field_name, 
            fg= 'black', font= ("Calibri", 12), bg= color, relief= 'groove'
            ).grid(row= r, column= c, sticky= 'we', pady = 10)

    def label_5(frame_name, field_name, r, c, color = '#BDBCB5'):
        Label(frame_name, text= field_name, 
            fg= 'black', font= ("Calibri", 12), bg= color, relief= 'groove'
            ).grid(row= r, column= c, rowspan= 2, sticky= 'nswe')

    def entry(frame_name, r, color = '#BDBCB5'):
        enter_field = Entry(frame_name, font= ("Calibri", 12), width="30")
        enter_field.grid(row= r, column= 1)
        return enter_field

    def entry_2(frame_name, r, c, color = '#BDBCB5'):
        enter_field = Entry(frame_name, font= ("Calibri", 12), width="40")
        enter_field.grid(row= r, column= 2, columnspan= 2)
        return enter_field

    def hide_entry(frame_name, r, color = '#BDBCB5'):
        enter_field = Entry(frame_name, show= '*', font= ("Calibri", 12),
                            width="30")
        enter_field.grid(row= r, column= 1)
        return enter_field

    def small_entry(frame_name, r, color = '#BDBCB5'):
        enter_field = Entry(frame_name, font= ("Calibri", 12), width="10")
        enter_field.grid(row= r, column= 1)
        return enter_field

    def button(frame_name, field_name, r, color = '#BDBCB5'):
        button = Button(frame_name, text= field_name,
            font= ("Calibri", 12), bg= color, fg='black')
        button.grid(row= r, column = 1, sticky= 'e', pady= 15)
        return button

    def button_2(frame_name, field_name, r, color = '#BDBCB5'):
        button = Button(frame_name, text= field_name,
            font= ("Calibri", 12), bg= color, fg='black')
        button.grid(row= r, columnspan = 2, sticky= 'we', pady= 10)
        return button

    def button_3(frame_name, field_name, r, color = '#BDBCB5'):
        button = Button(frame_name, text= field_name,
            font= ("Calibri", 10), bg= color, fg='black')
        button.grid(row= r, column= 0, sticky= 'w', pady= 10)
        return button

    def button_3_bis(frame_name, field_name, r, command, color = '#BDBCB5'):
        button = Button(frame_name, text= field_name,
            font= ("Calibri", 10), bg= color, fg='black', command= command)
        button.grid(row= r, column= 0, sticky= 'w', pady= 10)
        return button

    def button_4(frame_name, field_name, r, c, color = '#BDBCB5'):
        button = Button(frame_name, text= field_name,
            font= ("Calibri", 12), bg= color, fg='black')
        button.grid(row= r, column= c, sticky= 'we', pady= 10)
        return button

    def button_5(frame_name, field_name, r, c, color = '#BDBCB5'):
        button = Button(frame_name, text= field_name,
            font= ("Calibri", 12), bg= color, fg='black')
        button.grid(row= r, column= c, sticky= 'we', pady= 20, columnspan= 3)
        return button

    def button_6(frame_name, field_name, r, color = '#BDBCB5'):
        button = Button(frame_name, text= field_name,
            font= ("Calibri", 12), bg= color, fg='black')
        button.grid(row= r, column = 1, sticky= 'we', pady= 6)
        return button

    def load_button(frame_name, field_name, r, color = '#BDBCB5'):
        load_button = Button(frame_name, text= field_name,
            font= ("Calibri", 12), bg= color, fg='black')
        load_button.grid(row= r, column= 0, sticky= 'we', pady= 8)
        return load_button

    def load_button_2(frame_name, field_name, r, c, color = '#BDBCB5'):
        load_button = Button(frame_name, text= field_name,
            font= ("Calibri", 12), bg= color, fg='black')
        load_button.grid(row= r, column= c, sticky= 'we', pady= 6)
        return load_button

    def back_button(frame_name, field_name, r, command, color = '#BDBCB5'):
        back = Button(frame_name, text= field_name,
            font= ("Calibri", 10), bg= color, fg='black',
            command= command)
        back.grid(row= r, column= 1, sticky='e', pady= 20)
        return back

    def back_button_2(frame_name, field_name, command, r, c, color = '#BDBCB5'):
        back = Button(frame_name, text= field_name,
            font= ("Calibri", 10), bg= color, fg='black',
            command= command)
        back.grid(row= r, column= c, sticky='e', pady= 20)
        return back

    def back_button_3(frame_name, field_name, command, r, c, color = '#BDBCB5'):
        back = Button(frame_name, text= field_name,
            font= ("Calibri", 10), bg= color, fg='black',
            command= command)
        back.grid(row= r, column= c, sticky='w', pady= 20)
        return back



