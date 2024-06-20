#File Handling using Import Function
from Ola3 import Customer

print("-----------CUSTOMER MANAGEMENT SYSTEM --------------")

while True:
    print("1.Add Customer")
    print("2.View Customer")
    print("3.Exit")
    
    choice= int(input("Enter Your Choice: "))
    print("You Selected: ",choice)

    if choice == 1:
        file = open("customers.csv","a")
        customer = Customer()
        customer.add_customer_details()
        customer.show()

        data = customer.to_csv()
        file.write(data)
        print("Data written: ",data)
    

    elif choice == 2:
        file = open("customers.csv","r")
        lines= file.readlines()
        for line in lines:
            print(line)

        print("View Customers: ")
        
       
    elif choice == 3:
        print("-------------------------------------")
        print("Thank You ! For using Customer Mangement")
        print("-------------------------------------")
        file.close()
        break