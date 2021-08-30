from functools import reduce

def factorial_reduce(n):
    return reduce(lambda x,y : x*y, range(1,n+1))

def main():
    n = int(input())
    for _ in range(n):
        input_data = int(input())
        print(factorial_reduce(input_data))

if __name__ == "__main__":
    main()