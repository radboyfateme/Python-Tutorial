from abc import ABC,abstractmethod

class person(ABC) :
    
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @abstractmethod   
    def showinfo(self) :
        pass   

class student(person)  :
    def __init__(self,studentid,name,age)  :
        super().__init__(name,age) 
        self.studentid=studentid

    def showinfo(self):
        print(f'{self.name}\t\t{self.age}\t\t{self.studentid}')

class teacher(person):
    def __init__(self,teachercode,name,age):
        super().__init__(name,age) 
        self.teachercode=teachercode  

    def showinfo(self):
        print(f' Name :{self.name}\t\t Age :{self.age}\t\t Teachercode: {self.teachercode}')

student1=student('Hanar',35,1000)
tracher1=teacher(1,'Ferman',43)
student1.showinfo()
tracher1.showinfo()


# if person1==person3: 
#     print('yes') 
# else:
#     print('no')

# print(str(person1))
# print(person1.__str__())
# print(person1)



