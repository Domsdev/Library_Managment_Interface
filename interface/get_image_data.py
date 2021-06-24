
from tkinter import filedialog
from tkinter import *
import os

# get image data: ############################################################

def Get_image_data(window):

	open_file = filedialog.askopenfile(initialdir = "/home/doms/Bureau",
			                           parent=window,
			                           mode='rb',
			                           title='Choisissez un fichier',
			                           filetypes = (("fichier image","*.png"),
			                          	            ("fichier image","*.jpg"),
			                          	            ("fichier image","*.gif"),
			                          	            ("Tous les formats","*.*")
			                          	           )
			                          )
	# mode rb is for 'read binary'

	if open_file != None:
	    data = open_file.read()
	    file_Name = os.path.split(open_file.name)
	    open_file.close()
	    print("Info: file {} has {} bytes.".format(file_Name[1], len(data)))
	    # print file size info

	    # os.remove(open_file.name)
	    # if one need to remove the file after reading

	    return data, file_Name[1]

	else:
		return None, 'Aucun fichier sélectionné !'

##############################################################################

if __name__ == '__main__':
	
	window = Tk()
	Get_image_data(window)