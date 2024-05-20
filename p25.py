# WAP of method overriding

class Animal:
    def make_sound(self):
        print("Some generic animal makes sound")

class Dog(Animal):
    def make_sound(self):
        print("Bark")

class Cat(Animal):
    def make_sound(self):
        print("Meow")

# Create instances of Animal, Dog, and Cat
generic_animal = Animal()
dog = Dog()
cat = Cat()

# Call the make_sound method on each instance
generic_animal.make_sound()  # Output: Some generic animal sound
dog.make_sound()             # Output: Bark
cat.make_sound()             # Output: Meow