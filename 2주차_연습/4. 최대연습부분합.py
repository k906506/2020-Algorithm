num = int(input())

def find_maxsum(int_list):
    current_max = 0
    for i in range(len(int_list)):
        for j in range(i, len(int_list)):
            temp_sum = 0
            temp_sum = sum(int_list[i:j+1])
            current_max = max(current_max, temp_sum)
    return current_max

for i in range(num):
    int_list = list(map(int, input().split()))
    print(find_maxsum(int_list))