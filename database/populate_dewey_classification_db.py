import mysql.connector
from mysql.connector import Error
import os
from os import environ

##############################################################################

def populate_dewey_classification_db():

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

	else:
		cursor = connect.cursor()
		cursor.execute("select database();")
		db = cursor.fetchone()
		# print("Info: Connected to MySQL database", db)

		files_list = ["dewey_classification_class.txt",
		              "dewey_classification_division.txt",
		              "dewey_classification_section.txt",
		              "dewey_classification_subsection.txt"]

		# Load class, division, section and subsection data
		# from files in files_list
		for classification_file in files_list:

			with open(classification_file, 'r') as file:

				for line in file:

					if line == '\n': pass

					elif (line == 'Class\n'
						or line == 'Division\n'
						or line == 'Section\n'
						or line == 'Subsection\n'):

						category = line.strip('\n')
						print("Info: filling {} table".format(category))

					else:
						line = line.strip('\n')
						category_data = line.split(':', 1)
						load_category_data(category_data,
							               category,
							               connect,
							               cursor)

		cursor.close()
		connect.close()
		os.remove("dewey_classification_class.txt")
		os.remove("dewey_classification_division.txt")
		os.remove("dewey_classification_section.txt")
		os.remove("dewey_classification_subsection.txt")

		# print("Info: MySQL sever connection is closed")

##############################################################################

def load_category_data(category_data, category, connect, cursor):

	Query = """INSERT INTO {} (id, {}_name)
	           VALUES ("{}", "{}");""".format(category,
	           	                         category.lower(),
	           	                         category_data[0],
	           	                         category_data[1])

	cursor.execute(Query)
	connect.commit()

	# printing debug infomations:
	# print(category)
	# print(category_data[0])

##############################################################################

if __name__ == '__main__':

	populate_dewey_classification_db()