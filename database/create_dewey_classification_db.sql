
-- SOURCE /home/doms/Programmation/Projects/library/code/encours/library_mysql/create_dewey_classification_db.sql;

DROP DATABASE IF EXISTS dewey_classification;

CREATE DATABASE dewey_classification CHARACTER SET 'utf8';
USE dewey_classification;

################ CLASSES #####################################################

CREATE TABLE Class (
	id VARCHAR(3) NOT NULL,
	class_name TEXT NOT NULL,
	PRIMARY KEY (id),
	FULLTEXT INDEX ind_full_class_name (class_name)
)ENGINE=MyISAM;

################ DIVISIONS ###################################################

CREATE TABLE Division (
	id VARCHAR(3) NOT NULL,
	division_name TEXT NOT NULL,
	PRIMARY KEY (id),
	FULLTEXT INDEX ind_full_division_name (division_name)
)ENGINE=MyISAM;

################ SECTIONS ####################################################

CREATE TABLE Section (
	id VARCHAR(3) NOT NULL,
	section_name TEXT NOT NULL,
	PRIMARY KEY (id),
	FULLTEXT INDEX ind_full_section_name (section_name)
)ENGINE=MyISAM;

################ SUBSECTIONS #################################################

CREATE TABLE Subsection (
	id VARCHAR(30) NOT NULL,
	subsection_name TEXT NOT NULL,
	PRIMARY KEY (id),
	FULLTEXT INDEX ind_full_subsection_name (subsection_name)
)ENGINE=MyISAM;

##############################################################################

SELECT id, SUBSTR(class_name, 1, 100) as Class FROM Class;


SELECT id, SUBSTR(division_name, 1, 100) as Division FROM Division LIMIT 12;
SELECT id, SUBSTR(division_name, 1, 100) as Division
FROM (SELECT id, division_name FROM Division ORDER BY id DESC LIMIT 12)result
ORDER BY id ASC;


SELECT id, SUBSTR(section_name, 1, 100) as Section FROM Section LIMIT 12;
SELECT id, SUBSTR(section_name, 1, 100) as Section
FROM (SELECT id, section_name FROM Section ORDER BY id DESC LIMIT 12)result
ORDER BY id ASC;


SELECT id, SUBSTR(subsection_name, 1, 100) as Subsection FROM Subsection LIMIT 12;
SELECT id, SUBSTR(subsection_name, 1, 100) as Subsection
FROM (SELECT id, subsection_name FROM Subsection ORDER BY id DESC LIMIT 12)result
ORDER BY id ASC;

