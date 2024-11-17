
def can_live(li):
    living_member =  int(li[0])
    rooms_capacity = int(li[1])
    if living_member + 2 <= rooms_capacity :
        return True

def get_room(number_of_rooms):
    available_room = 0
    for _ in range(number_of_rooms):
        s = input()
        li = s.split(' ')
        if can_live(li):
            available_room += 1
    return available_room
        

number_of_rooms = int(input())
print(get_room(number_of_rooms))


