"""
문제
오늘 동빈이는 여행 가신 부모님을 대신해서 떡집 일을 하기로 했다. 오늘은 떡볶이 떡을 만드는 날이다.
동빈이네 떡볶이 떡은 재밌게도 떡볶이 떡의 길이가 일정하지 않다.
대신에 한 봉지 안에 들어가는 떡의 총 길이는 절단기로 잘라서 맞춰준다.
절단기의 높이(H)를 지정하면 줄지어진 떡을 한 번에 절단한다.
높이가 H보다 긴 떡은 H 위의 부분이 잘릴 것이고, 낮은 떡은 잘리지 않는다.
이걸 처리 안 해줘서 시간을 허비했다.
예를 들어 높이가 19, 14, 10, 17cm인 떡이 나란히 있고 절단기 높이를 15cm로 지정하면 자른 뒤 떡의 높이는 15, 14, 10, 15cm가 될 것이다.
잘린 떡의 길이는 차례대로 4, 0, 0, 2cm이다. 손님은 6cm만큼의 길이를 가져간다.
손님이 왔을 때 요청한 총 길이가 M일 때 적어도 M만큼의 떡을 얻기 위해 절단기에 설정할 수 있는 높이의 최댓값을 구하는 프로그램을 작성하시오.

입력
첫째 줄에 떡의 개수 N과 요청한 떡의 길이 M이 주어진다. (1<=N<=1,000,000, 1<=M<=2,000,000,000)
둘째 줄에는 떡의 개별 높이가 주어진다. 떡 높이의 총합은 항상 M 이상이므로, 손님은 필요한 양만큼 떡을 사갈 수 있다. 높이는 10억보다 작거나 같은 양의 정수 또는 0이다.

출력
적어도 M만큼의 떡을 집에 가져가기 위해 절단기에 설정할 수 있는 높이의 최댓값을 출력한다.

입력 예시
4 6
19 15 10 17
출력 예시
15
"""
import sys
import math
input = sys.stdin.readline


def cut_and_sum(array, h):

    sums = 0
    for i in array:
        # 절단기보다 떡 길이가 길면 차이를 합산한다.
        if i >= h:
            sums += i - h
        # 절단기가 떡 길이보다 길면 다 잘린다.
        else:
            sums += 0

    return sums


# 절단기의 이상점 찾기
def binary_search(array, target, start, end):
    while start <= end:

        height = (start + end) // 2
        sums = cut_and_sum(array, height)

        if sums == target:
            return height
        elif sums > target:
            start = height + 1
        else:
            end = height - 1

    return height


if __name__ == '__main__':
    n, m = map(int, input().split())
    array = list(map(int, input().split()))
    array.sort()

    # 예상 리스트는 array 의 최소값과 최대값 사이 값들
    target_array = range(array[-1], array[0], -1)

    # 1. 순차탐색 방법
    for h in target_array:
        target = cut_and_sum(array, h)
        if target >= m:
            print(h)
            break
    print()

    # 2. 이진탐색으로 풀어보기
    start = array[0]
    end = array[-1]
    mid = binary_search(array, m, start, end)
    print(mid)








