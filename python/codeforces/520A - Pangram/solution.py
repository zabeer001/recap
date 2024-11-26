char_no = int(input())
s = input()
s = s.lower()
li = list(s)
li = list(set(li))
if len(li) == 26:
    print("YES")
else:
    print("NO")
