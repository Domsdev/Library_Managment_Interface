# coding: UTF-8

import mysql.connector
from mysql.connector import Error
from os import environ

# raw connect to database: ###################################################

def connect_raw_db(account_id):
	try:
		user = environ.get('MYSQL_USER')
		password = environ.get('MYSQL_PASSWORD')

		connect = mysql.connector.connect(
			user = user,
			password = password,
			host = 'localhost',
			database = 'library',
			raw=True
			)

		# Need RAW mode of connection to database for BLOB data type reading

		# show info connection in terminal ...
		db_Info = connect.get_server_info()
		print("Connected to MySQL Server version", db_Info)
		cursor = connect.cursor()
		cursor.execute("select database();")
		record = cursor.fetchone()
		print("Connected to database: ", record)

		# Retrieve from Db identity_card binary data for selected account
		select_Query = """
		                  SELECT identity_card
	                      FROM   Coordinate
	                      WHERE  id = %s
	                   """
		select_values = (account_id,)
		cursor.execute(select_Query, select_values)
		identity_card_data = cursor.fetchone()
		connect.commit()

		cursor.close()
		connect.close()
		print("MySQL connection is closed")

		return identity_card_data

	except Error as err:
	    print("MySQL Error message: {}".format(err.msg))
	    return "Can't connect to MySQL server" # connection to server failed
