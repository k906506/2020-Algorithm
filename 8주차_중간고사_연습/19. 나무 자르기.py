def cut_wood(wood_list, n, m):
    max_len = wood_list[n-1]
    min_len = 0
    result = 0
    while min_len <= max_len:
        sum_wood = 0
        mid = int((max_len + min_len)//2)
        for i in range(len(wood_list)):
            if wood_list[i] > mid:
                sum_wood += (wood_list[i] - mid)
        if sum_wood >= m:       # 잘라낸 나무의 합이 m보다 크므로 기준점을 높인다.
            result = mid
            min_len = mid + 1
        else:
            max_len = mid - 1
    return result

def main():
    n, m = map(int, input().split())
    wood_list = list(map(int, input().split()))
    wood_list.sort()
    print(cut_wood(wood_list, n, m))

if __name__ == "__main__":
    main()