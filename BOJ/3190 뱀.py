"""
문제
 'Dummy' 라는 도스게임이 있다. 이 게임에는 뱀이 나와서 기어다니는데, 사과를 먹으면 뱀 길이가 늘어난다.
 뱀이 이리저리 기어다니다가 벽 또는 자기자신의 몸과 부딪히면 게임이 끝난다.

게임은 NxN 정사각 보드위에서 진행되고, 몇몇 칸에는 사과가 놓여져 있다.
\보드의 상하좌우 끝에 벽이 있다. 게임이 시작할때 뱀은 맨위 맨좌측에 위치하고 뱀의 길이는 1 이다. 뱀은 처음에 오른쪽을 향한다.

뱀은 매 초마다 이동을 하는데 다음과 같은 규칙을 따른다.

먼저 뱀은 몸길이를 늘려 머리를 다음칸에 위치시킨다.
만약 이동한 칸에 사과가 있다면, 그 칸에 있던 사과가 없어지고 꼬리는 움직이지 않는다.
만약 이동한 칸에 사과가 없다면, 몸길이를 줄여서 꼬리가 위치한 칸을 비워준다. 즉, 몸길이는 변하지 않는다.
사과의 위치와 뱀의 이동경로가 주어질 때 이 게임이 몇 초에 끝나는지 계산하라.

입력
첫째 줄에 보드의 크기 N이 주어진다. (2 ≤ N ≤ 100) 다음 줄에 사과의 개수 K가 주어진다. (0 ≤ K ≤ 100)

다음 K개의 줄에는 사과의 위치가 주어지는데, 첫 번째 정수는 행, 두 번째 정수는 열 위치를 의미한다. 사과의 위치는 모두 다르며, 맨 위 맨 좌측 (1행 1열) 에는 사과가 없다.

다음 줄에는 뱀의 방향 변환 횟수 L 이 주어진다. (1 ≤ L ≤ 100)

다음 L개의 줄에는 뱀의 방향 변환 정보가 주어지는데,  정수 X와 문자 C로 이루어져 있으며. 게임 시작 시간으로부터 X초가 끝난 뒤에 왼쪽(C가 'L') 또는 오른쪽(C가 'D')로 90도 방향을 회전시킨다는 뜻이다. X는 10,000 이하의 양의 정수이며, 방향 전환 정보는 X가 증가하는 순으로 주어진다.

출력
첫째 줄에 게임이 몇 초에 끝나는지 출력한다.

예제 입력 1
6
3
3 4
2 5
5 3
3
3 D
15 L
17 D
예제 출력 1
9
예제 입력 2
10
4
1 2
1 3
1 4
1 5
4
8 D
10 D
11 D
13 L
예제 출력 2
21
예제 입력 3
10
5
1 5
1 3
1 2
1 6
1 7
4
8 D
10 D
11 D
13 L
예제 출력 3
13
"""
import collections

if __name__ == '__main__':
    n = int(input()) # 보드 판
    k = int(input()) # 사과 개수

    apple = [[0] * (n) for j in range(n)] # 사과 개수 0으로 초기화

    for i in range(k):
        x, y = map(int, input().split())
        apple[x - 1][y - 1] = 1

    d_nums = int(input()) # 방향 변경 수
    dqueue = collections.deque()
    for i in range(d_nums):
        x, c = input().split()
        dqueue.append((int(x), str(c)))

    # 동 남 서 북
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]

    def turn(direction, c):
        if c == "L":
            direction = (direction - 1) % 4
        else:
            direction = (direction + 1) % 4
        return direction

    d = 'R'
    length = 1
    time = 0
    direction = 0

    # 초기 스네이크 위치 설정
    snake_queue = collections.deque([(0, 0)])
    while True:
        time += 1
        head = snake_queue[-1]
        print(time, snake_queue)

        # 현재 설정된 direction 으로 이동
        nx = head[0] + dx[direction]
        ny = head[1] + dy[direction]
        print("nx : {}, ny : {}".format(nx, ny))

        # 행렬 내부 일 경우 & 몸하고 안 부딪혓을 경우
        if ((0 <= nx < n) and (0 <= ny < n)) and ((nx, ny) not in snake_queue):
            # 진입하기
            snake_queue.append((nx, ny))
            length += 1

            # 사과 여부에 따른 조건 변경
            # 1. 사과 있다
            if apple[nx][ny] == 1:
                apple[nx][ny] = 0 # 사과 제거
            # 2. 사과 없다
            else:
                snake_queue.popleft()  # tail 이동
        else:
            break

        if dqueue:
            if time == dqueue[0][0]:
                d = dqueue[0][1]
                direction = turn(direction, d)
                dqueue.popleft()

    print(time)




