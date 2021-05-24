import math
import collections


def solution(progresses, speeds):
    answer = []

    # 며칠 남았는지 계산하기
    rest = [math.ceil((100 - progress)/speed) for progress, speed in zip(progresses, speeds)]
    queue = collections.deque(rest)

    while queue:
        item = queue.popleft()
        cnt = 1
        # item 보다 출하 일수 같거나 낮은 경우 0 혹은 음수로 전환
        queue = collections.deque([i - item for i in queue])
        if queue:  # queue 에 item 이 존재한다면
            try:
                while queue[0] <= 0: # 출하 일수 같거나 빠른 경우를 셈하며 pop 해주기
                    queue.popleft()
                    cnt += 1
            except IndexError:  # pop 하는 도중 생기는 indexError 방지
                pass
        answer.append(cnt)
    return answer


if __name__ == '__main__':
    print(solution([93, 31, 55],[1, 30, 5]))
    print(solution([95, 90, 99, 99, 80, 99],[1, 1, 1, 1, 1, 1]))
    print(solution([95, 90, 99, 99, 80, 99], [2,2,2,2,2,]))