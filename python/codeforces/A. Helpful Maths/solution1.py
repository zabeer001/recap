s = input()
nums = s.split('+')
nums.sort()
s = ''
for num in nums:
    s = s + '+' + num
s = s[1:]
print(s)