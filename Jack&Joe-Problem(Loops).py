"""
   Another Brick in the Wall
    Who placed, the last brick and how many ?
    
    Mr. John -> Requirement | create a wall with 13 bricks

                    Total Bricks Placed
    jack : 1            1
    joe  : 2            3

    jack : 2            5
    joe  : 4            9

    jack : 3            12
    joe  : 6            13   

    joe -> last brick
           1 brick
"""
number_of_brick = int(input("Enter the number of bricks: "))

brick = 0       #It represents Total placed Bricks
last_brick = 0

for jack in range(0, number_of_brick):
    for joe in range(0, number_of_brick):

        while brick < number_of_brick:
            if (brick+jack) <= number_of_brick:
                jack += 1
                brick = brick + jack
                placer = "jack"
                print("Jack placed ", jack, "bricks and no of bricks ", brick)
            else:
                last_brick = number_of_brick - brick
                brick = number_of_brick
                placer = "jack"
                print("Jack placed ", jack, "bricks and no of bricks ", last_brick)
                break

            if (brick+joe) <= number_of_brick:
                joe = jack*2
                brick = brick + joe
                placer = "joe"
                print("Joe placed ", joe, "bricks and no of bricks ", brick)

            else:
                last_brick = number_of_brick - brick
                brick = number_of_brick
                placer = "joe"
                print("Joe placed ", last_brick, "bricks and no of bricks ", brick)
                break

            # print("Jack  Joe  Bricks")
            # print(jack, "     " , joe , "   ", brick)

print("Last brick was placed by", placer, "and he placed", last_brick, "bricks.")


'''
#Another Approach for Similiar Problem using If-Else Statements

number = int(input("Enter the number of bricks to be used: "))
sum = 0
jack = 1 
joe = 2 * jack
while sum < number:
    sum += jack 
   
    if sum >= number:
        result = sum - jack 
        print("Jack puts the last brick... i.e :", number - result )
        break
    else:
        print("Jack put ", jack, "brick")

    sum += joe 
    
    if sum >= number:
        result = sum - joe 
        print("Joe puts the last brick... i.e :", number - result )
        break
    else:
        print("Joe put ", joe, "brick")

    jack = jack + 1
    joe = 2 * jack

'''