class Employee:
    def __init__(self,name,id):
        self.name=name
        self.id=id

    def showDetails(self):
        print(f"Thae name of Employee : {self.id} is {self.name}")


class Programmer(Employee):
    def showLanguages(self):
        print(f"The Dfaulr language is Python")

e1=Employee("Abc",500)
e2=Programmer("Pqr",34)
e1.showDetails()
e2.showLanguages()