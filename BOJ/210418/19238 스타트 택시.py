"""
스타트 택시 분류
시간 제한	메모리 제한	제출	정답	맞은 사람	정답 비율
1 초 (추가 시간 없음)	512 MB	11867	2588	1517	19.278%
문제
스타트링크가 "스타트 택시"라는 이름의 택시 사업을 시작했다. 스타트 택시는 특이하게도 손님을 도착지로 데려다줄 때마다 연료가 충전되고, 연료가 바닥나면 그 날의 업무가 끝난다.

택시 기사 최백준은 오늘 M명의 승객을 태우는 것이 목표이다. 백준이 활동할 영역은 N×N 크기의 격자로 나타낼 수 있고, 각 칸은 비어 있거나 벽이 놓여 있다. 택시가 빈칸에 있을 때, 상하좌우로 인접한 빈칸 중 하나로 이동할 수 있다. 알고리즘 경력이 많은 백준은 특정 위치로 이동할 때 항상 최단경로로만 이동한다.

M명의 승객은 빈칸 중 하나에 서 있으며, 다른 빈칸 중 하나로 이동하려고 한다. 여러 승객이 같이 탑승하는 경우는 없다. 따라서 백준은 한 승객을 태워 목적지로 이동시키는 일을 M번 반복해야 한다. 각 승객은 스스로 움직이지 않으며, 출발지에서만 택시에 탈 수 있고, 목적지에서만 택시에서 내릴 수 있다.

백준이 태울 승객을 고를 때는 현재 위치에서 최단거리가 가장 짧은 승객을 고른다. 그런 승객이 여러 명이면 그중 행 번호가 가장 작은 승객을, 그런 승객도 여러 명이면 그중 열 번호가 가장 작은 승객을 고른다. 택시와 승객이 같은 위치에 서 있으면 그 승객까지의 최단거리는 0이다. 연료는 한 칸 이동할 때마다 1만큼 소모된다. 한 승객을 목적지로 성공적으로 이동시키면, 그 승객을 태워 이동하면서 소모한 연료 양의 두 배가 충전된다. 이동하는 도중에 연료가 바닥나면 이동에 실패하고, 그 날의 업무가 끝난다. 승객을 목적지로 이동시킨 동시에 연료가 바닥나는 경우는 실패한 것으로 간주하지 않는다.



<그림 1>

<그림 1>은 택시가 활동할 영역의 지도를 나타내며, 택시와 세 명의 승객의 출발지와 목적지가 표시되어 있다. 택시의 현재 연료 양은 15이다. 현재 택시에서 각 손님까지의 최단거리는 각각 9, 6, 7이므로, 택시는 2번 승객의 출발지로 이동한다.



<그림 2>



<그림 3>

<그림 2>는 택시가 2번 승객의 출발지로 가는 경로를, <그림 3>은 2번 승객의 출발지에서 목적지로 가는 경로를 나타낸다. 목적지로 이동할 때까지 소비한 연료는 6이고, 이동하고 나서 12가 충전되므로 남은 연료의 양은 15이다. 이제 택시에서 각 손님까지의 최단거리는 둘 다 7이므로, 택시는 둘 중 행 번호가 더 작은 1번 승객의 출발지로 이동한다.



<그림 4>



<그림 5>

<그림 4>와 <그림 5>는 택시가 1번 승객을 태워 목적지로 이동시키는 경로를 나타낸다. 남은 연료의 양은 15 - 7 - 7 + 7×2 = 15이다.



<그림 6>



<그림 7>

<그림 6>과 <그림 7>은 택시가 3번 승객을 태워 목적지로 이동시키는 경로를 나타낸다. 최종적으로 남은 연료의 양은 15 - 5 - 4 + 4×2 = 14이다.

모든 승객을 성공적으로 데려다줄 수 있는지 알아내고, 데려다줄 수 있을 경우 최종적으로 남는 연료의 양을 출력하는 프로그램을 작성하시오.

입력
첫 줄에 N, M, 그리고 초기 연료의 양이 주어진다. (2 ≤ N ≤ 20, 1 ≤ M ≤ N2, 1 ≤ 초기 연료 ≤ 500,000) 연료는 무한히 많이 담을 수 있기 때문에, 초기 연료의 양을 넘어서 충전될 수도 있다.

다음 줄부터 N개의 줄에 걸쳐 백준이 활동할 영역의 지도가 주어진다. 0은 빈칸, 1은 벽을 나타낸다.

다음 줄에는 백준이 운전을 시작하는 칸의 행 번호와 열 번호가 주어진다. 행과 열 번호는 1 이상 N 이하의 자연수이고, 운전을 시작하는 칸은 빈칸이다.

그다음 줄부터 M개의 줄에 걸쳐 각 승객의 출발지의 행과 열 번호, 그리고 목적지의 행과 열 번호가 주어진다. 모든 출발지와 목적지는 빈칸이고, 모든 출발지는 서로 다르며, 각 손님의 출발지와 목적지는 다르다.

출력
모든 손님을 이동시키고 연료를 충전했을 때 남은 연료의 양을 출력한다. 단, 이동 도중에 연료가 바닥나서 다음 출발지나 목적지로 이동할 수 없으면 -1을 출력한다. 모든 손님을 이동시킬 수 없는 경우에도 -1을 출력한다.

예제 입력 1
6 3 15
0 0 1 0 0 0
0 0 1 0 0 0
0 0 0 0 0 0
0 0 0 0 0 0
0 0 0 0 1 0
0 0 0 1 0 0
6 5
2 2 5 6
5 4 1 6
4 2 3 5
예제 출력 1
14
예제 입력 2
6 3 13
0 0 1 0 0 0
0 0 1 0 0 0
0 0 0 0 0 0
0 0 0 0 0 0
0 0 0 0 1 0
0 0 0 1 0 0
6 5
2 2 5 6
5 4 1 6
4 2 3 5
예제 출력 2
-1
예제 입력 3
6 3 100
0 0 1 0 0 0
0 0 1 0 0 0
0 0 0 1 0 0
0 0 0 1 0 0
0 0 0 0 1 0
0 0 0 1 0 0
6 5
2 2 5 6
5 4 1 6
4 2 3 5
예제 출력 3
-1
"""
import collections

INF = 1e9


def bfs(start, target, visited):
    tx, ty = target
    dist_maps = [[0] * n for _ in range(n)]
    visited = [[False] * n for _ in range(n)]

    queue = collections.deque([start])

    while queue:
        x, y = queue.popleft()
        visited[x][y] = True
        print((x,y))

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            # 범위 밖 방문 x 갈수없는길
            if 0 <= nx < n and 0 <= ny < n:
                if maps[nx][ny] != 1 and not visited[nx][ny]:
                    queue.append((nx, ny))
                    dist_maps[nx][ny] = dist_maps[x][y] + 1

        if visited[tx][ty]:
            for d in dist_maps:
                print(d)
            return dist_maps[tx][ty]


if __name__ == '__main__':
    n, m, gas = map(int, input().split())
    maps = []
    for i in range(n):
        rows = list(map(int, input().split()))
        maps.append(rows)

    start_x, start_y = map(int, input().split())

    people = []
    for i in range(m):
        sx, sy, tx, ty = map(int, input().split())
        people.append((sx, sy, tx, ty))
    print(people)

    # 최단 경로 구하기 ! 가장 중요
    # start -> target 까지 전체 distance map 계산
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]


    print(bfs((4,5), (3,4), visited))



    # 이후 시뮬레이션

