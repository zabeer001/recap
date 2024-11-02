def sort_arr(arr):
    n = len(arr)
    for j in range(n):
        for i in range(n - 1 - j):  # Reduce the range with each pass
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]  # Swap
    return arr

arr = [12, 1, 32, 4, 2, 212, 23]
print(sort_arr(arr))
