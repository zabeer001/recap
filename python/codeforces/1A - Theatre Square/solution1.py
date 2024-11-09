import math
text = input()
arr = text.split()
area = int(arr[0]) * int(arr[1])
stones = area / int(arr[2])
print(math.ceil(stones))