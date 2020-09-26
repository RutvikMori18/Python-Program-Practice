#this program for my real life example
import numpy as np
import array
class room:
    def __init__(self,number):
        for i in range(0,len(number)):
            self.number=number


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


     if one <= two and one <= three and one <= four and one <= five and one <= six and one <= seven and one <= eight and one <= nine and one <= ten:
         print("the number 1 who choose is lucky and won the lotry")
     elif two<=one and two <= three and two <= four and two <= five and two <= six and two <= seven and two <= eight and two <= nine and two <= ten:
         print("the number 2 who choose is lucky and won the lotry")
     elif three <= one and three <= two and three <= four and three <= five and three <= six and three <= seven and three <= eight and three <= nine and three <= ten:
         print("the number 3 who choose is lucky and won the lotry")
     elif four <= one and four <= two and four <= three  and four <= five and four <= six and four <= seven and four <= eight and four <= nine and four <= ten:
         print("the number 4 who choose is lucky and won the lotry")
     elif five <= one and five <= two and five <= three and five <= four and five <= six and five <= seven and five <= eight and five <= nine and five <= ten:
         print("the number 5 who choose is lucky and won the lotry")
     elif six <= one and six <= two and six <= three and six<=four and six <= five and six <= seven and six <= eight and six <= nine and six <= ten:
         print("the number 6 who choose is lucky and won the lotry")
     elif seven <= one and seven <= two and seven <= three and seven <= four and seven <= five and seven <= six and seven <= eight and seven <= nine and seven <= ten:
         print("the number 7 who choose is lucky and won the lotry")
     elif eight <= one and eight <=two and eight <= three and eight <= four and eight <= five and eight <= six and eight <= seven and eight <= nine and eight <= ten:
         print("the number 8 who choose is lucky and won the lotry")
     elif nine <= one and nine <=two and nine <= three and nine <=four and nine <= five and nine <=six and nine <=seven and nine <=eight and nine <= ten:
        print("the number 9 who choose is lucky and won the lotry")
     else:
         print("the number 10 who choose is lucky and won the lotry")

num=1
number=0
while num<=10:
     number=int(input("enter the number : "))
     np.append(number)
     print(number)
     num+=1
#r1=room()
#r1.__init__(number)
#r1.count(number)



