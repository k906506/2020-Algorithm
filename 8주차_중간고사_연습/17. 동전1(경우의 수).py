def find_coin(input_list, k):
    dp = [0]*10001
    dp[0] = 1
    for coin in input_list:
        for i in range(coin, k+1):
            dp[i] = dp[i] + dp[i-coin]
    return dp[k]

def main():
    n, k = map(int, input().split())
    coin_list = []
    for _ in range(n):
        coin_list.append(int(input()))
    print(find_coin(coin_list, k))

if __name__ == "__main__":
    main()