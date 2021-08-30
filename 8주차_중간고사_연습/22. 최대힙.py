import heapq
import sys

num = int(input())
heap_list = []

for i in range(num):
    i = int(sys.stdin.readline())
    if i == 0:
        if len(heap_list) == 0:
            print(0)
        else:
            result = heapq.heappop(heap_list)[1]
            print(result)
    else:
        heapq.heappush(heap_list, (-i, i))