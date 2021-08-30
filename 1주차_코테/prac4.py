n, k, i = input().split()
num = []

n = int(n)
k = int(k)
i = int(i)

num = list(map(int, input().split()))
num.sort()

smallNum = num[k-1]
bigNum = num[n-i]
result = abs(bigNum-smallNum)
print(result)