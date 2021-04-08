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
import heapq
import sys
input = sys.stdin.readline
INF = int(1e9)


def dijkstra(start, distance, visited):
    q = []
    # 시작 노드의 최단 경로는 0으로 설정하고 큐에 삽입한다.
    heapq.heappush(q, (0, start))
    distance[start] = 0

    while q: # 큐가 비게 될 때까지 루프
        # 가장 최우선 (최단) 노드 꺼내기
        dist, now = heapq.heappop(q)
        # 노드가 이미 처리된 적 있는 노드라면 무시한다.
        if distance[now] < dist:
            continue
        # 최단 거리 갱신하기
        for i in graph[now]: # now node, now cost
            # 현재 노드 거쳐서 다른 노드 이동하는 거리 짧다면 바꿔치기
            cost = dist + i[1]
            if distance[i[0]] > cost:
                distance[i[0]] = cost
                # 힙에도 넣어준다.
                heapq.heappush(q, (cost, i[0]))


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
