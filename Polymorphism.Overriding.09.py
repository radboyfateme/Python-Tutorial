class A:
    def fun1(self):
        print('A class run fun2')


    def fun2(self) :
        print('A class run fun1')


    def fun3(self):
        print('A class run fun3')
        

#..........................................................................       
class B:
    def fun1(self):
        print('B class run fun1')

    def fun2(self):
        print('B class run fun2') 

    def sum(self,a,b):
        return a+b       
#..........................................................................
def func(obj):
    obj.fun1()
    obj.fun2()

a=A()
b=B()
func(a)
func(b)
