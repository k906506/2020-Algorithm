input_list = []
while True:
    try:
        string = input()
        input_list.append(string)
    except EOFError:
        break
input_list.sort()
for i in range(len(input_list)):
    print(input_list[i])