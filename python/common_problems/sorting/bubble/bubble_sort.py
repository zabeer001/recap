def sort_arr(arr):
    for j in arr:
        for i, item in enumerate(arr):
            # print(f"Index {index}: {value}")
            # print(arr[i])
            if(i < len(arr)-1):
                if(arr[i]>arr[i+1]):
                    temp = arr[i]
                    arr[i] = arr[i+1]
                    arr[i+1] = temp
    return arr
arr = [1, 2, 4, 12, 23, 32, 212]
print(sort_arr(arr))

