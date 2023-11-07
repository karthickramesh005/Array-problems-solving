# get the array input from user in python :

from array import array

# Specify the data type for the array (in this case, 'i' for integers)
data_type = 'i'

# Get user input as a space-separated string of values
user_input = input("Enter values separated by spaces: ")

# Split the input string into individual values and convert to the specified data type
values = [int(x) for x in user_input.split()]

# Create an array from the list of values
user_array = array(data_type, values)

# Print the array
print("User's array:", user_array)
