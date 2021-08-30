num = int(input())
int_list = list(map(int, input().split()))

for i in range(len(int_list)):
    for j in range(len(int_list)):
        if int_list[i] * int_list[j] == num:
            print(i, end = " ")
            print(j)