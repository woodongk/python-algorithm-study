
def bigbang(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    bottom_up_lst = [None] * (n + 1)
    bottom_up_lst[0] = 1
    bottom_up_lst[1] = 1

    for i in range(2, n + 1):
        bottom_up_lst[i] = bottom_up_lst[i - 1] + (1 + 4 * (i - 1))
    return bottom_up_lst


def solution(n):
    if n == 1:
        return 1

    dp = [0] * (n + 1) # 최소 덧셈 카운트 수
    dp[0] = 1
    dp[1] = 1

    bigbang_tables = bigbang(n)
    b = 1  # 빅뱅수의 현재 위치에서의 max num
    # 인덱스 3부터 n 까지 loop
    for i in range(2, n + 1):

        if i < bigbang_tables[b]:
            max_num = bigbang_tables[b - 1]
        elif i == bigbang_tables[b]:
            dp[i] = 1
            continue
        else:
            max_num = bigbang_tables[b]
            b += 1
        print(i, max_num)


        if i > 6:
            dp[i] = min(dp[i - max_num] + 1, dp[i - 1] + 1, dp[i - 6] + 1)
        else:
            dp[i] = min(dp[i - max_num] + 1, dp[i - 1] + 1)

    return dp


import sys
input = sys.stdin.readline


if __name__ == '__main__':
    n = int(input())
    dp = solution(n)
    for i in range(len(dp)):
        print(i, dp[i])
    print(dp[n])




