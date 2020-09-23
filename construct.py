class computer:
    def __init__(self):
        self.name="rutvik"
        self.age=20


    def compare(self,other):
        if self.age==other.age:
            return True
        else:
            return False

c1=computer()
c1.age=20
c2=computer()
c2.name="mori"
c2.age=30


if c1.compare(c2):
    print("they are same")
else:
    print("they are diffrent")
print(c2.name)
print(c1.name)
