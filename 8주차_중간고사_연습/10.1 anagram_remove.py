def anagram(string1, string2):
    string1 = list(string1)
    string2 = list(string2)
    
    find_anagram = string2.copy()
    for i in range(len(string1)):
        for j in range(len(string2)):
            if string1[i] == string2[j]:
                find_anagram.remove(string2[j])
                
    if len(find_anagram) == 0:
        print("True")
    else:
        print("False")

def main():
    string1, string2 = input().split()
    string1 = string1.lower()
    string2 = string2.lower()
    anagram(string1, string2)

if __name__ == "__main__":
    main()