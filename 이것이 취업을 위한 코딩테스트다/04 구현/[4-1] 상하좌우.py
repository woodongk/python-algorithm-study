"""
5
R R R U D D
"""

if __name__ == '__main__':

    # 1. input 받기
    N = int(input())
    directions = list(map(str, input().split()))

    di = {
         'D' : (1, 0), # L
         'U' : (-1, 0), # R
         'R': (0, 1), # U
         'L': (0, -1) # D
    }

    x = y = 1

    # directions 순서대로 서칭
    for d in directions:
        dx, dy = di[d]
        # 공간 벗어나는 경우 무시한다.
        if (1 <= x + dx <= N) and (1 <= y + dy <= N):
            nx = x + dx
            ny = y + dy
        # 이동!
        x, y = nx, ny

    print(x, y)
