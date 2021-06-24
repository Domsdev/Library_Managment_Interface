# Library Managment Interface

---

### In this repository you will find the code and elements I used to create a desktop application for the managment of a library using Python, Tkinter and MySQL. I created this app as a concrete exemple to put into practice the skills I acquired during training courses in Python and SQL. The app is still under construction!

---

![Linux](https://img.shields.io/badge/Linux-Mint20.1-informational?style=plastic)
[![python](https://img.shields.io/badge/python-3.8.5-brightgreen?style=plastic)](https://www.python.org/downloads/release/python-385/)
![Tkinter](https://img.shields.io/badge/Tkinter-8.6-brightgreen?style=plastic)
![MySQL](https://img.shields.io/badge/MySQL-8.0.25-brightgreen?style=plastic)
[![licence](https://img.shields.io/badge/licence-MIT-yellow?style=plastic)](https://github.com/Domsdev/Data-science-blog/blob/main/MIT%20Licence.md)
[![linkedIn](https://img.shields.io/badge/-LinkedIn%20-blue?style=plastic)](https://www.linkedin.com/in/dominique-pothin-dev/)


## Requirements

**MySQL server installed and configured for a user:** sudo apt-get install mysql-server<br/>
**MySQL Connector:** pip3 install mysql-connector-python<br/>
 <br/>
**Need to create environment variables to make the application run without modifications, adding the following two lines at the end of my .bashrc file**<br/>
export MYSQL_USER='username'<br/>
export MYSQL_PASSWORD='password'<br/>
 <br/>
**Tkinter:** sudo apt-get install python3-tk<br/>
**pil.imagetk:** sudo apt-get install python3-pil.imagetk<br/>
**Sendmail:** pip3 install sendmail<br/>


## Test the application

### Clone the repository

![png](img/step0.png)

### Create two databases: "dewey_classification" and "library"

![png](img/step1.png)

### Built and fill the databases using python scripts in the dedicated folder

![png](img/step2.png)
![png](img/step3.png)

### Launch the application using the python script

![png](img/step4.png)

### Now you can see the app welcome page!

![png](img/screen1.png)

### Let's imagine that a librarian wants to connect to its account:

![png](img/screen2.png)

### If you look the tables in the library database, and in the "User" table, you will find exemples of users already created. Note that for this exercice I did not encrypt passwords (maybe in future developments).

![png](img/step5.png)
![png](img/step6.png)

### Ok now let's connect to the "libra" user account!

![png](img/screen3.png)
![png](img/screen4.png)
![png](img/screen5.png)

### A librarian can search for a user account

![png](img/screen6.png)
![png](img/screen7.png)

### Can create a new reference and find the right category of a book using the Dewey Classification

![png](img/screen8.png)
![png](img/screen9.png)









