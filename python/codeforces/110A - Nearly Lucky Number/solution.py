lucky_digits = ['4', '7']
s = input()  # Input the number as a string

lucky_nums = []
possibility = False

# Count how many lucky digits are present in the input string
for item in s:
    if item in lucky_digits:
        lucky_nums.append(item)

# If there are lucky digits, check the count of lucky digits
if lucky_nums:
    # If the count of lucky digits is either 4 or 7, it's a nearly lucky number
    if len(lucky_nums) == 4 or len(lucky_nums) == 7:
        possibility = True
    else:
        # If there are other digits present (not lucky digits), it's not a nearly lucky number
        for item in s:
            if item not in lucky_digits:
                possibility = False
                break
        # If the string contains only lucky digits, then it's a lucky number by definition
        if all(item in lucky_digits for item in s):
            possibility = True

# Special case: if the number is just "4" or "7", we consider it "YES"
if possibility:
    print('YES')
else:
    print('NO')
