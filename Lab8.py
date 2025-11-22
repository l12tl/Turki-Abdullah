import math

def brute_force_closest_pair(points): 

     n = len(points)

     closest_distance = float('inf')

     closest_pair = None

for i in range(n-1):

    for j in range(i+1, n):

            xi, yi = points[i]

            xj, yj = points[j]

            distance = math.sqrt((xi-xj)**2 + (yi-yj)**2)

            if distance < closest_distance:

             closest_distance = distance

             closest_pair = (i+1, j+1)



return closest_pair, closest_distance

p = [(3, 2), (3, 6), (7, 12), (3, 1), (9, 18), (8, 56)]

closest_pair, closest_distance = brute_force_closest_pair(p)

print("Closest pair is", closest_pair," with distance", closest_distance)
