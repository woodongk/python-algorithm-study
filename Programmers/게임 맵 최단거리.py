import collections

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]


def bfs(maps, n, m, start, visited, dist):
    queue = collections.deque([start])
    dist[0][0] = 1
    while queue:
        x, y = queue.popleft()
        visited[x][y] = True

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                if not visited[nx][ny] and maps[nx][ny] == 1:
                    visited[nx][ny] = True
                    dist[nx][ny] = dist[x][y] + 1
                    queue.append((nx, ny))
    return dist


def solution(maps):
    answer = 0
    n, m = len(maps), len(maps[0])

    start = (0, 0)
    target = (n - 1, m - 1)
    visited = [[False] * m for _ in range(n)]
    dist = [[-1] * m for _ in range(n)]

    dist = bfs(maps, n, m, start, visited, dist)

    return dist[n - 1][m - 1]


if __name__ == '__main__':
    print(solution([[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,1],[0,0,0,0,1]]))
    print(solution([[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,0],[0,0,0,0,1]]	))