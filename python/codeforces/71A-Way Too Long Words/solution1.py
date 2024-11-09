def generateTextOutput(text):
    if len(text) < 10:
        return text
    else:
        text = text[0] + str(len(text) - 2) + text[-1]
        return text

n = int(input())
results = []

for _ in range(n):
    text = input()
    results.append(generateTextOutput(text))

# Print all results at once
print("\n".join(results))
