import heapq


def dijkstra(start, distance, graph):
    q = []
    # 시작 노드의 최단 경로는 0으로 설정하고 큐에 삽입한다.
    heapq.heappush(q, (0, start))
    distance[start] = 0

    while q:  # 큐가 비게 될 때까지 루프
        dist, now = heapq.heappop(q)
        print("dist is {} now is {}".format(dist, now))
        if distance[now] < dist:
            continue
        # 최단 거리 갱신하기
        for i in graph[now]:  # now node, now cost
            cost = dist + i[1]
            if distance[i[0]] > cost:
                distance[i[0]] = cost
                # 힙에도 넣어준다.
                heapq.heappush(q, (cost, i[0]))


def solution(n, s, a, b, fares):
    # graph
    graph = [[] for i in range(n + 1)]
    # 최단 거리 테이블
    distance = [INF] * (n + 1)

    for fare in fares:
        # a -> b : cost c
        x, y, c = fare
        graph[x].append((y, c))
        graph[y].append((x, c))

    dijkstra(s, distance, graph)

    min_fares = []

    for i in range(1, n + 1):
        min_fare = 0

        # A와 B의 공통 거리
        # if distance[i] == INF:
        #     print("INFINITY")
        # else:
        #     print("{}부터 {}까지의 최단경로 : {}".format(s, i, distance[i]))
        min_fare += distance[i]

        # 최단 거리 테이블
        a_distance = b_distance = [INF] * (n + 1)

        # 도착점부터 A까지의 최단경로 갱신
        dijkstra(i, a_distance, graph)
        min_fare += a_distance[a]

        # 도착점부터 B까지의 최단경로 갱신
        dijkstra(i, b_distance, graph)
        min_fare += b_distance[b]

        min_fares.append(min_fare)

    return min(min_fares)


INF = int(1e9)

if __name__ == '__main__':
    n = 6
    s = 4
    a = 6
    b = 2
    fares = [[4, 1, 10],
             [3, 5, 24],
             [5, 6, 2],
             [3, 1, 41],
             [5, 1, 24],
             [4, 6, 50],
             [2, 4, 66],
             [2, 3, 22],
             [1, 6, 25]]

    print(solution(n, s, a, b, fares))
