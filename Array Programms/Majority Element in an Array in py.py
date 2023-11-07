# Majority Element in an Array in py :

def majority(arr):
    max_count = 0
    index = -1  # sentinels

    for i in range(len(arr)):
        count = 0
        for j in range(len(arr)):
            if arr[i] == arr[j]:
                count += 1

        # update max_count if the count of the current element is greater
        if count > max_count:
            max_count = count
            index = i

    # if max_count is greater than n/2, return the corresponding element
    if max_count > len(arr) / 2:
        print("Majority Element =", arr[index])
    else:
        print("No Majority Element")


    
arr = list(map(int,input("Entera array items : ").split() ))
majority(arr)
