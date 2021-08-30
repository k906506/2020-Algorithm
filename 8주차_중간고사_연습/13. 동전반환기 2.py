def find_least(coin_list, price):
    coins = []
    result_coin = []
    result_many = []
    for coin in coin_list:
        if coin == price:
            print("%d 1" %coin)
            break
        else:
            if coin < price:
                coins.append(coin)
    if len(coins) >= 1:
        for coin in coins:
            if coin < price:
                mok = int(price//coin)
                price -= mok*coin
                result_coin.append(coin)
                result_many.append(mok)
        for i in range(len(result_coin)-1, -1, -1):
            print("%d %d" %(result_coin[i], result_many[i]))

def main():
    n = int(input())
    coin_list = list(map(int, input().split()))
    coin_list.sort(reverse=True)
    price = int(input())
    find_least(coin_list, price)

if __name__ == "__main__":
    main()