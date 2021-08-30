def find_coin(coin_list, k):
    coins_list = []
    result = 0
    for coin in coin_list:
        if coin == k:
            return 1
        else:
            if coin < k:
                coins_list.append(coin)
    coins_list.sort(reverse = True)
    for coins in coins_list:
        mok = int(k // coins)
        k -= mok*coins
        result += mok
    return result

def main():
    n, k = map(int, input().split())
    coin_list = []
    for _ in range(n):
        coin_list.append(int(input()))
    print(find_coin(coin_list, k))

if __name__ == "__main__":
    main()