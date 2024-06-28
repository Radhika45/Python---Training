import mysql.connector as db
from SQL1 import Customer

#Database username and password

#username = "root"
#password = "Radhika9$ "

#Local Host
#host = "127.0.0.1"
#database = "gw2024pds"

#Create Connection
connection=db.connect(user="root",
                      password = "Radhika9$",
                      host = "127.0.0.1",
                      database = "gw2024pds"
           )

print("Connection Created...")
print(connection)

customer = Customer()
customer.add_customer_details()



#Create SQL Statement
#sql="insert into Customer values(null, 'Sita', '+91 99888 77777', 'sita@gmail.com', 16 , 'Female')"
#sql="insert into Customer values(null, '{}', '{}', '{}', '{}', '{}')".format(customer.name, customer.phone, customer.email, customer.age, customer.gender)
sql_update = "update Customer set name = 'FionnaRest' , email='fionna@gmial.com' ,age = 18 , gender = 'Female' where cid = 2"

#Obtain Cursor -> Perform CRUD operations with MySQL
cursor = connection.cursor()

#Execute SQL Command
cursor.execute(sql_update)

#Commit the write operation
connection.commit()

print("Sql Statement Executed...")