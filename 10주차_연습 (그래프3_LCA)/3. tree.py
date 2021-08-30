def postorder(tree, node, visit_list):
    if (tree[node][0] != '.'):
        postorder(tree, tree[node][0], visit_list)
    if (tree[node][1] != '.'):
        postorder(tree, tree[node][1], visit_list)
    visit_list.append(node)

def inorder(tree, node, visit_list):
    if (tree[node][0] != '.'):
        inorder(tree, tree[node][0], visit_list)
    visit_list.append(node)
    if (tree[node][1] != '.'):
        inorder(tree, tree[node][1], visit_list)


def preorder(tree, node, visit_list):
    visit_list.append(node)
    if (tree[node][0] != '.'):
        preorder(tree, tree[node][0], visit_list)
    if (tree[node][1] != '.'):
        preorder(tree, tree[node][1], visit_list)

def main():
    n = int(input())
    tree = {}
    for _ in range(n):
        node_list = input().split(' ')
        tree[node_list[0]] = [node_list[1], node_list[2]]

    visit_list = []
    postorder(tree, 'A', visit_list)
    print(*visit_list)

    visit_list = []
    inorder(tree, 'A', visit_list)
    print(*visit_list)

    visit_list = []
    preorder(tree, 'A', visit_list)
    print(*visit_list)
    

if __name__ == "__main__":
    main()
