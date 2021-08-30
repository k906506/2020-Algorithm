def is_palindrome(s):
    return s == s[::-1]

num = int(input())
word_list = []
for i in range(num):
    word_list.append(input().strip())

for i in word_list:
    if(is_palindrome(i)):
        print("Its palindrome")
    else:
        print("Its not palindrome")
