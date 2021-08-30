import bisect

def find_number(n_dict, t):
    if t in n_dict.values():
        return 1
    else:
        return 0

def find_number_bisert(input_list, t):
    input_list.sort()
    if bisect.bisect(input_list, t) >= 0:
        return 1
    else:
        return 0

def main():
    target = int(input())
    input_key_string = input().strip().split()
    input_val_integer = list(map(int, input_key_string))
    input_dict = dict(zip(input_key_string, input_val_integer))
    print(input_dict)
    print(find_number(input_dict, target))
    print(find_number_bisert(input_val_integer, target))

if __name__ == "__main__":
    main()