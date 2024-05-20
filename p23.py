# WAP of constructor overloading

class MyClass:
    def __init__(self, attr1=None, attr2=None):
        if attr1 is not None and attr2 is not None:
            self.attr1 = attr1
            self.attr2 = attr2
        elif attr1 is not None:
            self.attr1 = attr1
            self.attr2 = "Default value"
        else:
            self.attr1 = "Default value 1"
            self.attr2 = "Default value 2"
    
    def display(self):
        print(f'attr1: {self.attr1}, attr2: {self.attr2}')

# Creating instances with different constructor parameters
obj1 = MyClass()
obj2 = MyClass("Value for attr1")
obj3 = MyClass("Value for attr1", "Value for attr2")

# Displaying attributes
obj1.display()  # Output: attr1: Default value 1, attr2: Default value 2
obj2.display()  # Output: attr1: Value for attr1, attr2: Default value
obj3.display()  # Output: attr1: Value for attr1, attr2: Value for attr2
