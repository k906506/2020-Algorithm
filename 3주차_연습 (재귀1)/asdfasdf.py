rsp_list = list(map(int, input().split()))
num = int(input())


rsp_list.sort()
rsp_list.reverse()
result = 0
for i in range(len(rsp_list)):
    rsp = rsp_list[i]
    if rsp <= num:
        result += num//rsp
        num -= (num//rsp)*rsp

if num != 0:
    result = -1
print(result)
22 22 22 66/ 5 71/ 3 3 3 80