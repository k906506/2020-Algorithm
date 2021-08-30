def find_list(int_list, n, k, i):
    int_list.sort()
    k_th = int_list[k-1]
    i_th = int_list[n-i]
    return abs(k_th-i_th)

def main():
    n, k, i = map(int, input().split())
    input_list = list(map(int, input().split()))
    print(find_list(input_list, n, k, i))

if __name__ == "__main__":
    main()
