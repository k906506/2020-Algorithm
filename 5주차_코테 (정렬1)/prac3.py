import re
def sort(input_list):
    result = sorted(input_list, key = lambda x : (x[2].lower(),x[0],int(x[1])))
    return result

file_list = []
while True:
    try:
        file_list.append(input())
    except EOFError:
        break

for i in range(len(file_list)):
    file_list[i] = re.split('[.|-]', file_list[i])

for i in range(len(file_list)):
    if len(file_list[i]) == 2:
        file_list[i].insert(1,0)

result = sort(file_list)

for i in range(len(result)):
    if result[i][1] == 0:
        result[i].remove(result[i][1])

for i in range(len(result)):
    if len(result[i]) > 2:
        print(result[i][0] + "-" + result[i][1] + "." + result[i][2])
    else:
        print(result[i][0] + "." + result[i][1])