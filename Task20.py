''' Write a Python class to reverse a string word by word. '''
class py_reverse:
   def revr(self, strs):
       sp=strs.split()
       sp.reverse()
       res=" ".join(sp)
       return res

str1=input("Enter a string with 2 or more words : ")
print("Reverse of string word by word: \n",py_reverse().revr(str1));