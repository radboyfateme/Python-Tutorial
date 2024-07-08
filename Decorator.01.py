def mainFun(func):
    def fun1():
        print('*****************')
        func()
        print('######################')
    return fun1    


def printName():
    print('Hanar')

k=mainFun(printName) 
k()   