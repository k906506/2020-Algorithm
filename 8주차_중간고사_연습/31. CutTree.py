import heapq

def cut_tree(input_list, max_length):
    heap_list = []
    count = 0

    for i in input_list:
        if i > max_length:
            heapq.heappush(heap_list, (-i, i))
    max_wood = heapq.heappop(heap_list)[1]
    while max_wood > max_length:
        count += 1
        wood1 = int(max_wood*2/3)
        wood2 = int(max_wood*1/3)
        heapq.heappush(heap_list, (-wood1, wood1))
        heapq.heappush(heap_list, (-wood2, wood2))
        max_wood = heapq.heappop(heap_list)[1]
    return count

def main():
    max_length = int(input())
    input_list = list(map(int, input().split()))
    print(cut_tree(input_list, max_length))

if __name__ == "__main__":
    main()