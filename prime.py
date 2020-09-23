print("enter ypur number...")
num=int(input())
for i in range (2,num):
    if num % i ==0 :
        print("your number is not prime...")
        break
else:
        print("your number is prime...")


