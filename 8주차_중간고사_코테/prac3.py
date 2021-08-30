import re

input_list = []
while True:
    try:
        input_list.append(input())
    except EOFError:
        break

new_list = []
for i in input_list:
    if i != "<!DOCTYPE html>" and i != "<html>" and i != "<body>" and i != "</body>" and i != "</html>":
        new_list.append(i)
        
for i in range(len(new_list)):
    new_list[i] = re.split("[<|>|=]", new_list[i])

for i in range(len(new_list)):
    new_list[i] = new_list[i][2]

for i in range(len(new_list)):
    string = str(new_list[i])
    string = string.replace('"', "")
    new_list[i] = string

for i in range(len(new_list)):
    new_list[i] = re.split("[/|.]", new_list[i])

for i in range(len(new_list)):
        if len(new_list[i]) != 8:
            new_list[i].insert(5, "x")

new_list = sorted(new_list, key = lambda x : (x[6], x[7]))

for i in new_list:
    print(*i)