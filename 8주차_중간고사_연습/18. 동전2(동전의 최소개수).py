def find_coin(coin_list, k):
    dp = [10001]*10001
    dp[0] = 0
    for i in range(len(coin_list)):
        for j in range(coin_list[i], k+1):
            dp[j] = min(dp[j], dp[j-coin_list[i]] + 1)
    if dp[k] == 10001:
        return -1
    else:
        return dp[k]

def main():
    n, k = map(int, input().split())
    coin_list = []
    for _ in range(n):
        coin_list.append(int(input()))
    print(find_coin(coin_list, k))

if __name__ == "__main__":
    main()