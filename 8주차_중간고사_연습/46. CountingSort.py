import sys

num = int(input())
int_list = [0]*10001

for i in range(num):
    x = int(sys.stdin.readline())
    int_list[x] += 1

for i in range(1, 10001):
    if int_list[i] != 0:
        for _ in range(int_list[i]):
            print(i, end = " ")