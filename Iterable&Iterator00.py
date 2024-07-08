# list1=[1,2,3,4,5,6]
# it_list=iter(list1)
# print(next(it_list))


# name ='Hanar'
# it_name=iter(name)

# while True:
#     try:
#         print(next(it_name))
#     except:
#         break

# list1=[12,1,31,2,11,16,18,19]
# # for i in list1:
# #     print(i,end='\t')
# itlist1=iter(list1)
# for i in range(len(list1)):
#     print(next(itlist1))

def checkitrable(obj):
    try:
        iter(obj)
        return True
    except:
       return False
        

class person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
def __str__(self):
    return f'{self.name}\t\t{self.age}' 

person1 = person('Hanar','35') 
person2 = person('Ferman', 43)
person3 =person('sara', 25) 
people =[person1,person2,person3]  

print(checkitrable(people))
itpeople=iter(people)
print(next(itpeople))
print(next(itpeople))
print(next(itpeople))

