number_of_people = int(input())
opinions = input()
opinions = opinions.split(' ')

problem_type = "EASY"

for opinion in opinions:
    if opinion == "1":
        problem_type = "HARD"
print(problem_type)