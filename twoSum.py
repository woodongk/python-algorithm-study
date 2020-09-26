from typing import List


def twoSum(nums: List[int], target: int) -> List[int]:
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if (nums[i] + nums[j]) == target:
                return [i,j]

if __name__ == '__main__':
    print(twoSum([3,2,4], 6)) # [1,2]
    print(twoSum([3,3], 6)) # [0,1]