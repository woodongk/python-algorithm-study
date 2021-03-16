"""
Given a string s, remove duplicate letters so that every letter appears once and only once. You must make sure your result is the smallest in lexicographical order among all possible results.

Note: This question is the same as 1081: https://leetcode.com/problems/smallest-subsequence-of-distinct-characters/



Example 1:

Input: s = "bcabc"
Output: "abc"
Example 2:

Input: s = "cbacdcbc"
Output: "acdb"
"""
from itertools import product
from itertools import combinations

import collections

class Solution:
    def removeDuplicateLetters(self, s: str) -> str:

        # 가장 처음 나오는 unique 값 최소를 기준으로
        counter = collections.Counter(list(s))
        print(counter)









if __name__ == '__main__':
    sol = Solution()
    print(sol.removeDuplicateLetters("bcabc"))
