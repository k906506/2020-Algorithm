def dfs(graph, start_node, visit = None):
    if visit is None:
        visit = list()
    visit.append(start_node)
    for next in graph[start_node]:
        if next not in visit:
            dfs(graph, next, visit)
    return visit

def searchN(node, value):
    if value not in node:
        node.append(value)

def main():
    n, m = map(int, input().split())
    node = list(input().split())
    node_dic = {}
    for i in range(n):
        node_dic[node[i]] = []
    for _ in range(m):
        input_node = list(input().split())
        searchN(node_dic[input_node[0]], input_node[1])
        searchN(node_dic[input_node[1]], input_node[0])
    target = input()
    for i in range(len(node_dic)):
        node_dic[node[i]].sort()
    print(*dfs(node_dic, target))

if __name__ == "__main__":
    main()