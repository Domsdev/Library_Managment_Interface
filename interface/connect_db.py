import mysql.connector
from mysql.connector import Error
import datetime
from os import environ
import sys, traceback
from send_mail import *

# connect to database: #######################################################

def connect_db(query, queryList):

	try:
		user = environ.get('MYSQL_USER')
		password = environ.get('MYSQL_PASSWORD')

		# connect to database
		connect = mysql.connector.connect(
			user = user,
			password = password,
			host = 'localhost',
			database = 'library'
			)

	except Error as err:
		print("MySQL Error message: {}".format(err.msg))

		date_of_today = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

		traceback_lines = traceback.format_exc().splitlines()

		# print error in error.txt file
		with open('error.txt', 'a+') as f:
			f.write(f"\n\nError occured: {date_of_today}\n")
			f.write(f"MySQL Error message: {err.msg}")
			for k in range(len(traceback_lines)):
				f.write(traceback_lines[k])

		return "Can't connect to MySQL server" # connection to server failed

	else:
		# show info connection in terminal:
		# db_Info = connect.get_server_info()
		# print("Info: Connected to MySQL Server version", db_Info)

		# select database 'library'
		cursor = connect.cursor()
		cursor.execute("select database();")
		db = cursor.fetchone()
		print("Info: Connected to MySQL database", db)

		# create dictionary as a menu for query selection
		query_dict = {'check activation code': check_activation_code,
		              'create user account': create_user_account,
		              'login': login,
		              'activate': activate,
		              'search user account': search_user_account,
		              'fetch account data': fetch_account_data,
		              'update': update,
		              'fetch category list': fetch_category_list,
		              'check reference': check_reference,
		              'new reference': new_reference,
		              'extented search': extented_search,
		              'custom search': custom_search}

		# LIST OF DATABASE INTERACTIONS :

		# check activation code: check if generated activation code
		#                        does not already exists in dB

		# create user account:   register coordinates of a new user in dB

		# login:                 check if given (pseudo + password) match
		#                        with those in dB

		# activate:              account activation

		# search user account:   search and select accounts_id in dB
		#                        that match to user search

		# fetch account data:    fetch data from a list of accounts

		# update:                update coordinates for a selected account

		# fetch category:        fecth category_list from Category table in dB

		# check reference:       check if a reference already exists in dB

		# new reference:         create new ressource or copy reference in dB

		# extented search:       search a reference in all dB 
		#                        with a list of keywords and sentences

		# custom search:         for each selected table, search a referece 
		#                        with a list of keywords and sentences

		if query in query_dict: # execution of query sequences
			q = query_dict[query](queryList, connect, cursor)
		
		cursor.close()
		connect.close()
		print("Info: MySQL sever connection is closed")

		return q # return result of query sequences

##############################################################################

def check_activation_code(activation_code, connect, cursor):
	"check if generated activation code does not already exists in dB"

	# try to select id with generated activation code
	Query = "SELECT id FROM Coordinate WHERE activation_code = %s;"
	Values = (activation_code,)
	cursor.execute(Query, Values)
	record = cursor.fetchone()
	connect.commit()

	if record == None: # generated activation code is not in dB
		return True

##############################################################################

def create_user_account(account_data, connect, cursor):
	"register coordinates of a new user in database"

	# account_data == [first_name, last_name, phone_number, email,
	#                  id_card_data, activation_code]

	#######################################################
	# attempt to send mail to user with activation code:
	# generate html_body message

	name = (account_data[0] + ' ' + account_data[1])
	code = account_data[5]

	html_body, subject = html_body_activation_code(name, code)
	receiver = account_data[3]

	#############################################
	# TESTING MAIL ADRESS                       #
	# replace user's adress for test phases:    #
	receiver = "domsdev.receiver@outlook.com"   #
	#############################################

	s = Send_mail(receiver, html_body, subject)
	#######################################################

	if s == True:
		# if mail has actually been sent, then populate Coordinate table

		date_of_today = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

		Query = """INSERT INTO Coordinate (first_name,
		                                   last_name,
		                                   phone_number,
		                                   email,
		                                   identity_card,
		                                   creation_date,
		                                   active_state,
		                                   activation_code)
		           VALUES (%s, %s, %s, %s, %s, %s, %s, %s);"""

		Values = (account_data[0],
			      account_data[1],
			      account_data[2],
			      account_data[3],
			      account_data[4],
			      date_of_today,
			      0,
			      account_data[5])

		cursor.execute(Query, Values)
		connect.commit()

		return True # registration is Ok

	else:
		return False

