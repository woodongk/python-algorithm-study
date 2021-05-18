"""
m	n	board	answer
4	5	["CCBDE", "AAADE", "AAABF", "CCBBF"]	14
6	6	["TTTANT", "RRFACC", "RRRFCC", "TRRRAA", "TTMMMF", "TMMTTJ"]	15

예제에 대한 설명
입출력 예제 1의 경우, 첫 번째에는 A 블록 6개가 지워지고, 두 번째에는 B 블록 4개와 C 블록 4개가 지워져, 모두 14개의 블록이 지워진다.
입출력 예제 2는 본문 설명에 있는 그림을 옮긴 것이다. 11개와 4개의 블록이 차례로 지워지며, 모두 15개의 블록이 지워진다.
"""

dx = [0, 1, 1]
dy = [1, 1, 0]


import copy


def is_four_near(node, m, n, tmp):
    x, y = node
    block = tmp[x][y]
    check = True
    for i in range(3):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < m and 0 <= ny < n: # 범위 내부라면
            if block == tmp[nx][ny]: # 같다면
                continue
            else: # 다르다면 초기화시키고 나가기
                return False
        else: # 범위 밖이어도 나
            return False
    # 모든 노드가 같았다면 체크는 true 일 것. 한 노드라도 달랐다면 체크를 false 일 것.
    return check


# 같은 모양의 블록이 2 2 형태일때 지워지는 함수
# 지워야할 노드에서 가장 왼쪽 위 노드만 탐색 (겹칠수도 있으므로)
def delete_nodes(m, n, my_board):
    tmp = copy.deepcopy(my_board)
    to_delete = []
    for x in range(m):
        for y in range(n):
            if tmp[x][y] != 0:
                check_flag = is_four_near((x, y), m, n, tmp)
                if check_flag is True:
                    to_delete.append((x, y))
                    to_delete.append((x, y+1))
                    to_delete.append((x+1, y))
                    to_delete.append((x+1, y+1))

    # to_deleted 리스트에 있는 노드 지우기
    for node in to_delete:
        x, y = node
        tmp[x][y] = 0

    return tmp, to_delete


# 중력에 의해 아래로 내려오는 함수
def down_board(m, n, my_board):
    tmp = copy.deepcopy(my_board)
    for y in range(n):
        # 거꾸로 체크해야 함 ! 그래야 순서대로 아래로 내려감
        for x in range(m - 1, -1, -1):
            nx, ny = x, y
            # 아래칸이 빈칸이라면 가장 밑 빈칸이 어디인지 추적하기
            while 0 <= nx + 1 < m:
                if tmp[nx + 1][ny] == 0:  # 빈칸이라면
                    nx += 1
                else:
                    break
            tmp[x][y], tmp[nx][ny] = tmp[nx][ny], tmp[x][y]
    return tmp


def solution(m, n, board):
    answer = 0

    board = [list(b) for b in board]

    temp_board = copy.deepcopy(board)
    while True:
        # 1. 겹치는 칸 삭제
        temp_board2, to_delete = delete_nodes(m, n, temp_board)
        answer += len(set(to_delete))
        # 삭제된 노드 개수가 더는 없다면 나가기
        if len(set(to_delete)) == 0:
            break

        # 2. 블럭 내리기
        temp_board3 = down_board(m, n, temp_board2)
        temp_board = temp_board3

    return answer


if __name__ == '__main__':
    print(solution(4,5,["CCBDE", "AAADE", "AAABF", "CCBBF"]))
    print(solution(6,6,["TTTANT", "RRFACC", "RRRFCC", "TRRRAA", "TTMMMF", "TMMTTJ"]))