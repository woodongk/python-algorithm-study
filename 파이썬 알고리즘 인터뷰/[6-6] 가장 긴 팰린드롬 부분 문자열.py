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

    for i in range(l):
        for j in range(l, i, -1):
            sub_s = s[i:j]
            if sub_s[0] == sub_s[-1]:
                if (is_palindrome(sub_s)) & (len(sub_s) > len(max_len_sub_s)):
                    max_len_sub_s = sub_s
            else:
                pass

    return max_len_sub_s


if __name__ == '__main__':
    print(longestPalindrome("bb"))