##############################################################################

def activate(login_list, connect, cursor):
	"account activation"

	# get account's id corresponding to the given activation code
	Query = """SELECT id
		       FROM   Coordinate
		       WHERE  activation_code = {};""".format(login_list[0])
	cursor.execute(Query)
	coordinate_id = cursor.fetchone()
	connect.commit()
	print('activate---------------------coordinate_id', coordinate_id)

	if coordinate_id == None: # given activation code is not in dB
		return "code error"

	else: # given activation code match !
		# try to select pseudo from User table
		Query = """SELECT pseudo
		           FROM   User
		           WHERE  Coordinate_id = {};""".format(coordinate_id[0])
		cursor.execute(Query)
		pseudo = cursor.fetchone()
		connect.commit()
		print('activate---------------------pseudo', pseudo)

		if pseudo == None: # case of a new user !
			print('activate-------------------- new user case')
			if len(login_list) == 1: # only check for activation code
				return "new user"

			elif len(login_list) == 3: # user entered pseudo + password
				try: # insert pseudo + password in dB
					Query = """INSERT INTO User (pseudo,
					                             password,
					                             coordinate_id)
					           VALUES (%s, %s, %s);"""
					Values = (login_list[1], login_list[2], coordinate_id[0])
					cursor.execute(Query, Values)
					connect.commit()

				except Error as err:
					print("Query Error message: {}".format(err.msg))
					return False # pseudo already exists in dB

				else:
					# update active_state and activation_code
					Query = """UPDATE Coordinate
					           SET    active_state = 1, activation_code = NULL
					           WHERE  id = {};""".format(coordinate_id[0])
					cursor.execute(Query)
					connect.commit()
					return True

		else: # case of an existing user
			print('activate----------------- existing user case')
			if len(login_list) == 1: # only check for activation code
				return pseudo[0]

			elif len(login_list) > 1:
				print('activate------------------- login list > 1')
				# update activation_code
				Query = """UPDATE Coordinate
				           SET    activation_code = NULL
				           WHERE  id = {};""".format(coordinate_id[0])
				cursor.execute(Query)
				connect.commit()

				if len(login_list) == 3: # existing user entered new password
					# insert new password in dB
					Query = """UPDATE User
					           SET    password = %s
					           WHERE  pseudo = %s;"""
					Values = (login_list[2], login_list[1])
					cursor.execute(Query, Values)
					connect.commit()
					return True

				elif len(login_list) == 2:
					print('activate------------------- login list = 2')
					return True

##############################################################################

def login(login_list, connect, cursor): 
	"check if given (pseudo + password) match with those in database"

	# check if pseudo is in User table
	Query = """SELECT User.password, 
	                  Coordinate.active_state,
	                  Coordinate.activation_code
	           FROM   User INNER JOIN Coordinate
	           ON     User.coordinate_id = Coordinate.id
	           WHERE  User.pseudo = %s;"""

	Values = (login_list[0],)
	cursor.execute(Query, Values)
	user_data = cursor.fetchall()
	connect.commit()

	# if given pseudo is not in User table, query will return []
	if user_data == []:
		return "pseudo error"

	else: # pseudo is in User table...
	    # now check if password given match to password in User table
		if user_data[0][0] != login_list [1]:
			return "password error"
			
		else:
			# given pseudo and password are Ok
			# now check type of user

			if user_data[0][1] == 1 and user_data[0][2] == None :
				return "user"

			elif user_data[0][1] == 1 and user_data[0][2] != None :
				return 'activation'

			elif user_data[0][1] == 2:
				return "librarian"

			elif user_data[0][1] == 3:
				return "administrator"

