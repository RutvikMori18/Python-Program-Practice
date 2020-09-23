#exaption

a=5
b=0
try:
    print(a/b)
except Exception:
    print("you can not divide a number by zero")
finally:
    print('bye')