"""
3
3
10 7 6
3
3 5 9
5
1 1 3 1 2
"""


def solution(n, prices):
    buy_money = 0  # 산 돈
    profit = 0  # 이익
    count = 0  # 물건수

    # 마지막 날이 값이 제일 클 경우 무조건 전부 사기
    if max(prices) == prices[-1]:
        buy_money = sum(prices[:-1])
        count = len(prices) - 1
        profit = (prices[-1] * count) - buy_money
        return profit

    # 그게 아닐 경우 치솟은 부분 직전까지 샀다가 팔기
    i = 0
    while True:
        now = i
        try:
            while prices[now] <= prices[now + 1]:
                now = now + 1
        except IndexError:
            pass
        buy_money = sum(prices[i: now]) # now 전까지 풀매수
        count = now - i
        profit += (prices[now] * count) - buy_money

        i = now + 1 # i 갱신
        if i >= len(prices) - 1:
            break

    return profit


if __name__ == '__main__':
    T = int(input())
    for test_case in range(1, T + 1):
        n = int(input())
        prices = list(map(int, input().split()))
        print("#{} {}".format(test_case,solution(n, prices)))



