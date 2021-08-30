parent = {}
rank = {}

def make_set(v):
    parent[v] = v
    rank[v] = 0

def find(v):
    if parent[v] != v:
        parent[v] = find(parent[v])
    return parent[v]

def union(u, v):
    root1 = find(u)
    root2 = find(v)
    if root1 != root2:
        if rank[root1] > rank[root2]:
            parent[root2] = root1
        else:
            parent[root1] = root2
            if rank[root1] == rank[root2]:
                rank[root2] += 1

def kruskal(vertices_list, edges_list):
    for u in vertices_list:
        make_set(u)
    edges = edges_list
    edges.sort()
    sum = 0
    for e in edges:
        cost, u, v = e
        if find(u) != find(v):
            union(u,v)
            sum += cost
    return sum

def main():
    n, m = map(int, input().split())
    vertices = []
    edges = []
    input_list = input().split()
    for i in range(n):
        vertices.append(input_list[i])
    for _ in range(m):
        u, v, c = input().split()
        c = int(c)
        edges.append((c, u, v))
    print(kruskal(vertices, edges))

if __name__ == "__main__":
    main()