import mysql.connector
from mysql.connector import Error
from os import environ

# connect to database: #######################################################

def connect_classification_db(query, index):

	try:
		user = environ.get('MYSQL_USER')
		password = environ.get('MYSQL_PASSWORD')

		# connect to database
		connect = mysql.connector.connect(
			user = user,
			password = password,
			host = 'localhost',
			database = 'dewey_classification')

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
		query_dict = {'fetch class data': fetch_class_data,
		              'fetch division data': fetch_division_data,
		              'fetch section data': fetch_section_data,
		              'fetch subsection data': fetch_subsection_data
		              }

		if query in query_dict: # execution of query sequences
			q = query_dict[query](index, connect, cursor)

		cursor.close()
		connect.close()
		print("Info: MySQL sever connection is closed")

		return q # return result of query sequences

##############################################################################

def fetch_class_data(index, connect, cursor):

	Query = """SELECT id, class_name
	           FROM   Class;"""
	cursor.execute(Query)
	class_data = cursor.fetchall()
	connect.commit()

	return class_data

##############################################################################

def fetch_division_data(index, connect, cursor):

	Query = """SELECT id, division_name
	           FROM   Division
	           WHERE  id LIKE "{}__";""".format(index)
	cursor.execute(Query)
	division_data = cursor.fetchall()
	connect.commit()

	return division_data

##############################################################################

def fetch_section_data(index, connect, cursor):

	Query = """SELECT id, section_name
	           FROM   Section
	           WHERE  id LIKE "{}_";""".format(index)
	cursor.execute(Query)
	section_data = cursor.fetchall()
	connect.commit()

	return section_data

##############################################################################

def fetch_subsection_data(index, connect, cursor):

	Query = """SELECT id, subsection_name
	           FROM   Subsection
	           WHERE  id LIKE "{}.%";""".format(index)
	cursor.execute(Query)
	subsection_data = cursor.fetchall()
	connect.commit()

	return subsection_data
