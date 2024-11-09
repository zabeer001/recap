lucky_digits = ['4', '7']
s = input()
 
# Count lucky digits in the input string
lucky_count = sum(1 for char in s if char in lucky_digits)
 
# Check if the count of lucky digits is 4 or 7, and if the count itself is a lucky number
if lucky_count == 4 or lucky_count == 7:
    print("YES")
else:
    print("NO")