if __name__ == '__main__':

    """
    이 풀이의 경우 케이스 바이 케이스로 하였으나, 완전 탐색으로 전부 탐색하여도 데이터 10000개 정도라 3중 포문도 ㄱㅊ  
    """

    n = int(input())

    cnt = 0

    # 0시 부터 N시 까지
    is_three_hour = [3, 13, 23]
    # 3 이 들어가는 분 초 수 = 3 in 분 + 3 in 초 - 3 in 분초
    m_cases = [x for x in range(0, 60) if "3" in str(x)]
    s_cases = m_cases  # minute = second

    for i in range(0, n + 1):
        if i in is_three_hour:
            cnt += 60 * 60
        else:  # 3 안들어가는 시간
            # 겹치는 경우를 제한다.
            cnt += len(m_cases) * 60 + len(s_cases) * 60 - len(m_cases) * len(s_cases)

    print(cnt)

