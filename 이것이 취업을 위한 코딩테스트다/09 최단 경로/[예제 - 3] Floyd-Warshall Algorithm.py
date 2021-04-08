"""
입력
4
7
1 2 4
1 4 6
2 1 3
2 3 7
3 1 5
3 4 4
4 3 2
출력
0 4 8 6
3 0 7 9
5 9 0 4
7 11 2 0
"""

if __name__=='__main__':
    INF = int(1e9)

    n = int(input())
    m = int(input())
    graph = [[INF] * (n + 1) for _ in range(n + 1)]

    # 자기 자신일 경우 비용 0 으로 초기화한다.
    for a in range(1, n + 1):
        for b in range(1, n + 1):
            if a == b :
                graph[a][b] = 0

    # 각 간선에 대한 정보를 입력받아서 그 값으로 그래프 초기화
    for _ in range(m):
        a, b, c = map(int, input().split())
        graph[a][b] = c

    print(graph)

    # 플루이드 워셜 알고리즘 수행
    for k in range(1, n + 1): # k step
        for a in range(1, n + 1):
            for b in range(1, n + 1):
                graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

    for a in range(1, n + 1):
        for b in range(1, n + 1):
            if graph[a][b] == INF:
                print("INFINITY", end=' ')
            else:
                print(graph[a][b], end= ' ')
        print()