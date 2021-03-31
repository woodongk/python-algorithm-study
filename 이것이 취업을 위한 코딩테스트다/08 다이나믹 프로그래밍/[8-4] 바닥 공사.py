

if __name__ == '__main__':
    n = int(input())

    dp = [0] * (n + 1)

    dp[1] = 1
    dp[2] = 3

    for i in range(3, n + 1):
        # i - 1 일 경우, i - 2 일 경우 생각하기.
        # 중간에 복잡한 과정은 생략해도 된다. 왼쪽부터 이미 채웠다고 가정하고 있으므로.
        dp[i] = (dp[i - 1] * 1 + dp[i - 2] * 2) % 796796

    print(dp[n])


