# Linear search in py : 

def linear_search(arr, target):
    for i, element in enumerate(arr):
        if element == target:
            return i
    return -1

# Get user input for the array
arr = input("Enter the array (space-separated numbers): ").split()
arr = [int(num) for num in arr]

# Get user input for the target value
target = int(input("Enter the value to find: "))

# Perform linear search
result = linear_search(arr, target)

if result != -1:
    print(f"The value {target} was found at index {result}.")
else:
    print(f"The value {target} was not found in the array.")
