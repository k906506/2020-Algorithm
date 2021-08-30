def dfs(matrix, n, count, x, y):
    matrix[x][y] = 0
    dx = (1, -1, 0, 0)
    dy = (0, 0, 1, -1)

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx >=0 and nx < n and ny >= 0 and ny < n:
            if matrix[nx][ny] == 1:
                count = dfs(matrix, n, count+1, nx, ny)
    return count

def main():
    num = int(input())
    matrix = [list(map(int, input())) for _ in range(num)]

    apart = []
    for i in range(num):
        for j in range(num):
            if matrix[i][j] == 1:
                apart.append(dfs(matrix, num, 1, i, j))
    
    print(len(apart))
    for i in sorted(apart):
        print(i)

if __name__ == "__main__":
    main()