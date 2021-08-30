def longest_palindrome(s):
    table = [[False for i in range(len(s))] for i in range(len(s))]
    longest = 0

    for i in range(len(s)):
        for j in range(len(s)-i):
            if i < 2:
                if s[j] == s[i+j]:
                    table[j][i+j] = True
                    longest = i + 1
                else:
                    table[j][i+j] = False
            else:
                if s[j] == s[i+j] and table[j+1][i+j-1]:
                    table[j][i+j] = True
                    longest = i + 1
                else:
                    table[j][i+j] = False
    return longest

num = int(input())
for i in range(num):
    string = input().strip().lower()
    print(longest_palindrome(string))
