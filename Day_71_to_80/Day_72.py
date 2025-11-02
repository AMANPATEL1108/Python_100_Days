# class ParentClass:


#     def parent_method(self):
#         print("This is a Parent Method")

# class ChildClass(ParentClass):
#     def parent_method(self):
#         print("Asd")
#         super().parent_method()

#     def child_method(self):
#         print("This is a child method")
#         super().parent_method()

# child_object=ChildClass()   
# child_object.child_method()
# child_object.parent_method()


class Employee:
    def __init__(self,name,id):
        self.name=name
        self.id=id


class Programemr(Employee):
    def __init__(self,name,lang,id):
        self.name=name
        # self.lang=lang
        # self.id=id
        super().__init__(name,id)
        self.lang=lang
        
asd=Employee("Asd","450")
qwe=Programemr("Qwe","321","Py")

print(qwe.name)
print(qwe.id)
print(qwe.lang)
