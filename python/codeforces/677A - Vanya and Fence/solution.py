s = input()
friends = input()
friends = friends.split()
s = s.split()
width = 0 
number_of_friends = int(s[0])
max_height = int(s[1])
for friend in friends:
    friend = int(friend)
    if friend > max_height:
        width += 2
    else:
        width += 1
print(width)

