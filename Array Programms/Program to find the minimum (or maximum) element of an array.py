# Program to find the minimum (or maximum) element of an array : 
import sys
 
# Define an array
a = list(map(int,input("Enter a array items : ").split()))
 
# Sort the array using the built-in sorted() function
a_sorted = sorted(a)
 
# Find the minimum and maximum values
min_value = a_sorted[0]
max_value = a_sorted[-1]
 
# Print the results
print(f"min-{min_value} max-{max_value}")
