import collections

num = int(input())
input_list = []
while True:
    try:
        input_list.append(input().split())
    except EOFError:
        break
result = collections.Counter(input_list[0])
for i in range(1, len(input_list)):
    result += collections.Counter(input_list[i])
result = result.most_common(len(result))
result = sorted(result, key = lambda x : (-x[1], x[0]))
for i in range(num):
    print(result[i][0])