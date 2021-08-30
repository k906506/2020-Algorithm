def factory(stock, dates, supplies, k):
    need = k - 1
    index = 0
    for _ in range(index, len(dates)):
        stock += supplies[index]
        index += 1
        if stock >= need:
            break
    return index

def main():
    stock = int(input())
    supply_date = list(map(int, input().split()))
    supply_many = list(map(int, input().split()))
    deadline = int(input())
    print(factory(stock, supply_date, supply_many, deadline))

if __name__ == "__main__":
    main()