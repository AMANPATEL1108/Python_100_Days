x=[1,2,3]   #list,tuple ....
# print(dir(x)) #//get all attribute methods all things get of that object
# print(x.__add__) 


#__dict__
class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age

p=Person("A","22")
# print(p.__dict__)  #as a dictory return a get all value of object return 



#Help method
print(help(str))
print(help(Person))  #return a Documentation of a that Object Related all Things