"""
예제 입력 1
10
5
2
3
1
4
2
3
5
1
7
예제 출력 1
1
1
2
2
3
3
4
5
5
7
"""

import sys
input = sys.stdin.readline

if __name__ == '__main__':
    n = int(input())

    numbers = [0] * 10001

    for i in range(n):
        numbers[int(input())] += 1

    for i, num in enumerate(numbers):
        if num:
            for _ in range(num):
                print(i)
