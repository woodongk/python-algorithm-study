import heapq

#
# def solution(scoville, K):
#     answer = 0
#     heapq.heapify(scoville) # list to heap
#     print(scoville)
#
#     # K 보다 작은 스코빌지수 음식이 없을 경우 바로 리턴
#     if len([i for i in scoville if i < K]) == 0:
#         return 0
#
#     # K 보다 작은 스코빌지수 음식 없을 때까지 루프
#     while scoville[0] < K:
#         if len(scoville) <
#         # 적어도 2개 이상 있어야 루프 돌 수 있으므로
#         if len(scoville) >= 2:
#             new_food = heapq.heappop(scoville) + heapq.heappop(scoville) * 2
#             heapq.heappush(scoville, new_food)
#             answer += 1
#             if scoville[0] >= K:
#                 break
#         # 원소가 2개 미만일 경우 매운 음식 생성 불가
#         else:
#             return -1
#
#     return answer

# 더 짧게
import heapq


def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)  # list to heap

    # K 보다 작은 스코빌지수 음식 없을 때까지 루프
    while scoville[0] < K:
        if len(scoville) <= 1:
            return -1
            break
        new_food = heapq.heappop(scoville) + heapq.heappop(scoville) * 2
        heapq.heappush(scoville, new_food)
        answer += 1
    return answer


if __name__ == '__main__':
    print(solution([1, 2, 3, 9, 10, 12]	,7))
    print(solution([1, 2, 3, 9, 10, 12], 0))