##############################################################################

def search_user_account(search_dict, connect, cursor):
	"search and select accounts_id in database that match to user search"

	result_dict = {}
	# creating a dictionary that will contain all id of accounts

	for column_query in search_dict:
		if (search_dict[column_query][0] == 'Ok'
			and search_dict[column_query][1] != ''):
			# for each colum_query in search_dict, 
			# if search box has been activated
			# and user entered something in field:

			if column_query == 'pseudo':
				table = 'User'
				column_result = 'coordinate_id'
				
			else:
				table = 'Coordinate'
				column_result = 'id'
				
			searching = search_dict[column_query][1]

			Query = """SELECT {} FROM {} WHERE {} LIKE '%{}%';
			        """.format(column_result, table, column_query, searching)

			cursor.execute(Query)
			record = cursor.fetchall()
			connect.commit()

			result_dict[column_query] = record

	# return a dictionary with a tuple list of id found for each Query
	# {'first_name': [(8,), (9,)], 'last_name': [(8,), (10,), (15,)], ...}
	return result_dict

##############################################################################

def fetch_account_data(account_id_list, connect, cursor):
	"fetch data from a list of accounts"

	account_data_list = []

	for account_id in account_id_list:

		Query = """SELECT first_name,
		                  last_name,		                  
		                  phone_number,
		                  email,
		                  active_state
		           FROM   Coordinate
		           WHERE  id = '{}';""".format(account_id)

		cursor.execute(Query)
		coordinates = cursor.fetchone()
		connect.commit()
		coordinates = list(coordinates)

		if coordinates[4] != 0: # if account is active

			Query = """SELECT pseudo
			           FROM   User
			           WHERE  coordinate_id = '{}';""".format(account_id)

			cursor.execute(Query)
			pseudo = cursor.fetchone()
			connect.commit()
			pseudo = list(pseudo)

			coordinates.insert(0, pseudo[0]) # insert pseudo in coordinates

		else:
			coordinates.insert(0, 'Inactive') # account is inactive

		coordinates.insert(0, account_id)
		account_data_list.append(coordinates)

	return account_data_list

##############################################################################

def update(account_data, connect, cursor):
	"update coordinates for a selected account"

	# account_data == [id, pseudo, first_name, last_name, 
	#                 phone_number, email, activation_code]

	#######################################################
	# attempt to send mail to user with new activation code:
	# generate html_body message
	name = (account_data[2] + ' ' + account_data[3])
	code = account_data[6]

	html_body, subject = html_body_new_activation_code(name, code)
	receiver = account_data[5]

	#############################################
	# TESTING MAIL ADRESS                       #
	# replace user's adress for test phases:    #
	receiver = "domsdev.receiver@outlook.com"   #
	#############################################

	s = Send_mail(receiver, html_body, subject)
	#######################################################

	if s == True:
		# if mail has actually been sent, then populate Coordinate table

		Query = """UPDATE Coordinate
		           SET    first_name = %s,
		                  last_name = %s,
		                  phone_number = %s,
		                  email = %s,
		                  activation_code = %s
		           WHERE  id = %s;"""

		Values = (account_data[2],
			      account_data[3],
			      account_data[4],
			      account_data[5],
			      account_data[6],
			      account_data[0])

		cursor.execute(Query, Values)
		connect.commit()

		return True # registration is Ok

	else:
		return False

##############################################################################

def fetch_category_list(void_list, connect, cursor):
	"fecth category list from Category table in dB"

	Query = """SELECT   category_name
	           FROM     Category
	           ORDER BY category_name;"""

	cursor.execute(Query)
	category_list = cursor.fetchall()
	connect.commit()

	return category_list

