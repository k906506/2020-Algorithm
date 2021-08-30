def find_number(input_dict, target):
    if target in input_dict:
        return 1
    else:
        return 0

def main():
    target = int(input())
    input_key= input().strip().split()
    input_value = list(map(int, input_key))
    input_dict = dict(zip(input_key, input_value))
    print(find_number(input_dict, target))

if __name__ == "__main__":
    main()