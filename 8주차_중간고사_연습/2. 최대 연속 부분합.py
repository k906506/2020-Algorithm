def max_list(input_list):
    current_max = input_list[0]
    sum_max = input_list[0]
    for i in range(1, len(input_list)):
        current_max = max(input_list[i], input_list[i] + current_max)
        sum_max = max(current_max, sum_max)
    return sum_max

def main():
    input_list = list(map(int, input().split()))
    print(max_list(input_list))

if __name__ == "__main__":
    main()