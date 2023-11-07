# Binary search in py :

def binary_search(arr, target):
    left, right = 0, len(arr) - 1

    while left <= right:
        mid = (left + right) // 2 # this was a formula for binary search.
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1

# Get user input for the sorted array
arr = input("Enter a sorted array (space-separated numbers): ").split()
arr = [int(num) for num in arr]

# Get user input for the target value
target = int(input("Enter the value to find: "))

# Perform binary search
result = binary_search(arr, target)

if result != -1:
    print(f"The value {target} was found at index {result}.")
else:
    print(f"The value {target} was not found in the array.")
