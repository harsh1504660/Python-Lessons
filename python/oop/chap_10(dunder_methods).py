class Employee:
    def __init__(self,name):
        self.name = name

    def __len__(self):
        i=0
        for c in self.name:
            i=i+1
        return i

    def __str__(self):
        return "the name of employee"
    def __repr__(self):
        return "the name of employee"

    def __call__(self):
        print("hey i am good")
e = Employee("hary")
#print(e.name)
#print(len(e))
print(e)
e()