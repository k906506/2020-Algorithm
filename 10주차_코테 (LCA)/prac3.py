def preorder(tree, node, visit_list, count, count_list):
    visit_list.append(node)
    count += 1
    count_list.append(count)
    if (tree[node][0] != '.'):
        preorder(tree, tree[node][0], visit_list, count, count_list)
        visit_list.append(node)
    if (tree[node][1] != '.'):
        preorder(tree, tree[node][1], visit_list, count, count_list)
        visit_list.append(node)
    count -= 1
    count_list.append(count)

def main():
    num = int(input())
    node_parent = []
    node_child = []
    tree = {}
    for _ in range(num):
        node_list = list(input().split())
        tree[node_list[0]] = [node_list[1], node_list[2]]
        if node_list[1] != '.' or node_list[2] != '.':
            node_parent.append(node_list[0])
            node_child.append(node_list[1])
            node_child.append(node_list[2])
    for i in node_parent:
        if i not in node_child:
            result = i

    count = 0
    visit_list = []
    count_list = []
    depth_list = []
    preorder(tree, result, visit_list, count, count_list)
    for i in range(len(visit_list)):
        depth_list.append(count_list[i])
    select_node = list(input().split())
    for i in range(len(visit_list)):
        if visit_list[i] == select_node[0]:
            index_a = i
        if visit_list[i] == select_node[1]:
            index_b = i
    if index_a == index_b:
        print(visit_list[index_a])
    else:
        if index_a > index_b:
            temp = index_a
            index_a = index_b
            index_b = temp
        min_depth = depth_list[index_a]
        index = index_a
        for i in range(index_a, index_b+1):
            if min_depth > depth_list[i]:
                min_depth = depth_list[i]
                index = i
        result = visit_list[index]
        print(result)

if __name__ == "__main__":
    main()
