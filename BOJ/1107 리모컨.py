"""
문제
수빈이는 TV를 보고 있다. 수빈이는 채널을 돌리려고 했지만, 버튼을 너무 세게 누르는 바람에, 일부 숫자 버튼이 고장났다.

리모컨에는 버튼이 0부터 9까지 숫자, +와 -가 있다. +를 누르면 현재 보고있는 채널에서 +1된 채널로 이동하고, -를 누르면 -1된 채널로 이동한다. 채널 0에서 -를 누른 경우에는 채널이 변하지 않고, 채널은 무한대 만큼 있다.

수빈이가 지금 이동하려고 하는 채널은 N이다. 어떤 버튼이 고장났는지 주어졌을 때, 채널 N으로 이동하기 위해서 버튼을 최소 몇 번 눌러야하는지 구하는 프로그램을 작성하시오.

수빈이가 지금 보고 있는 채널은 100번이다.

입력
첫째 줄에 수빈이가 이동하려고 하는 채널 N (0 ≤ N ≤ 500,000)이 주어진다.  둘째 줄에는 고장난 버튼의 개수 M (0 ≤ M ≤ 10)이 주어진다. 고장난 버튼이 있는 경우에는 셋째 줄에는 고장난 버튼이 주어지며, 같은 버튼이 여러 번 주어지는 경우는 없다.

출력
첫째 줄에 채널 N으로 이동하기 위해 버튼을 최소 몇 번 눌러야 하는지를 출력한다.

예제 입력 1
5457
3
6 7 8
예제 출력 1
6
예제 입력 2
100
5
0 1 2 3 4
예제 출력 2
0
예제 입력 3
500000
8
0 2 3 4 6 7 8 9
예제 출력 3
11117
힌트
5455++ 또는 5459--
"""


def solution(n, m):

    # 100일 경우 예외처리
    if n == 100:
        cnt = 0
        return cnt

    # 0에서 9까지 버튼 할당
    channels = [i for i in range(0, 10)]

    # m 이 0이 아닐 경우 채널에서 제외하기
    if m != 0:
        brokens = list(map(int, input().split()))
    channels = list(set(channels) - set(brokens))
    channels.sort()  # 작은 자리부터 오도록 정렬하기

    splited_n = list(map(int, list(str(n))))
    cnt = 0
    i = 0  # N의 자릿수대로 옮겨가는 변수
    while True:
        # 고장난 채널이 아니라면 다시 와일문 돌기
        if splited_n[i] in channels:
            cnt += 1
            i += 1
            continue

        # 고장난 채널이라면, 최소 차이가 나는 채널 찾기
        else:
            new_channels = [abs(int(x) - int(y)) for x, y in zip(channels, [splited_n[i]] * len(channels))]
            idx = new_channels.index(min(new_channels))
            min_value = channels[idx]

            # 최소 차이가 나는 채널을 기준으로 cnt 돌기
            while True:
                if splited_n[i] > min_value:
                    min_value += 1
                    cnt += 1
                elif splited_n[i] < min_value:
                    min_value -= 1
                    cnt += 1
                else:
                    cnt += 1
                    break

            i += 1

        # 자릿수 넘어가면 나가기
        if i == len(splited_n):
            return cnt

    return cnt


if __name__ == '__main__':
    n = int(input())
    m = int(input())

    print(solution(n, m))



