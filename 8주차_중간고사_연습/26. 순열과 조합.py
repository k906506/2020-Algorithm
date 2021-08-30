from itertools import permutations, combinations
input_list = list(map(str, input().split()))
print(list(map("".join, permutations(input_list))))
print(list(map("".join, combinations(input_list,4))))