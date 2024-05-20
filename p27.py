#WAP of super function

class Parent:
    def __init__(self):
        self.parent_attribute = "Parent attribute"

    def parent_method(self):
        print("Method from Parent")

class Child(Parent):
    def __init__(self):
        super().__init__()  # Call the constructor of the parent class
        self.child_attribute = "Child attribute"

    def child_method(self):
        super().parent_method()  # Call the parent method
        print("Method from Child")

# Create an instance of Child
child = Child()

# Access attributes and call methods using super()
print(child.parent_attribute)  # Output: Parent attribute
print(child.child_attribute)   # Output: Child attribute
child.child_method()           # Output: Method from Parent
                               #         Method from Child