#Nested Loop
#Chess problem -> Printing white and Black Squares

'''
for i in range(0,8):
   # print("i is: ",i)

    for j in range(0,8):
      # print(j, end="#")

        if i % 2 == 0:
            print(j % 2, end=" ")
        
        else:
         print((j + 1) % 2, end=" ")
    print()  
'''
   
white_square = "\u25A1"
black_square = "\u25A0"


for i in range ( 0 , 8):
    
    for j in range ( 0 , 8):
        if(i%2 == 0):
            if j%2 == 0:
                print('\u25A0' , end = " ")
            else:
                print('\u25A1' , end = " ")
            
        else:
            if (j+1)%2 == 0:
                print('\u25A0' , end = " ")
            else:
                print('\u25A1' , end = " ")
    print()
    