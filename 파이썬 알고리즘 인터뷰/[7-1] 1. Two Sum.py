"""
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.



Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Output: Because nums[0] + nums[1] == 9, we return [0, 1].
Example 2:

Input: nums = [3,2,4], target = 6
Output: [1,2]
Example 3:

Input: nums = [3,3], target = 6
Output: [0,1]
"""
from typing import List


def twoSum(nums: List[int], target: int) -> List[int]:

    for ix, x in enumerate(nums):
        y = target - x

        try:
            iy = nums[ix+1:].index(y)
            iy += ix + 1
            return (ix, iy)
        except:
            pass


# using dictionary
def fast_twoSum(nums: List[int], target: int) -> List[int]:

    # 딕셔너리로 조회
    nums_map = {}
    for i, num in enumerate(nums):
        nums_map[num] = i

    for i, num in enumerate(nums):
        if target - num in nums_map and i != nums_map[target - num]:  # 딕셔너리에 값이 있고 중복 index 아니라면
            return [i, nums_map[target-num]]


if __name__ == '__main__':
    #nums = [3, 2, 4]
    nums = [3, 1, 3]
    target = 6
    print(twoSum(nums, target))
    print(fast_twoSum(nums, target))
