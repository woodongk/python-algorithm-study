# def solution(phone_book):
#     phone_book = sorted(phone_book, key=lambda x: x[0])
#
#     prefix = phone_book[0] # 최솟값을 prefix로 설정한다.
#     phone_book = phone_book[1:]  # 최솟값 제외한 전화번호 목록 갱신한다.
#
#     while len(phone_book) > 0:
#         for p in phone_book:
#             if str(p).startswith(prefix):
#                 return False
#             else:
#                 continue
#
#         # 발견되지 않았다면 prefix와 phone_book 갱신해준다.
#         prefix = phone_book[0]
#         phone_book = phone_book[1:]
#
#     return True


def solution(phone_book):
    # 예외 처리
    if len(phone_book) == 1:
        return False

    phone_book = sorted(phone_book, key=lambda x: x[0])

    for i in range(len(phone_book) - 1):
        prefix = phone_book[i]
        print(prefix)
        if prefix == phone_book[i + 1][:len(prefix)]:
            return False

    return True


if __name__ == '__main__':
    print(solution(["119", "97674223", "1195524421"]))
    print(solution(["123","456","789"]))
    print(solution(["12","123","1235","567","88"]))

