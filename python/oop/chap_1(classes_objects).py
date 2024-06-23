class Person:
    name = "harry"
    occupation = "software developer"
    networth =10
    def info(self):
        print(f"{self.name} is a {self.occupation}")

a = Person()
"""print(a.name)"""
a.name = "shubham"
a.occupation = "acc"
print(a.occupation)
a.info()