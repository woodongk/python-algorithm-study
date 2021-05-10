"""
4
5 1 7 9

5
"""
import sys
input = sys.stdin.readline


if __name__ == '__main__':
    n = int(input())
    homes = list(map(int, input().split()))
    homes.sort()

    # 중앙값부터 시작하기
    print(homes[(n - 1) // 2])
