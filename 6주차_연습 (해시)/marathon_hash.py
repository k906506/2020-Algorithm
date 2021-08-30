import collections

def find_marathon(a_list, b_list):
    result = collections.Counter(a_list) - collections.Counter(b_list)
    return list(result.keys())

def main():
    start = input().split()
    finish = input().split()
    print(*find_marathon(start, finish))

if __name__ == '__main__':
    main()