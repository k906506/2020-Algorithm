rsp_list = list(map(int,input().split()))
total = int(input())

dp = [[0 for col in range(total+1)] for row in range(len(rsp_list))]
for i in range(len(rsp_list)):
    dp[i][0] = 0
for i in range(total+1):
    dp[0][i] = i
for i in range(1, len(rsp_list)):
    for j in range(1,total+1):
        if rsp_list[i] > j:
            dp[i][j] = dp[i-1][j]
        else:
            dp[i][j] = min(dp[i-1][j], dp[i][j-rsp_list[i]])

i = len(rsp_list) - 1
j = total
count = 0
min = dp[i][j]
while j != 0:
    if dp[i-1][j] == min:
        i -= 1
    else:
        count += 1
        j -= rsp_list[i]
print(count)
