class cricketer:
    # class variable
    cricketer_name = 'KL Rahul'

    def __init__(self,name,jersey_no):
        self.name = name
        self.jersey_no = jersey_no

# create objects
c1 = cricketer('KL Rahul',1)
c2 = cricketer('virat',18)

print('before')
print(c1.name, c1.jersey_no, c1.cricketer_name)
print(c2.name, c2.jersey_no, c2.cricketer_name)

#modify class variable using object reference
c1.cricketer_name = 'virat'
print('After')
print(c1.name, c1.jersey_no, c1.cricketer_name)
print(c2.name, c2.jersey_no, c2.cricketer_name)
