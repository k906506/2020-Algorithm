def anagram(string1, string2):
    if "".join(sorted(string1)) == "".join(sorted(string2)):
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