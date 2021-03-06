"""
각 자리가 숫자(0부터 9)로만 이루어진 문자열 S가 주어졌을 때,
왼쪽부터 오른쪽으로 하나씩 모든 숫자를 확인하며 숫자 사이에
‘*’ 혹은 ‘+’ 연산자를 넣어 결과적으로 만들어질 수 있는
가장 큰 수를 구하는 프로그램을 작성하세요.
단, +보다 X를 먼저 계산하는 일반적인 방식과는 달리,
모든 연산은 왼쪽에서부터 순서대로 이루어진다고 가정합니다.

예를 들어 02984라는 문자열이 주어지면,
만들어질 수 있는 가장 큰 수는 ((((0+2) 9) 8) * 4) = 576 입니다.

입력 예시1:
02984

출력 예시1:
576

입력 예시2:
567

출력 예시2:
210
"""


def solution(s):
    # 예외 처리 / s가 0일 경우 0
    if s == 0:
        return 0

    # s가 1자리 일 경우 바로 리턴
    if len(s) == 0:
        return s

    # s의 앞자리가 0일 경우 0이 아닐때까지 s 자르기 (결과 변화 없음)
    for i in range(len(s) - 1):
        if s[i] == 0:
            s = s[i + 1:]
        else:
            break

    # s 앞자리가 0이 아닌 경우 첫째 자리 부터 계산 진행
    re = s[0]
    for i in range(1, len(s)):
        if s[i] <= 1 or re <= 1:
            re += s[i]
        else:
            re *= s[i]
    return re


if __name__ == '__main__':
    s = list(map(int, list(input())))
    print(solution(s))