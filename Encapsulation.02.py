class person :
    def __init__ (self,name, lastName, age):
        self.__name = self.__toPascalCase(name)
        self.__lastName =self.__toPascalCase(lastName)
        self.__age = age

    def __toPascalCase(self,str1) :
        strlist=list(str1)
        strlist[0]=chr(ord(strlist[0])-32)
        return''.join(strlist)
    
    def _showpersoninfo(self):
        print(f'Name : {self.__name}')
        print(f'lastName :{self.__lastName}')
        print(f'Age :{self.__age}')


    def _getFullNamelength(self) :
        return len(self.__name) + len(self.__lastName)


class student(person) :
    def __init__(self,name,lastName,Age, studentId) :
        super().__init__(name,lastName,Age)
        self.__studentId = studentId

    def showstudentinfo(self) :
        print(f'student Id :{self.__studentId}') 
        self._showpersoninfo() 
        print(self._getFullNamelength) 


class Teacher(person) :
    def __init__(self,name,lastName,Age,teachercode):
        super().__init__(name,lastName,Age)
        self.__teachercode=teachercode

    def showteacherinfo(self):
        print(f'Teacher Code is :{self.__teachercode}')
         
           







student1 =student('hanar', 'rad',35, 10000) 
student1.showstudentinfo()

print('--------------------------------------------------')

teacher1 = Teacher('ferman', 'raad', 43,567)
teacher1.showteacherinfo()


        

           




person1 =person('Hanar','Rad',35)