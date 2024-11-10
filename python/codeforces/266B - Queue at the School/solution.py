s = input()
line = input()

li = s.split(' ')
time = int(li[1])

line = list(line)  # Convert the string to a list for swapping

for _ in range(time):
    index = 0
    while index < len(line) - 1:
        if line[index] == "B" and line[index + 1] == "G":
            # Swap positions
            line[index], line[index + 1] = line[index + 1], line[index]
            index += 1  # Skip the next index to prevent double swapping in the same step
        index += 1

print(''.join(line))  # Convert list back to string for output
