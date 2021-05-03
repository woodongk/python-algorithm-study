"""
게임 화면의 격자의 상태가 담긴 2차원 배열 board와 인형을 집기 위해 크레인을 작동시킨 위치가 담긴 배열 moves가 매개변수로 주어질 때,
크레인을 모두 작동시킨 후 터트려져 사라진 인형의 개수를 return 하도록 solution 함수를 완성해주세요.

[제한사항]
board 배열은 2차원 배열로 크기는 "5 x 5" 이상 "30 x 30" 이하입니다.
board의 각 칸에는 0 이상 100 이하인 정수가 담겨있습니다.
0은 빈 칸을 나타냅니다.
1 ~ 100의 각 숫자는 각기 다른 인형의 모양을 의미하며 같은 숫자는 같은 모양의 인형을 나타냅니다.
moves 배열의 크기는 1 이상 1,000 이하입니다.
moves 배열 각 원소들의 값은 1 이상이며 board 배열의 가로 크기 이하인 자연수입니다.
"""


def solution(board, moves):
    cnt = 0

    # 인덱스 맞추기 위해 move 한칸씩 줄이기
    moves = [i - 1 for i in moves]
    n_cols = n_rows = len(board)

    doll_stack = []

    for move in moves:
        print("move  = {}".format(move))
        for b in board:
            print(b)
        print(doll_stack, cnt)
        # 가장 상위 인형이 있는 곳 인형 뽑아서 스택에 넣기
        col = move
        doll = 0
        for row in range(n_rows):
            if board[row][col] == 0:
                continue
            else:
                # 뽑으면 out of loop
                doll = board[row][col]
                board[row][col] = 0
                break
        if doll != 0:
            # 스택 체크 (2개 연속 같으면 제거)
            if len(doll_stack) != 0:
                if doll_stack[-1] == doll:
                    doll_stack.pop()
                    cnt += 2
                else:
                    doll_stack.append(doll)
            else:
                doll_stack.append(doll)
    return cnt


if __name__ == '__main__':
    print(solution([[0,0,0,0,0],
                    [0,0,1,0,3],
                    [0,2,5,0,1],
                    [4,2,4,4,2],
                    [3,5,1,3,1]],
                   [1,5,3,5,1,2,1,4]))