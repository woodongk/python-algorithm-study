"""
문제
동빈이는 N * M 크기의 직사각형 미로에 갇혀 있다. 미로에는 여러 마리의 괴물이 있어 이를 피해 탈출해야 한다. 동빈이의 위치는 (1, 1)이고 미로의 출구는 (N, M)의 위치에 존재하며 한 번에 한 칸씩 이동할 수 있다. 이때 괴물이 있는 부분은 0으로, 괴물이 없는 부분은 1로 표시되어 있다. 미로는 반드시 탈출할 수 있는 형태로 제시된다. 이때 동빈이가 탈출하기 위해 움직여야 하는 최소 칸의 개수를 구하시오. 칸을 셀 때는 시작 칸과 마지막 칸을 모두 포함해서 계산한다.

입력

첫째 줄에 두 정수 N, M(4<=N, M <= 200)이 주어집니다.
다음 N개의 줄에는 각각 M개의 정수(0 혹은 1)로 미로의 정보가 주어진다.
각각의 수들은 공백 없이 붙어서 입력으로 제시된다.
또한 시작 칸과 마지막 칸은 항상 1이다.

출력
첫째 줄에 최소 이동 칸의 개수를 출력한다.

예시 입력
5 6
101010
111111
000001
111111
111111
예시 출력
10
"""
import collections


# 최소값 구하기니까 bfs 사용할 것
def bfs(array, node, visited):
    x, y = node
    visited[x][y] = True
    queue = collections.deque([node])

    while queue:
        # 원소 제거하기
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            # 테두리 안 넘어갈 때
            if 0 <= nx <= n and 0 <= ny <= m:
                # 이전에 방문한적 없고, 동시에 괴물이 없을 때
                if not visited[nx][ny] and array[nx][ny] == 1:
                    # 최단 거리 갱신 .. ?
                    array[nx][ny] = array[x][y] + 1

                    # 종점이면 return
                    if nx == n:
                        return array[n][m]

                    #print(nx, ny)
                    queue.append((nx,ny))

    return array[n][m]


if __name__ == '__main__':
    # input 입력받기
    n, m = map(int, input().split())

    array_2d = [[0] * (m + 1)]
    for i in range(n):
        array_2d.append([0] + list(map(int, input())))

    print(array_2d)

    # visited map
    visited = [[False] * (m + 1) for _ in range(n + 1)]

    dx = [1, 0, 0, -1]
    dy = [0, 1, -1, 0]

    # 어차피 엔딩이 무조건 정해져있으므로 좌표 루프 돌지 않음.
    print(bfs(array_2d, (1,1), visited))


