import collections
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# 최단거리 구하기
def bfs(start):

    queue = collections.deque([start])
    dist = [[-1] * 3 for _ in range(4)] # 경로를 -1 으로 초기화
    dist[start[0]][start[1]] = 0

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < 4 and 0 <= ny < 3: # 갈 수 있는 길이라면,
                if dist[nx][ny] == -1: # 아직 방문하지 않았다면 ( 경로 최단 거리 위해 )
                    dist[nx][ny] = dist[x][y] + 1
                    queue.append((nx, ny))

    return dist


def solution(numbers, hand):

    keypads = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9],
        ['*', 0, '#'],
    ]

    loc_maps = {
        1: (0, 0),
        2: (0, 1),
        3: (0, 2),
        4: (1, 0),
        5: (1, 1),
        6: (1, 2),
        7: (2, 0),
        8: (2, 1),
        9: (2, 2),
        0: (3, 1)
    }

    left_loc = (3, 0)
    right_loc = (3, 2)

    answer = ''
    for num in numbers:
        if num == 1 or num == 4 or num == 7:
            answer += "L"
            left_loc = loc_maps[num]
        elif num == 3 or num == 6 or num == 9:
            answer += 'R'
            right_loc = loc_maps[num]
        else:
            target_x, target_y = loc_maps[num]
            dist_left = bfs(left_loc)[target_x][target_y]
            dist_right = bfs(right_loc)[target_x][target_y]

            if dist_left > dist_right:
                answer += "R"
                right_loc = loc_maps[num]
            elif dist_left < dist_right:
                answer += "L"
                left_loc = loc_maps[num]
            else: #같다
                if hand == 'right':
                    answer += 'R'
                    right_loc = loc_maps[num]
                else:
                    answer += 'L'
                    left_loc = loc_maps[num]
    return answer

if __name__ == '__main__':

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    a = solution([1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5], "right")
    print(a)
    print(a == "LRLLLRLLRRL")