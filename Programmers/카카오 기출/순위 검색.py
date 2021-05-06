def solution2(info, query):
    info = [i.split() for i in info]
    query = [q.replace("and",'').split() for q in query]
    print(query)

    answer = []
    for q in query:
        (q1, q2, q3, q4, q5) = q
        print("현재 쿼리 q는 q",q)

        # 1로 좁히고
        cnt = 0
        for (i1, i2, i3, i4, i5) in info:
            if i1 == q1 or q1 == '-':
                if i2 == q2 or q2 == '-':
                    if i3 == q3 or q3 == '-':
                        if i4 == q4 or q4 == '-':
                            if int(i5) >= int(q5):
                                cnt += 1
                            else:
                                continue
                        else:
                            continue
                    else:
                        continue
                else:
                    continue
            else:
                continue
        answer.append(cnt)

    return answer


from collections import defaultdict


def binary_search_iter(array, target, start, end):

    while start <= end:
        mid = (start + end) // 2
        print("target = {}, start = {}, end = {}".format(target, start, end))

        # target 을 찾으면 return index
        if array[mid] == target:
            return mid
        # 중간값이 타겟 값보다 큰 경우 왼쪽 확인
        elif array[mid] > target:
            end = mid - 1
        # 중간값이 타겟 값보다 작은 경우 오른쪽 확인
        else:
            start = mid + 1

    return None


def create_dict_map(lst):
    lst = ["".join(i[:-1]).replace("-", "") for i in lst]
    info_dict = defaultdict(list)


def solution(info, query):
    info = [i.split() for i in info]
    query = [q.replace("and",'').split() for q in query]

    print(create_dict_map(query))

    print(info)
    print(query)
    print()

    info_dict = defaultdict(list)
    for info in infos:
    #
    # check_lst =[]
    # for qry in query:
    #     for ifo in info:
    #         print("!!", qry, ifo)
    #
    #         tmp_answer = [i for q, i in zip(qry, ifo) if bin(q & i) == bin(q) and qry[4] <= ifo[4]]
    #         print(tmp_answer)


    return answer

if __name__ == '__main__':
    info = ["java backend junior pizza 150",
            "python frontend senior chicken 210",
            "python frontend senior chicken 150",
            "cpp backend senior pizza 260",
            "java backend junior chicken 80",
            "python backend senior chicken 50"]
    query = ["java and backend and junior and pizza 100",
             "python and frontend and senior and chicken 200",
             "cpp and - and senior and pizza 250",
             "- and backend and senior and - 150",
             "- and - and - and chicken 100",
             "- and - and - and - 150"]

    print(solution(info, query))
