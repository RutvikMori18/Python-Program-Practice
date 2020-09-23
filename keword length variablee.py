def person(name,**data):
    print(name)
    for i,j in data.items():
        print(i,j)
 
person('rutvik',age=20,city='gujrat',mob=7878787878)
