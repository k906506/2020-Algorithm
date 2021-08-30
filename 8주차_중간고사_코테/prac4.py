import heapq

num = int(input())
input_list = []
for i in range(num):
    input_list.append(input().split())

data_min = []
j = 0
for i in range(len(input_list)):
    if input_list[i][0] == "In":
        heapq.heappush(data_min, input_list[i][1])
    else:
        if int(input_list[i][1]) == -1:
            heapq.heappop(data_min)
        else:
            data_min.remove(max(data_min))
result = data_min
if len(result) >= 2:
    print(max(result), min(result))
elif len(result) == 1:
    print(result[0], result[0])
else:
    print(0, 0)