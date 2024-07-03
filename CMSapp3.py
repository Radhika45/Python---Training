#customer management app
from CMSapp1 import Customer
from CMSapp2 import Database
from tabulate import tabulate

def main():
    print("------------------")
    print("Welcome to CMS App")
    print("------------------")

    db= Database()

    while True:
        print("1. Add New Customer")
        print("2. Update Exixting Customer")
        print("3. Delete Existing Customer")
        print("4. View Customer by phone")
        print("5. View Customer by CID")
        print("6. View All Customers")
        print("0: To Quit App")

        choice = int(input("Enter Your Choice: "))

        if choice == 1:
            customer = Customer()
            customer.add_customer_details()
            sql = "insert into Customer values(null, '{name}','{phone}','{email}',{age},'{gender}','{created_on}')".format_map(vars(customer))
          # sql = "insert into Customer values(null,'{}','{}','{}',{},'{}',null)"
          #.format(customer.name,custome.phone,customer.email,customer.age,customer.gender)
          
            db.write(sql)
            print("[CMS App]",customer.name,"Saved in Database")

        elif choice == 2:
            cid = int(input("Enter Customer cid to Update: "))
            sql = "select * from Customer where cid = {}".format(cid)
            rows = db.read(sql)
            print(rows)

            customer = Customer( cid=rows[0][0], name=rows[0][1], phone=rows[0][2], email=rows[0][3], age=rows[0][4] , gender=rows[0][5] )

            print("Customer to update: ")
            customer.show()
            customer.update_customer_details()
            
            sql = "update Customer set name = '{name}', phone= '{phone}', email= '{email}',age= {age} ,gender= '{gender}',created_on ='{created_on}' where cid ={cid}".format_map(vars(customer))
           
            db.write(sql)

            customer.show()
            
        elif choice == 3:
            cid = int(input("Enter Customer Id to Delete: "))
            sql = "delete from customer where cid = {}".format(cid)
            ask = input("Are you sure you want to delete ? ")
            if ask == "yes":
                db.write(sql)
                print("[CMS App]",cid,"Deleted from Database")

            else:
                print("Delete opearation skipped")

            
        elif choice == 4:
            phone = (input("Enter Customer Phone to View: "))
            sql = "select * from Customer where phone = '{}' ".format(phone)
            rows = db.read(sql)
            
            columns = ["cid","name","phone","email","age","gender","created_on"]
            print(tabulate(rows, headers=columns, tablefmt ='grid'))


        elif choice == 5:
            cid = int(input("Enter Customer cid to View: "))
            sql = "select * from Customer where cid = {}".format(cid)
            rows = db.read(sql)
            
            columns = ["cid","name","phone","email","age","gender","created_on"]
            print(tabulate(rows, headers=columns, tablefmt ='grid'))

            

        elif choice == 6:
            sql = "select * from customer"
            rows = db.read(sql)
            
            columns = ["cid","name","phone","email","age","gender","created_on"]
            print(tabulate(rows, headers=columns, tablefmt ='grid'))
          
           # for customer in customers:
            #    print(customer)
            

        elif choice == 0:
            break

        else:
             print("[CMS App]Invalid choice")

if __name__ == "__main__":
   main()
