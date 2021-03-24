def maxSubArray(nums) -> int:
    print(nums)

    dp = [0] * (len(nums) + 1)
    for i in range(1, len(nums)):
        dp[i] = max(dp[i - 1] + nums[i], nums[i])

    return max(dp)


if __name__ == '__main__':
    print(maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))
