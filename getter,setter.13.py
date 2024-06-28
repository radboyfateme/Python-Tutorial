class person :
    
    def __init__(self, name, age):
        self.__name = name
        self.__age = age
        

    def showpersoninfo(self):
        print(self.__name)
        print(self.__age)
    @property                         #
    def name(self):
        return self.__name 
    @name.setter
    def name(self,name):
        self.__name=name  

    @property
    def age(self) :
        return self.__age
    @age.setter
    def age(self,age):
        self.__age=age
            


    # def getname(self) :       #getter
    #     return self.__name 

    # def setname(self,name):   #setter
    #     self.__name=name  

      

person1 = person('Hanar', 'Rad')  
person1.showpersoninfo()           # Instance Method
print(person1.name)
# print(person1.getname())
# person1.setname('Ferman')
# person1.showpersoninfo()


