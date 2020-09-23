class students:
    school="vvp eengineering college"


    def __init__(self,m1,m2,m3):

        self.m1=m1
        self.m2=m2
        self.m3=m3
    def avg(self,):
        return (self.m1+self.m2+self.m3)/3
    @classmethod
    def getschool(cls):
        return cls.school
    @staticmethod
    def info():
        print("it is additional method...")
s1=students(50,60,70)
s2=students(40,80,100)
print(s1.avg())
print(s2.avg())
print(students.getschool())
print(students.info())
