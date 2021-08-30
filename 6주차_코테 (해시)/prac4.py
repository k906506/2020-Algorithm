input_list = list(map(int, input().split()))
plus_list = list(map(int, input().split()))

sum_list = [0 for i in range(len(plus_list))]
for i in range(len(input_list)):
    sum_list[i] = int(input_list[i]//plus_list[i])
multiply = min(sum_list)
for i in range(len(plus_list)):
    plus_list[i] *= multiply
print(*plus_list)