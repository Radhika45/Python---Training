"""
SQL  -> Structured Query Language

1. Executing Some SQL Commands in MySQL Command Line Client

        Object Relational Mapping (ORM)
        
        # 1: List Databases
        show databases;

        # 2: Creating Database
        create database gw2024pds;

        # 3: Selecting the database , to create a table inside it
        use gw2024pds;

        # 4: Create table
        create table Customer(
            cid int primary key auto_increment,
            name varchar(256), 
            phone varchar(15), 
            email varchar(256),
            age int, 
            gender varchar(10)
        );

        # 5: To Check if table is created in database
        show tables;

        # 6: To Check the table structure
        describe Customer;


        # 7: Create Customer in Table or Inserting Values in Database
        insert into Customer values(null, 'John', 
            '+91 99999 11111', 'john@example,com', 20, 'male');

        insert into Customer values(null, 'Fionna', 
            '+91 99999 22222', 'fionna@example,com', 22, 'female');
            
        insert into Customer values(null, 'George', 
            '+91 99999 33333', 'george@example,com', 31, 'male');

        insert into Customer values(null, 'Ben', 
            '+91 99999 44444', 'ben@example,com', 19, 'male');

        # 8: Fetching Data from Customer
        select * from Customer;
        select * from Customer where email = 'john@example.com';
        select * from Customer where cid = 2;
        select * from Customer where cid = 2 and email = 'fionna@example.com';
        select * from Customer where gender = 'male' and age >=20;
        select name, phone from Customer where cid = 2;

        # 9: Update Operation
        update Customer set name = 'Johnnathon', 
            email = 'john.jj@example.com', age=45 where cid = 1;

        # 10: Delete Customer
        delete from Customer where cid = 1;

        create table Address(
            aid int primary key auto_increment,
            houseno varchar(256), 
            addressline varchar(15), 
            city varchar(256),
            state varchar(256),
            zipCode int, 
            landmark varchar(10)
        );

2. Work with Virtual Environment
        # 1: Creating Virtual Environment in VS Code  New Terminal
        python -m venv myenv
        
        # 2: Activate Virtual Environment
        (windows)
        .\myenv\Scripts\activate

        (mac/linux)
        source myenv/bin/activate

3. Installation of Driver
        pip install mysql-connector-python

4. SQL Connection with Python

"""
class Customer:

    def __init__(self, name=" ", phone=" ", email=" ", age=" ", gender=" "):
        self.name = name
        self.phone = phone
        self.email = email
        self.age = age
        self.gender = gender

    def add_customer_details(self):
        self.name = input("Enter Your Name: ")
        self.phone= input("Enter Your Phone: ")
        self.email= input("Enter Your Email: ")
        self.age = int(input("Enter Your Age: "))
        self.gender = input("Enter Your Gender: ")
        

    def show(self):
        print("------------CUSTOMER--------------")
        print("{} | {}".format(self.name, self.phone))
        print("{} | {}".format(self.email, self.age))
        print("{} ".format(self.gender))

        print("----------------------------------")

class Address :

    def __init__(self,houseno,addressline,city,state,zipcode,landmark):
        self.houseno = houseno
        self.addressline = addressline
        self.city = city
        self.state = state
        self.zipcode = zipcode
        self.landmark = landmark


customer1 = Customer(name="John", phone ="+91 99999 11111", email="john@example.com" , age = 20, gender="Male")
#print(vars(customer1)) #Default Format

customer1.show()