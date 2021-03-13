"""
Given an array nums of n integers, are there elements a, b, c in nums such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.

Notice that the solution set must not contain duplicate triplets.



Example 1:

Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]
Example 2:

Input: nums = []
Output: []
Example 3:

Input: nums = [0]
Output: []
"""

from typing import List


# big oh n^2 => 시간 초과
def greedy_threeSum(nums: List[int]) -> List[List[int]]:

    answer = []

    if len(nums) <= 2:
        return []

    for ai in range(len(nums)):
        for bi in range(ai + 1, len(nums)):
            a, b = nums[ai], nums[bi]
            c = (a + b) * (-1)
            print("cc", a, b, c, ai, bi)

            try:
                ci = nums.index(c)
                print(ai, bi, ci)
                if ai != ci and bi != ci:
                    triplet = sorted([a, b, c])
                    if triplet not in answer:
                        answer.append(triplet)
            except:
                pass

    return answer


def threeSum(nums: List[int]) -> List[List[int]]:

    # 길이가 2 이하면 성립 불가
    if len(nums) <= 2:
        return []

    # 최솟값이랑 최댓값이 전부 음수거나 전부 양수일 경우 성립 불가
    if min(nums) * max(nums) > 0:
        return []

    # nums 를 정렬하고 양쪽의 최솟값과 최댓값을 기준으로 비교
    nums.sort()
    answer = []

    # 양쪽 좌표 초기화
    # left 는 최솟값을 가리키고 right 은 최댓값을 가리킨다.
    print(nums)
    for i in range(0, len(nums)):
        left, right = i, len(nums) - 1
        sum = nums[left] + nums[right]
        print("와앙", nums[left], nums[right], sum)
        while left < right or sum != 0:
            print("지금 섬:{}".format(sum))
            if sum < 0:
                right -= 1
                sum += nums[right]
                if sum == 0:
                    continue
            elif sum > 0:
                left += 1
                sum += nums[left]
                if sum == 0:
                    continue
            # sum 이 0인 경우 이므로 정답 처리
            else:
                answer.append([nums[left], nums[i], nums[right]])
                print([nums[left], nums[i], nums[right]])

            #sum = nums[left] + nums[right]



    return answer


if __name__=='__main__':
    print(threeSum([-1,0,1,2,-1,-4]))