##############################################################################

def check_reference(query_list, connect, cursor):
	"check in database if a reference already exists"

	Title = query_list[1]

	# check if given title is linked to a book or comic or magazine
	if query_list[0] == 'Book':
		select_1 = 'Book.author'
		select_2 = 'Book.isbn'

	elif query_list[0] == 'Comic':
		select_1 = 'Comic.author'
		select_2 = 'Comic.album'

	elif query_list[0] == 'Magazine':
		select_1 = 'Magazine.volume'
		select_2 = 'Magazine.publication'

		# formating publication date
		date_list = query_list[3].split('-')
		query_list[3] = datetime.date(
			int(date_list[0]),
			int(date_list[1]),
			int(date_list[2])
			)

	Query = f"""SELECT {select_1}, {select_2}, Ressource.id
	            FROM   {query_list[0]} INNER JOIN Ressource
	            ON     {query_list[0]}.ressource_id = Ressource.id
	            WHERE  Ressource.title = "{Title}";"""

	cursor.execute(Query)
	artwork_data = cursor.fetchall()
	connect.commit()

	if artwork_data == []:
		# return 'new' ...
		# and None (as no ressource id where found with given title)
		return 'new', None

	else:
		# check if author/isbn/album/volume/publication
		# linked to the title found in dB

		if (artwork_data[0][0] == query_list[2] or 
			artwork_data[0][1] == query_list[3]):

			# return 'copy' and Ressource.id
			return 'copy', artwork_data[0][2]

		else:
			# return 'new' ...
			# and None, as no ressource id where found
			# with given title and author/isbn/album/volume/publication
			return 'new', None

##############################################################################

def new_reference(reference_data, connect, cursor):
	"create new ressource or copy reference in database"

	# for new reference creation only :
	if reference_data[10] == 'new':

		# enter title, abstract and location_id in Ressource table
		Query = """INSERT INTO Ressource (title,
		                                  theme,
		                                  abstract)
		           VALUES (%s, %s, %s);"""
		Values = (reference_data[1],
			      reference_data[4],
			      reference_data[5])
		cursor.execute(Query, Values)
		cursor.execute("SELECT LAST_INSERT_ID();")
		ressource_id = cursor.fetchone()
		connect.commit()

		# insert classification reference in Ressource_Classification table
		Query = """INSERT INTO Ressource_Classification (ressource_id,
		                                                 classification_ref)
		           VALUES (%s, %s);"""
		Values = (ressource_id[0], reference_data[6])
		cursor.execute(Query, Values)
		connect.commit()


		# insert data in table according to ressource type
		if reference_data[0] == 'Book':
			select_1 = 'author'
			select_2 = 'isbn'

		elif reference_data[0] == 'Comic':
			select_1 = 'author'
			select_2 = 'album'

		elif reference_data[0] == 'Magazine':
			select_1 = 'volume'
			select_2 = 'publication'

			# formating publication date
			date_list = reference_data[3].split('-')
			reference_data[3] = datetime.date(
				int(date_list[0]),
				int(date_list[1]),
				int(date_list[2])
				)

		Query = f"""INSERT INTO {reference_data[0]} ({select_1},
		                                             {select_2},
		                                             ressource_id)
		            VALUES ("{reference_data[2]}",
		                    "{reference_data[3]}", 
		                    {ressource_id[0]});"""
		cursor.execute(Query)
		connect.commit()


	# for copy reference creation only :
	if reference_data[10] == 'copy':
		ressource_id = []
		# retrieve corresponding Ressource id:
		ressource_id.append(reference_data[11])


	# finally, in all cases (new or copy reference):
	# insert buying price, loan_permission and ressource_id in Copy table
	Query = """INSERT INTO Copy (buying_price, loan_permission, ressource_id)
	           VALUES ( %s, %s, %s);"""
	Values = (reference_data[8], reference_data[9], ressource_id[0])
	cursor.execute(Query, Values)
	cursor.execute("SELECT LAST_INSERT_ID();")
	copy_barcode = cursor.fetchone()
	connect.commit()

	# if a cover has been loaded, add cover in Copy table
	if reference_data[7] != 'None':
		Query = """UPDATE Copy 
		           SET    cover = %s
		           WHERE  barcode = %s;"""
		Values = (reference_data[7], copy_barcode[0])
		cursor.execute(Query, Values)
		connect.commit()

	return copy_barcode[0] # new reference created !!

