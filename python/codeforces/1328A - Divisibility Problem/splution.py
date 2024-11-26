res = int(input())  # Number of test cases

for _ in range(res):
    s = input()  # Input a and b as a space-separated string
    li = list(map(int, s.split(' ')))  # Convert input to a list of integers
    r = li[0] % li[1]  # Calculate the remainder
    moves = 0 if r == 0 else li[1] - r  # If remainder is 0, no moves needed; else calculate moves
    print(moves)  # Output the result
