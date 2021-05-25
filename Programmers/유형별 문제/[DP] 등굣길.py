def solution(m, n, puddles):
    # 배열 초기화
    dp = []
    for _ in range(n + 1):
        dp.append([0] * (m + 1))

    dp[1][1] = 1  # start - 집
    for puddle in puddles:  # 웅덩이
        px, py = puddle
        dp[py][px] = -1

    for d in dp:
        print(d)
    print()

    # 최단거리 경로 총 개수 구하기
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if i == 1 and j == 1:
                continue

            if dp[i][j] >= 0:
                dp[i][j] = (dp[i - 1][j] + dp[i][j - 1]) % 1000000007
            else:
                dp[i][j] = 0

    for d in dp:
        print(d)

    return dp[n][m]


if __name__ == '__main__':
    print(solution(4, 3, [[2, 2]]))