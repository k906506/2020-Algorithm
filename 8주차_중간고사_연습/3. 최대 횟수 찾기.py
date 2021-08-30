def max_match(num):
    if num <= 1:
        return num
    else:
        i = 0
        for k in range(num):
            i += k
            k += 1
        return i

def main():
    num = int(input())
    input_list = list(map(int, input().split()))
    input_list.sort()
    print(max_match(num))
    for i in range(len(input_list)):
        print(input_list[i], end = " ")

if __name__ == "__main__":
    main()