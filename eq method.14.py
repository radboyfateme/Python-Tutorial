class person :
    
    def __init__(self, name, age):
        self.__name = name
        self.__age = age
        

    def showpersoninfo(self):
        print(self.__name)
        print(self.__age)

    def __eq__(self,obj2) :
        return self.__name==obj2.__name and self.__age==obj2.__age  
    def __str__(self):
        return f'{self.__name}\t\t {self.__age}'
        
person1 = person('Hanar', 35)
person2=person('Ferman', 43)
person3=person('Hanar', 35)

if person1==person3: 
    print('yes') 
else:
    print('no')

print(str(person1))
print(person1.__str__())
print(person1)


# print(person1.getname())
# person1.setname('Ferman')
# person1.showpersoninfo()


