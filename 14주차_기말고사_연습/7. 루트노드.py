def main():
    n = int(input())
    parent = []
    child = []

    for i in range(n):
        a, b, c = input().split()
        if b != '.' or c != '.':
            parent.append(a)
            child.append(b)
            child.append(c)
        
    for i in parent:
        if i not in child:
            print(i)

if __name__ == "__main__":
    main()