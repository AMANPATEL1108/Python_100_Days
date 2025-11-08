class Animal():
    def __init__(self,name,species):
        self.name=name
        self.species=species


    def make_sounf(self):
        print("Sound Mad e by Animal")
    

class Dog(Animal):

    def __init__(self, name, breed):
        Animal.__init__(self,name,species="dog")
        self.breed=breed

    def make_sound(self):
        print("bark")

d=Dog("Dog Say","Doggg")
d.make_sound()

a=Animal("Amimal Say","Anmialll")
a.make_sounf()