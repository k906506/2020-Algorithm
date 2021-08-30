
target = int(input())
input_list = list(map(int, input().split()))
result = []

dic = dict()
for i, t in enumerate(input_list):
    dic[t] = i # t = 값, i = index

for i, t in enumerate(input_list):
    d = int(target//t)
    if d in dic.keys():
        element = (dic[t], dic[d])
        result.append(element)
        
for i in result:
    print(*i)
