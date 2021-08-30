def sort_list(input_list):
    result = sorted(input_list, key = lambda x : (-int(x[1]), x[2], x[3]))
    return result

def main():
    input_list = []
    while True:
        try:
            input_list.append(input().split())
        except EOFError:
            break
    print(sort_list(input_list))

if __name__ == "__main__":
    main()
