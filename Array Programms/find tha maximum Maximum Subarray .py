# find tha maximum Maximum Subarray :

def max_subarray(nums):
    max_sum = nums[0]  # Initialize max_sum with the first element of the array
    current_sum = nums[0]  # Initialize current_sum with the first element

    for num in nums[1:]:
        current_sum = max(num, current_sum + num)
        max_sum = max(max_sum, current_sum)

    return max_sum

# Example usage:
nums = list(map(int,(input("Enter a array items : ").split())))
result = max_subarray(nums)
print("Maximum subarray sum:", result)

