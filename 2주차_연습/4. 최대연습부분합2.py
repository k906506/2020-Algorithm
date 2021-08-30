num = int(input())

def find_maxsum(int_list):
    current_max = int_list[0]
    temp_max = int_list[0]

    for i in range(1, len(int_list)):
        current_max = max(int_list[i], int_list[i]+current_max)
        temp_max = max(current_max, temp_max)
        print(current_max, temp_max)
    return temp_max

for i in range(num):
    int_list = list(map(int, input().split()))
    print(find_maxsum(int_list))
