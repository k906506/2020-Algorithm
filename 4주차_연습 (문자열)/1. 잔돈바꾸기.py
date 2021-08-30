def change_money(coin_list, target):
    coin_count = []
    min_coins = target 

    if target in coin_list:
        return 1
    else:
        coins = []
        for coin in coin_list:
            if coin <= target:
                coins.append(coin)
        for coin in coins:
            num_coins = 1 + change_money(coin_list, target - coin)
            if num_coins < min_coins:
                min_coins = num_coins
        print(coin_count)
    return min_coins

num = int(input())
coin_list = list(map(int, input().split()))
coin_list.sort()
target = int(input())
print(change_money(coin_list, target))