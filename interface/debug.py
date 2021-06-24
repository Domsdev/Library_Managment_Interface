
#############################################################################
# Test: Menubutton widget
from tkinter import *

def Poison():
	print('Poison')

def Remede():
	print('Remède')

root = Tk()

root.geometry('100x200')

mb = Menubutton(root, text='condiments', relief='raised')
mb.grid()

mb.menu = Menu(mb, tearoff=0)
mb['menu'] = mb.menu

mb.menu.add_command(label='Poison', command= Poison)
mb.menu.add_command(label='Remède', command= Remede)

root.mainloop()

"""
##############################################################################
# Test: Labels inside a Canvas with scrollbar
import tkinter as tk

root = tk.Tk()

canvas = tk.Canvas(root)
scrolly = tk.Scrollbar(root, orient='vertical', command=canvas.yview)

# display labels in the canvas
for i in range(10):
    label = tk.Label(canvas, text='label %i' % i)
    canvas.create_window(0, i*50, anchor='nw', window=label, height=50)

canvas.configure(scrollregion=canvas.bbox('all'), yscrollcommand=scrolly.set)

canvas.pack(fill='both', expand=True, side='left')
scrolly.pack(fill='y', side='right')

root.mainloop()


##############################################################################
# Testing *args and **kwargs

def test_var_args(f_arg, *argv):
    print("first normal arg:", f_arg)
    for arg in argv:
        print("another arg through *argv :", arg)

test_var_args('Programing','python','snake','venom')


##############################################################################
# python prompt test
# command linux: python3 -i test.py

def verif(n):

	if type(n) not in [int, float]:
		print('error type')
		
	else:
		print('given number is float or integer')
		n = float(n)
		n = n + 3.14
		print('number + pi =', n)


##############################################################################
# popup test
from tkinter import *

class info_popup:
	
	def __init__(self, window):
		self.window = window
		self.label_info = Label(self.window, text= "L'info dont tu as besoin est ici")
		self.label_info.pack(padx= 50, pady= 50)
		self.label_info.bind("<Enter>", self.enter)

	def enter(self, event):
		self.label_info.unbind("<Enter>")
		self.top_info = Toplevel()
		self.top_label = Label(self.top_info, text= "This is what you need")
		self.top_label.pack(padx= 10, pady= 10)
		self.top_label.bind("<Leave>", self.leave)

	def leave(self, event):
		self.top_info.destroy()
		self.label_info.bind("<Enter>", self.enter)

if __name__ == '__main__':

	root = Tk()
	root.title("Info")
	Info = info_popup_2(root)
	root.mainloop()


##############################################################################
# try/except/else/finally test
try:
	f = open('error.txt')
	print('opening file')
	print(f.read())
except:
	print("Something went wrong")
finally:
	print('closing file')
	f. close()

"""
