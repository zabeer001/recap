word = input()
upperCases = []
lowerCases = []
for char in word:
    if char.isupper():
        upperCases.append(char)
    else:
        lowerCases.append(char)
if len(upperCases) > len(lowerCases):
    word = word.upper()
else:
    word = word.lower()

print(word)