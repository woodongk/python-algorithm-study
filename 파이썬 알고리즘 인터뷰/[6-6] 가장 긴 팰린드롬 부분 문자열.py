"""
Given a string s, return the longest palindromic substring in s.



Example 1:

Input: s = "babad"
Output: "bab"
Note: "aba" is also a valid answer.
Example 2:

Input: s = "cbbd"
Output: "bb"
Example 3:

Input: s = "a"
Output: "a"
Example 4:

Input: s = "ac"
Output: "a"


Constraints:

1 <= s.length <= 1000
s consist of only digits and English letters (lower-case and/or upper-case),
"""


def is_palindrome(string):
    if string == string[::-1]:
        return True
    else:
        return False


def longestPalindrome(s: str) -> str:

    l = len(s)
    max_len_sub_s = s[0]

    # 예외 처리는 코드의 앞 부분에 먼저해서 뒷 계산 생략시킴
    if len(s) < 2 or is_palindrome(s):
        return s

    for i in range(l):
        for j in range(l, i, -1):
            sub_s = s[i:j]
            if sub_s[0] == sub_s[-1]:
                if (is_palindrome(sub_s)) & (len(sub_s) > len(max_len_sub_s)):
                    max_len_sub_s = sub_s
            else:
                pass

    return max_len_sub_s


def twopointer_way_longestPalindrome(s: str) -> str:

    # 예외 처리는 코드의 앞 부분에 먼저해서 뒷 계산 생략시킴
    if len(s) < 2 or is_palindrome(s):
        return s

    # 팰린드롬 판별 및 투 포인터 확장
    def expand(left, right):
        while left >= 0 and right < len(s) and s[left] == s[right - 1]:
            left += 1
            right -= 1
        return s[left + 1: right - 1]

    # 최대 팰린드롬 찾
    result = ''
    for i in range(len(s) - 1):
        result = max(result,
                     expand(i, i + 1),  # 홀짝
                     expand(i, i + 2),
                     key=len
                     )
    return result


if __name__ == '__main__':
    print(longestPalindrome("bb"))
    print(twopointer_way_longestPalindrome("babad"))
