def solution(phone_book):
    phone_book = sorted(phone_book, key=len)

    prefix = phone_book[0] # 최솟값을 prefix로 설정한다.
    phone_book = phone_book[1:]  # 최솟값 제외한 전화번호 목록 갱신한다.

    while len(phone_book) > 1:
        for p in phone_book:
            if prefix == p[:len(prefix)]:
                return False
            else:
                continue

        # 발견되지 않았다면 prefix와 phone_book 갱신해준다.
        prefix = phone_book[0]
        phone_book = phone_book[1:]

    answer = True
    return answer


if __name__ == '__main__':
    print(solution(["119", "97674223", "1195524421"]))
    print(solution(["123","456","789"]))
    print(solution(["12","123","1235","567","88"]))

