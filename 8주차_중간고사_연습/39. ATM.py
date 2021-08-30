def main():
    answer = 0
    result = 0
    num = int(input())
    input_list = list(map(int, input().split()))
    input_list.sort()
    for i in range(num):
        result += input_list[i]
        answer += result
    print(answer)

if __name__ == "__main__":
    main()