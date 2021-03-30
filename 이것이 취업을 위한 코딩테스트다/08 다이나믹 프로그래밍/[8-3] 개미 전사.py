"""
입력
4
1 3 1 5
출력
8
"""
if __name__ == '__main__':
    n = int(input())
    food_array = list(map(int, input().split()))

    dp = [0] * n

    dp[0] = food_array[0]
    dp[1] = max(food_array[0], food_array[1])

    for i in range(2, n):
        dp[i] = max(dp[i - 1], dp[i - 2] + food_array[i])

    print(dp[n - 1])