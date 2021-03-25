def equation(w, h, x, y):
    return w * y + h * x - w * h


def solution(w, h):
    # 한 변 1일 경우
    if w == 1 or h == 1:
        return 0

    # 정사각형 일 경우
    if w == h:
        return w * h - w

    # 포문 두번..?
    cnt = w * h
    for i in range(0, h + 1):
        for j in range(w + 1):
            print(j, i)
            if equation(w, h, j, i) * equation(w, h, j + 1, i + 1) < 0:
                cnt -= 1

    return cnt


if __name__ == '__main__':
    print(solution(8, 12))