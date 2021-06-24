import mysql.connector
from mysql.connector import Error
from os import environ
import csv
import os

##############################################################################

def populate_library_db():

	try:
		user = environ.get('MYSQL_USER')
		password = environ.get('MYSQL_PASSWORD')

		# connect to database
		connect = mysql.connector.connect(
			user = user,
			password = password,
			host = 'localhost',
			database = 'library')

	except Error as err:
		print("MySQL Error message: {}".format(err.msg))
		return "Can't connect to MySQL server" # connection to server failed

	else:
		cursor = connect.cursor()
		cursor.execute("select database();")
		db = cursor.fetchone()
		# print("Info: Connected to MySQL database", db)

		# STEP 1: populate references types
		populate_type(connect, cursor)

		# STEP 2: populate library db with
		# administrator account and at least one librarian account:
		populate_user_coordinate(connect, cursor)

		# STEP 3: populate library db with
		# data references extracted from file 'library_db_references.csv'
		populate_references(connect, cursor)

		cursor.close()
		connect.close()
		# print("Info: MySQL sever connection is closed")

##############################################################################

def populate_type(connect, cursor):
	"insert reference types in 'Type' table"

	Query = """INSERT INTO Type (type_name)
	           VALUES ('Livre'),
	                  ('Bande dessinée'),
	                  ('Manga'),
	                  ('Comic book'),
	                  ('Magazine'),
	                  ('Journal')
	                  ;"""
	cursor.execute(Query)
	connect.commit()

##############################################################################

def populate_user_coordinate(connect, cursor):
	"insert administrator and librarian accounts in Coordinate table:"

	Query = """INSERT INTO Coordinate (first_name,
	                                   last_name,
	                                   phone_number,
	                                   email,
	                                   active_state)
	           VALUES ('Library',
	                   'Administrator',
	                   '06 35 83 27 53',
	                   'domsdev_admin@gmail.com', 3),
	                  ('Olivia',
	                   'Ortus',
	                   '06 23 45 78 89',
	                   'oliv.ortus@hotmail.com', 2)
	                   ;"""
	cursor.execute(Query)


	Query = """INSERT INTO User (pseudo, password, coordinate_id)
	           VALUES ('Domsdev', '123456', 1),
	                  ('libra', '123', 2)
	                  ;"""
	cursor.execute(Query)
	connect.commit()

##############################################################################

def populate_references(connect, cursor):

	# Load book references:
	with open("library_db_references.csv", 'r') as file:
		k = 0

		for line in file:
			if line[0] == '$' and k == 0: # reading the first line
				reference_data = line.split('#')
				k += 1

			# for the over lines of file:
			elif line[0] == '$' and k != 0:
				insert_reference(reference_data, connect, cursor)
				reference_data = line.split('#')

			elif line[0] != '$':
				reference_data[11] += line

		# insert last line
		insert_reference(reference_data, connect, cursor)


# reference_data[0]  == $    >> (beginning of each reference data set)
# reference_data[1]  == type_id              (Type)
# reference_data[2]  == title                (Reference)
# reference_data[3]  == volume_info          (Volume)
# reference_data[4]  == publication_info     (Publication)
# reference_data[5]  == author_name          (Author / Reference_author)
# reference_data[6]  == classification_id    (Reference)
# reference_data[7]  == isn                  (Reference)
# reference_data[8]  == buying_price         (Copy)
# reference_data[9]  == loan_permission      (Copy)
# reference_data[10] == theme                (Reference)
# reference_data[11] == abstract             (Reference)

##############################################################################

def insert_reference(reference_data, connect, cursor):

	print("Adding reference: {}".format(reference_data[2]))

	##################################
	# fetch id of reference type
	Query = f"""SELECT id FROM Type WHERE type_name = "{reference_data[1]}";"""
	cursor.execute(Query)
	type_id = cursor.fetchone()
	connect.commit()

	
	##################################
	# insert data into Reference table
	Query = """INSERT INTO Reference (type_id,
	                                  title,
	                                  classification_id,
	                                  isn,
	                                  theme,
	                                  abstract)
	           VALUES (%s, %s, %s, %s, %s, %s);"""
	Values = (type_id[0],
		      reference_data[2],
		      reference_data[6],
		      reference_data[7],
		      reference_data[10],
		      reference_data[11])

	cursor.execute(Query, Values)
	cursor.execute("SELECT LAST_INSERT_ID();")
	reference_id = cursor.fetchone()
	connect.commit()


	###############################
	# insert data into Volume table
	if reference_data[3] != 'Néant':
		Query = """INSERT INTO Volume (reference_id, volume_info)
		           VALUES (%s, %s);"""
		Values = (reference_id[0], reference_data[3])

		cursor.execute(Query, Values)
		connect.commit()


	####################################
	# insert data into Publication table
	if reference_data[4] != 'Néant':
		Query = """INSERT INTO Publication (reference_id, publication_info)
		           VALUES (%s, %s);"""
		Values = (reference_id[0], reference_data[4])

		cursor.execute(Query)
		connect.commit()

	
	###############################
	# insert data into Author table
	# and Reference_author table
	if reference_data[5] != 'Néant':
		Query = """SELECT id
		           FROM Author
		           WHERE  author_name = %s;"""
		Values = (reference_data[5],)

		cursor.execute(Query, Values)
		author_id = cursor.fetchone()		
		connect.commit()

		if author_id == None: # if author_name does not exists yet in dB
			Query = """INSERT INTO Author (author_name)
			           VALUES (%s);"""
			Values = (reference_data[5],)

			cursor.execute(Query, Values)
			cursor.execute("SELECT LAST_INSERT_ID();")
			author_id = cursor.fetchone()
			connect.commit()

		Query = """INSERT INTO Reference_author (reference_id, author_id)
		           VALUES (%s, %s);"""
		Values = (reference_id[0], author_id[0])
		cursor.execute(Query, Values)
		connect.commit()


	#############################
	# insert data into copy table
	Query = """INSERT INTO Copy (buying_price, loan_permission, reference_id)
	           VALUES (%s, %s, %s);"""
	Values = (reference_data[8], reference_data[9], reference_id[0])

	cursor.execute(Query, Values)
	connect.commit()

##############################################################################

if __name__ == '__main__':
	populate_library_db()