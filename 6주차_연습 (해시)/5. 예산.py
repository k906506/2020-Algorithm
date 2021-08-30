def solution(d, budget):
    left = 0
    right = max(budget)
    answer = 0

    while left <= right:
        mid = (left + right) // 2
        result = 0
        for i in budget:
            if i <= mid:
                result += i
            else:
                result += mid
        if result > d:  # 총 예산보다 큰 경우
            right = mid - 1
        else:           # 총 예산보다 작거나 같은 경우
            answer = mid
            left = mid + 1
    return answer

def main():
    budget_list = list(map(int, input().split()))
    money = int(input())
    print(solution(money, budget_list))

if __name__ == "__main__":
    main()