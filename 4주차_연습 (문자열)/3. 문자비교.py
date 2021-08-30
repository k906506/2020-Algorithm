def is_anagram(str1, str2):
    if "".join(sorted(str1)) == "".join(sorted(str2)):
        return True
    else:
        return False

num = int(input())
for _ in range(num):
    word1 = input().strip().lower().replace(" ", "")
    word2 = input().strip().lower().replace(" ", "")
    print(word1, word2)
    if(is_anagram(word1, word2)):
        print("Its anagram")
    else:
        print("Its not anagram")