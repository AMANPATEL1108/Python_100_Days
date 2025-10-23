#public Example For Access Modifier
# class Employee:
#     def __init__(self):
#         self.name="Asd"

# a=Employee()
# print(a.name)

#private Example For Access Modifier __ using we can  create a Private Acess Modifier
# class Employee:
#     def __init__(self):
#         self.__name="Asd"

# a=Employee()
# print(a._Employee__name)  #we can acess indrirectly like this 

#Protected Example For Access Modifier
class Student:
    def __init__(self):
        self._name="Asd"

    def _funName(self):
        return "QWE"
        
class Subject(Student):
    pass

obj=Student()
obj1=Subject()

print(obj._name)
print(obj._funName())
print(obj1._name)
print(obj1._funName())