##this program is perform the first fifty fibonacci numbers
av=50
x=1
y=2
print(0)
print(1)
print(1)
print(2)
for i in range(0,100):
    if i>av :
        break
    else :
        z=x+y

        x=y
        y=z
        print(z)
print("first 50 fibonacci....")