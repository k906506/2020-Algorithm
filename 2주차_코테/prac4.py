size = int(input())
int_list = []
new_list = []

for i in range(size):
    int_list.append(list(map(int, input().split())))

new_list = int_list

for i in range(size):   # 세로로 더하고
    sum_list = int_list[0][i]
    for j in range(1,size):
        sum_list += int_list[j][i]
        new_list[j][i] = sum_list

for i in range(size):   # 가로로 더하고
    sum_list = int_list[i][0]
    for j in range(1,size):
        sum_list += int_list[i][j]
        new_list[i][j] = sum_list
        
current_max = 0

for i in range(size):
    for j in range(size):
        for x in range(i,size):
            for y in range(j,size):
                if i != 0 and j != 0:
                    result = new_list[x][y] - new_list[x][j-1] - new_list[i-1][y] + new_list[i-1][j-1]
                elif i == 0 and j != 0:
                    result = new_list[x][y] - new_list[x][j-1]
                elif i != 0 and j == 0:
                    result = new_list[x][y] - new_list[i-1][y]
                else:
                    result = new_list[x][y]
                current_max = max(current_max, result)

print(current_max)
