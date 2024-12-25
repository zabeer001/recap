def brute_force_window_sum(arr, window_size=3):
    sums = []
    # Loop through all windows
    for start in range(len(arr) - window_size + 1):
        current_sum = 0
        # Recalculate sum for each window
        for i in range(window_size):
            current_sum += arr[start + i]
        sums.append(current_sum)
    return sums

# Example array
arr = [68, 67, 7, 81, 76, 33, 19, 10, 2, 37]

# Calculating sliding window sums using brute force
result = brute_force_window_sum(arr)
print("Brute Force Result:", result)