##############################################################################

def extented_search(search_query, connect, cursor):
	"search a reference in all dB with a list of keywords and sentences"

	print('')

	#######################################################
	print('SEARCH in Ressource: TITLE')

	Query = f"""SELECT  id,
	                    title,
	                    MATCH(title)
	                    AGAINST ("{search_query}") as score
	            FROM    Ressource
	            WHERE   MATCH(title)
	            AGAINST ("{search_query}") > 0.1
	            ORDER BY score DESC;"""
	cursor.execute(Query)
	search_result1 = cursor.fetchall()
	connect.commit()

	for k in range(len(search_result1)):
		print("{:3}".format(search_result1[k][0]), "{:48}".format(
			search_result1[k][1]), search_result1[k][2])

	print('')

	#######################################################
	print('SEARCH in Ressource: THEME, ABSTRACT')

	Query = f"""SELECT  id,
	                    title,
	                    MATCH(theme, abstract)
	                    AGAINST ("{search_query}") as score
	            FROM    Ressource
	            WHERE   MATCH(theme, abstract)
	            AGAINST ("{search_query}") > 0.1
	            ORDER BY score DESC;"""
	cursor.execute(Query)
	search_result2 = cursor.fetchall()
	connect.commit()

	for k in range(len(search_result2)):
		print("{:3}".format(search_result2[k][0]), "{:48}".format(
			search_result2[k][1]), search_result2[k][2])

	print('')

	#######################################################
	print('SEARCH in Book: AUTHOR')

	Query = f"""SELECT  ressource_id,
	                    author,
	                    MATCH(author)
	                    AGAINST ("{search_query}") as score
	            FROM    Book
	            WHERE   MATCH(author)
	            AGAINST ("{search_query}") > 0.1
	            ORDER BY score DESC;"""
	cursor.execute(Query)
	search_result3 = cursor.fetchall()
	connect.commit()

	for k in range(len(search_result3)):
		print("{:3}".format(search_result3[k][0]), "{:48}".format(
			search_result3[k][1]), search_result3[k][2])

	print('')

	#######################################################
	print('SEARCH in Comic: AUTHOR')

	Query = f"""SELECT  ressource_id,
	                    author,
	                    MATCH(author, album)
	                    AGAINST ("{search_query}") as score
	            FROM    Comic
	            WHERE   MATCH(author, album)
	            AGAINST ("{search_query}") > 0
	            ORDER BY score DESC;"""
	cursor.execute(Query)
	search_result4 = cursor.fetchall()
	connect.commit()

	for k in range(len(search_result4)):
		print("{:3}".format(search_result4[k][0]), "{:48}".format(
			search_result4[k][1]), search_result4[k][2])

	print('')

	#######################################################
	print('SEARCH in Comic: ALBUM')

	Query = f"""SELECT  ressource_id,
	                    album,
	                    MATCH(author, album)
	                    AGAINST ("{search_query}") as score
	            FROM    Comic
	            WHERE   MATCH(author, album)
	            AGAINST ("{search_query}") > 0
	            ORDER BY score DESC;"""
	cursor.execute(Query)
	search_result5 = cursor.fetchall()
	connect.commit()

	for k in range(len(search_result5)):
		print("{:3}".format(search_result5[k][0]), "{:48}".format(
			search_result5[k][1]), search_result5[k][2])

	print('')

	return search_result5



##############################################################################

def custom_search(search_list, connect, cursor):
	"for each selected table, search a referece with keywords and sentences"

	pass

