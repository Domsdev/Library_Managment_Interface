import re

# check mail and password validity: ##########################################

def mail_validity(email):
	# email = local@domain.topleveldomain

	# local in [A-Za-z0-9._%+-]
	# domain in @[A-Za-z0-9.-]

	# top level domain in .[A-Za-z]{2,4}
	# lenth between 2 and 4 charracters

	# ^ begining of the regular expression
	# $ ending of the regular expression

	validity = re.match("^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,4}$",
		email
		)
	return bool(validity)


def password_validity(password):
	for caracter in password:
		if caracter == ' ':
			return False # space character not allowed

##############################################################################

if __name__ == '__main__':
	
	email="some_kind-of.email+adress@domsdev.co.uk"
	print(check_mail_validity(email))
