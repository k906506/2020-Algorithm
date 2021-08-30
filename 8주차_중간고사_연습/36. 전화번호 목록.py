def solution(phone_book):
    answer = True
    phone_book.sort()
    for p1, p2 in zip(phone_book, phone_book[1:]):
        if p2.startswith(p1):
            answer = False
    return answer

def main():
    number = list(input().split())
    print(solution(number))

if __name__ == "__main__":
    main()

    string = input().split()

for i in string:
    new_s = string.copy()
    new_s.remove(i)
    print(new_s)
    print()
    for j in new_s:
        if j.find(i) != -1:
            print(j)
