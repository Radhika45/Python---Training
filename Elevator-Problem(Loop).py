#Elevator Problem

floors = 10 
floor = 0 #0th floor or default floor

floor_to_go = int(input("Enter Floor Number to go: "))
"""
while floor <= floors:
    print("At floor Number: ",floor) #Infinite loop since this condition is always true 0<10
    
    if floor_to_go == floor:
        print("You have reached the floor,"floor)
        break
       
    floor += 1
"""


for floor in range(0,11): #As Range 0 to 11 will only print 0 to 10
    print("At Floor number:",floor)

    if floor_to_go == floor:
        print("You have reached the required floor",floor)
        break
   

