#this program for my real life example
#import numpy as np
from array import *
from time import *

class room:



    def count(self,number):
     one=0
     two=0
     three=0
     four=0
     five=0
     six=0
     seven=0
     eight=0
     nine=0
     ten=0

     for i in range(0,len(number)):
            if 1==number[i]:
                one+=1
            elif 2==number[i]:
                two+=1
            elif 3==number[i]:
                three+=1
            elif 4==number[i]:
                four+=1
            elif 5==number[i]:
                five+=1
            elif 6==number[i]:
                six+=1
            elif 7==number[i]:
                seven+=1
            elif 8==number[i]:
                eight+=1
            elif 9==number[i]:
                nine+=1
            elif 10==number[i]:
                ten+=1
            else:
                print("the number you choose is greater than 10")

     sleep(5)
     if one <= two and one <= three and one <= four and one <= five and one <= six and one <= seven and one <= eight and one <= nine and one <= ten:
         print("the number 1 who choose is lucky and won the lotry")
     elif two <= three and two <= four and two <= five and two <= six and two <= seven and two <= eight and two <= nine and two <= ten:
         print("the number 2 who choose is lucky and won the lotry")
     elif three <= four and three <= five and three <= six and three <= seven and three <= eight and three <= nine and three <= ten:
         print("the number 3 who choose is lucky and won the lotry")
     elif four <= five and four <= six and four <= seven and four <= eight and four <= nine and four <= ten:
         print("the number 4 who choose is lucky and won the lotry")
     elif  five <= six and five <= seven and five <= eight and five <= nine and five <= ten:
         print("the number 5 who choose is lucky and won the lotry")
     elif six <= seven and six <= eight and six <= nine and six <= ten:
         print("the number 6 who choose is lucky and won the lotry")
     elif seven <= eight and seven <= nine and seven <= ten:
         print("the number 7 who choose is lucky and won the lotry")
     elif eight <= nine and eight <= ten:
         print("the number 8 who choose is lucky and won the lotry")
     elif nine <= ten:
        print("the number 9 who choose is lucky and won the lotry")
     else:
         print("the number 10 who choose is lucky and won the lotry")

arr=array('i', [])

n = int(input("enter the length..."))


for i in range(n) :
    x=int(input("enter the value..."))
    arr.append(x)

print(arr)
r1=room()
#r1.__init__(arr)
r1.count(arr)



