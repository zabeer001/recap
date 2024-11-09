n = int(input())
count = 0

for i in range(n):
    s = input()
    split_list = s.split()
    split_list = [int(x) for x in split_list] 
    countFor1 = sum(1 for num in split_list if num == 1)
    if countFor1 > 1:
        count = count + 1
print(count)


    

