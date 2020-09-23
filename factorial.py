def fact(n) :
    x = 1
    for i in range (1,n+1):
        x = x*i

    return x

a=int(input("enter the number which you get fectorial"))
number= fact(a)
print(number)