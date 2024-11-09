ages = input()
li = ages.split(' ')
limak_age = int(li[0])
bob_age = int(li[1])
year = 0 

while limak_age <= bob_age:
    year += 1
    limak_age *= 3
    bob_age *= 2

print(year)



