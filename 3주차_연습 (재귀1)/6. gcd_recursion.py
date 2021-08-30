import sys

def gcd(a,b):
    if b == 0:
        return a
    else:
        return gcd(b, a%b)

size = int(input())
for i in range(size):
    a, b = map(int, sys.stdin.readline().split())  # rstrip() 공백문자 제거
    print(gcd(a,b))