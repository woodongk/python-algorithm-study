"""
예제 입력 1
5
3 5 2 5 9
예제 출력 1
1

6
1 2 1000 2000 10001 10002
0

4
5 5 5 6
`
"""
import itertools
import heapq

if __name__ == '__main__':
    n = int(input())
    numbers = list(map(int, input().split()))
    numbers.sort()
    print(numbers)
    # 1. 조건에 맞는 네 쌍을 추려서 iter 돌리는 방법은 너무 느림. 예상 했음

    # 2. min (a + d) - (b + c) = min(a - b) + min(d - c).
    # 즉, 차이가 적은 두 값을 가져오면 됨

    # 두 쌍 씩 만들기
    two_cases = list(itertools.combinations(list(enumerate(numbers)), 2))

    # 최소 힙 만들어서, (차이, 인덱스) 넣기
    diff_heap = []
    for a, b in two_cases:
        a_idx, a_num = a
        b_idx, b_num = b
        heapq.heappush(diff_heap, (abs(a_num - b_num), (a_idx, b_idx)))
    print(diff_heap)

    # 차이가 적은 순서대로 numbers 에서 빼서 눈사람으로 넣어버려
    diff = []
    snow_idx = []
    while diff_heap:
        df, (a_idx, b_idx) = heapq.heappop(diff_heap)
        if (a_idx not in snow_idx) and (b_idx not in snow_idx):
            snow_idx.append(a_idx)
            snow_idx.append(b_idx)
            diff.append(df)
            print(numbers[a_idx],numbers[b_idx])
    print(diff)
    print(abs(diff[0] - diff[1]))



