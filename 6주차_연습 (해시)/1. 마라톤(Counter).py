import collections

def find_marathon(a_list, b_list):
    result = collections.Counter(a_list) - collections.Counter(b_list)
    return list(result.elements())

def main():
    start = input().split()
    finish = input().split()
    result = find_marathon(start, finish)
    result.sort()
    for i in range(len(result)):
        print(result[i])

if __name__ == '__main__':
    main()