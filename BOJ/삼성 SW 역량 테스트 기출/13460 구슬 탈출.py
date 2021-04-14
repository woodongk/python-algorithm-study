"""
문제
스타트링크에서 판매하는 어린이용 장난감 중에서 가장 인기가 많은 제품은 구슬 탈출이다.
구슬 탈출은 직사각형 보드에 빨간 구슬과 파란 구슬을 하나씩 넣은 다음, 빨간 구슬을 구멍을 통해 빼내는 게임이다.

보드의 세로 크기는 N, 가로 크기는 M이고, 편의상 1×1크기의 칸으로 나누어져 있다.
가장 바깥 행과 열은 모두 막혀져 있고, 보드에는 구멍이 하나 있다.
빨간 구슬과 파란 구슬의 크기는 보드에서 1×1크기의 칸을 가득 채우는 사이즈이고, 각각 하나씩 들어가 있다.
게임의 목표는 빨간 구슬을 구멍을 통해서 빼내는 것이다. 이때, 파란 구슬이 구멍에 들어가면 안 된다.

이때, 구슬을 손으로 건드릴 수는 없고, 중력을 이용해서 이리 저리 굴려야 한다.
왼쪽으로 기울이기, 오른쪽으로 기울이기, 위쪽으로 기울이기, 아래쪽으로 기울이기와 같은 네 가지 동작이 가능하다.

각각의 동작에서 공은 동시에 움직인다. 빨간 구슬이 구멍에 빠지면 성공이지만, 파란 구슬이 구멍에 빠지면 실패이다.
빨간 구슬과 파란 구슬이 동시에 구멍에 빠져도 실패이다. 빨간 구슬과 파란 구슬은 동시에 같은 칸에 있을 수 없다.
또, 빨간 구슬과 파란 구슬의 크기는 한 칸을 모두 차지한다. 기울이는 동작을 그만하는 것은 더 이상 구슬이 움직이지 않을 때 까지이다.

보드의 상태가 주어졌을 때, 최소 몇 번 만에 빨간 구슬을 구멍을 통해 빼낼 수 있는지 구하는 프로그램을 작성하시오.

입력
첫 번째 줄에는 보드의 세로, 가로 크기를 의미하는 두 정수 N, M (3 ≤ N, M ≤ 10)이 주어진다.
다음 N개의 줄에 보드의 모양을 나타내는 길이 M의 문자열이 주어진다.
이 문자열은 '.', '#', 'O', 'R', 'B' 로 이루어져 있다.
'.'은 빈 칸을 의미하고, '#'은 공이 이동할 수 없는 장애물 또는 벽을 의미하며, 'O'는 구멍의 위치를 의미한다.
'R'은 빨간 구슬의 위치, 'B'는 파란 구슬의 위치이다.

입력되는 모든 보드의 가장자리에는 모두 '#'이 있다. 구멍의 개수는 한 개 이며, 빨간 구슬과 파란 구슬은 항상 1개가 주어진다.

출력
최소 몇 번 만에 빨간 구슬을 구멍을 통해 빼낼 수 있는지 출력한다. 만약, 10번 이하로 움직여서 빨간 구슬을 구멍을 통해 빼낼 수 없으면 -1을 출력한다.

예제 입력 1
5 5
#####
#..B#
#.#.#
#RO.#
#####
예제 출력 1
1
예제 입력 2
7 7
#######
#...RB#
#.#####
#.....#
#####.#
#O....#
#######
예제 출력 2
5
예제 입력 3
7 7
#######
#..R#B#
#.#####
#.....#
#####.#
#O....#
#######
예제 출력 3
5
예제 입력 4
10 10
##########
#R#...##B#
#...#.##.#
#####.##.#
#......#.#
#.######.#
#.#....#.#
#.#.#.#..#
#...#.O#.#
##########
예제 출력 4
-1
예제 입력 5
3 7
#######
#R.O.B#
#######
예제 출력 5
1
예제 입력 6
10 10
##########
#R#...##B#
#...#.##.#
#####.##.#
#......#.#
#.######.#
#.#....#.#
#.#.##...#
#O..#....#
##########
예제 출력 6
7
예제 입력 7
3 10
##########
#.O....RB#
##########
"""


def move(x, y, di):
    check = 0 # 2개 구슬 겹쳤을 경우 이동 경로 많은 구슬의 칸을 하나 줄임
    while maps[x + dx[di]][y + dy[di]] != '#' and maps[x][y] != "O":
        x += dx[di]
        y += dy[di]
        check += 1
    return x, y, check


def init():
    # R이랑 B랑 구멍 위치 찾기
    for i in range(n):
        for j in range(m):
            if maps[i][j] == "R": # 만약 R을 만나면 저장
                rx, ry = i, j
            elif maps[i][j] == "B": # 만약 B를 만나면 저장
                bx, by = i, j

    #print(rx, ry, bx, by)

    q.append((rx, ry, bx, by, 1))  # 위치 정보와 cnt 넣기
    visited[rx][ry][bx][by] = True


def bfs(maps, visited):
    init()  # R과 B 값 업데이트, visited 업데이트

    while q:
        rx, ry, bx, by, cnt = q.popleft()

        if cnt > 10: # 10을 넘으면 실패.
            break

        for di in range(4):
            nrx, nry, r_check = move(rx, ry, di)
            nbx, nby, b_check = move(bx, by, di)

            #print("count : ", cnt, "direction : ", dx[di], dy[di], 'RED', nrx, nry, 'BLUE', nbx, nby)

            if maps[nbx][nby] == "O": # 파란 구슬이 구멍에 떨어졌음 실패
                continue

            if maps[nrx][nry] == "O": # 빨간 구슬이 구멍에 떨어진다면 성공
                return cnt

            if nrx == nbx and nry == nby: # 둘의 위치가 겹친다면
                if r_check > b_check: # 이동거리가 많은 구슬을 한칸 역 이동시켜주기
                    nrx -= dx[di]
                    nry -= dy[di]
                else:
                    nbx -= dx[di]
                    nby -= dy[di]

            # BFS 탐색을 마치고, 방문 여부 확인해줌 .
            if not visited[nrx][nry][nbx][nby]:
                visited[nrx][nry][nbx][nby] = True
                q.append((nrx, nry, nbx, nby, cnt + 1))

    return -1


import collections

if __name__ == '__main__':
    # 입력값 받는 곳
    n, m = map(int, input().split())

    maps = []
    for _ in range(n):
        rows = list(input())
        maps.append(rows)

    #print(maps)

    # 필요한 변수들 초기화
    q = collections.deque()
    visited = [[[[False]*m for _ in range(n)] for _ in range(m)] for _ in range(n)]

    dx = [0, 1, 0, -1]
    dy = [-1, 0, 1, 0]

    cnt = bfs(maps, visited)
    print(cnt)



