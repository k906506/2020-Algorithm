def coin_change(coin_list, price):
    coins_list = []
    for coin in coin_list:
        if coin == price:
            return coin
        else:
            if coin < price:
                coins_list.append(coin)
    
    coins_list.sort(reverse = True)
    mok = 0
    coin_kind = []
    coin_many = []
    for coin in coins_list:
        if coin < price:
            coin_kind.append(coin)
            mok = price//coin
            coin_many.append(mok)
            price -= mok*coin
    for i in range(len(coin_kind)-1, -1, -1):
        print(str(coin_kind[i]) + " " + str(coin_many[i]))

def main():
    coin_list = list(map(int, input().split()))
    price = int(input())
    coin_change(coin_list, price)

if __name__ == "__main__":
    main()