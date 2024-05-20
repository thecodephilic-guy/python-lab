# WAP to create a class and method and display the build-in attributes of the class

class MyClass:
    def __init__(self, attr1, attr2):
        self.attr1 = attr1
        self.attr2 = attr2

    def display_attributes(self):
        print(f'attr1: {self.attr1}, attr2: {self.attr2}')

# Create an instance of MyClass
instance = MyClass(attr1="value1", attr2="value2")

# Display the instance's attributes using the method
instance.display_attributes()

# Display the built-in attributes of the class
print("Built-in attributes of MyClass:")
print("Class Name:", MyClass.__name__)
print("Module Name:", MyClass.__module__)
print("Documentation String:", MyClass.__doc__)
print("Class Dictionary:", MyClass.__dict__)
print("Base Classes:", MyClass.__bases__)