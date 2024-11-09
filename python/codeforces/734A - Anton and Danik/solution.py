no_of_games = int(input())
anton = ['A']
danik =['D']
result = input()
anton_winning_no = sum(1 for char in result if char in anton)
danik_winning_no = sum(1 for char in result if char in danik)

if anton_winning_no > danik_winning_no:
    print('Anton')
if anton_winning_no < danik_winning_no:
    print('Danik')
if anton_winning_no == danik_winning_no:
    print('Friendship')