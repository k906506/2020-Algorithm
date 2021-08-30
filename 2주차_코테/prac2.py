num = int(input())
int_list = list(map(int,input().split()))

i = 1
j = 2
if num == 2 or num == 1:
    print(1)
else:
    for k in range(num-2):
        i += j
        j += 1
    print(i)
int_list.sort()
for i in range(num):
    print(int_list[i], end = " ")