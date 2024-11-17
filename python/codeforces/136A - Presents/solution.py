n = int(input())
# 2 3 4 1
s = input()
arr = list(map(int,s.split(" ")))
res = []
s_res = ''

for i in range(n):
    position = arr.index(i+1)
    res.append(position)
res = list(map(lambda x: x + 1, res))
for item in res:
    s_res = s_res + str(item) + ' '
print(s_res)



# my_dict = {'name': 'Alice', 'age': 25}
# my_dict['city'] = 'New York'
# print(my_dict)