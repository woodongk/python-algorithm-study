"""
Given two arrays, write a function to compute their intersection.

Example 1:

Input: nums1 = [1,2,2,1], nums2 = [2,2]
Output: [2,2]
Example 2:

Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
Output: [4,9]
Note:

Each element in the result should appear as many times as it shows in both arrays.
The result can be in any order.
Follow up:

What if the given array is already sorted? How would you optimize your algorithm?
What if nums1's size is small compared to nums2's size? Which algorithm is better?
What if elements of nums2 are stored on disk, and the memory is limited such that you cannot load all elements into the memory at once?
"""
from typing import List
import collections


class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:

        #  크기가 작은 리스트를 nums1로 할당
        if len(nums1) > len(nums2):
            temp = nums1
            nums1 = nums2
            nums2 = temp

        # 우선 정렬하기
        nums1.sort()
        nums2.sort()

        intersect = []

        # 크기 작은 리스트 기준으로 루프 돌리면서 비교하기
        j = 0
        check = False
        for i in range(len(nums1)):
            check = False
            while j < len(nums2) and check == False:
                # 같다면, 하나 증가
                print(i, nums1[i], j, nums2[j])
                if nums1[i] == nums2[j]:
                    intersect.append(nums1[i])
                    j += 1
                    check = True  # while 문 나가서 i 업데이트
                # update j
                elif nums1[i] > nums2[j]:
                    j += 1
                # update i
                elif nums1[i] < nums2[j]:
                    check = True  # while 문 나가서 i 업데이트

        return intersect

    def intersect_with_counter(self, nums1, nums2):

        counts = collections.Counter(nums1)
        res = []

        for num in nums2:
            if counts[num] > 0 : # nums2에 nums1에 있는 원소 존재한다면
                res.append(num)
                counts[num] -= 1

        return res

    def intersect_with_switch(self, nums1, nums2):

        nums1, nums2 = sorted(nums1), sorted(nums2)
        left = right = 0
        res = []

        while True:
            try:
                if nums1[left] > nums2[right]:
                    right += 1
                elif nums1[left] < nums2[right]:
                    left += 1
                else: # 같다
                    res.append(nums1[left])
                    left += 1
                    right += 1
            except IndexError:
                break

        return res


if __name__ == '__main__':
    sol = Solution()
    # print(sol.intersect(nums1=[4, 9, 5], nums2=[9, 4, 9, 8, 4]))
    # print(sol.intersect(nums1=[1, 2, 2, 1], nums2=[2, 2]))
    # print(sol.intersect([-2147483648, 1, 2, 3], [1, -2147483648, -2147483648]))
    print()
    print(sol.intersect_with_counter(nums1=[4, 9, 5], nums2=[9, 4, 9, 8, 4]))
    print(sol.intersect_with_counter(nums1=[1, 2, 2, 1], nums2=[2, 2]))
    print(sol.intersect_with_counter([-2147483648, 1, 2, 3], [1, -2147483648, -2147483648]))
    print()
    print(sol.intersect_with_switch(nums1=[4, 9, 5], nums2=[9, 4, 9, 8, 4]))
    print(sol.intersect_with_switch(nums1=[1, 2, 2, 1], nums2=[2, 2]))
    print(sol.intersect_with_switch([-2147483648, 1, 2, 3], [1, -2147483648, -2147483648]))
