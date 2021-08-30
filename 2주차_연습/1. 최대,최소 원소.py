set1 = int(input())

for i in range(set1):
    int_list = list(map(int,input().split()))
    print(max(int_list),min(int_list))