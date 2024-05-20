# WAP to create an istance of a specified class and display the namespace (attributes) off that instance

class MyClass:
    def __init__(self, attr1, attr2):
        self.attr1 = attr1
        self.attr2 = attr2

# Create an instance of MyClass
instance = MyClass(attr1="value1", attr2="value2")

# Print the namespace (attributes) of the instance
print("Namespace of the instance:", instance.__dict__)
