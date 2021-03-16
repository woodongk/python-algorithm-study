from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:

        if not nums:
            return 0

        dp = [0] * len(nums)

        # 현재값은 가장 첫번째 값
        dp[0] = nums[0]

        # for 문 돌면서 갱신
        # i - 1 인덱스까지의 최대값 + 현재 값 vs 현재값
        for i in range(1, len(nums)):
            dp[i] = max(dp[i-1] + nums[i], nums[i])
        return max(dp)


if __name__ == '__main__':
    sol = Solution().maxSubArray([-2,1,-3,4,-1,2,1,-5,4])
    print("max_vlaue = {}".format(sol))