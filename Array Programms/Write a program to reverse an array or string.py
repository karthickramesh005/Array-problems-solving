# Write a program to reverse an array or string :

def reverseList(A, start, end): 
    while start < end: 
        A[start], A[end] = A[end], A[start] 
        start += 1
        end -= 1
  
# Driver function to test above function 
A =list(map(int,input("Enter array items :").split()))
print(A) 
reverseList(A, 0, 5) 
print("Reversed list is") 
print(A) 
