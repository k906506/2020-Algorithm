def input_sort(input_list):
    input_list = sorted(input_list, key = lambda x : (len(x), x))
    return input_list

def main():
    input_list = []
    num = int(input())
    for i in range(num):
        input_list.append(input())
    input_list = set(input_list)
    input_list = list(input_list)
    result = input_sort(input_list)
    for i in result:
        print(i)

if __name__ == "__main__":
    main()