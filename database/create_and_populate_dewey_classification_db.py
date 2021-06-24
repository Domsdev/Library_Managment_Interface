##############################################################################
# STEP 1:
# CREATING dewey_classification DATABASE
# FROM file create_dewey_classification.sql

# STEP 2:
# FORMATING DATA AND FILES
# FROM file Dewey_decimal_classification_FR.txt

# STEP 3:
# POPULATING dewey_classification DATABASE
# FROM file populate_dewey_classification_db.py
##############################################################################

import mysql.connector
from mysql.connector import Error
import re
import os
import psutil
import time
from os import environ
from populate_dewey_classification_db import populate_dewey_classification_db

##############################################################################

def create_dewey_classification():

	try:
		user = environ.get('MYSQL_USER')
		password = environ.get('MYSQL_PASSWORD')

		# connect to dewey_classification database
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

		create_dewey_classification_db(
			'create_dewey_classification_db.sql', connect, cursor)

		cursor.close()
		connect.close()
		# print("Info: MySQL sever connection is closed")

##############################################################################

def create_dewey_classification_db(filename, connect, cursor):
	# reading file create_dewey_classification_db.sql ...
	with open(filename, 'r') as file:
		mysql_file = file.read()
		print('Info: Reading sql file / ', memory_use())
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

def formate_data_files():

	# writing a temporary file where all void lines
	# from source file Dewey_decimal_classification_FR.txt are removed
	with open("Dewey_decimal_classification_FR.txt", 'r') as file:
		print('Info: reading data from source file / ', memory_use())

		for line in file:
			if line == '\n':
				pass # do nothing
			else:
				with open("temp_file.txt", "a+") as temp:
					temp.write(line)

	# create lists of classes, divisions, sections and subsections
	with open("temp_file.txt", 'r') as file:

		category = ''
		class_number_list = []
		class_name_list = []
		division_number_list = []
		division_name_list = []
		section_number_list = []
		section_name_list = []
		subsection_number_list = []
		subsection_name_list = []
		i, j, k, l = 0, 0, 0, 0

		for line in file:

			# using reular expressions to verify if line contains
			# class, division, section or subsection number
			class_number = re.match("^[0-9]00$", line)
			division_number = re.match("^[0-9][0-9]0$", line)
			section_number = re.match("^[0-9][0-9][1-9]$", line)
			subsection_number = re.match("^[0-9]+\.[0-9 ]{,30}$", line)

			if line == '\n':
				pass

			elif bool(class_number):
				i = 0
				category = 'class'
				class_number_list.append(line.strip('\n'))

			elif bool(division_number):
				j = 0
				category = 'division'
				division_number_list.append(line.strip('\n'))

			elif bool(section_number):
				k = 0
				category = 'section'
				section_number_list.append(line.strip('\n'))

			elif bool(subsection_number):
				l = 0
				category = 'subsection'
				subsection_number_list.append(line.strip('\n'))

			else:
				# populate category lists
				# and concatenate separated text lines
				if category == 'class':
					if i < 1:
						class_name_list.append(line.strip('\n'))
						i += 1
					else:
						class_name_list[-1] += " " + line.strip('\n')

				elif category == 'division':
					if j < 1:
						division_name_list.append(line.strip('\n'))
						j += 1
					else:
						division_name_list[-1] += " " + line.strip('\n')

				elif category == 'section':
					if k < 1:
						section_name_list.append(line.strip('\n'))
						k += 1
					else:
						section_name_list[-1] += " " + line.strip('\n')

				elif category == 'subsection':
					if l < 1:
						subsection_name_list.append(line.strip('\n'))
						l += 1
					else:
						subsection_name_list[-1] += " " + line.strip('\n')

	os.remove("temp_file.txt")
	print('Info: data lists created / ', memory_use())


	# creating files with classes, divisions, sections and subsections data
	with open("dewey_classification_class.txt", "w+") as file:
		file.write("Class\n\n")

		for k in range(len(class_number_list)):

			# writing class number
			file.write(class_number_list[k] + ':')

			# formating and writing class name text
			class_name_list[k] = class_name_list[k].replace("  ", " ")
			class_name_list[k] = class_name_list[k].replace(" ,", ",")
			class_name_list[k] = class_name_list[k].replace(" ;", ";")
			class_name_list[k] = class_name_list[k].replace(" )", ")")
			class_name_list[k] = class_name_list[k].replace("\"", "\'")
			file.write(class_name_list[k] + '\n' + '\n')

	with open("dewey_classification_division.txt", "w+") as file:
		file.write("Division\n\n")

		for k in range(len(division_number_list)):
			
			# writing division number
			file.write(division_number_list[k] + ':')

			# formating and writing division name text
			division_name_list[k] = division_name_list[k].replace("  ", " ")
			division_name_list[k] = division_name_list[k].replace(" ,", ",")
			division_name_list[k] = division_name_list[k].replace(" ;", ";")
			division_name_list[k] = division_name_list[k].replace(" )", ")")
			division_name_list[k] = division_name_list[k].replace("\"", "\'")
			file.write(division_name_list[k] + '\n' + '\n')

	with open("dewey_classification_section.txt", "w+") as file:
		file.write("Section\n\n")

		for k in range(len(section_number_list)):
			
			# writing section number
			file.write(section_number_list[k] + ':')

			# formating and writing section name text
			section_name_list[k] = section_name_list[k].replace("  ", " ")
			section_name_list[k] = section_name_list[k].replace(" ,", ",")
			section_name_list[k] = section_name_list[k].replace(" ;", ";")
			section_name_list[k] = section_name_list[k].replace(" )", ")")
			section_name_list[k] = section_name_list[k].replace("\"", "\'")
			file.write(section_name_list[k] + '\n' + '\n')

	with open("dewey_classification_subsection.txt", "w+") as file:
		file.write("Subsection\n\n")

		for k in range(len(subsection_number_list)):
			
			# writing subsection number
			file.write(subsection_number_list[k] + ':')

			# formating and writing subsection name text
			subsection_name_list[k] = subsection_name_list[k].replace("  ", " ")
			subsection_name_list[k] = subsection_name_list[k].replace(" ,", ",")
			subsection_name_list[k] = subsection_name_list[k].replace(" ;", ";")
			subsection_name_list[k] = subsection_name_list[k].replace(" )", ")")
			subsection_name_list[k] = subsection_name_list[k].replace("\"", "\'")
			file.write(subsection_name_list[k] + '\n' + '\n')

##############################################################################

def memory_use():
	process = psutil.Process(os.getpid())
	mem_use = process.memory_info()

	return f'Merory use: {mem_use.rss//8000} Ko'

##############################################################################

if __name__ == '__main__':

	start_time = time.time()

	print('1: CREATING dewey_classification DATABASE ...')
	create_dewey_classification()
	step_time1 = time.time()
	print('Step 1 running time: ',
		  '{:.3f}'.format(step_time1 - start_time),
		  'sec', '\n')

	print('2: FORMATING DATA AND FILES ...')
	formate_data_files()
	step_time2 = time.time()
	print('Step 2 running time: ',
		  '{:.3f}'.format(step_time2 - step_time1),
		  'sec', '\n')

	print('3: POPULATING dewey_classification DATABASE')
	populate_dewey_classification_db() # < populate_dewey_classification_db.py
	step_time3 = time.time()
	print('Step 3 running time: ',
		  '{:.3f}'.format(step_time3 - step_time2),
		  'sec', '\n')

	print('JOB DONE / Total running time: ',
		  '{:.3f}'.format(time.time() - start_time),
		  'sec', '\n')

