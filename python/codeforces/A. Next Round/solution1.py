nums_n_k = input()  # Read input for n and k
scores = input()  # Read input for scores
count = 0

# Split the inputs
nums_n_k = nums_n_k.split()
scores = scores.split()

# Extract k and the k-th place score
k = int(nums_n_k[1]) - 1
target_score = int(scores[k])

# Loop through the scores and count participants meeting the condition
for score in scores:
    if int(score) >= target_score and int(score) > 0:  # Ensure the score is positive
        count += 1

# Output the result
print(count)
