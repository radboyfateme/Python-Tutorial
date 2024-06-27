class A:
    def __init__(self):
        print('run init of A  class')

    def showA(self):
        print('AAAAA') 
#............................................................
class B(A) :
    def __init__(self):
        A.__init__(self)
        print('ran init of B  class') 

    def showB(self):
        print('BBBBB')   
#.............................................................
class C(A) :
    def __init__(self) : 
        A.__init__(self) 
        print('run init of c class') 

    def showC(self):
        print('CCCCC')     
#............................................................
class D(B,C) :
    def __init__(self):
        B.__init__(self)
        C.__init__(self)
        print('run init of D class')

    def showD(self) :
        print('DDDDD')  
#.........................................................
d=D()

