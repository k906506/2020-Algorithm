import heapq

def kth_smallest(arr, k):
    min_heap = []
    for e in arr:
        heapq.heappush(min_heap, e)
    for _ in range(k):
        result = heapq.heappop(min_heap)
    return result

num = int(input())

for i in range(num):
    a = int(input("k값을 입력해주세요."))
    int_list = list(map(int, input().split()))
    print(kth_smallest(int_list,a))
