import heapq, sys

def input_sort(input_list):
    result = sorted(input_list, key = lambda x : x[0])
    return result

def main():
    num = int(input())
    input_list = [[0, 0] for _ in range(num)]

    for i in range(num):
        age, name = sys.stdin.readline().split()
        age = int(age)
        input_list[i][0] = age
        input_list[i][1] = name
    result = input_sort(input_list)
    
    for i in range(len(result)):
        print("%d %s" %(result[i][0], result[i][1]))

if __name__ == "__main__":
    main()