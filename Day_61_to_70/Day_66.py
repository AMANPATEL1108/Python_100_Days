class Employee:
    companyName="Apple"
    noOfEmployee=0
    def __init__(self,name):
        self.name=name
        self.raise_amount=0.02
        Employee.noOfEmployee += 1

    def showDetails(self):
        print(f"The name of Employee is {self.name} and the raise amount in {self.noOfEmployee} sized  {self.companyName} is {self.raise_amount}")

# Employee.showDetails(emp1)
emp1=Employee("Qwe")
emp1.raise_amount=0.3
emp1.companyName="Apple India"
emp1.showDetails()
Employee.companyName="Google"
print(Employee.companyName)
emp2=Employee("Asd")
emp2.companyName="Nestle"
emp2.showDetails()
