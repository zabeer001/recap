def get_orangeJuiceFraction(n,li):
    sum = 0
    for item in li:
        sum += item
    avg = sum / n
    return avg


n = int(input())
s = input()
li = list(map(int,s.split(' ')))
print(get_orangeJuiceFraction(n,li))

