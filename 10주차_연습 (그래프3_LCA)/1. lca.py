from math import log2
from collections import deque

def generate_tree(tree, num):
    for _ in range(num-1):
        parent, child = map(int, input().split())
        tree[child].append(parent)
        tree[parent].append(child)

def dfs(tree, parent_list, depth, num):
    visited = [False for _ in range(num+1)]
    q = deque()
    q.append(1)

    while q:
        p = q.popleft()
        visited[p] = True
        for i in tree[p]:
            if visited[i] == False:
                q.append(i)
                parent_list[i] = p
                depth[i] = depth[p] + 1

def compute_exp_parent(exp_parent, num):
    logN = int(log2(num) + 1)
    for i in range(1, num+1):
        for j in range(1, logN):
            exp_parent[i][j] = exp_parent[exp_parent[i][j-1]][j-1]

def search_lca(exp_parent, depth, num, m):
    logN = (int)(log2(num) + 1)
    for _ in range(m):
        a, b = map(int, input().split())
        if depth[a] > depth[b]:
            a, b = b, a
        level_diff = depth[b] - depth[a]
        for i in range(logN):
            if level_diff & 1 << i:
                b = exp_parent[b][i]
        if a == b:
            print(a)
            continue
        for i in range(logN-1, -1, -1):
            if exp_parent[a][i] != exp_parent[b][i]:
                a = exp_parent[a][i]
                b = exp_parent[b][i]
        print(exp_parent[b][0])

def main():
    num = int(input())
    tree = [[] for _ in range(num+1)]
    generate_tree(tree, num)

    parent_list = [0 for _ in range(num+1)]
    depth = [0 for _ in range(num+1)]
    dfs(tree, parent_list, depth, num)

    logN = (int)(log2(num) + 1)
    exp_parent = [[0 for _ in range(logN)] for i in range(num+1)]
    for i in range(num+1):
        exp_parent[i][0] = parent_list[i]
    compute_exp_parent(exp_parent, num)

    m = int(input())
    search_lca(exp_parent, depth, num, m)

if __name__ == "__main__":
    main()