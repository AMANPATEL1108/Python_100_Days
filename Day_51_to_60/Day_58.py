class Person:
    def __init__(self,n,o):
        print("Hy this is constrctor Called")
        self.name=n
        self.occ=o

    
    def info(self):
        print(f"{self.name} is a {self.occ}")

a=Person("A","B")
b=Person("C","D")
a.info()
b.info()