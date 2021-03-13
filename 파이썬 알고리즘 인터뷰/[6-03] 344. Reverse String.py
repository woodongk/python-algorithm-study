"""
Write a function that reverses a string. The input string is given as an array of characters char[].

Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.

You may assume all the characters consist of printable ascii characters.



Example 1:

Input: ["h","e","l","l","o"]
Output: ["o","l","l","e","h"]
Example 2:

Input: ["H","a","n","n","a","h"]
Output: ["h","a","n","n","a","H"]
"""
from typing import List


def reverseString(s: List[str]) -> None:
    """
    Do not return anything, modify s in-place instead.
    """
    s[:] = s[::-1]
    s.reverse()

    left, right = 0, len(s) - 1
    print("Two Point reverse")
    while left < right:
        s[left], s[right] = s[right], s[left]
        left += 1
        right -= 1

    return s


if __name__ == '__main__':
    string = ["h","e","l","l","o"]
    print(reverseString(string))
