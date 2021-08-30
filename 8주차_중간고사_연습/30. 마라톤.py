import collections

def find_finish(start_list, finish_list):
    result = collections.Counter(start_list) - collections.Counter(finish_list)
    result = list(result.elements())
    return result

def main():
    start_list = list(input().split())
    finish_list = list(input().split())
    result = find_finish(start_list, finish_list)
    for i in result:
        print(i)

if __name__ == "__main__":
    main()