import heapq

def factory(stock, dates, supplies, k):
    import_count = 0
    stock_heap = []
    index = 0

    while (stock < k):
        for i in range(index, len(dates)):
            if dates[i] <= stock:
                heapq.heappush(stock_heap, (-supplies[i], supplies[i]))
                index = i + 1
            else:
                break
        max_amount = heapq.heappop(stock_heap)[1]
        stock += max_amount
        import_count += 1
    return import_count

def main():
    initial_amount = int(input())
    import_data = list(map(int, input().split()))
    import_amount = list(map(int, input().split()))
    regular_import_data = int(input())

    print(factory(initial_amount, import_data, import_amount, regular_import_data))

if __name__ == "__main__":
    main()