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
            if maps[i][j] > 0:
                dirt = maps[i][j]
                part_of_dirt = dirt // 5
                cnt = 0

                for k in range(4):
                    nx = i + dx[k]
                    ny = j + dy[k]

                    if 0 <= nx < r and 0 <= ny < c:  # 범위 벗어나지 않으면
                        if tmp[nx][ny] >= 0:  # 공기 청정기 없으면
                            tmp[nx][ny] += part_of_dirt
                            cnt += 1  # 확산된 만큼 더해준다
                            tmp[i][j] -= part_of_dirt


def clean():
    for pos in range(len(cleaners)):  # 위, 아래 순서임
        if pos == 0:  # 위 이동

            x, y = cleaners[0]
            nx, ny = x, y

            # 모든 값 리스트에 넣어버리기
            up_values = [0]
            k = 0
            for i in range(4):
                nx = nx + up[i][0]
                ny = ny + up[i][1]
                while True:
                    if (0 <= nx < r) and (0 <= ny < c):
                        up_values.append(tmp[nx][ny])
                        tmp2[nx][ny] = up_values[k] # 한칸씩 밀리게 넣기
                        k += 1
                        if tmp[nx][ny] != -1:
                            nx += up[i][0]
                            ny += up[i][1]
                    else:
                        nx -= up[i][0]
                        ny -= up[i][1]
                        if tmp[nx][ny] == -1:
                            tmp2[nx][ny] = 0
                        break
            print(up_values)
        else: # 아래

            x, y = cleaners[1]
            nx, ny = x, y

            # 모든 값 리스트에 넣어버리기
            down_values = [0]
            k = 0
            for i in range(4):
                nx = nx + down[i][0]
                ny = ny + down[i][1]
                while True:
                    if (0 <= nx < r) and (0 <= ny < c) and tmp[nx][ny] != -1:
                        down_values.append(tmp[nx][ny])
                        tmp2[nx][ny] = down_values[k]
                        k += 1
                        nx += down[i][0]
                        ny += down[i][1]
                    else:
                        nx -= down[i][0]
                        ny -= down[i][1]
                        if tmp[nx][ny] == -1:
                            tmp2[nx][ny] = 0
                        break
            print(down_values)


if __name__ == '__main__':
    # 입력값 받기
    r, c, t = map(int, input().split())

    maps = []
    for _ in range(r):
        rows = list(map(int, input().split()))
        maps.append(rows)

    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]

    up = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    down = [(1, 0), (0, -1), (-1, 0), (0, 1)]

    # 공기 청정기 위치 찾기
    cleaners = []
    for i in range(r): # 공기청정기는 1열에만 존재한다
        if maps[i][0] == -1:
            cleaners.append((i, 0)) # 앞에꺼가 위, 뒤에꺼가 아래

    tmp = copy.deepcopy(maps)
    spread()  # 미세먼지 확산 함수
    tmp2 = copy.deepcopy(tmp)
    print(tmp)
    clean()  # 미세먼지 제거 함
    print(tmp2)

    # # t초 만큼 돌리기
    # for i in range(t):
    #     # 딥카피해서 루프마다 원본 손상 없게 하기
    #     tmp = copy.deepcopy(maps)
    #     spread()  # 미세먼지 확산 함수
    #     tmp2 = copy.deepcopy(tmp)
    #     clean() # 미세먼지 제거 함
    #     maps = tmp2

    dirts = 0
    for i in range(r):
        for j in range(c):
            if maps[i][j] > 0:
                dirts += tmp2[i][j]

    print(dirts)



