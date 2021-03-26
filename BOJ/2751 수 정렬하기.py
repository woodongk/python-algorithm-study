"""
문제
N개의 수가 주어졌을 때, 이를 오름차순으로 정렬하는 프로그램을 작성하시오.

입력
첫째 줄에 수의 개수 N(1 ≤ N ≤ 1,000,000)이 주어진다. 둘째 줄부터 N개의 줄에는 숫자가 주어진다. 이 수는 절댓값이 1,000,000보다 작거나 같은 정수이다. 수는 중복되지 않는다.

출력
첫째 줄부터 N개의 줄에 오름차순으로 정렬한 결과를 한 줄에 하나씩 출력한다.

예제 입력 1
5
5
4
3
2
1
예제 출력 1
1
2
3
4
5
"""
import sys
input = sys.stdin.readline

if __name__ == '__main__':
    n = int(input())
    nums = [int(input()) for _ in range(n)]

    # 1. 계수 정렬로 시간 단축하기! == > 시간 초과
    # # 가장 큰 값으로 리스트 생성
    # count_sort = [0] * (1000000 + 1)
    #
    # #  데이터 값과 동일한 인덱스의 데이터를 1씩 증가시킴
    # for i in nums:
    #     count_sort[i] += 1
    #
    # # 순서대로 출력
    # for i in range(len(nums) + 1):
    #     if count_sort[i] > 0:
    #         print(i)

    # # 2. quick sort == > 시간 초과
    # nums = simple_quick_sort(nums)
    # for i in nums:
    #     print(i)
    for i in sorted(nums):
        sys.stdout.write(str(i)+'\n')