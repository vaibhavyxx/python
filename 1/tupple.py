#tupple is similar to list but w a few differences
#it is immutaable
#start from index 0
import math

def calculateDistance(A, B):
    x1,y1 = A
    x2, y2 =B   #destructures a tupple
    dist = math.sqrt((x2-x1)**2 + (y2- y1)**2)
    return dist

coordinates = (4,5), (8,9)
print(coordinates[0])
print(f"Distance between {coordinates[0]} and {coordinates[1]} is {calculateDistance(coordinates[0], coordinates[1])} units")

#difference from a list- lists allow you flexibility to change values
