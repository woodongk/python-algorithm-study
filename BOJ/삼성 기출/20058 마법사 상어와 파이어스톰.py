"""
예 입
3 1
1 2 3 4 5 6 7 8
8 7 6 5 4 3 2 1
1 2 3 4 5 6 7 8
8 7 6 5 4 3 2 1
1 2 3 4 5 6 7 8
8 7 6 5 4 3 2 1
1 2 3 4 5 6 7 8
8 7 6 5 4 3 2 1
1
예 출
284
64
"""
import copy


# L : 몇 단계
def split(L):
    num_l = 2 ** L
    rotate_maps = [[0] * (2 ** n) for _ in range(2 ** n)]

    for i in range(N):
        for j in range(N):
            # 회전하기
            for di in range(num_l):
                for dj in range(num_l):
                    if 0 <= ni < N and 0 <= nj < N:
                        rotate_maps[nj][num_l - 1 - ni] = maps[i + ][nj]
    return rotate_maps


if __name__ == '__main__':
    n, q = map(int, input().split())
    N = 2 ** n

    maps= []
    for _ in range(N):
        rows = list(map(int, input().split()))
        maps.append(rows)
    print(maps)


    print(split(1))
    # 부분 격자로 나누는 함수

    # 회전하는 함수

