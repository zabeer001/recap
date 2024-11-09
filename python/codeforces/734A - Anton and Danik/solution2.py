# Input the number of games and results string
n = int(input())
result = input()

# Count the wins for Anton and Danik
anton_wins = result.count('A')
danik_wins = result.count('D')

# Print the result based on the counts
if anton_wins > danik_wins:
    print('Anton')
elif anton_wins < danik_wins:
    print('Danik')
else:
    print('Friendship')
