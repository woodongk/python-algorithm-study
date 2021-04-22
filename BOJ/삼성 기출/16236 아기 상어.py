import collections
INF = 1e9


def find_next_target(dist):
    x, y = 0, 0
    min_dist = INF

    for i in range(n):
        for j in range(n):
            # 도달 가능 and 먹을 수 있음
            if dist[i][j] != -1 and (1 <= maps[i][j] < shark_size):
                # 가장 작은 물고기 선택
                if dist[i][j] < min_dist:
                    min_dist = dist[i][j]
                    x, y = i, j
    # 먹을 수 있는 물고기 없다.
    if min_dist == INF:
        return None
    else:
        return x, y, min_dist


# 현재 상어 위치로부터 모든 노드까지의 최단거리 계산하는 함수
def bfs():
    queue = collections.deque([(shark_x, shark_y)])

    dist = [[-1] * n for _ in range(n)]  # 매번 초기화 해야함
    dist[shark_x][shark_y] = 0

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n: # 범위 밖이 아니라면
                # 방문하지 않았다면, 갈 수 있는 길이라면
                if maps[nx][ny] <= shark_size and dist[nx][ny] == -1:
                    queue.append((nx, ny))
                    dist[nx][ny] = dist[x][y] + 1
    return dist


if __name__ == '__main__':
    n = int(input())
    maps = []
    for i in range(n):
        rows = list(map(int, input().split()))
        maps.append(rows)

    # 아기 상어의 위치와 물고기 위치 찾기
    for i in range(n):
        for j in range(n):
            if maps[i][j] == 9:
                shark_x, shark_y = i, j
                maps[shark_x][shark_y] = 0 # 아무것도 없다고 처리

    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]

    time = 0  # 경과 시간
    shark_size = 2 # 현재 상어 크기
    eat = 0
    # 물고기 타겟 위치 구하기
    while True:
        # 최단경로 탐색하기
        distance_map = bfs()
        # 다음 물고기 위치 구하기
        next_target = find_next_target(distance_map)

        if next_target == None:
            break
        else:
            fx, fy, fdist = next_target

            # 물고기 먹기
            shark_x, shark_y = fx, fy
            maps[shark_x][shark_y] = 0
            eat += 1
            time += fdist

            if eat >= shark_size:
                shark_size += 1
                eat = 0

    print(time)
