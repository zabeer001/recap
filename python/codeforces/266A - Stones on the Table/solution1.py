number_of_stones = int(input())
table1 = input()
table2 = ''

for i in range(number_of_stones - 1):
    if(table1[i] == table1[i+1]):
        table2 = table2 + table1[i]
print(len(table2))