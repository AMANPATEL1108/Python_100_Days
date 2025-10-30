class Employee:

    company="Apple"

    def show(self):
        print(f"The Name is {self.name} an Complany is {self.company}")


    @classmethod  #using this that an upaet Apple to Tesla Other Wise Object company Name not Change
    def changedCompany(cls,newCompany):
        cls.company=newCompany


e1=Employee()
e1.name="Asd"
e1.show()
e1.changedCompany("Tesla")
e1.show()
print(Employee.company)