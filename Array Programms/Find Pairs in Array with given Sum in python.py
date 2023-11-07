# Find Pairs in Array with given Sum in python :

def pair(arr,target):
    l = len(arr)
    f = 0
    for i in range(l):
        for j in range(i+ 1,l):
            if arr[i] + arr[j] == target :
                print(f"Pair found ({arr[i]}, {arr[j]})")
                f = 1
        if f == 0:
            print("Pairs not found")


if __name__ == "__main__":
    
    arr = list(map(int,input("Giove array items in separate space : ").split()))
    target = int(input("Enter a you want pair in the array : "))
    pair(arr,target)
