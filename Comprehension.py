# list1 =[]
# for i in range (1,11):
#     list1.append(i*i)
# print(list1)    
# list1=[x*x for x in range(1, 11)]
# print(list1)

# list1=[(x+100) for x in range(1, 11)]
# print(list1)

# def fun1(n):
#     y=n-1
#     z=n+5
#     return y+z-n

# list1=[ fun1(i) for i in range(1, 11)]
# print(list1)
# list1 = [10,20,30,40,50]
# list2 =[i*i*i if i%2==0 else i+100 for i in list1 if i >20]
# print(list2)

# dic1 ={x:x*x for x in range (1, 11)}
# print(dic1)

# dic1 ={x:str(x*x) for x in range (1, 11)}
# print(dic1)

# def getcolor(n):
#     if n==1:
#         return 'Red'
#     elif n==2:
#         return 'Blue'
#     return 'Green'
# list1=[1,2,3,4,5,6,7,8,9,10]
# dic1 ={x*x:getcolor(x) for x in list1 }
# print(dic1)

#zip class
# list1=[1,2,3,4,5,6]
# list2=['hanar','ferman','neda','ali','sara','anna']
# zip1=zip(list1,list2)
# print(zip1)
# print(type(zip1))

# for key,value in zip1:
#     print(f'{key} : {value}')


# list1=[1,2,3,4,5,6,7]
# list2=['hanar','ferman','neda','ali','sara','anna']
# zip1=zip(list1,list2)
# print(zip1)
# print(type(zip1))

# for key,value in zip1:
#     print(f'{key} : {value}')


# list1=[1,2,3,4,5,6]
# list2=['hanar','ferman','neda','ali','sara','anna']
# dic1={key:value for key, value in zip(list1,list2)}
# print(dic1)


#set comprehention
# list1=[1,2,3,4,2,2,2,2,2,2,2,2,2,5,6,7,8]
# set={x for x in list1}
# print(set)


##nested comprehention
# matrix=[]
# for i in range (0,3):
#     matrix.append([])
#     for j in range(1,6):
#         matrix[i].append(j)
# print(matrix)   
# 


# matrix=[[ j for j in range (1,6)] for i in range(0,3)]
# print(matrix)


# matrix =[[ j*i for j in range (1,11)] for i in range(1,11)]
# print(matrix)







