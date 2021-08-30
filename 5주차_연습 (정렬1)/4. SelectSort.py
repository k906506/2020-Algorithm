def select_sort(input_list):
    for i in range(len(input_list)):
        index = i
        for j in range(i, len(input_list)):
            if input_list[index] > input_list[j]:
                temp = input_list[j]
                input_list[j] = input_list[index]
                input_list[index] = temp
    return input_list
    
input_list = list(input().split())
print(select_sort(input_list))
