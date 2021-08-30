num = int(input())
coin_list = list(map(int, input().split()))
result = int(input())

count = 0
coins_list = []
coins_count = []
coin_list.sort()

for i in range(num-1, -1, -1):
    coin = coin_list[i]
    if result >= coin:
        coins_list.append(coin) #액면가 저장
        mid = result//coin
        coins_count.append(mid) #개수 저장
        result -= coin*mid

for i in range(len(coins_list)-1, -1, -1):
    print("%d %d" %(coins_list[i], coins_count[i]))