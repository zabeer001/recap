lucky_digits = ['4', '7']
s = input()  # Input the number as a string

# If the string consists only of lucky digits, it's automatically a lucky number
if all(char in lucky_digits for char in s):
    print("YES")
else:
    # Count how many lucky digits (4 or 7) are present in the input string
    lucky_count = sum(1 for char in s if char in lucky_digits)

    # Check if the count of lucky digits is 4 or 7
    if lucky_count == 4 or lucky_count == 7:
        print("YES")
    else:
        print("NO")
