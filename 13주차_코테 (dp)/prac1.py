def main():
    num = int(input())
    dp = [0] * (num+1)
    if num == 0:
        print(0)
    elif num == 1:
        print(1)
    else:
        dp[0] = 0
        dp[1] = 1
        for i in range(2,num+1):
            dp[i] = dp[i-1] + dp[i-2]
        print(dp[num])

if __name__ == "__main__":
    main()