def main():
    num = int(input())
    node_parent = []
    node_child = []
    for _ in range(num):
        node_list = list(input().split())
        if node_list[1] != '.' or node_list[2] != '.':
            node_parent.append(node_list[0])
            node_child.append(node_list[1])
            node_child.append(node_list[2])
    for i in node_parent:
        if i not in node_child:
            result = i
    print(result)

if __name__ == "__main__":
    main()
