from itertools import permutations

num = int(input())

def max_min(int_list):
    pair = permutations(int_list,2)
    result = 0
    for a, b in pair:
        result = max(result, a-b, b-a)
    return result

for i in range(num):
    int_list = list(map(int, input().split()))
    print(max_min(int_list))