class A:
    def __init__(self):
        print('run init of A  class')

    def shoe(self):
        print('AAAAA') 
#............................................................
class B :
    def __init__(self):
        print('ran init of B  class') 

    def show(self):
        print('BBBBB')   
#.............................................................
class C(A,B) :
    def __init__(self) :
        A.__init__(self) 
        B.__init__(self) 
        print('run init of c class') 

    def showC(self):
        print('CCCCC')     
#............................................................
c=C()
c.showC()  
        

