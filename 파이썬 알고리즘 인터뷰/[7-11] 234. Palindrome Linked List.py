"""
Given the head of a singly linked list, return true if it is a palindrome.

Example 1:


Input: head = [1,2,2,1]
Output: true
Example 2:


Input: head = [1,2]
Output: false
"""

# Definition for singly-linked list.


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def isPalindrome(head: ListNode) -> bool:
    q : List = []

    if not head:
        return True

    node = head

    while node is not None:
        q.append(node.val)
        node = node.next

    if q == q[::-1]:
        return True
    else:
        return False




