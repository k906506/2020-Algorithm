input_list = list(map(int, input().split()))
target_list = list(map(int, input().split()))
result = []

dic = dict()
for i, j in enumerate(input_list):
    dic[i] = j

for i in target_list:
    if i in dic.values():
        result.append(1)
    else:
        result.append(0)

print(*result)
