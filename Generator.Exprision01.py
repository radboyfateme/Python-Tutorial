#Generator Comprihension  sign ()
#It is like a list comprehension []

# list1=[x for x in range(1,100)]
# print(list1)

# obj1 =(x for x in range (1,100))
# #print(obj1) it is not work
# for item in obj1:
#     print(item,end='\t')

#Lazy Evaluation

# list1=[x for x in range(1,1000)]
# print(list1[0:8])

# obj1=(x for x in range(1,1000))
# for i in range(0,8):
#    print(next(obj1), end=' , ')


#fib with Generator
def fib(n):
    a=0
    b=1
    yield b
    for i in range(1,n):
        a,b=b,a+b
        yield b
for item in fib(5) :
    print(item,end='\t')       






    









