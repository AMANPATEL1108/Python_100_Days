class Employee:
    name="Asd"

    # def __init__(self,name):
    #     self.name=name

        
    def __len__(self):
        i=0
        for c in self.name:
            i=i+1
        return i;



    def __str__(self):
        return (f"The name of Empoyee is {self.name} str")
    
    def __repr__(self):
        return (f"The name of Empoyee is {self.name} repr")
    
    def __call__(self):
        print("Hey I am Good")
        

e=Employee()
print(str(e))
print(repr(e))
# print(call())
# print(e.name)
# print(len(e))