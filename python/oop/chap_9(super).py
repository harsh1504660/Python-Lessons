class ParentClass:
    def parent_method(self):
        print("this isthe parent method")
    
class ChildClass(ParentClass):
    def Parent_method(self):
        print("hrllo")
    def child_method(self):
        print("This is the child method ")

        super().parent_method()    ### call the method from parent class

child_obj = ChildClass()
child_obj.child_method()