import heapq

def find_max(input_list, m, n):
    heap_list = []
    for i in input_list:
        heapq.heappush(heap_list,i)
    index = m - n
    for i in range(index):
        result = heapq.heappop(heap_list)
    return result

def main():
    m, n = map(int, input().split())
    input_list = list(map(int, input().split()))
    print(find_max(input_list, m, n))

if __name__ == "__main__":
    main()