# WAP of multiple, multilevel, hierarchical inheritance

# Multiple Inheritance
class Parent1:
    def method_parent1(self):
        print("Method from Parent1")

class Parent2:
    def method_parent2(self):
        print("Method from Parent2")

class MultipleInheritanceChild(Parent1, Parent2):
    def method_child(self):
        print("Method from MultipleInheritanceChild")

# Multilevel Inheritance
class Grandparent:
    def method_grandparent(self):
        print("Method from Grandparent")

class Parent(Grandparent):
    def method_parent(self):
        print("Method from Parent")

class MultilevelInheritanceChild(Parent):
    def method_child(self):
        print("Method from MultilevelInheritanceChild")

# Hierarchical Inheritance
class BaseParent:
    def method_base_parent(self):
        print("Method from BaseParent")

class HierarchicalChild1(BaseParent):
    def method_child1(self):
        print("Method from HierarchicalChild1")

class HierarchicalChild2(BaseParent):
    def method_child2(self):
        print("Method from HierarchicalChild2")

# Create instances and call methods to demonstrate inheritance

# Multiple Inheritance
multiple_child = MultipleInheritanceChild()
print("Multiple Inheritance:")
multiple_child.method_parent1()  # Output: Method from Parent1
multiple_child.method_parent2()  # Output: Method from Parent2
multiple_child.method_child()    # Output: Method from MultipleInheritanceChild

print()

# Multilevel Inheritance
multilevel_child = MultilevelInheritanceChild()
print("Multilevel Inheritance:")
multilevel_child.method_grandparent()  # Output: Method from Grandparent
multilevel_child.method_parent()       # Output: Method from Parent
multilevel_child.method_child()        # Output: Method from MultilevelInheritanceChild

print()

# Hierarchical Inheritance
hierarchical_child1 = HierarchicalChild1()
hierarchical_child2 = HierarchicalChild2()
print("Hierarchical Inheritance:")
hierarchical_child1.method_base_parent()  # Output: Method from BaseParent
hierarchical_child1.method_child1()       # Output: Method from HierarchicalChild1

hierarchical_child2.method_base_parent()  # Output: Method from BaseParent
hierarchical_child2.method_child2()       # Output: Method from HierarchicalChild2

