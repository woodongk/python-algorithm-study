"""
문제
방문원 A는 1에 있는데 K번에 있는 사람과 소개팅을 한다고 한다.
그리고 방문원 A는 X 회사로 가야한다.
즉, 소개팅을 할 K번 회사를 방문 후에 X 회사에 최종 도착해야 한다.
이 때, 총 N개의 도시와 M개의 도로가 주어질 경우 A가 갈 경로의 최단 거리를 구하라


입력

첫째 줄에 전체 회사의 개수 N과 경로의 개수 M이 공백으로 구분되어 차례대로 주어진다(1<= N, M<=100)
둘째 줄부터 M+1 번째 줄에는 연결된 두 회사의 번호가 공백으로 구분되어 주어진다.
M+2번 째 줄에는 X와 K가 공백으로 구분되어 차례대로 주어진다 (1<= K <= 100)

출력
첫째 줄에 방문 판매원 A가 K번 회사를 거쳐 X번 회사로 가는 최소 이동 시간을 출력한다.
만약 X번 회사에 도달할 수 없다면 -1을 출력한다.

입 예
5 7
1 2
1 3
1 4
2 4
3 4
3 5
4 5
4 5
출 예
3

4 2
1 3
2 4
3 4

-1
"""
from collections import deque


def dijkstra(start, distance, visited):
    distance[start] = 0
    visited[start] = True
    queue = deque()
    for v, dist in graph[start]:
        distance[v] = dist
        queue.append(v)
    while queue:
        now = queue.popleft()
        for v, dist in graph[now]:
            distance[v] = min(distance[v],  distance[now] + dist)


if __name__ == '__main__':
    INF = int(1e9)

    n, m = map(int, input().split())

    # 그래프 초기화.
    graph = [[] for i in range(n + 1)]
    for _ in range(m):
        a, b = map(int,input().split())
        graph[a].append((b, 1))
        graph[b].append((a, 1))

    # 1 부터 k 까지의 최단거리
    start = 1
    distance = [INF for _ in range(n + 1)]
    visited = [False] * (n + 1)

    x, k = map(int, input().split())
    dijkstra(start, distance, visited)
    start_to_k = distance[k]

    # k 부터 x 까지의 최단거리
    start = k
    distance = [INF for _ in range(n + 1)]
    visited = [False] * (n + 1)

    dijkstra(start, distance, visited)
    k_to_x = distance[x]

    if start_to_k + k_to_x > INF:
        print(-1)
    else:
        print(start_to_k + k_to_x)



