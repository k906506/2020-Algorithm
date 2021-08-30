import re

def sort_file(input_list):
    for i in range(len(input_list)):
        input_list[i] = re.split("[-|.]", input_list[i])
    
    for i in range(len(input_list)):
        if len(input_list[i]) == 2:
            input_list[i].insert(1,0)
    
    input_list = sorted(input_list, key = lambda x : (x[2].lower(), x[0], int(x[1])))

    for i in range(len(input_list)):
        if input_list[i][1] == 0:
            input_list[i].remove(0)
    
    for i in range(len(input_list)):
        if len(input_list[i]) == 2:
            print(input_list[i][0] + "." + input_list[i][1])
        else:
            print(input_list[i][0] + "-" + input_list[i][1] + "." + input_list[i][2])

def main():
    input_list = []
    while True:
        try:
            input_list.append(input())
        except EOFError:
            break
    sort_file(input_list)

if __name__ == "__main__":
    main()