"""
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.


Example 1:

Input: s = "()"
Output: true
Example 2:

Input: s = "()[]{}"
Output: true
Example 3:

Input: s = "(]"
Output: false
Example 4:

Input: s = "([)]"
Output: false
Example 5:

Input: s = "{[]}"
Output: true
"""


def isValid(s: str) -> bool:
    stack = []
    table = {
        ')': '(',
        ']': '[',
        '}': '{'
    }

    if len(s) <= 1:
        return False

    # # 왼쪽 괄호 만나면 push, 오른쪽 괄호 만나면 pop
    # # 주의 : 짝꿍을 찾아야됨
    for char in s:
        print(stack)
        if char in ['(', '{', '[']:
            stack.append(char)
        else:
            if len(stack) == 0:
                return False
            elif stack[-1] == table[char]:
                stack.pop()
            else:
                return False

    return len(stack) == 0


if __name__ == '__main__':
    print(isValid("){"))
