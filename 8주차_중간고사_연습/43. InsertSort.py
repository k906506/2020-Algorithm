def insert_sort(input_list):
    for i in range(1, len(input_list)):
        key = input_list[i]
        for j in range(i-1, -1, -1):
            if input_list[j] > key:
                input_list[j+1] = input_list[j]
                input_list[j] = key
            else:
                break
    return input_list

input_list = list(input().split())
print(insert_sort(input_list))

