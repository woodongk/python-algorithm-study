"""
Given an integer n, return true if it is a power of three. Otherwise, return false.

An integer n is a power of three, if there exists an integer x such that n == 3x.
Example 1:

Input: n = 27
Output: true
Example 2:

Input: n = 0
Output: false
Example 3:

Input: n = 9
Output: true
Example 4:

Input: n = 45
Output: false
"""


class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        # 0 이하 경우 제거
        if n <= 0:
            return False

        # 3으로 더이상 나눠지지 않을 때까지 3으로 나누기
        while n % 3 == 0:
            n = n / 3

        print(n)
        if n == 1:
            return True
        else:
            return False


if __name__ == '__main__':
    sol = Solution()
    print(sol.isPowerOfThree(27))
    print(sol.isPowerOfThree(45))