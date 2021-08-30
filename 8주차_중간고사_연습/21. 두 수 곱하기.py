k = int(input())
num = list(map(int, input().split()))
dic = dict()
for i, t in enumerate(nums):
    dic[t] = i
result = []
for i, t in enumerate(nums):
    d = k / t
    if d in dic.key():
        result.append