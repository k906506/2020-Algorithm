import heapq

def bellman_ford(node_dict, node, V, E, src, dst):
    INF = float('inf')
    distance = {}
    for i in node:
        distance[i] = INF
    distance[src] = 0
    predecessor = {}
    for i in node:
        predecessor[i] = None

    for i in range(V-1):
        for i in node:
            for j, c in node_dict[i]:
                if distance[j] > distance[i] + c:   # 거리 최소 값으로 변경
                    distance[j] = distance[i] + c
                    predecessor[j] = [i, j, c]
    
    for i in v_dic: # 음의 사이클이 있는 경우
        for j, c in v_dic[i]:
            if distance[j] > distance[i] + c:
                return -1
    
    return predecessor

def main():
    V, E = map(int, input().split())
    node = input().split()
    node_dict = {}

    for i in node:
        node_dict[i] = []

    for _ in range(E):
        i, j, c = input().split()
        v_dic[i].append([j,int(c)])

    src, dst = input().split()
    predecessor = bellman_ford(node_dict, node, V, E, src, dst)

    if predecessor == -1:
        print("Negative Cycle!")
    else:
        prev_list = []
        prev_e = dst

        while prev_e != src:
            prev_list.append(predecessor[prev_e])
            prev_e = predecessor[prev_e][0]

        prev_list.reverse()
    
        for i in prev_list:
         print(*i)

if __name__ == "__main__":
    main()