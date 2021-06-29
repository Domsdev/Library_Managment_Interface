# Library Managment Interface

---

#### In this repository you will find the code and elements I used to create a desktop application for the managment of a library using Python, Tkinter and MySQL. I created this app as a concrete exemple to put into practice the skills I acquired during training courses in Python and SQL. The app is still under construction!

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
 <br/>
**Sending mails with smtplib: I created and configured a dedicated gmail adress (normaly set by the administrator of the library) in order to send emails with an activation code when a new user of the library is registered. Then, the user will be able to connect to the interface and connect to its newly created account by entering its activation code.** <br/>
 <br/>
Gmail by default tries to make your email secure by preventing this type of third-party access. You can manage your gmail security settings by allowing less secure apps. <br/>
 <br/>
![png](img/less_secure_app.png)
 <br/>
![png](img/critical_security_alert.png) <br/>
I allowed less secure apps only to test the code and experiment with it. I recommend to return your security settings back to its defaults when finished. <br/>
If you don’t want to lower the security settings of your Gmail account, check out Google’s documentation on how to gain access credentials for your Python script, using the OAuth2 authorization framework. <br/>
 <br/>
**Need to create environment variables as well for mail authentication, adding the following two lines at the end of my .bashrc file**<br/>
export SENDER_MAIL='email-adress'<br/>
export PASSWORD_MAIL='password'<br/>


## Test the application

### Clone the repository
![png](img/step0.png)


### Create two databases: "dewey_classification" and "library"
![png](img/step1.png)


### Built and fill the databases using python scripts in the dedicated folder.
![png](img/step2.png)
![png](img/step3.png)


### Launch the application using the python script.
![png](img/step4.png)


### Now you can see the app welcome page!
![png](img/screen1.png)


### Let's imagine that a librarian wants to connect to its own account:
![png](img/screen2.png)


### If you look the tables in the library database, and in the "User" table, you will find exemples of users I already created. Note that for this exercice I did not encrypt passwords (maybe in future developments).
![png](img/step5.png)
![png](img/step6.png)


### Ok now let's connect to the "libra" user account!
![png](img/screen3.png)
![png](img/screen4.png)
![png](img/screen5.png)


### And create a new User account.
![png](img/screen10.png)


### When entering informations, errors are handled specifically for each field (empty, not valid ...).
![png](img/screen11.png)

### Imagine the librarian has scanned the identity card of the new user to its computer desktop. The document will be inserted in the database for later consultation if needed.
![png](img/screen12.png)

### If an error occurs, this one is reported in a specific file for later consulation by administrator.
![png](img/error_file.png)
![png](img/error_report.png)
**In this case it was a smtplib credentials problem (forgot to allow Gmail less secure apps option)

### But now it is ok ... a mail with activation code has been sent to the new user's mail adress.
![png](img/screen14.png)
![png](img/screen15.png)


### Back to welcoming page, the user can select the account activation button.
![png](img/screen1.png)
![png](img/screen16.png)


### The user will be asked for a Pseudo and Password, then he will be able to connect normally to its account.
![png](img/screen17.png)
![png](img/screen18.png)
![png](img/screen19.png)
![png](img/screen20.png)
![png](img/screen21.png)


### A librarian can search for a user account
![png](img/screen6.png)

### Check the selected user account
![png](img/screen7.png)
![png](img/screen8.png)

### And modify/update entries if needed
![png](img/screen9.png)


### A librarian can also search for a book reference (I used Full-Text Search Functions of MySQL)
![png](img/screen40.png)
![png](img/screen41.png)

### Or can create a new reference and find the right category of a book using the Dewey Classification
![png](img/screen50.png)
![png](img/screen51.png)









