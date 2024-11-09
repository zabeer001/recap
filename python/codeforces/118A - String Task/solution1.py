vowels = ['a','e','i','o','u','y']
res = ''
s = input()
s = s.lower()
for i in s:
 if i in vowels:
  s = s.replace(i, '')
s = list(s)
for i in s:
 res = res + "." + i
print(res)
