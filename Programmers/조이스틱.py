def get_count(char):
    alphabets = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
                 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

    if char == 'A':
        return 0
    else:
        return min(alphabets.index(char), alphabets[::-1].index(char) + 1)


def solution(name):

    dp = [0] * len(name)
    dp[0] = get_count(name[0])

    for i in range(len(name)):
        dp[i] = get_count(name[i])
    print(dp)

    for i in range(1, len(name)):
        dp[i] += min(dp[i - 1] + 1, dp[i - 1] + (len(name) - i - 1))

        print(dp)


if __name__ == '__main__':
    print(solution("JEROEN"))
    print(solution("JAN"))