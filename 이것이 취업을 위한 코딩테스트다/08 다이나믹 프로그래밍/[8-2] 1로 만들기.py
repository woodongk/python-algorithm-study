"""
입력
26
출력
3
"""


def solution(x):

    # 각 인덱스 별로 최소 연산값 저장하는 리스트
    dp = [0] * (x + 1)

    for i in range(2, x + 1):
        # 현재 값에서 1 뺀 경우의 최소값하고 계속해서 비교한다.
        dp[i] = dp[i - 1] + 1 # 최악의 상황

        if i % 2 == 0:
            dp[i] = min(dp[i], dp[int(i / 2)] + 1)

        if i % 3 == 0:
            dp[i] = min(dp[i], dp[int(i / 3)] + 1)

        # 가장 이상적인 케이스를 바닥에 둬야, 마지막에 min 값이 제대로 바뀔 수 있다.
        if i % 5 == 0:
            dp[i] = min(dp[i], dp[int(i / 5)] + 1)

    return dp


if __name__ == '__main__':
    x = int(input())

    dp = solution(x)
    for i, dp in enumerate(dp):
        print("i가 {}일 때, dp 값은 {}".format(i, dp))

    print(dp[-1])




