"""
문제
상근이는 어렸을 적에 "봄보니 (Bomboni)" 게임을 즐겨했다.

가장 처음에 N×N크기에 사탕을 채워 놓는다. 사탕의 색은 모두 같지 않을 수도 있다.
상근이는 사탕의 색이 다른 인접한 두 칸을 고른다. 그 다음 고른 칸에 들어있는 사탕을 서로 교환한다.
이제, 모두 같은 색으로 이루어져 있는 가장 긴 연속 부분(행 또는 열)을 고른 다음 그 사탕을 모두 먹는다.

사탕이 채워진 상태가 주어졌을 때, 상근이가 먹을 수 있는 사탕의 최대 개수를 구하는 프로그램을 작성하시오.

입력
첫째 줄에 보드의 크기 N이 주어진다. (3 ≤ N ≤ 50)

다음 N개 줄에는 보드에 채워져 있는 사탕의 색상이 주어진다. 빨간색은 C, 파란색은 P, 초록색은 Z, 노란색은 Y로 주어진다.

사탕의 색이 다른 인접한 두 칸이 존재하는 입력만 주어진다.

출력
첫째 줄에 상근이가 먹을 수 있는 사탕의 최대 개수를 출력한다.

예제 입력 1
5
YCPZY
CYZZP
CCPPP
YCYZC
CPPZZ
"""


# di = 0 오른쪽 보기 di = 1 아래쪽 보기
def dfs(check_steps, array, node, visited):
    global cnt

    x, y = node
    visited[x][y] = True

    for step in check_steps:
        nx = x + step[0]
        ny = y + step[1]

        # 테두리 밖 안나가고 방문 하기 전 일 때
        if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny]:
            # 색깔이 같은 값일 경우! 방문
            if array[x][y] == array[nx][ny]:
                cnt += 1
                dfs(check_steps, array, (nx, ny), visited)


if __name__ == '__main__':

    n = int(input())

    maps = []
    for _ in range(n):
        rows = list(input())
        maps.append(rows)

    visited = [([False] * n) for _ in range(n)]

    # 일직선만 이동 가능
    # 오른쪽하고 아래 방향만 고려
    check_rows = [(1, 0), (-1, 0)]
    check_cols = [(0, 1), (0, -1)]
    cnt = 1

    cnt_lst = []

    for i in range(n):
        for j in range(n):
            # 오른쪽 노드랑 다르면 위치 바꾸기
            if (0 <= j + 1 < n) and (maps[i][j] != maps[i][j + 1]):
                maps[i][j], maps[i][j + 1] = maps[i][j + 1], maps[i][j]

                for check_steps in [check_cols, check_rows]:
                    cnt = 1
                    visited = [([False] * n) for _ in range(n)]
                    dfs(check_steps, maps, (i, j), visited)
                    cnt_lst.append(cnt)

                    cnt = 1
                    visited = [([False] * n) for _ in range(n)]
                    dfs(check_steps, maps, (i, j + 1), visited)
                    cnt_lst.append(cnt)

                # 원상 복귀
                maps[i][j], maps[i][j + 1] = maps[i][j + 1], maps[i][j]

            # 아래 노드랑 다르면 위치 바꾸기
            if (0 <= i + 1 < n) and (maps[i][j] != maps[i + 1][j]):
                maps[i][j], maps[i + 1][j] = maps[i + 1][j], maps[i][j]

                for check_steps in [check_cols, check_rows]:
                    cnt = 1
                    visited = [([False] * n) for _ in range(n)]
                    dfs(check_steps, maps, (i, j), visited)
                    cnt_lst.append(cnt)

                    cnt = 1
                    visited = [([False] * n) for _ in range(n)]
                    dfs(check_steps, maps, (i + 1, j), visited)
                    cnt_lst.append(cnt)

                # 원상 복귀
                maps[i][j], maps[i + 1][j] = maps[i + 1][j], maps[i][j]

    print(max(cnt_lst))

