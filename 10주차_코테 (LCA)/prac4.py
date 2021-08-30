def preorder(tree, node, visit_list, count, count_list):
    visit_list.append(node)
    count += 1
    count_list.append(count)
    if (tree[node][0] != '.'):
        preorder(tree, tree[node][0], visit_list, count, count_list)
    if (tree[node][1] != '.'):
        preorder(tree, tree[node][1], visit_list, count, count_list)

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
    preorder(tree, result, visit_list, count, count_list)
    depth = max(count_list) # 최대 깊이
    max_depth_node = count_list.count(depth) # 최대 깊이 노드의 개수

    max_node = []
    for i in range(len(count_list)):
        if count_list[i] == depth:
            max_node.append(i)
    length = max_node[len(max_node)-1] - max_node[0] - 1 # 최대 깊이 노드끼리의 최대 간격
    if length == 0: # 최대 깊이 노드가 같은 부모의 자식일 때
        length = 1

    index = count_list.index(depth) # 최대 깊이를 갖는 노드 중에 맨 앞에 있는 노드의 인덱스

    if max_depth_node >= 2: # 최대 깊이 노드가 2개 이상일 때
        print(visit_list[index-length])
    else: # 최대 깊이 노드가 1개일 때
        max_depth_node = max_depth_node//2  #log2와 같은 의미
        print(visit_list[index-max_depth_node])
    
if __name__ == "__main__":
    main()
