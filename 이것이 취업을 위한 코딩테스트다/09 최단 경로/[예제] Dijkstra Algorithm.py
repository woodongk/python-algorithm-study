"""
입력
6 11
1
1 2 2
1 3 5
1 4 1
2 3 3
2 4 2
3 2 3
3 6 5
4 3 3
4 5 1
5 3 1
5 6 2
출력
0
2
3
1
2
4
"""

import sys
input = sys.stdin.readline
INF = int(1e9)

# 방문하지 않은 노드 중에서 최단 거리 노드 반환
def get_smallest_node(distance, visited):
    min_value = INF
    index = 0 # 최단 노드 인덱스
    for i in range(1, n + 1):
        if distance[i] < min_value and not visited[i]:
            min_value = distance[i]
            index = i
    return index


def dijkstra(start, distance, visited):
    # 시작 노드 0 최단 거리로 시작
    distance[start] = 0
    visited[start] = True
    # 시작 노드에 대해서 가리키고 있는 노드들의 비용 갱신
    for v, cost in graph[start]:
        distance[v] = cost
    # 나머지 노드에 대해서 최단 거리 구하기
    for i in range(n - 1):
        # 최단 거리 가장 짧은 노드 꺼내고 방문 처리해준다.
        now = get_smallest_node(distance, visited)
        visited[now] = True
        for v, cost in graph[now]:
            # 현재 노드 거쳐서 다른 노드 이동 거리가 짧은 경우 갱신.
            distance[v] = min(distance[now] + cost, distance[v])


if __name__ == '__main__':
    # 노드 개수, 간선 개수
    n, m = map(int, input().split())
    # 시작 노드
    start = int(input())
    # graph
    graph = [[] for i in range(n + 1)]
    # 방문 경로 체크 리스트
    visited = [False] * (n + 1)
    # 최단 거리 테이블
    distance = [INF] * (n + 1)

    for _ in range(m):
        # a -> b : cost c
        a, b, c = map(int, input().split())
        graph[a].append((b, c))

    print(graph)

    dijkstra(start, distance, visited)

    for i in range(1, n + 1):
        if distance[i] == INF:
            print("INFINITY")
        else:
            print("{}부터 {}까지의 최단경로 : {}".format(start, i, distance[i]))
