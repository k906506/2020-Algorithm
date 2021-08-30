def stair(n,m):
    if n == 1 or n == 0:
        return 1
    else:
        stair = [0 for _ in range(n+1)]
        stair[0] = 1
        stair[1] = 1
        k = 1
        for i in range(2, n+1):
            stair[i] += stair[i-1] + k
            k += 1
        if n > m:
            dis = n - m
            for i in range(1, dis+1):
                stair[n] -= i
        return stair[n]

n, m = map(int, input().split())
print(stair(n, m))