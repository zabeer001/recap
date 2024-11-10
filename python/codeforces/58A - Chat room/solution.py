def vasya_says_hello(s):
    word = 'hello'
    pointer = 0
    for char in s:
        if pointer < len(word)  and char == word[pointer]:
            pointer += 1
    if pointer == len(word):
        return("YES")  
    else:
        return("NO")

# ahhellllloou
# hlelo
s = input()
print(vasya_says_hello(s))