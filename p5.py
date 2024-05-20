#WAP to Create a list, perform insert, delete and reverse operation in a list 

class ListOperations:
    def __init__(self):
        self.my_list = []
        print("New empty list created!")
    
    def print_list(self):
        print("Current list is:", self.my_list)

    def insert_element(self, index, element):
        self.my_list.insert(index, element)
        print(f"Inserted {element} at index {index}")

    def delete_element(self, element):
        if element in self.my_list:
            self.my_list.remove(element)
            print(f"Deleted element {element}.")
        else:
            print(f"Element {element} not found in the list!")

    def reverse_list(self):
        self.my_list.reverse()
        print("list reversed!")

list_obj = ListOperations()

#inserting elements:
list_obj.insert_element(0, 10)
list_obj.insert_element(1, 20)
list_obj.insert_element(2, 30)
list_obj.insert_element(3, 40)
list_obj.insert_element(4, 50)

list_obj.print_list()

list_obj.delete_element(20)
list_obj.print_list()

list_obj.delete_element(5)

list_obj.reverse_list()
list_obj.print_list()