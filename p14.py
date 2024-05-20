# WAP using dictionary with keys having multiple inputs

# Define the equation  
def equation(x, y, z):  
    return x + y * z  
  
# Create an empty dictionary to store the values  
values_dict = {}  
  
# Calculate the value of the equation for different input triplets  
values_dict[(1, 2, 3)] = equation(1, 2, 3)  
values_dict[(4, 5, 6)] = equation(4, 5, 6)  
values_dict[(7, 8, 9)] = equation(7, 8, 9)  
  
# Print the dictionary  
print(values_dict)  