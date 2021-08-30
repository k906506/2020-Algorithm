import heapq

def find_min(num, wood_list):
    heap_list = []
    max_size = num
    count = 0

    for i in range(len(wood_list)):     # num보다 큰 나무토막만 힙에 넣는다.
        if wood_list[i] > num:
            heapq.heappush(heap_list, wood_list[i])
        else:
            pass

    while len(heap_list) != 0:          # 힙의 0번째 값이 num보다 작거나 같으면 pop, 그렇지 않으면 2/3, 1/3으로 나누고 push 한다
        if heap_list[0] <= max_size:
            # result = heapq.heappop(heap_list)
            pass
        else:
            i = int(heap_list[0]*(2/3))
            j = int(heap_list[0]*(1/3))
            # result = heapq.heappop(heap_list)
            heapq.heappush(heap_list, i)
            heapq.heappush(heap_list, j)    
            count += 1
    return count

def main():
    num = int(input())
    wood_list = list(map(int, input().split()))
    result = find_min(num, wood_list)
    print(result)

if __name__ == "__main__":
    main()
