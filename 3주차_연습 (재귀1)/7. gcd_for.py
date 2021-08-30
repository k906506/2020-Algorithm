import sys

def gcd(a, b):
    if b == 0:
        return a
    else:
        while b!= 0:
            n = a%b
            a = b
            b = n
        return a

size = int(input())
for i in range(size):
    a, b = map(int, sys.stdin.readline().split)
    print(gcd(a,b))