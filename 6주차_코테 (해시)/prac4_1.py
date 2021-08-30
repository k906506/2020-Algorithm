input_list = list(map(int, input().split()))
plus_list = list(map(int, input().split()))

sum_list = [0, 0, 0]
check = True
while (check == True):
    for i in range(len(input_list)):
        if sum_list[i] <= input_list[i]:
            check = True
        else:
            check = False
            break  
    if check == True:
        for i in range(len(sum_list)):
            sum_list[i] = sum_list[i] + plus_list[i]

result = [0, 0, 0]
for i in range(len(sum_list)):
    result[i] = sum_list[i] - plus_list[i]
print(*result)