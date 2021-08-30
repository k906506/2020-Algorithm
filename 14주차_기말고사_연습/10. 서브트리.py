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
    visit.remove(visit[len(visit)-1])
    depth_list.remove(depth_list[len(depth_list)-1])
    depth_list.remove(depth_list[len(depth_list)-2])

    minimum = min(depth_list)   # 최대 깊이 인덱스 저장
    count = depth_list.count(minimum)

    min_list = []

    if count > 1:
        for i in range(len(depth_list)):
            if depth_list[i] == minimum:
                min_list.append(i)  # 최대 깊이 인덱스 저장
        minimum = int(visit[min_list[0]])
        for i in range(min_list[0]+1, min_list[len(min_list)-1]+1):
            if minimum > depth_list[i]:
                minimum = depth_list[i]
        print(visit[minimum])
    else:
        print(visit[depth_list.index(minimum)])

if __name__ == "__main__":
    main()