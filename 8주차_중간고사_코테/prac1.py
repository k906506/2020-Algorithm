num = int(input())
input_list = []
for i in range(num):
    input_list.append(input().lower())

string_list = []
for i in input_list:
    string = "".join(sorted(i))
    string_list.append(string)
string_list.sort()
print(string_list)