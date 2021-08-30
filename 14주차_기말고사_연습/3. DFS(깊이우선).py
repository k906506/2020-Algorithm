def dfs(node_dict, start_node, visit):
    if visit is None:
        visit = []
    visit.append(start_node)
    for e in node_dict[start_node]:
        if e not in visit:
            dfs(node_dict, e, visit)
    return visit

def main():
    n, m = map(int, input().split())
    visit = []
    node_list = input().split()
    node_dict = dict()

    for i in range(n):
        node_dict[node_list[i]] = []
    
    for i in range(m):
        a, b = input().split()
        if b not in node_dict[a]:
            node_dict[a].append(b)

    start_node = input()

    for i in node_list:
        node_dict[i].sort()
    
    print(*dfs(node_dict, start_node, visit))
   

if __name__ == "__main__":
    main()