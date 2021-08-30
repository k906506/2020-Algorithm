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
    
    result_node = input()
    print(node_dict)
    print(len(node_dict[result_node]))

if __name__ == "__main__":
    main()