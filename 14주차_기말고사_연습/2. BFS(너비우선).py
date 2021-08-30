def bfs(node_dict, start_node):
    queue = []
    visit = []
    queue.append(start_node)

    while queue:
        e = queue.pop(0)
        if e not in visit:
            visit.append(e)
            queue.extend(node_dict[e])
    
    return visit

def main():
    n, m = map(int, input().split())
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
        
    print(*bfs(node_dict, start_node))
   

if __name__ == "__main__":
    main()