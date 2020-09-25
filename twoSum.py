from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i,n_i in enumerate(nums):
            for j,n_j in enumerate(nums):
                if ((n_i+n_j) == target):
                    return [i,j]

if __name__ == '__main__':
    sol = Solution()
    print(sol.twoSum([3,2,4], 6))