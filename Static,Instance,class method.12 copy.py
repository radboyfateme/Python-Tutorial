class person :
    
    def __init__(self, name, age):
        self.name = name
        self.age = age
        

    def showpersoninfo(self):
        print(self.name)
        print(self.age)

    @staticmethod
    def sum(x,y):
        return x+y
    @classmethod
    def func1(cls,x,y):
        return cls.sum(x,y)+2000
      

person1 = person('Hanar', 'Rad')  
person1.showpersoninfo()           # Instance Method

print(person.sum(20,40))           #Static Method
