
#Patient management app
from Patient1 import Patient
from Patient1A import Consultation
from DatabaseFile import Database
from tabulate import tabulate

def main():
    print("---------------------------")
    print("=======DOCTOR's App========")
    print("---------------------------")

    db = Database()

    while True:
        print("1. Add New Patient")
        print("2. Update Exixting Patient")
        print("3. Delete Existing Patient")
        print("4. View Patient by phone")
        print("5. View Patient by PID")
        print("6. View All Patients")
        print("7. Add Consultation For Patient")
        print("8. View All Consultations")
        print("9. View Consultation of a Patient")
        print("10.View Follow ups")
        
        print("0: To Quit App")

        choice = int(input("Enter Your Choice: "))

        if choice == 1:
            patient = Patient()
            patient.add_patient_details()
            sql = "insert into Patient values(null, '{name}','{phone}','{email}','{dob}','{gender}','{created_on}')".format_map(vars(patient))
          # sql = "insert into Patient values(null,'{}','{}','{}',{},'{}',null)"
          #.format(patient.name,patient.phone,patient.email,patient.dob,patient.gender)
          
            db.write(sql)
            print("[Patient App]",patient.name,"Saved in Database")

        elif choice == 2:
            pid = int(input("Enter Patient pid to Update: "))
            sql = "select * from Patient where pid = {}".format(pid)
            rows = db.read(sql)
            print(rows)

            patient = Patient( pid=pid, name=rows[0][1], phone=rows[0][2], email=rows[0][3], dob=rows[0][4] , gender=rows[0][5] )

            print("Patient to update: ")
            patient.show()
            patient.update_patient_details()
            
            sql = "update Patient set name = '{name}', phone= '{phone}', email= '{email}',dob= '{dob}' ,gender= '{gender}',created_on ='{created_on}' where pid ={pid}".format_map(vars(patient))
           
            db.write(sql)
            patient.show()
            
        elif choice == 3:
            pid = int(input("Enter Patient Id to Delete: "))
            sql = "delete from Patient where pid = {}".format(pid)
            ask = input("Are you sure you want to delete ? ")
            if ask == "yes":
                db.write(sql)
                print("[PMS App]",pid,"Deleted from Database")

            else:
                print("Delete opearation skipped")

            
        elif choice == 4:
            phone = (input("Enter Patient Phone to View: "))
            sql = "select * from Patient where phone = '{}' ".format(phone)
            rows = db.read(sql)
            
            columns = ["pid","name","phone","email","dob","gender","created_on"]
            print(tabulate(rows, headers=columns, tablefmt ='grid'))


        elif choice == 5:
            pid = int(input("Enter Patient pid to View: "))
            sql = "select * from Patient where pid = {}".format(pid)
            rows = db.read(sql)
            
            columns = ["pid","name","phone","email","dob","gender","created_on"]
            print(tabulate(rows, headers=columns, tablefmt ='grid'))

            

        elif choice == 6:
            sql = "select * from patient"
            rows = db.read(sql)
            
            columns = ["pid","name","phone","email","dob","gender","created_on"]
            print(tabulate(rows, headers=columns, tablefmt ='grid'))
          
           # for patient in Patients:
            #    print(patient)
            
        elif choice == 7:
            consultation = Consultation()
            consultation.add_consultation_details()
            sql = "insert into Consultation values(null, '{pid}','{remarks}','{medicines}','{next_followup}','{created_on}')".format_map(vars(consultation))
         
            db.write(sql)
            print("Consultation Created.....")
        
        elif choice == 8:
            sql = "select * from Consultation"
            rows = db.read(sql)

            columns = ["cid","pid","remarks","medicines","next_followup","created_on"]
            print(tabulate(rows,headers=columns, tablefmt ='grid'))
        
        elif choice == 9:
            pid = int(input("Enter Patient ID: "))
            sql = "select * from Consultation where pid = {}".format(pid)
            rows = db.read(sql)

            columns = ["cid","pid","remarks","medicines","next_followup","created_on"]

            print(tabulate(rows, headers = columns, tablefmt= 'grid'))

        elif choice == 10:
            start_date = (input("Enter Start Date Time(yyyy-mm-dd  hh:mm:ss):"))
            end_date = (input("Enter End Date Time(yyyy-mm-dd  hh:mm:ss): "))

            sql = "select * from Consultation where next_followup>= '{}' and next_followup<= '{}'".format(start_date,end_date)
            rows = db.read(sql)

            columns = ["cid","pid","reamrks","medicines","next_followup","created_on"]

            print(tabulate(rows,headers=columns,tablefmt='grid'))


        elif choice == 0:
            break

        else:
            print("[Patient Management System App]Invalid choice")

if __name__ == "__main__":
   main()

