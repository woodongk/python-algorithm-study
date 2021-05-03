import itertools
import collections


def solution(orders, course):

    # 주문 목록을 문자 단위로 나누어 준다.
    orders_splitted = [list(i) for i in orders]

    # 단품 메뉴 별로 개수를 센다.
    single_menu_counter = collections.Counter(list(itertools.chain(*orders_splitted)))
    single_menu_over_two = [(k,v) for (k,v) in single_menu_counter.items() if v >= 2]

    # 코스에 들어갈 수 있는 단품 개수
    unique_menus = sorted([k for k, v in single_menu_over_two])
    result = []

    # 코스의 개수만큼 루프 돈다.
    for num_course in course:
        order_dict = collections.defaultdict(int) # 매 코스마다 새로운 딕셔너리 생성해주기

        # 코스 개수만큼 조합을 생성한다.
        combination_orders = []
        for order in orders_splitted:
            combination_orders += itertools.combinations(sorted(order), num_course)

        most_ordered = collections.Counter(combination_orders).most_common()
        result += [k for k, v in most_ordered if v > 1 and v == most_ordered[0][1]]
    return [ ''.join(v) for v in sorted(result) ]

    #     # 가능한 조합만큼 돌기
    #     for menu_order in combination_orders:
    #         string = "".join(menu_order)
    #         for order in orders_splitted:
    #             check = True
    #             for i in range(len(string)):
    #                 # 먹은 메뉴에 없다면 나가기
    #                 if string[i] not in order:
    #                     check = False
    #                     break
    #             if check:
    #                 print(string, order)
    #
    #                 order_dict[string] += 1
    #     if order_dict:
    #         max_value = max(order_dict.values())
    #         if max_value >= 2:
    #             cs = [k for k, v in order_dict.items() if v == max_value]
    #             answer.append(cs)
    #
    # answer = sorted(list(itertools.chain(*answer)))
    #
    # return answer


if __name__ == '__main__':
    print(solution(["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"],[2,3,4]))
    print()
    print(solution(["ABCDE", "AB", "CD", "ADE", "XYZ", "XYZ", "ACD"], [2,3,5]))
    print()
    print(solution(["XYZ", "XWY", "WXA"], [2,3,4]))


