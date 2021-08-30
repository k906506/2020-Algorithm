import heapq

def prim(node_dict, node, n):
    queue = []
    heapq.heappush(queue, [0, node[0], node[1]]) # 비용, 이전 노드, 다음 노드

    visit = {}

    for i in range(n):  # 모든 노드를 방문하지 않은 상태로
        visit[node[i]] = False

    result = []
    sum_path = 0

    while queue:
        h = heapq.heappop(queue)
        if visit[h[2]] == True: # 방문한 노드면 그냥 지나침
            continue
        else:
            visit[h[2]] = True
            sum_path += h[0]
            result.append([h[1], h[2], h[0]])
        
        for e in node_dict[h[2]]:
            if (visit[e[0]]) : continue
            heapq.heappush(queue, [e[1], h[2], e[0]])
            
    for e in visit.values():
        if e == False:
            sum_path = 0

    return sum_path

def main():
    n, m = map(int, input().split())
    node = input().split()
    node_dict = {}

    for i in range(n):
        node_dict[node[i]] = []

    for _ in range(m):
        u, v, c = input().split()
        edges[u].append([v, int(c)])
        edges[v].append([u, int(c)])

    print(prim(node_dict, node, n))

if __name__ == "__main__":
    main()