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
def dfs(di, array, node, visited, cnt):
    x, y = node
    visited[x][y] = True

    # 오른쪽 쫙 훑고, 왼쪽 쫙 훑기
    nx = x + dx[di]
    ny = y + dy[di]

    # 테두리 밖 안나가고 방문 하기 전 일 때
    if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny]:
        # 색깔이 같은 값일 경우! 방문
        if array[x][y] == array[nx][ny]:
            cnt += 1
            dfs(di, array, (nx, ny), visited, cnt)
    return cnt


if __name__ == '__main__':
    n = int(input())

    maps = []
    for _ in range(n):
        rows = list(input())
        maps.append(rows)

    visited = [([False] * n) for _ in range(n)]

    # 일직선만 이동 가능
    # 왼쪽 꼭대기서부터 내려오니까 다른 방향은 고려할 필요 없어보임!
    # 오른쪽하고 아래쪽만 고려한다.
    dx = [0, 1]
    dy = [1, 0]
    cnt = 1

    print(dfs(0, maps, (2, 2), visited, cnt))
    print(cnt)