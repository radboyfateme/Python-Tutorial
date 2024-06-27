class person :
    count = 0
    def __init__(self, name, lastname):
        self.name = name
        self.lastname = lastname
        person.count+=1

    def __str__(self) :
        return self.name+ '\t\t'+self.lastname 

    def __del__(self):
        print(self.name+'the end') 
    

person1 = person('Hanar', 'Rad')  
print(str(person1)) 
print(person.count) 
