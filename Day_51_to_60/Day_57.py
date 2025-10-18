class Person:
    name="dev"
    occupation="Software Dev"
    netwoth=10

    def info(self):
        print(f"{self.name} is a {self.occupation}")

a=Person()
b=Person()
a.name="Dp"
a.occupation="Acc"
# print(a.name,a.occupation)
b.name="NK"
b.occupation="HR"
a.info()
b.info()