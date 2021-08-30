import heapq

def dijkstra(node_dict, node, V, E, src, dst):
    INF = float('inf')

    distance = {}
    found = {}
    queue = []

    for i in range(V):
        distance[node[i]] = INF
        found[node[i]] = False

    distance[src] = 0

    heapq.heappush(queue, [0, src])
    while queue:
        v = heapq.heappop(queue)
        found[v[1]] = True
        for node_weight in node_dict[v[1]]:
            if (found[node_weight[0]]):
                continue
            if (distance[node_weight[0]] > distance[v[1]] + node_weight[1]):
                distance[node_weight[0]] = distance[v[1]] + node_weight[1]
                heapq.heappush(queue, [distance[node_weight[0]], node_weight[0]])
    return distance[dst]

def main():
    V, E = map(int, input().split())
    node = input().split()
    node_dict = {}
    for i in node:
        node_dict[i] = []

    for _ in range(E):
        i, j, c = input().split()
        node_dict[i].append([j,int(c)])
        node_dict[j].append([i,int(c)])
    
    len_dict = {}
    for i in node:
        len_dict[i] = []

    min_len = int(input())

    for i in node:
        for j in node:
            result = dijkstra(node_dict, node, V, E, i, j)
            if min_len >= result:
                len_dict[i].append(result)
                len_dict[j].append(result)
    
    result = []

    for i in range(len(len_dict)):
        result.append([node[i],len_dict[node[i]]])
    result = sorted(result, key = lambda x : len(x[1]))
    print(result[len(result)-1][0], int(len(result[len(result)-1][1])//2))

if __name__ == "__main__":
    main()