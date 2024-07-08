def mainFun(func):
    def fun1(*args,**kwargs):
        print('¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤')
        func(*args,**kwargs)
        print('¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤')
    return fun1    

@mainFun
def sum(x,y):
    print(x+y)

sum(23,4)    