def multiple_sort(input_list):
    result = sorted(input_list, key = lambda x : (len(x), x))
    return result

input_list = list(input().split())
print(multiple_sort(input_list))
