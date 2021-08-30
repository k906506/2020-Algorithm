def find_palindrome(string_list):
    palin_list = []
    for i in range(len(string_list)):
        if len(string_list[i])%2 == 0: #짝수
            half = len(string_list[i])//2
            before_half = string_list[i][:half]
            after_half = string_list[i][half:]
            after_half.reversed()
        else:
            half = len(string_list[i])//2 + 1
            before_half = string_list[i][:(half-1)]
            after_half = string_list[i][:(half+1)]
            after_half.reversed()
        if before_half == after_half:
            palin_list.append(string_list[i])
    return palin_list

string_list = list(input().split())
print(find_palindrome(string_list))

