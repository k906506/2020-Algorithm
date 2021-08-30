def preorder(tree, node, visit_list):
    visit_list.append(node)
    if (tree[node][0] != '.'):
        preorder(tree, tree[node][0], visit_list)
    if (tree[node][1] != '.'):
        preorder(tree, tree[node][1], visit_list)

def inorder(tree, node, visit_list):
    if (tree[node][0] != '.'):
        inorder(tree, tree[node][0], visit_list)
    visit_list.append(node)
    if (tree[node][1] != '.'):
        inorder(tree, tree[node][1], visit_list)

def postorder(tree, node, visit_list):
    if (tree[node][0] != '.'):
        postorder(tree, tree[node][0], visit_list)
    if (tree[node][1] != '.'):
        postorder(tree, tree[node][1], visit_list)
    visit_list.append(node)

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
    
    visit_list = []
    preorder(tree, result, visit_list)
    print(*visit_list)

    visit_list = []
    inorder(tree, result, visit_list)
    print(*visit_list)

    visit_list = []
    postorder(tree, result, visit_list)
    print(*visit_list)

if __name__ == "__main__":
    main()
