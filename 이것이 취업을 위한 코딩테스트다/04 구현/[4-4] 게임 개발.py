"""
4 4
1 1 0
1 1 1 1
1 0 0 1
1 1 0 1
1 1 1 1
"""

if __name__ == '__main__':
    n, m = map(int, input().split())
    a, b, d = map(int, input().split())

    maps = []
    for _ in range(n):
        maps.append(list(map(int, input().split())))
    print(maps)
    # visited 여부 체크
    check_visited = [[False] * m for _ in range(n)]

    # 왼쪽부터 순서대로 왼쪽으로 90도 도는 순서
    # di = [0, 3, 2, 1]
    steps = [(-1, 0), (0, -1),(1, 0), (0, 1)]

    di = [0, 3, 2, 1].index(d)
    check = 0  # escape loop 체크용
    while True:

        # step 리스트에서 왼쪽 이동 방향의 index
        d_left = (di + 1) % 4 # 다음 direction 는 4의 나머지 + 1
        print(a, b)
        na = a + steps[d_left][0]
        nb = b + steps[d_left][1]

        # 왼쪽 방문하지 않았거나 바다 아니라면
        print(check_visited[na][nb] == False, (maps[na][nb] != 1))
        if (check_visited[na][nb] == False) and (maps[na][nb] != 1):
            # 가장자리 체크
            if 0 <= na <= n - 1 and 0 <= nb <= m - 1:
                # left 이동
                di = d_left
                # 좌표 이동
                a, b = na, nb
                # 방문 체크
                check_visited[na][nb] = True
                # 체크 재갱신
                check = 0
        # 방문했거나 바다라면
        else:
            # left 이동
            di = d_left
            check += 1

        # 아무데도 갈 데 없는 상황
        if check < 4:
            continue
        else:
            na = a + (-1) * steps[d_left][0]
            nb = b + (-1) * steps[d_left][1]

            if maps[na][nb] == 1 or na >= n or na < 0 or nb >= m or nb < 0:
                break
            else:
                a = na
                b = nb

    visited = 0
    for line in check_visited:
        visited += len([i for i in line if i == True])

    print(visited)











