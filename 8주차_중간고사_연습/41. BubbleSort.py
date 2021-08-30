def bubble_sort(input_list):
    for i in range(len(input_list)):
        for j in range(len(input_list)-1, i, -1):
            if input_list[j-1] > input_list[j]:
                temp = input_list[j]
                input_list[j] = input_list[j-1]
                input_list[j-1] = temp
    return input_list

input_list = list(input().split())
print(bubble_sort(input_list))