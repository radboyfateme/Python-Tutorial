#Decorator
#every thing in python is a object
# def func1(name):
#     return 'Hello'+name
# print(func1('HANAR'))
# func2=func1
# print(func2('Ferman'))

# del func1
# print(func2('Zara'))

#Nested Function
# def fun(name):
#     print('inside in fun'+name)
#     def fun1():
#         return 'inside in fun1'
#     def fun2():
#         return 'inside in fun2'
#     print('inside in fun2 '+ name)
#     print(fun1())
#     print(fun2())

# fun('Hanar') 
# fun2()  it is not  possible call here 

# def fun1(text):
#     return ' * '+text+' * '

# def fun2(text):
#     str1=''
#     for i in range (5):
#         str1+=text
#     return str1   

# def mainfun(func):
#    print(func('Ferman'))

# print(mainfun(fun1))
# print(mainfun(fun2))


def mainfun(name):
    def fun1():
        print(name)
    print('-----------------------------------')  
    return fun1  

k=mainfun('Hanar')
k()

        



