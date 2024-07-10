#Built-In-Functions in SET

john_followers = {"Fionna","Sia","Joe","George"}
print(john_followers)
print(type(john_followers))
print(len(john_followers))

numbers = list(range(10,101,10)) #Converting list of numbers into set
numbers1 = set(numbers)
print("Numbers: ",numbers)
print("Numbers1: ",numbers1)

#(1) add() ->   variable_name.add(new_element)
numbers1.add(101)
numbers1.add(201)

print("Numbers1: ",numbers1)


#(2) remove() -> variable_name.remove(ele_to_remove)
# pop() -> Pop function does not work on Set
# remove() -> Remove is applicable both on List and Set
print("1.numbers1: ",numbers1)
numbers1.remove(90)
print("2.numbers1: ",numbers1)
numbers1.remove(101)
print("3.numbers1: ",numbers1)
numbers1.discard(20)
print("4.numbers1: ",numbers1)


john_follower = {"a","b","c","d"}
jake_follower = {"b","d"}
fionna_follower = {"d","b"}

#(3)Intersection function -> new_var = set_var1.intersection(set_var2)
mutual_follower = john_follower.intersection(jake_follower)
print(mutual_follower)

#(4)Issubset function -> If one set is contained in other
result = fionna_follower.issubset(john_follower)
print("Result is: ",result)

A = {1,2,3,4,5}
B = {4,5,6,7,8}

""" Concatenation Opearation does not work on Set i.e +
C= A + B
print("C is: ",C)"""

D = A - B
print("D is: ",D)

E = A  ^ B # It will print friends except mutual ones XOR
print("E is: ",E)

F = A|B   # It will Concatenate all emlements OR
print("F is :",F)

A.clear()
print("A is: ",A)
print("Length of A is: ",len(A))


