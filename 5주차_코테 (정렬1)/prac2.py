def sort(input_list):
    result = sorted(input_list, key = lambda x : (x[1],x[2],x[3],x[0]))
    return result

input_list = []
while True:
    try:
        input_list.append(input().split())
    except EOFError:
        break
result = sort(input_list)
for i in range(len(result)):
    print(result[i][0])