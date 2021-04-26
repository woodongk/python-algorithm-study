"""
5
100 200 300 400 200
300 243 432 334 555
999 111 0 999 333
888 777 222 333 900
100 200 300 400 500

10
"""
import collections


def search(start):
    x, y = start
    visited = [[False] * n for _ in range(n)]
    visited[x][y] = True
    paths = [(x, y)]

    i = 0 # 방향 관리 변수

    # 현재 방향에서 한차례 이동
    nx = x + dx[i]
    ny = y + dy[i]

    while True:

        i = i % 4
        # 방문하지 않은 곳이라면, 이동 성공
        if not visited[nx][ny]:
            visited[nx][ny] = True

            # 새로운 좌표로 업데이트 하고 다시 시작
            x, y = nx, ny
            i += 1
        # 방문한 곳이라면 이동이 가능할 때 까지 이전 스테이트 반복
        else:
            while not visited[nx][ny]:
                nx = nx + dx[i]
                ny = ny + dy[i]
                visited[nx][ny] = True

        if nx == 0 and ny == 0:
            break


if __name__ == '__main__':
    n = int(input())

    x = y = int(n / 2) # 스타트 시작

    maps = []
    for _ in range(n):
        maps.append(list(map(int, input().split())))

    # 확률표 입력 받기
    prop_map = [[0] * n for _ in range(n)]
    prop_map[x][y - 2] = 2
    prop_map[x + 1][y] = prop_map[x - 1][y] = 7
    prop_map[x + 1][y - 1] = prop_map[x - 1][y - 1] = 10
    prop_map[x + 1][y + 1] = prop_map[x - 1][y + 1] = 1
    prop_map[x + 2][y] = prop_map[x - 2][y] = 2
    print(prop_map)

    # 왼쪽 아래 오른쪽 위
    dx = [0, 1, 0, -1]
    dy = [-1, 0, 1, 0]




