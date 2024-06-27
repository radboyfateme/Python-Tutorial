class person : 
    id=None
    _name=None
    __lastName=None

    def __init__(self,id,name, lastName):
        self.id= id
        self._name=name
        self.__lastName=lastName

    def getlastname(self) :
        return self.__lastName 

    def setlastname(self,newlastname) :
        self.__lastName=newlastname 

    def _showpersoninfo(self)  :
        print(f'{self.id}\t\t{self._name}\t\t{self.__lastName}')  

class student(person):
    __studentId=None
    def __init(self,studentId, id, name, lastName):
        super().__init__(id,name,lastName)
        self.__studentId=studentId

    def showstudentinfo(self):
        print(self.__studentId)
        self._showpersoninfo()

student1 =student(1234, 'Hanar','Rad')  
student1.showstudentinfo()  


# person1=person(1, 'Hanar', 'Rad')
# print(person1.id)  
# print(person1._name) 
# print(person1.getlastname())
# person1.setlastname('Raad') 
# print(person1.getlastname())
# person1.showpersoninfo()

