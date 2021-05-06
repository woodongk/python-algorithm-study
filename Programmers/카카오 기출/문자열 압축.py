import collections


def comperess(s, n):
    small_s = ''
    for i in range(len(s)):
        j = 1
        while s[i] == s[i + j]:
            j += 1
        small_s += s[i]
        i += j
    return small_s


def solution(s):

    n = 1 # 나눌 개수
    s = list(s)
    print([s[i * n:(i + 1) * n] for i in range((len(s) + n - 1) // n)])
    unique_sub_s = set(["".join(s[i * n:(i + 1) * n]) for i in range((len(s) + n - 1) // n)])

    min_value =
    for n in range(1, len(s) + 1):
        splitted_s = ["".join(s[i * n:(i + 1) * n]) for i in range((len(s) + n - 1) // n)]
        print(splitted_s)
        print(unique_sub_s)

    print(unique_sub_s)

    answer = 0
    return answer


if __name__ == '__main__':
    print(solution("aabbaccc"))
    # print(solution("ababcdcdababcdcd"))
    # print(solution("abcabcdede"))
    # print(solution("abcabcabcabcdededededede"	))
    # print(solution("xababcdcdababcdcd"))

