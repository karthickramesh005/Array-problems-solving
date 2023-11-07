# K’th Smallest/Largest Element in Unsorted Array :

def kthSmallest(arr, n, k):
    arr.sort()
    return arr[k-1]


arr = list(map(int,input("Enter a array items :  ").split()))
n = len(arr)
k = int(input("Enter a number : "))
print("k'th smallest element is",kthSmallest(arr, n, k))
