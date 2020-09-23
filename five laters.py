def fivenums(list):
    num=0
    for i in range (list) :
        if len(list[i])>=5:
          num+=1


    return num



for i in range (10):
    list=int(input("enter the numbers.."))


numbers = fivenums(list)
print(numbers)