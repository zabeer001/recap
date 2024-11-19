def find_triplet(n,target,li):
    result = ''
    res_li = []
    for i in range (n):
        for j in range(i + 1, n):
            x = li[i] + li[j]
            y = target - x
            if y in li:
                res_li.append(li[i])
                res_li.append(li[j])
                res_li.append(y)
                res_li.sort()
                for k in res_li:
                    result += str(k) + ' '
                return result
    return None

n = int(input())
s = input()
target = int(input())

li = list(map(int, s.split(' ')))
print(find_triplet(n,target,li))

            


