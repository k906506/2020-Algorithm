def quick_sort(input_list):
    if len(input_list) <= 1:
        return input_list
    else:
        pivot = input_list[0]
        left = []
        right = []
        for i in range(1, len(input_list)):
            if pivot > input_list[i]:
                left.append(input_list[i])
            else:
                right.append(input_list[i])
        return quick_sort(left) + [pivot] + quick_sort(right)

input_list = list(input().split())
print(quick_sort(input_list))      