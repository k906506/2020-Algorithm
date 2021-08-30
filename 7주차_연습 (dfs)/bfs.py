def bfs(graph, start_node):
    visit = list()
    queue = list()
    queue.append(start_node)
    while queue:
        node = queue.pop(0)
        if node not in visit:
            visit.append(node)
            queue.extend(graph[node])
    return visit
    
def main():
    n, m = map(int, input().split())
    node = [0 for _ in range(n)]
    node = list(input().split())
    node_dic = dict()
    a_list = []
    for i in range(m):
        a_list.append(input().split())
    for i in node:
        b_list = []
        for j in range(len(a_list)):
            if a_list[j][0] == i:
                b_list.append(a_list[j][1])
        node_dic[i] = b_list
    target = input()
    print(*bfs(node_dic, target))

if __name__ == "__main__":
    main()