def mainFun(func):
    def fun1():
        print('###############')
        for i in range (6):
            func()
        print('##############') 
    return fun1 




@mainFun
def printStar():
    print('************************') 

printStar()     