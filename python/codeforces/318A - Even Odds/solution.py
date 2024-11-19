def get_volodya_num(s):
    li = list(map(int,s.split(' ')))
    n = li[0]
    k = li[1]
    odd_li = []
    even_li = []
    for i in range(n+1):
        if i % 2 != 0:
            odd_li.append(i)
        else:
            even_li.append(i)
    even_li = even_li[1:]
    li = odd_li + even_li
    return li[k-1]
s = input()
print(get_volodya_num(s))



