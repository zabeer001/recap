from itertools import groupby

def get_group_characters(s):
    return [''.join(group) for _, group in groupby(s)]

def cal_lone_zero(s):
    li = get_group_characters(s)
    count = 0
    for i in li:
        if i == '0':
            count += 1
    return count

        
s = input()
print(cal_lone_zero(s))

