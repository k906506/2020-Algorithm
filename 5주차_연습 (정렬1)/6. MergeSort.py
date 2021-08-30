def merge_sort(input_list):
    if len(input_list) <= 1:
        return input_list
    mid = len(input_list)//2
    left = input_list[:mid]
    right = input_list[mid:]
    leftList = merge_sort(left)
    rightList = merge_sort(right)
    #재귀가 종료되면 한개씩 나눠져있다
    return merge(leftList, rightList)

def merge(left, right):
    result_list = []
    while len(left) > 0 or len(right) > 0 :
        if len(left) > 0 and len(right) > 0:
            if left[0] <= right[0]:
                result_list.append(left[0])
                left = left[1:]
            else:
                result_list.append(right[0])
                right = right[1:]
        elif len(left) > 0:
            result_list.append(left[0])
            left = left[1:]
        elif len(right) > 0:
            result_list.append(right[0])
            right = right[1:]
    return result_list

input_list = list(input().split())
choice = int(input())
result = merge_sort(input_list)
if choice%2 == 0:
    result.reverse()
print(result)