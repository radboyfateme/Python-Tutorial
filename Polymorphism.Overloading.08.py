
# from multipledispatch import dispatch

# @dispatch(int,int)   #Decorator
# def sum(a,b):
#     return a+b

# @dispatch(int,int,int)
# def sum(a,b,c):
#     return a+b+c


# print(sum(10,20))
# print(sum(10,20,30))

class person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __add__(self,object2):
        return self.age+object2.age  
    
    def __mul__(self,object2):
        return self.age*object2.age
    
    def __lt__(self,object2):
        return self.age<object2.age
    
    #.....................................................................

    def sum (datatype,*args):     #Overloading
        if (datatype=='int'):
            s=0

        elif(datatype=='str'):
            s=''

        for item in args:
            s+=item
        return s

    print(sum('int',12,34,5))
    print(sum('int',12,13,14,15,16))
    print(sum('int',12,13))  
    print(sum('str','Hanar','Ferman'))  

person1 = person('Hanar', 35)
person2 = person('Ferman', 43)  
print(person1+person2 ) 
print(person1*person2) 
print(person1<person2)   

