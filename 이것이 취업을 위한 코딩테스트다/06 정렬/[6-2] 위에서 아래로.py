"""
수열 정렬
입력
3
15
27
12
출력
27 15 12
"""


if __name__ == '__main__':
    n = int(input())
    nums = [int(input()) for _ in range(n)]

    for i in sorted(nums)[::-1]:
        print(i, end = ' ')