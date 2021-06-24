import random
from connect_db import *

##############################################################################

def Generate_activation_code():
	"generate activation code which is not in database"

	activation_code = ''
	q = False

	while q == False:

		for k in range(6):
			activation_code = activation_code + str(random.randint(1,9))

		activation_code = int(activation_code) # like 978265 with none 0 digit
		
		q = connect_db('check activation code', activation_code)

		if q == True:
			print('Info: Activation code generated')
			return activation_code

##############################################################################

if __name__ == '__main__':
	gen_code = Generate_activation_code()
	print(gen_code)