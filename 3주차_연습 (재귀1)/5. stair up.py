def stair(n):
    if n <= 1:
        print(1)
    else:
        stair = [0 for _ in range(n+1)]
        stair[0] = 1
        stair[1] = 1
        for i in range(2, n+1):
            stair[i] = stair[i-1] + stair[i-2]
        print(stair[n])

num = int(input())
stair(num)