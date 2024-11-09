import math
text = input()
arr = text.split()
stones_x = int(arr[0]) / int(arr[2])
stones_y = int(arr[1]) / int(arr[2])
stones = math.ceil(stones_x) * math.ceil(stones_y)
print(stones)