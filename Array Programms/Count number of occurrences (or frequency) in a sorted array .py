# Count number of occurrences (or frequency) in a sorted array :

def counts(arr,l,x):
    res = 0
    for i in range(l):
        if x == arr[i]:
            res += 1
    return res


arr = list(map(int,input("Enter a array items : ").split()))
l = len(arr)
x = int(input("Enter a want accurence of number  : "))
print("The accurence of counts :  ",counts(arr,l,x))
