import sys
sys.setrecursionlimit(10**5)
rsp = list(map(int, input().split()))
distance = int(input())
def find_result(dist, result):
    if dist == 0:
        return result
    elif dist < 0:
        return -1
    else:
        result_list = []
        for i in rsp:
            temp = find_result(dist-i, result+1)
            if temp != -1:
                result_list.append(temp)
    if len(result_list) == 0:
        return -1
    return min(result_list)
print(find_result(distance, 0))
