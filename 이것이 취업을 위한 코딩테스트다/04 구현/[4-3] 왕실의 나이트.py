"""
L 자 형태로만 이동 가능하다..문제 똑바로 읽자 ^^
직접 케이스를 셈하는게 훨 200배 빠름.
a1
2
c2
6

"""

if __name__ == '__main__':
    pos = str(input())

    # 위치 숫자로 바꾸기
    x, y = list(pos)
    col = {c: i for i, c in enumerate(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h'])}
    x = col[x] + 1

    # 움직일 방향 정하기
    move_plans = []

    # 1
    for i in [(2, 0), (-2, 0)]:
        for j in [(0, 1), (0, -1)]:
            move_plans.append([i, j])
    # 2
    for i in [(0, 2), (0, -2)]:
        for j in [(1, 0), (-1, 0)]:
            move_plans.append([i, j])

    # 루프 없이 더한 값으로 바로 이동할 수 있다.
    move_plans = [(xx + yx, xy + yy) for (xx, xy), (yx, yy) in move_plans]
    move_plans = list(set(move_plans))  # 중복 제거

    cnt = 0

    # 체크
    for move in move_plans:
        nx = int(x)
        ny = int(y)

        dx, dy = move

        if 1 <= nx + dx <= 8 and 1 <= ny + dy <= 8:
            cnt += 1
            print(move)

    print(cnt)
