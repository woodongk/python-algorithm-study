"""
6
1 2 3
4 5 6
7 8 9
10 11 12
13 14 15
16 17 18
"""
if __name__ == '__main__':
    n = int(input())

    x = y = int(n / 2) # 스타트 시작

    maps = []
    for _ in range(n):
        maps.append(list(map(int, input().split())))
    print(maps)
    print(maps[::-1])
    print(*maps[::-1])
    print(zip(*maps[::-1]))
    maps = list(map(list, zip(*maps[::-1])))
    print(maps)
