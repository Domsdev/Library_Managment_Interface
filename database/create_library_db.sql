
-- SOURCE /home/doms/Programmation/Projects/library/code/encours/library_mysql/create_library_db.sql;

DROP DATABASE IF EXISTS library;
CREATE DATABASE library CHARACTER SET 'utf8';
USE library;

################## TYPE TABLE ################################################

CREATE TABLE Type (
	id INT UNSIGNED AUTO_INCREMENT NOT NULL,
	type_name VARCHAR(50) NOT NULL,
	PRIMARY KEY (id)
)ENGINE=InnoDB;

################ REFERENCE TABLE #############################################

CREATE TABLE Reference (
	id INT UNSIGNED AUTO_INCREMENT NOT NULL,
	type_id INT UNSIGNED NOT NULL,
	title VARCHAR(150) NOT NULL,
	classification_id VARCHAR(30) NOT NULL,
	isn text DEFAULT NULL,
	theme text DEFAULT NULL,
	abstract text DEFAULT NULL,
	PRIMARY KEY (id),
	FULLTEXT INDEX ind_full_title (title, theme, abstract),
	CONSTRAINT fk_Reference_type_id FOREIGN KEY (type_id) 
	REFERENCES Type(id)
)ENGINE=InnoDB;

# ISN  : International Standard Number (ISBN for Book and ISSN for Serials)

################## AUTHOR TABLE ##############################################

CREATE TABLE Author (
	id INT UNSIGNED AUTO_INCREMENT NOT NULL,
	author_name VARCHAR(150) NOT NULL,
	PRIMARY KEY (id),
	UNIQUE INDEX ind_uni_coordinate (author_name),
	FULLTEXT INDEX ind_full_author (author_name)
)ENGINE=InnoDB;

################ RESSOURCE-AUTHOR TABLE ######################################

CREATE TABLE Reference_author (
	reference_id INT UNSIGNED NOT NULL,
	author_id INT UNSIGNED NOT NULL,
	PRIMARY KEY(reference_id, author_id),
	CONSTRAINT fk_Author_reference_id FOREIGN KEY (reference_id) 
	REFERENCES Reference(id),
	CONSTRAINT fk_Reference_author_id FOREIGN KEY (author_id) 
	REFERENCES Author(id)
)ENGINE=InnoDB;

################## VOLUME TABLE ##############################################

CREATE TABLE Volume (
	reference_id INT UNSIGNED AUTO_INCREMENT NOT NULL,
	volume_info VARCHAR(150) NOT NULL,
	PRIMARY KEY (reference_id, volume_info),
	FULLTEXT INDEX ind_full_volume (volume_info),
	CONSTRAINT fk_Volume_reference_id FOREIGN KEY (reference_id) 
	REFERENCES Reference(id)
)ENGINE=InnoDB;

################## PUBLICATION TABLE #########################################

CREATE TABLE Publication (
	reference_id INT UNSIGNED AUTO_INCREMENT NOT NULL,
	publication_info VARCHAR(150) NOT NULL,
	PRIMARY KEY (reference_id, publication_info),
	CONSTRAINT fk_Publication_reference_id FOREIGN KEY (reference_id) 
	REFERENCES Reference(id)
)ENGINE=InnoDB;

################## COPY TABLE ################################################

CREATE TABLE Copy (
	barcode INT(8) ZEROFILL UNSIGNED AUTO_INCREMENT,
	buying_price DECIMAL(7,2) UNSIGNED DEFAULT NULL,
	cover MEDIUMBLOB DEFAULT NULL,
	loan_permission TINYINT(1) NOT NULL, # BOOLEAN equivalent
	reference_id INT UNSIGNED NOT NULL,
	PRIMARY KEY(barcode),
	CONSTRAINT fk_Copy_reference_id FOREIGN KEY (reference_id)
	REFERENCES Reference(id)
)ENGINE=InnoDB;

################# COORDINATE TABLE ###########################################

CREATE TABLE Coordinate (
	id INT UNSIGNED AUTO_INCREMENT,
	first_name VARCHAR(150) NOT NULL,
	last_name VARCHAR(150) NOT NULL,
	phone_number VARCHAR(150) NOT NULL,
	email VARCHAR(254) NOT NULL,
	identity_card MEDIUMBLOB DEFAULT NULL,
	creation_date DATETIME DEFAULT NULL,
	active_state TINYINT(1) NOT NULL,
	activation_code INT(6) UNSIGNED DEFAULT NULL,
	PRIMARY KEY (id),
	UNIQUE INDEX ind_uni_coordinate (first_name, last_name,
		                             phone_number, email)
)ENGINE=InnoDB;

################## USER TABLE ################################################

CREATE TABLE User (
	pseudo VARCHAR(150) NOT NULL,
	password VARCHAR(150) NOT NULL,
	coordinate_id INT UNSIGNED NOT NULL,
	PRIMARY KEY (pseudo),
	UNIQUE INDEX ind_uni_coordinate_id (coordinate_id),
	CONSTRAINT fk_User_coordinate_id FOREIGN KEY (coordinate_id)
	REFERENCES Coordinate(id)
)ENGINE=InnoDB;

################## LOAN TABLE ################################################

CREATE TABLE Loan (
	return_date DATE NOT NULL,
	copy_barcode INT UNSIGNED NOT NULL,
	user_pseudo VARCHAR(150) NOT NULL,
    PRIMARY KEY(return_date, copy_barcode),
	CONSTRAINT fk_loan_copy_barcode_id FOREIGN KEY (copy_barcode)
	REFERENCES Copy(barcode),
	CONSTRAINT fk_Loan_user_pseudo FOREIGN KEY (user_pseudo)
	REFERENCES User(pseudo)
)ENGINE=InnoDB;

##############################################################################

SELECT pseudo,
       password,
       coordinate_id
FROM User ORDER BY coordinate_id;

SELECT id,
       first_name,
       last_name,
       phone_number,
       email,
       creation_date,
       active_state,
       activation_code
FROM Coordinate;

SELECT * FROM Type;

SELECT id,
       type_id,
       title,
       classification_id,
       isn,
       SUBSTR(theme, 1, 20) as theme,
       SUBSTR(abstract, 1, 20) as abstract
FROM Reference LIMIT 50;

