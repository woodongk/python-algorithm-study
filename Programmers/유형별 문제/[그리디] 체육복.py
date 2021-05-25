def solution(n, lost, reserve):

    # 체육복 수 초기화하기
    closet = [1] * (n)
    for i in lost:
        closet[i - 1] -= 1
    for i in reserve:
        closet[i - 1] += 1
    print(closet)

    # 앞부터 채우기
    for i in range(n):
        if closet[i] == 0: # 도난
            # 2개 가진 애는 앞부터 한번만 체크하게 if else
            if i > 0 and closet[i - 1] == 2:
                closet[i - 1] -= 1
                closet[i] += 1
            elif (i + 1 < n) and closet[i + 1] == 2:
                closet[i + 1] -= 1
                closet[i] += 1

    print(closet)
    return len([i for i in closet if i >= 1])


if __name__ == '__main__':
    print(solution(5, [2, 4],[1, 3, 5]))
    print(solution(5, [2, 4], [3]))
    print(solution(3, [3], [1]))
    print(solution(4, [3, 1, 2], [2, 4, 3]))