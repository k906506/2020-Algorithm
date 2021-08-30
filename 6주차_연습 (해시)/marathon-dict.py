def compareDict(p_list, c_list):
    incomplete = []
    dict_name = {}

    for s in p_list:
        dict_name[s] = 1
    for s in c_list:
        dict_name[s] -= 1
    for s in p_list:
        if dict_name[s] == 1:
            incomplete.append(s)
    return incomplete

def main():
    a = input().split()
    b = input().split()
    print(compareDict(a,b))

if __name__ == "__main__":
    main()
