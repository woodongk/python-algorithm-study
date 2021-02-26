
if __name__ == '__main__':
    # 1. initialization
    n = int(input())
    array = []
    for _ in range(n):
        array.append(tuple(map(int, input().split())))

    t = [t for(t, p) in array]
    p = [p for (t, p) in array]

    max_value = 0

    # 2. dp solve
    dp = [0] * (n + 1) # dp[i] = i 번째부터 마지막날까지의 최대값

    for i in range(n - 1, - 1, -1):
        if t[i] + i <= n: # 상담이 n일을 넘기지 않을 경우
            with_i = p[i] + dp[t[i] + i]
            dp[i] = max(with_i, max_value)
            max_value = dp[i]
            #print(with_i, max_value)
        else:
            dp[i] = max_value

    print(max_value)
