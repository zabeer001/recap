def sliding_window_sum(arr, window_size=3):
    # Check if the array is long enough for the window
    if len(arr) < window_size:
        return "Array is too short for the window size"
    
    # Initialize the sum of the first window
    current_sum = sum(arr[:window_size])  # Sum of the first window
    sums = [current_sum]
    
    # Apply sliding window starting from the second window
    for start in range(1, len(arr) - window_size + 1):
        # Subtract the element going out and add the new element coming in
        current_sum = current_sum - arr[start - 1] + arr[start + window_size - 1]
        sums.append(current_sum)
    
    return sums  # Return the list of sums

# Example array
arr = [68, 67, 7, 81, 76, 33, 19, 10, 2, 37]

# Calculating sliding window sums using optimized sliding window
result = sliding_window_sum(arr)
print("Sliding Window Result:", result)
