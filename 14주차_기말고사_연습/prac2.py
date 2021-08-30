def preorder(node, root, visit, depth, depth_list):
    visit.append(root)
    depth += 1
    depth_list.append(depth)
    if (node[root][0] != '.'):
        preorder(node, node[root][0], visit, depth, depth_list)
        visit.append(root)
    if (node[root][1] != '.'):
        preorder(node, node[root][1], visit, depth, depth_list)
        visit.append(root)
    depth -= 1
    depth_list.append(depth)
    return visit, depth_list

def main():
    n = int(input())
    parent = []
    child = []
    node = {}

    for i in range(n):
        a, b, c = input().split()
        node[a] = [b, c]
        parent.append(a)
        child.append(b)
        child.append(c)
    
    for i in parent:
        if i not in child:
            root = i

    visit = []
    depth = -1
    depth_list = []
    visit, depth_list = preorder(node, root, visit, depth, depth_list)

    new_depth_list = []
    for i in range(len(visit)):
        new_depth_list.append(depth_list[i])

    node_a, node_b = input().split()

    for i in range(len(visit)):
        if visit[i] == node_a:
            node_a = i
        if visit[i] == node_b:
            node_b = i
    
    if node_a > node_b: # a의 index를 더 작게
        temp = node_a
        node_a = node_b
        node_b = temp
        
    min_node = new_depth_list[node_a]
    root_index = 0

    for i in range(node_a+1, node_b+1):
        if min_node > new_depth_list[i]:
            min_node = new_depth_list[i]
            root_index = i

    left_index_list = []
    left_depth_list = []
    right_index_list = []
    right_depth_list = []
    for i in range(node_a, node_b+1):
        if (new_depth_list[i] not in left_depth_list) and (i < root_index):
            left_depth_list.append(new_depth_list[i])
            left_index_list.append(i)
        elif (new_depth_list[i] not in right_index_list) and i >= root_index:
            right_depth_list.append(new_depth_list[i])
            right_index_list.append(i)
    
    left_index_list.extend(right_index_list)
    for i in left_index_list:
        print(visit[i], end = " ")

if __name__ == "__main__":
    main()