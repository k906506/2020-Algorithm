def palindrome(string):
    string_list = [[False for _ in range(len(string))] for _ in range(len(string))]
    longest_string = 0

    for i in range(len(string)):
        for j in range(len(string)-i):
            if i < 2:
                if string[j] == string[i+j]:
                    string_list[j][i+j] = True
                    longest_string = i + 1
                else:
                    string_list[j][i+j] = False
            else:
                if string[j] == string[i+j] and string_list[j+1][i+j-1]:
                    string_list[j][i+j] = True
                    longest_string = i + 1
                else:
                    string_list[j][i+j] = False
    return longest_string

string = input().strip().lower().replace(" ", "")
print(palindrome(string))
