s = input()
li = s.split(' ')
number = int(li[0])
number_str = li[0]
operation = int(li[1])

for i in range(operation):
    if number_str[-1] != '0':
        number = number - 1
        number_str = str(number)
    else:
        number = number // 10  # "51.0" avoid this
        number_str = str(number)

print(int(number))
