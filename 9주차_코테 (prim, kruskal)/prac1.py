import heapq

def prim(edges, vertices, n):
    queue = []
    heapq.heappush(queue, [0, vertices[0], vertices[1]])

    visit = {}
    for i in range(n):
        visit[vertices[i]] = False
    result = []
    sum = 0

    while queue:
        h = heapq.heappop(queue)
        if visit[h[2]] == True:
            continue
        else:
            visit[h[2]] = True
            sum += h[0]
            result.append([h[1], h[2], h[0]])
        
        for e in edges[h[2]]:
            if (visit[e[0]]) : continue
            heapq.heappush(queue, [e[1], h[2], e[0]])
            
    for e in visit.values():
        if e == False:
            sum = 0

    return sum

def main():
    n, m = map(int, input().split())
    vertices = list(input().split())
    edges = {}
    for i in range(n):
        edges[vertices[i]] = []
    for _ in range(m):
        u, v, c = input().split()
        c = int(c)
        edges[u].append([v, c])
        edges[v].append([u, c])
    print(prim(edges, vertices, n))

if __name__ == "__main__":
    main()