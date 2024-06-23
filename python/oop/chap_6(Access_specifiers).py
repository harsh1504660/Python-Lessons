class Employee:
    def __init__(self):
        self.__name = "harry"  ### private variabe


a = Employee()
#print(a.__name)  ## error

print(a._Employee__name)