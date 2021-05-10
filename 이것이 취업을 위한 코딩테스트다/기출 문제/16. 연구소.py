"""
예제 입력 1
7 7
2 0 0 0 1 1 0
0 0 1 0 1 2 0
0 1 1 0 1 0 0
0 1 0 0 0 0 0
0 0 0 0 0 1 1
0 1 0 0 0 0 0
0 1 0 0 0 0 0
예제 출력 1
27
예제 입력 2
4 6
0 0 0 0 0 0
1 0 0 0 0 2
1 1 1 0 0 2
0 0 0 0 0 2
예제 출력 2
9
예제 입력 3
8 8
2 0 0 0 0 0 0 2
2 0 0 0 0 0 0 2
2 0 0 0 0 0 0 2
2 0 0 0 0 0 0 2
2 0 0 0 0 0 0 2
0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0
예제 출력 3
3
"""

import itertools
import copy
import sys
input = sys.stdin.readline


def dfs(start, graph, visited):
    x, y = start
    visited[x][y] = True

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]


        if 0 <= nx < n and 0 <= ny < m: # 범위 내부
            if (not visited[nx][ny]) and (graph[nx][ny] == 0): # 빈칸일 때만 진입
                visited[nx][ny] = True
                graph[nx][ny] = 2 # 바이러스 전염
                dfs((nx, ny), graph, visited)


if __name__ == '__main__':
    # 초기값 받기
    n, m = map(int, input().split())
    maps = []
    for _ in range(n):
        maps.append(list(map(int, input().split())))

    # 모든 0의 위치 구하기
    empty = []
    for i in range(n):
        for j in range(m):
            if maps[i][j] == 0:
                empty.append((i, j))

    # 모든 0의 위치 combination 3 곳 구하기
    wall_candidate = list(itertools.combinations(empty, 3))

    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]

    # 후보 세곳 체크하면서 순회하기
    max_safe_zone = 0
    for a, b, c in wall_candidate:
        tmp = copy.deepcopy(maps)
        tmp[a[0]][a[1]] = 1
        tmp[b[0]][b[1]] = 1
        tmp[c[0]][c[1]] = 1

        # 바이러스 전염
        visited = [[False] * m for _ in range(n)]
        for i in range(n):
            for j in range(m):
                if tmp[i][j] == 2:
                    dfs((i, j), tmp, visited)

        # 남은 안전 영역
        safe_zone = sum(x.count(0) for x in tmp)
        if max_safe_zone <= safe_zone:
            max_safe_zone = safe_zone

    print(max_safe_zone)