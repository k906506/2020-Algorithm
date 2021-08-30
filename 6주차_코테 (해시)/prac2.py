import heapq

def find_min(num, wood_list):
    heap_list = []
    max_size = num
    count = 0

    for i in range(len(wood_list)):     # num보다 큰 나무토막만 힙에 넣는다.
        if wood_list[i] > num:
            heapq.heappush(heap_list, (-wood_list[i], wood_list[i]))
        else:
            pass

    while heap_list[0][1] > max_size:          # 힙의 0번째 값이 num보다 작거나 같으면 pop, 그렇지 않으면 2/3, 1/3으로 나누고 push 한다
        result = heapq.heappop(heap_list)[1]
        i = int(result*(2/3))
        j = int(result*(1/3))
        heapq.heappush(heap_list, (-i, i))
        heapq.heappush(heap_list, (-j, j))
        count += 1
    return count

def main():
    num = int(input())
    wood_list = list(map(int, input().split()))
    result = find_min(num, wood_list)
    print(result)

if __name__ == "__main__":
    main()
