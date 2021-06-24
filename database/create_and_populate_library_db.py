##############################################################################
# STEP 1:
# CREATING library DATABASE
# FROM file create_library_db.sql

# STEP 2:
# POPULATING library DATABASE
# FROM file populate_library_db.py
##############################################################################

import mysql.connector
from mysql.connector import Error
import re
import os
from os import environ
from populate_library_db import populate_library_db
import psutil
import time

##############################################################################
def create_library_db(filename, connect, cursor):
	# reading file create_library_db.sql ...
	with open(filename, 'r') as file:
		mysql_file = file.read()
		# ... and separate each query
		mysql_queries = mysql_file.split(';')

		# format queries
		for k in range(len(mysql_queries)):
			mysql_queries[k] = mysql_queries[k] + ";"
		del mysql_queries[-1]
		
		for query in mysql_queries:
			# execute all queries except SELECT queries at the end of the file
			# wich are used for debug and verification
			if query.find('SELECT') == -1:
				try:
					cursor.execute(query)
					connect.commit()

				except Error as err:
					print("MySQL Error message: {}".format(err.msg))

##############################################################################
def create_library():

	try:
		user = environ.get('MYSQL_USER')
		password = environ.get('MYSQL_PASSWORD')

		# connect to library database
		connect = mysql.connector.connect(
			user = user,
			password = password,
			host = 'localhost',
			database = 'library')

	except Error as err:
		print("MySQL Error message: {}".format(err.msg))

	else:
		cursor = connect.cursor()
		cursor.execute("select database();")
		db = cursor.fetchone()
		# print("Info: Connected to MySQL database", db)

		create_library_db('create_library_db.sql', connect, cursor)

		cursor.close()
		connect.close()
		# print("Info: MySQL sever connection is closed")

##############################################################################

if __name__ == '__main__':

	start_time = time.time()

	print('1: CREATING library DATABASE ...')
	create_library()
	step_time1 = time.time()
	print('Step 1 running time: ',
		  '{:.3f}'.format(step_time1 - start_time),
		  'sec', '\n')

	print('2: POPULATING library DATABASE ...')
	populate_library_db() # < populate_dewey_classification_db.py
	step_time2 = time.time()
	print('Step 2 running time: ',
		  '{:.3f}'.format(step_time2 - step_time1),
		  'sec', '\n')

	print('JOB DONE / Total running time: ',
		  '{:.3f}'.format(time.time() - start_time),
		  'sec', '\n')
