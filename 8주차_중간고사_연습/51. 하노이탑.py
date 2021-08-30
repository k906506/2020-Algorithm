def hanoi(n, start, mid, finish):
    if n <= 1:
        print(start, finish)
        return
    hanoi(n-1, start, finish, mid)
    print(start, finish)
    hanoi(n-1, mid, start, finish)

def main():
    num = int(input())
    result = 2**num-1
    print(result)
    hanoi(num, 1, 2, 3)

if __name__ == "__main__":
    main()