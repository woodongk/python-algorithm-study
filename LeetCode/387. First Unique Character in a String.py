import collections


class Solution:
    def firstUniqChar(self, s: str) -> int:

        counter = collections.Counter(list(s)) # order 유지

        unique_char = [k for k, v in counter.items() if v == 1]

        if not unique_char:
            return -1
        else:
            return s.index(unique_char[0])


if __name__ == '__main__':
    sol = Solution()
    sol.firstUniqChar("loveleetcode")