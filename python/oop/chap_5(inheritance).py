class Employee:
    def __init__(self,name,id):
        self.name = name
        self.id = id
    
    def showDetailes(self):
        print(f"The name of exmployee: {self.id} is {self.name}")

class Programmer(Employee):
    def showLanguage(self):
        print("the langage is python")

e = Employee('harsh',420)
e.showDetailes()

e1 = Programmer('harsh',420)
e1.showDetailes()
e1.showLanguage()