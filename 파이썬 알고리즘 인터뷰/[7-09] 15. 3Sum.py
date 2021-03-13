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


# 방법은 떠올렸는데 구현을 못함
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

    for i in range(len(nums) - 1):
        # 양쪽 좌표 초기화, left 는 최솟값을 가리키고 right 은 최댓값을 가리킨다.
        # 매번 right 은 최대 좌표로 갱신
        left, right = i, len(nums) - 1

        # 루프는 두개 이상일 수 밖에 없음. 명심
        while left < right:
            # 여기서 left, right 만 업데이트 진행
            sums = nums[i] + nums[left] + nums[right]
            print(left, right, nums[left], nums[right], sums)

            # 세 수 합이 음수라면 양수를 찾아야 0이 될 가능성
            if sums < 0:
                print("두 수 합이 음수 ")
                right -= 1

            # 세 수 합이 양수라면 음수를 찾아야 0이 될 가능성
            elif sums > 0:
                print("두 수 합이 양수 ")
                left += 1
            # 세 수의 합이 0이라면 강제 return
            else:
                print("C", [nums[left], nums[i], nums[right]])
                answer.append([nums[left], nums[i], nums[right]])

                # 정지 포인트는 갱신되는 left 이 right 보다 커질 때
                while left < right:
                    sums = nums[left] + nums[right] + nums[i]
                    if sums == 0:  # 세 수의 합이 0 이라면
                        print(nums[left], nums[i], nums[right])
                        answer.append([nums[left], nums[i], nums[right]])
                        break
                    else:
                        left += 1
                        right -= 1

    return answer


if __name__ == '__main__':
    print(threeSum([-1, 0, 1, 2, -1, -4]))
