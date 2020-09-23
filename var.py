class car:
    wheel=5#class variable
    def __init__(self):
        self.name='bmw'#instance variable
        self.mil=20



c1=car()
c2=car()
car.wheel=4
print(c1.name,c1.mil,c1.wheel)
print(c2.name,c2.mil,c1.wheel)