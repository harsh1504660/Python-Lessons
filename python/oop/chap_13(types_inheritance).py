# SINGLE INHERITANCE
class Animal:
    def __init__(self,name,species):
        self.name = name
        self.species = species
    
    def make_sound(self):
        print("sound made by the animal")

class Dog(Animal):
    def __init__(self,name,breed):
        Animal.__init__(self,name,species="Dog")
        self.species = breed
    
    def make_sound(self):
        print("Bark")


d = Dog("dog","doggerman")
d.make_sound()

a = Animal("dog","dog")
a.make_sound()




#MULTIPLE INHERITANCE
class Employee:
    def __init__(self,name):
        self.name=name
class Dancer:
    def __init__(self,dance):
        self.dance=dance
    
class DancerEmployee(Employee,Dancer):
    def __init__(self,dance,name):
        self.dance=dance
        self.name=name


o = DancerEmployee("kathak",'shivani')
print(o.name)
print(o.dance)

print(DancerEmployee.mro())



#MULTILEVEL INHERITANCE

class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species
        
    def show_details(self):
        print(f"Name: {self.name}")
        print(f"Species: {self.species}")
        
class Dog(Animal):
    def __init__(self, name, breed):
        Animal.__init__(self, name, species="Dog")
        self.breed = breed
        
    def show_details(self):
        Animal.show_details(self)
        print(f"Breed: {self.breed}")
        
class GoldenRetriever(Dog):
    def __init__(self, name, color):
        Dog.__init__(self, name, breed="Golden Retriever")
        self.color = color
        
    def show_details(self):
        Dog.show_details(self)
        print(f"Color: {self.color}")

o = GoldenRetriever("tommy", "Black")
o.show_details()
print(GoldenRetriever.mro())