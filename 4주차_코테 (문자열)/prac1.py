def check_anagram(string1, string2):
    if "".join(sorted(string1)) == "".join(sorted(string2)):
        return True
    else:
        return False

string1, string2 = input().split()
string1 = string1.lower().replace(" ", "")
string2 = string2.lower().replace(" ", "")
if(check_anagram(string1, string2)):
    print("True")
else:
    print("False")