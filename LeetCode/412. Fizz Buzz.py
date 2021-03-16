"""
Write a program that outputs the string representation of numbers from 1 to n.

But for multiples of three it should output “Fizz” instead of the number and for the multiples of five output “Buzz”. For numbers which are multiples of both three and five output “FizzBuzz”.

Example:

n = 15,

Return:
[
    "1",
    "2",
    "Fizz",
    "4",
    "Buzz",
    "Fizz",
    "7",
    "8",
    "Fizz",
    "Buzz",
    "11",
    "Fizz",
    "13",
    "14",
    "FizzBuzz"
]
"""

from typing import List


class Solution:
    def fizzBuzz(self, n: int) -> List[str]:

        results = []

        for i in range(1, n + 1):
            mod3 = i % 3
            mod5 = i % 5

            if  mod3 == 0 and mod5 == 0:
                results.append("FizzBuzz")
            elif mod3 == 0:
                results.append("Fizz")
            elif mod5 == 0:
                results.append("Buzz")
            else:
                results.append(str(i))

        return results


if __name__ == '__main__':
    sol = Solution()
    print(sol.fizzBuzz(15))