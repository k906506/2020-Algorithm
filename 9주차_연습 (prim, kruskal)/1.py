from collections import deque

n = 8
k = 2
cmd = ["D 2","C","U 3","C","D 4","C","U 2","Z","Z"]

def main(): # n = 행의 개수, k = 처음 위치, cmd = 문자열
    change_cmd = [i for i in range(n)]
    delete_pos = deque()
    
    index = k
    length = n
    for i in range(n+1):
        if cmd[i][0] == 'C':
            delete_pos.append(index)
            change_cmd[index] = -1 # 삭제된 원소
            index += 1
            if index == length-1:
                index -= 1
            length -= 1
        elif cmd[i][0] == 'Z':
            repair = delete_pos.pop()
            change_cmd[repair] = repair # 다시 생성
        else:
            command, pos = cmd[i].split(" ")
            if command == 'U':
                index -= int(pos)
            else:
                index += int(pos)
        print(cmd[i][0], index, length, delete_pos)
    
    print(change_cmd)
    ans = ""
    for i in range(n):
        if change_cmd[i] == i:
            ans += 'O'
        else:
            ans += 'X'
    
    print(ans)

if __name__ == "__main__":
    main()