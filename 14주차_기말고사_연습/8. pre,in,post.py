def preorder(node, root, visit):
    visit.append(root)
    if (node[root][0] != "."):
        preorder(node, node[root][0], visit)
    if (node[root][1] != "."):
        preorder(node, node[root][1], visit)
    return visit

def Inorder(node, root, visit):
    if (node[root][0] != "."):
        Inorder(node, node[root][0], visit)
    visit.append(root)
    if (node[root][1] != "."):
        Inorder(node, node[root][1], visit)
    return visit

def postorder(node, root, visit):
    if (node[root][0] != "."):
        postorder(node, node[root][0], visit)
    if (node[root][1] != "."):
        postorder(node, node[root][1], visit)
    visit.append(root)
    return visit

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
    print(*preorder(node, root, visit))
    visit = []
    print(*Inorder(node, root, visit))
    visit = []
    print(*postorder(node, root, visit))

if __name__ == "__main__":
    main()
