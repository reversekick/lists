# lists

1. To clone use the command 
git clone git@github.com:{github user id}/lists.git

2. After you make changes use 
a. git add <<changed files>>
b. git commit -s 
c. git push 


##INSTALL CASSANDRA DRIVER FOR PYTHON
pip install cassandra-driver


##rest.py
we are using web package to create the REST service.
###Install web.py (MANDATORY)
pip install web.py

###TO START THE SERVICE
python rest.py

###TEST(GET)

###BY USER
To get data of particular user
http://localhost:8080/task/siddiq

###ALL USERS
This will give all infomation
http://localhost:8080/all

###TEST(POST)
python post.py