import heapq

def dijkstra(node_dict, node, V, E, src, dst, maximum):
    INF = float('inf')

    distance = {}
    prev = {}
    count = {}
    found = {}
    queue = []

    for i in range(V):
        distance[node[i]] = INF
        prev[node[i]] = []
        count[node[i]] = maximum
        found[node[i]] = False

    distance[src] = 0

    heapq.heappush(queue, [0, src])
    while queue:
        v = heapq.heappop(queue)
        found[v[1]] = True
        for node_weight in node_dict[v[1]]:
            if (found[node_weight[0]]):
                continue
            if (distance[node_weight[0]] > distance[v[1]] + node_weight[1]) and count[v[1]] > 0:
                distance[node_weight[0]] = distance[v[1]] + node_weight[1]
                count[v[1]] -= 1
                heapq.heappush(queue, [distance[node_weight[0]], node_weight[0]])
                prev[node_weight[0]] = [v[1], node_weight[0], node_weight[1]]

    return prev
        
def main():
    V, E, maximum = map(int, input().split())
    node = input().split()
    node_dict = {}

    for i in node:
        node_dict[i] = []
    
    for i in range(E):
        a, b, c = input().split()
        node_dict[a].append([b, int(c)])
    
    src, dst = input().split()
    prev = dijkstra(node_dict, node, V, E, src, dst, maximum)

    prev_list = []
    prev_e = dst
    check = False

    for i in node:
        if len(prev[i]) != 0:
            check = True

    if check == True:
        while prev_e != src:
            prev_list.append(prev[prev_e])
            prev_e = prev[prev_e][0]

        prev_list.reverse()
        for i in prev_list:
            print(*i)
    else:
        print(src, dst, node_dict[src][1][1])



if __name__ == "__main__":
    main()