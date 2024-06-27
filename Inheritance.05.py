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

    def show(self):
        print('BBBBB')   
#.............................................................
class C(B) :
    def __init__(self) : 
        B.__init__(self) 
        print('run init of c class') 

    def showC(self):
        print('CCCCC')     
#............................................................
c=C()
c.showC()
c.showA()  
        

