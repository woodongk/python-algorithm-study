def solution(name):
    name = list(name)
    cnt = 0

    i = 0
    while True:
        # 알파벳 바꾸기
        cnt += min(ord(name[i]) - ord('A'), ord('Z') - ord(name[i]) + 1)
        name[i] = 'A'

        if name.count('A') == len(name):
            return cnt

        left, right = 1, 1
        # 왼쪽으로 갔을 때 최초의 A 아닌 문자 찾기
        for l in range(1, len(name)):
            if name[i - l] == "A":
                left += 1
            else:
                break
        # 오른쪽으로 갔을 때 최초의 A 아닌 문자 찾기
        for r in range(1, len(name)):
            if name[i + r] == "A":
                right += 1
            else:
                break

        if right <= left:
            cnt += right
            i += right
        else:
            cnt += left
            i -= left

    return cnt


if __name__ == '__main__':
    print(solution("AAJ"))
    print(solution("JAN"))
    print(solution("ZZZAAAZ"))
