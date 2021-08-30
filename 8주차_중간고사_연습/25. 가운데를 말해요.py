import heapq
import sys

num = int(input())
heap_list = []
pop_list = []
result = 0

for i in range(1, num+1):
    e = int(sys.stdin.readline())
    heapq.heappush(heap_list, e)
    pop_list = [] 
    if i%2 == 0:
        i = int(i//2)
        for j in range(i):
            result = heapq.heappop(heap_list)
            pop_list.append(result)
        print(result)
    else:
        i = int(i//2)
        for j in range(i+1):
            result = heapq.heappop(heap_list)
            pop_list.append(result)
        print(result)
    for e in pop_list:
        heapq.heappush(heap_list, e)