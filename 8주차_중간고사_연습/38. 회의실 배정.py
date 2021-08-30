import sys

def find_room(input_list):
    room_list = sorted(input_list, key = lambda x : (x[1], x[0]))
    end_time = 0
    count = 0
    for i in range(len(room_list)):
        if end_time <= room_list[i][0]:
            end_time = room_list[i][1]
            count += 1
    return count

def main():
    num = int(input())
    input_list = []
    
    for _ in range(num):
        input_list.append(list(map(int, sys.stdin.readline().split())))

    print(find_room(input_list))

if __name__ == "__main__":
    main()