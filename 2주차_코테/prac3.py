import heapq

def findElement(arr, k):
    heapArray = []
    for e in arr:
        heapq.heappush(heapArray, e)
    for _ in range(len(arr)-k):
        result = heapq.heappop(heapArray)
    return result

n, m = map(int, input().split())
int_list = list(map(int, input().split()))
print(findElement(int_list, m))