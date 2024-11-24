s1 = input()
s2 = input()
res = ''
if len(s1)==len(s2):
    for i in range(len(s1)):
        if s1[i] == s2[i]:
            res += '0'
        else:
            res += '1'
print(res)
# 1 0 1 0 1 0 0
# 0 1 0 0 1 0 1
# 1 1 1 0 0 0 1