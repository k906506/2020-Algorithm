import sys

def binary_search(input_list, i, start, end):
    if start > end:
        return 0
    mid = (start + end) // 2
    if i == input_list[mid]:
        return 1
    elif i > input_list[mid]:
        return binary_search(input_list, i, mid+1, end)
    else:
        return binary_search(input_list, i, start, mid-1)

def main():
    a = int(input())
    input_list = list(map(int, sys.stdin.readline().split()))
    input_list.sort()
    b = int(input())
    target_list = list(map(int, sys.stdin.readline().split()))
    
    print(input_list, target_list)

    for i in target_list:
        start = 0
        end = a - 1
        print(binary_search(input_list, i, start, end))

if __name__ == "__main__":
    main()