class A:
    def __init__(self):
        print('run init of A  class')

    def shoe(self):
        print('AAAAA') 
#............................................................
class B(A) :
    def __init__(self):
        A.__init__(self)
        print('ran init of B  class') 

    def show(self):
        print('BBBBB')   
#.............................................................
b=B()         

