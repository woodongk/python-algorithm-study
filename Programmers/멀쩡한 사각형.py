from math import gcd


def solution(w, h):
    # 한 변 1일 경우
    if w == 1 or h == 1:
        return 0

    # 정사각형 일 경우
    if w == h:
        return w * h - w

    g = gcd(w, h)
    #print(g)

    small_w = int(w / g)
    smalL_h = int(h / g)
    deleted = small_w + smalL_h - 1
    cnt = w * h - deleted * g

    return cnt


if __name__ == '__main__':
    print(solution(8, 12))