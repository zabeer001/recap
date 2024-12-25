import math

point1 = input()
point2 = input()

# Convert into list
point1 = point1.split(' ')
point2 = point2.split(' ')

# Point1 
x1, y1 = int(point1[0]), int(point1[1])
# Point2
x2, y2 = int(point2[0]), int(point2[1])

# Calculate squared distance
distanceSqr = (x1 - x2) * (x1 - x2) + (y1 - y2) * (y1 - y2)

# Calculate the actual distance
distance = math.pow(distanceSqr, .5)

# Convert the distance to 2 decimal places
distance = round(distance, 2)

print(distance)
