# Find the Missing Number   in array:
def find_missing_number(nums):
    n = len(nums)
    missing = n  # Initialize missing to n because it's the largest possible missing number
    
    for i in range(n):
        missing ^= i ^ nums[i]  # XOR all the array elements and their indices
        
    return missing

# Example usage:
nums =list(map(int,input("Enter a array items : ").split()))
result = find_missing_number(nums)
print("The missing number is:", result)

