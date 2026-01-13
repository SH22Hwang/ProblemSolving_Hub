# 방향없는 그래프, 연결요소 개수 구하기
# 딕셔너리로 그래프 구현, deque로 DFS 구현하고 탐색하기  

from collections import deque
import sys
input = sys.stdin.readline


def main():
    node, edge = map(int, input().split())
    node_range = range(1, node+1)
    graph = {i: [] for i in node_range}

    # 그래프 만들기
    for _ in range(edge):
        n, m = map(int, input().split())
        graph[n].append(m)
        graph[m].append(n)

    cnt = 0
    node_list = list(node_range)
    
    while node_list:
        visited = dfs(graph, node_list[0])
        res_set = set(node_list) - set(visited)

        node_list = list(res_set)
        cnt += 1

    print(cnt)

def dfs(graph, start_node):
    visited = []
    to_visit_stack = deque()
    
    ## 시작 노드 설정해주기
    to_visit_stack.append(start_node)
    
    ## 방문이 필요한 리스트가 아직 존재한다면
    while to_visit_stack:
        ## 시작 노드를 지정하고
        node = to_visit_stack.pop()
 
        ##만약 방문한 리스트에 없다면
        if node not in visited:
 
            ## 방문 리스트에 노드를 추가
            visited.append(node)
            ## 인접 노드들을 방문 예정 리스트에 추가
            to_visit_stack.extend(graph[node])
                
    return visited
    


if __name__ == "__main__":
    main()