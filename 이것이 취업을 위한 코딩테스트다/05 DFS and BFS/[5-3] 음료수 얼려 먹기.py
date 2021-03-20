"""
DFS 문제) 음료수 얼려먹기
1. 문제
N * M 크기의 얼음틀이 있다. 구멍이 뚫려있는 부분은 0, 칸막이가 존재하는 부분은 1로 표시된다.
구멍이 뚫려 있는 부분끼리 상, 하, 좌, 우로 붙어 있는 경우 서로 연결되어 있는 것으로 간주한다.
이때 얼음 틀의 모양이 주어졌을 때 생성되는 총 아이스크림의 개수를 구하는 프로그램을 작성하시오.
다음의 4 X 5 얼음 틀 예시에서는 아이스크림이 총 3개 생성된다.

00110
00011
11111
00000
2. 입력
첫 번째 줄에 얼음 틀의 새로 길이 N과 가로 길이 M이 주어진다.( 1<=N, M <= 1000)
두 번째 줄부터 N+1번째 줄까지 얼음 틀의 형태가 주어진다.
이때 구멍이 뚫여있는 부분은 0, 그렇지 않은 부분은 1이다.
3. 출력
한 번에 만들 수 있는 아이스크림 개수를 출력한다.

4 5
00110
00011
11111
00000
3

15 14
00000111100000
11111101111110
11011101101110
11011101100000
11011111111111
11011111111100
11000000011111
01111111111111
00000000011111
01111111111000
00011111111000
00000001111000
11111111110011
11100011111111
11100011111111
8

"""


def dfs(array, node, visited):
    x, y = node
    visited[x][y] = True

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        # 행렬 내부일 경우 진입.
        if (0 <= nx < n) and (0 <= ny < m):
            # 방문하지 않은 0 일 경우
            if not visited[nx][ny] and array[nx][ny] == 0:
                dfs(array, (nx, ny), visited)


# 27분 solve! ㅎㅎㅎㅎ
if __name__ == '__main__':

    # input 입력받기
    n, m = map(int, input().split())

    array_2d = []
    for i in range(n):
        array_2d.append(list(map(int, input())))

    # 밖에 있을 변수들 (cnt, visited)
    cnt = 0
    visited = [[False] * m for _ in range(n)]

    dx = [0, 1, -1, 0]
    dy = [1, 0, 0, -1]

    # (0,0)부터 시작하여 행렬 순서대로 훑기
    for i in range(n):
        for j in range(m):
            # count 동작을 위해 밖에도 visited 장치를 둔다. (visited 없다면 모든 0의 개수가 세어짐
            if array_2d[i][j] == 0 and not visited[i][j]:
                # dfs 함수의 역할은 "모든 0을 훑으면서 visited True를 마크하고 나오는 것"
                dfs(array_2d, (i, j), visited)
                cnt += 1

    print(cnt)


