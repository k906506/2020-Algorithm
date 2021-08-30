# from itertools import combinations
import itertools

def tsp():
    input_list = list(map(int, input().split()))
    start = (input_list[0], input_list[1])
    finish = (input_list[2], input_list[3])
    points = []
    points_sliced = input_list[4:]
    for i in range(0, len(points_sliced), 2):
        points.append((points_sliced[i], points_sliced[i+1]))
    min_distance = float('inf')
    for i in itertools.permutations(points):
        path = [start, *list(i), finish]
        distance = 0

        for j in range(0, len(path)-1):
            distance += abs(path[j][0] - path[j+1][0]) + abs(path[j][1] - path[j+1][1])
        min_distance = distance if distance < min_distance else min_distance

    return min_distance
tsp()