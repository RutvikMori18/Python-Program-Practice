import array

arr=array.array('i', [])

n = int(input("enter the length..."))


for i in range(n) :
    x=int(input("enter the value..."))
    arr.append(x)




print("your array is here...",arr)



val=int(input("enter the value for search..."))
k=0
for i in arr:
    if i ==val :
        print("your number in index... ",k)
        break

    k+=1