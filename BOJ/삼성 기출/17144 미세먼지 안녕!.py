"""입력
첫째 줄에 R, C, T (6 ≤ R, C ≤ 50, 1 ≤ T ≤ 1,000) 가 주어진다.

둘째 줄부터 R개의 줄에 Ar,c (-1 ≤ Ar,c ≤ 1,000)가 주어진다.
공기청정기가 설치된 곳은 Ar,c가 -1이고, 나머지 값은 미세먼지의 양이다.
-1은 2번 위아래로 붙어져 있고, 가장 윗 행, 아랫 행과 두 칸이상 떨어져 있다.

출력
첫째 줄에 T초가 지난 후 구사과 방에 남아있는 미세먼지의 양을 출력한다.
예제 입력 1
7 8 1
0 0 0 0 0 0 0 9
0 0 0 0 3 0 0 8
-1 0 5 0 0 0 22 0
-1 8 0 0 0 0 0 0
0 0 0 0 0 10 43 0
0 0 5 0 15 0 0 0
0 0 40 0 0 0 20 0
예제 출력 1
188
미세먼지의 확산이 일어나면 다음과 같은 상태가 된다.



공기청정기가 작동한 이후 상태는 아래와 같다.



예제 입력 2
7 8 2
0 0 0 0 0 0 0 9
0 0 0 0 3 0 0 8
-1 0 5 0 0 0 22 0
-1 8 0 0 0 0 0 0
0 0 0 0 0 10 43 0
0 0 5 0 15 0 0 0
0 0 40 0 0 0 20 0
예제 출력 2
188
예제 입력 3
7 8 3
0 0 0 0 0 0 0 9
0 0 0 0 3 0 0 8
-1 0 5 0 0 0 22 0
-1 8 0 0 0 0 0 0
0 0 0 0 0 10 43 0
0 0 5 0 15 0 0 0
0 0 40 0 0 0 20 0
예제 출력 3
186
예제 입력 4
7 8 4
0 0 0 0 0 0 0 9
0 0 0 0 3 0 0 8
-1 0 5 0 0 0 22 0
-1 8 0 0 0 0 0 0
0 0 0 0 0 10 43 0
0 0 5 0 15 0 0 0
0 0 40 0 0 0 20 0
예제 출력 4
178
예제 입력 5
7 8 5
0 0 0 0 0 0 0 9
0 0 0 0 3 0 0 8
-1 0 5 0 0 0 22 0
-1 8 0 0 0 0 0 0
0 0 0 0 0 10 43 0
0 0 5 0 15 0 0 0
0 0 40 0 0 0 20 0
예제 출력 5
172
예제 입력 6
7 8 20
0 0 0 0 0 0 0 9
0 0 0 0 3 0 0 8
-1 0 5 0 0 0 22 0
-1 8 0 0 0 0 0 0
0 0 0 0 0 10 43 0
0 0 5 0 15 0 0 0
0 0 40 0 0 0 20 0
예제 출력 6
71
예제 입력 7
7 8 30
0 0 0 0 0 0 0 9
0 0 0 0 3 0 0 8
-1 0 5 0 0 0 22 0
-1 8 0 0 0 0 0 0
0 0 0 0 0 10 43 0
0 0 5 0 15 0 0 0
0 0 40 0 0 0 20 0
예제 출력 7
52
예제 입력 8
7 8 50
0 0 0 0 0 0 0 9
0 0 0 0 3 0 0 8
-1 0 5 0 0 0 22 0
-1 8 0 0 0 0 0 0
0 0 0 0 0 10 43 0
0 0 5 0 15 0 0 0
0 0 40 0 0 0 20 0
예제 출력 8
46

"""
import copy


def spread():
    for i in range(r):
        for j in range(c):
            if maps[i][j] >= 5:
                dirt = maps[i][j] // 5

                for k in range(4):
                    nx = i + dx[k]
                    ny = j + dy[k]

                    if 0 <= nx < r and 0 <= ny < c:  # 범위 벗어나지 않으면
                        if tmp[nx][ny] != -1:  # 공기 청정기 없으면
                            tmp[nx][ny] += dirt
                            tmp[i][j] -= dirt


def clean():
    # up
    x, y = cleaners[0]

    # 오른쪽 방향
    v1 = tmp[x][c - 1] # keep value for 다음 방향
    for i in range(c - 2, 0, -1):
        tmp[x][i + 1] = tmp[x][i]

    # 위쪽 방향
    v2 = tmp[0][c - 1]
    for i in range(x - 1):
        tmp[i][c - 1] = tmp[i + 1][c - 1]
    tmp[x - 1][c - 1] = v1

    # 왼쪽 방향
    v3 = tmp[0][0]
    for i in range(c - 1):
        tmp[0][i] = tmp[0][i + 1]
    tmp[0][c - 2] = v2

    # 아래 방향
    for i in range(x - 1, 1, -1):
        tmp[i][0] = tmp[i - 1][0]
    tmp[x][1] = 0  # 미세먼지 후륵
    tmp[1][0] = v3

    # down
    x, y = cleaners[1]

    # 오른쪽 방향
    v1 = tmp[x][c - 1]
    for i in range(c - 2, 0, -1):
        tmp[x][i + 1] = tmp[x][i]

    # 아래 방향
    v2 = tmp[r - 1][c - 1]
    for i in range(r - 1, x, -1):
        tmp[i][c - 1] = tmp[i - 1][c - 1]
    tmp[x + 1][c - 1] = v1

    # 왼쪽 방향
    v3 = tmp[r - 1][0]
    for i in range(c - 1):
        tmp[r - 1][i] = tmp[r - 1][i + 1]
    tmp[r - 1][c - 2] = v2

    # 위쪽 방향
    for i in range(x + 1, r - 1):
        tmp[i][0] = tmp[i + 1][0]
    tmp[x][1] = 0
    tmp[r - 2][0] = v3

import sys
input = sys.stdin.readline

if __name__ == '__main__':
    # 입력값 받기
    r, c, t = map(int, input().split())

    maps = []
    for _ in range(r):
        rows = list(map(int, input().split()))
        maps.append(rows)

    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]

    # 공기 청정기 위치 찾기
    cleaners = []
    for i in range(r): # 공기청정기는 1열에만 존재한다
        if maps[i][0] == -1:
            cleaners.append((i, 0)) # 앞에꺼가 위, 뒤에꺼가 아래

    # t초 만큼 돌리기
    for _ in range(t):
        # 딥카피해서 루프마다 원본 손상 없게 하기
        tmp = copy.deepcopy(maps)
        spread()  # 미세먼지 확산 함수
        clean() # 미세먼지 제거 함
        maps = copy.deepcopy(tmp)

    s = 0
    for dirt in maps:
        s += sum(dirt)

    print(s + 2)



