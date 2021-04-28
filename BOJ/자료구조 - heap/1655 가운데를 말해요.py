"""
문제
수빈이는 동생에게 "가운데를 말해요" 게임을 가르쳐주고 있다.
수빈이가 정수를 하나씩 외칠때마다 동생은 지금까지 수빈이가 말한 수 중에서 중간값을 말해야 한다.
 만약, 그동안 수빈이가 외친 수의 개수가 짝수개라면 중간에 있는 두 수 중에서 작은 수를 말해야 한다.

예를 들어 수빈이가 동생에게 1, 5, 2, 10, -99, 7, 5를 순서대로 외쳤다고 하면, 동생은 1, 1, 2, 2, 2, 2, 5를 차례대로 말해야 한다.
수빈이가 외치는 수가 주어졌을 때, 동생이 말해야 하는 수를 구하는 프로그램을 작성하시오.

입력
첫째 줄에는 수빈이가 외치는 정수의 개수 N이 주어진다. N은 1보다 크거나 같고, 100,000보다 작거나 같은 자연수이다.
그 다음 N줄에 걸쳐서 수빈이가 외치는 정수가 차례대로 주어진다. 정수는 -10,000보다 크거나 같고, 10,000보다 작거나 같다.

출력
한 줄에 하나씩 N줄에 걸쳐 수빈이의 동생이 말해야하는 수를 순서대로 출력한다.

예제 입력 1
7
1
5
2
10
-99
7
5
예제 출력 1
1
1
2
2
2
2
5
"""

import heapq
import sys
input = sys.stdin.readline


def solution(n):
    # 두 개의 힙을 이용하여 서칭, 둘의 사이가 항상 중앙이 되도록
    max_heap = []
    min_heap = []
    re = []

    for _ in range(n):
        num = int(input())

        # 최대 힙의 루트는 항상 중앙값
        # 최대 힙의 루트는 항상 최소힙의 루트보다 같거나 작아야 한다
        if len(max_heap) == len(min_heap):
            heapq.heappush(max_heap, (-num, num))
        else:
            heapq.heappush(min_heap, num)

        # max heap 의 top 이 min heap top 보다 작아야 함
        if len(max_heap) >= 1 and len(min_heap) >= 1 and max_heap[0][1] > min_heap[0]:
            a, b = heapq.heappop(max_heap)
            c = heapq.heappop(min_heap)

            heapq.heappush(max_heap, (-c, c))
            heapq.heappush(min_heap, b)

        #print(min_heap, max_heap)
        re.append(max_heap[0][1])

    return re


def binary_search(nums, target):
    left, right = 0, len(nums)

    while left < right:
        mid = (left + right) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] > target:
            right = mid
        else:
            left = mid + 1
    return right


if __name__ == '__main__':
    n = int(input())

    re = solution(n)
    for r in re:
        print(r)

    array = []
    for _ in range(n):
        num = int(input())
        idx = 0
        idx = binary_search(array, num)
        array.insert(idx, num)
        # print(nums)
        print(array[(len(array) - 1) // 2])



