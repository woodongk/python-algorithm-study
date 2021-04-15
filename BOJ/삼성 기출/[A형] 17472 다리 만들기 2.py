"""
다리 만들기 2 분류
시간 제한	메모리 제한	제출	정답	맞은 사람	정답 비율
1 초	512 MB	11361	3800	2171	29.204%
문제
섬으로 이루어진 나라가 있고, 모든 섬을 다리로 연결하려고 한다. 이 나라의 지도는 N×M 크기의 이차원 격자로 나타낼 수 있고, 격자의 각 칸은 땅이거나 바다이다.

섬은 연결된 땅이 상하좌우로 붙어있는 덩어리를 말하고, 아래 그림은 네 개의 섬으로 이루어진 나라이다. 색칠되어있는 칸은 땅이다.



다리는 바다에만 건설할 수 있고, 다리의 길이는 다리가 격자에서 차지하는 칸의 수이다. 다리를 연결해서 모든 섬을 연결하려고 한다. 섬 A에서 다리를 통해 섬 B로 갈 수 있을 때, 섬 A와 B를 연결되었다고 한다. 다리의 양 끝은 섬과 인접한 바다 위에 있어야 하고, 한 다리의 방향이 중간에 바뀌면 안된다. 또, 다리의 길이는 2 이상이어야 한다.

다리의 방향이 중간에 바뀌면 안되기 때문에, 다리의 방향은 가로 또는 세로가 될 수 밖에 없다. 방향이 가로인 다리는 다리의 양 끝이 가로 방향으로 섬과 인접해야 하고, 방향이 세로인 다리는 다리의 양 끝이 세로 방향으로 섬과 인접해야 한다.

섬 A와 B를 연결하는 다리가 중간에 섬 C와 인접한 바다를 지나가는 경우에 섬 C는 A, B와 연결되어있는 것이 아니다.

아래 그림은 섬을 모두 연결하는 올바른 2가지 방법이고, 다리는 회색으로 색칠되어 있다. 섬은 정수, 다리는 알파벳 대문자로 구분했다.


다리의 총 길이: 13

D는 2와 4를 연결하는 다리이고, 3과는 연결되어 있지 않다.

다리의 총 길이: 9 (최소)

다음은 올바르지 않은 3가지 방법이다


C의 방향이 중간에 바뀌었다	D의 길이가 1이다.	가로 다리인 A가 1과 가로로 연결되어 있지 않다.
다리가 교차하는 경우가 있을 수도 있다. 교차하는 다리의 길이를 계산할 때는 각 칸이 각 다리의 길이에 모두 포함되어야 한다. 아래는 다리가 교차하는 경우와 기타 다른 경우에 대한 2가지 예시이다.


A의 길이는 4이고, B의 길이도 4이다.

총 다리의 총 길이: 4 + 4 + 2 = 10

다리 A: 2와 3을 연결 (길이 2)

다리 B: 3과 4를 연결 (길이 3)

다리 C: 2와 5를 연결 (길이 5)

다리 D: 1과 2를 연결 (길이 2)

총 길이: 12

나라의 정보가 주어졌을 때, 모든 섬을 연결하는 다리 길이의 최솟값을 구해보자.

입력
첫째 줄에 지도의 세로 크기 N과 가로 크기 M이 주어진다. 둘째 줄부터 N개의 줄에 지도의 정보가 주어진다. 각 줄은 M개의 수로 이루어져 있으며, 수는 0 또는 1이다. 0은 바다, 1은 땅을 의미한다.

출력
모든 섬을 연결하는 다리 길이의 최솟값을 출력한다. 모든 섬을 연결하는 것이 불가능하면 -1을 출력한다.

제한
1 ≤ N, M ≤ 10
3 ≤ N×M ≤ 100
2 ≤ 섬의 개수 ≤ 6
예제 입력 1
7 8
0 0 0 0 0 0 1 1
1 1 0 0 0 0 1 1
1 1 0 0 0 0 0 0
1 1 0 0 0 1 1 0
0 0 0 0 0 1 1 0
0 0 0 0 0 0 0 0
1 1 1 1 1 1 1 1
예제 출력 1
9
예제 입력 2
7 8
0 0 0 1 1 0 0 0
0 0 0 1 1 0 0 0
1 1 0 0 0 0 1 1
1 1 0 0 0 0 1 1
1 1 0 0 0 0 0 0
0 0 0 0 0 0 0 0
1 1 1 1 1 1 1 1
예제 출력 2
10
예제 입력 3
7 8
1 0 0 1 1 1 0 0
0 0 1 0 0 0 1 1
0 0 1 0 0 0 1 1
0 0 1 1 1 0 0 0
0 0 0 0 0 0 0 0
0 1 1 1 0 0 0 0
1 1 1 1 1 1 0 0
예제 출력 3
9
예제 입력 4
7 7
1 1 1 0 1 1 1
1 1 1 0 1 1 1
1 1 1 0 1 1 1
0 0 0 0 0 0 0
1 1 1 0 1 1 1
1 1 1 0 1 1 1
1 1 1 0 1 1 1
-1
"""
import collections
import copy


