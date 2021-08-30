import collections

def find_target(input_list, target_list):
    p = collections.Counter(input_list)
    for i in range(len(target_list)):
        if p.keys() == target_list[i]:
            print(p.values())

def main():
    n = int(input())
    input_list = list(map(int, input().split()))
    m = int(input())
    target_list = list(map(int, input().split()))
    find_target(input_list, target_list)

if __name__ == "__main__":
    main()