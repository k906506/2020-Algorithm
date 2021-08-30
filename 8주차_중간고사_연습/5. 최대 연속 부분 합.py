def find_max(input_list, num):
    new_list = input_list
    sum_list = []
    for i in range(num):    # 세로로 더하고
        sum_list = input_list[0][i]
        for j in range(1, num):
            sum_list += input_list[j][i]
            new_list[j][i] = sum_list
    for i in range(num):    # 가로로 더하고
        sum_list = input_list[i][0]
        for j in range(1, num):
            sum_list += input_list[i][j]
            new_list[i][j] = sum_list

    current_max = 0
    for x in range(num):
        for y in range(num):
            for i in range(x, num):
                for j in range(y, num):
                    if x != 0 and y != 0:
                        result = new_list[i][j] - new_list[x-1][j] - new_list[i][y-1] + new_list[x-1][y-1]
                    elif x != 0 and y == 0:
                        result = new_list[i][j] - new_list[x-1][j]
                    elif x == 0 and y != 0:
                        result = new_list[i][j] - new_list[i][y-1]
                    else:
                        result = new_list[i][j]
                    current_max = max(current_max, result)
    return current_max

def main():
    num = int(input())
    input_list = []
    for _ in range(num):
        input_list.append(list(map(int, input().split())))
    print(find_max(input_list, num))

if __name__ == "__main__":
    main()
    