# 인근의 섬은 하나의 큐에 넣어버린다.
def bfs(maps, node, visited):
    x, y = node
    queue = collections.deque([(x, y)])
    visited[x][y] = True
    island = [(x, y)]

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < m:
                if not visited[nx][ny] and maps[nx][ny] == 1:
                    queue.append((nx, ny))
                    visited[nx][ny] = True
                    island.append((nx, ny))
    return island


if __name__ == '__main__':

    # 입력값 초기화하기
    n, m = map(int, input().split())

    maps = []
    for i in range(n):
        rows = list(map(int, input().split()))
        maps.append(rows)

    visited = [[False] * m for _ in range(n)]
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]
    INF = 1e9

    # 각각의 섬마다 좌표 노드를 리스트로 넣는 코드
    islands = []
    for i in range(n):
        for j in range(m):
            if maps[i][j] == 1 and not visited[i][j]:
                islands.append(bfs(maps, (i, j), visited))

    print(islands)
    print(len(islands))

    # 각 섬마다의 최소 거리 구하는 코드
    # 주의) 1. 2칸 이상, 2. 일직선
    min_dist_bridges = []  # 섬I, 섬J, 거리
    for i in range(len(islands)):
        for j in range(i + 1, len(islands)):
            a = islands[i]
            b = islands[j]
            dist = []

            # 각 좌표마다 칸 계산하기
            for ax, ay in a:
                for bx, by in b:
                    if ax == bx:  # 가로
                        if abs(ay - by) >= 2:  # 2칸 제약 사항
                            dist.append(abs(ay - by))

                    if ay == by:  # 세로
                        if abs(ax - bx) >= 2:  # 2칸 제약 사항
                            dist.append(abs(ax - bx))
            print("썸!", i, j, dist)
            if dist:
                min_dist_bridges.append((i, j, min(dist)))  # 섬I, 섬J, 최소거리
            else:
                min_dist_bridges.append((i, j, INF))

    min_dist_bridges = sorted(min_dist_bridges, key=lambda x: x[2], reverse=True)
    print(min_dist_bridges)

    # 각각의 섬마다 최소거리 노드 구한 뒤로는 visited 리스트 만들어서 노드 채우기
    #### 1!!! 어케하지
    visited = [False] * len(islands)
    sum_dist = 0
    while min_dist_bridges:
        i, j, dist = min_dist_bridges.pop()
        print(i,j, dist)
        if dist < INF and not visited[i] and not visited[j]:
            visited[i] = True
            visited[j] = True
            sum_dist += dist

        # visited 다 채워지면 break
        if [i for i in visited if i == False] is None:
            break

    print(sum_dist)