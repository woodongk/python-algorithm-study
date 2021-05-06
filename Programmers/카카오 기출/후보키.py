import collections
import itertools
import copy


# relation 이 유일성을 만족하는지 판별하는 함수.
def check_uniqueness(tuple_lst):
    return True if len(tuple_lst) == len(collections.Counter(tuple_lst)) else False


# relation 이 최소성을 만족하는지 판별하는 함수.
def check_minimal(case, relation):
    checkFlag = True
    for i in range(len(case)):
        tmp_case = list(copy.deepcopy(case))
        del tmp_case[i]
        tmp_lst = extract_relation(tmp_case, relation)
        if check_uniqueness(tmp_lst):
            checkFlag = False
            break

    # 최소성을 만족하지 않으면 False, 만족한다면 True
    return False if checkFlag is False else True


# 주어진 인덱스에 해당하는 relation column 을 추출해주는 함수.
def extract_relation(case, relation):
    tuple_lst = []
    for rel in relation:
        tuple_lst.append(tuple([rel[i] for i in list(case)]))
    return tuple_lst


def solution(relation):
    answer = []

    # 칼럼 인덱스 리스트. (0 ~ n_cols)
    n_cols = [i for i in range(len(relation[0]))]

    # combination 라이브러리로 모든 케이스 만들기.
    all_cases = []
    for i in range(len(n_cols) + 1):
        all_cases += list(itertools.combinations(n_cols, i))
    print(all_cases)

    # 특정 케이스에 해당하는 relation 을 tuple in list 형태로 extract 하기.
    for case in all_cases:
        tmp = extract_relation(case, relation)
        # 유일성 & 최소성 체크
        if check_uniqueness(tmp) and check_minimal(case, relation):
            answer.append(case)

    print(answer)

    return len(answer)


if __name__ == '__main__':
    print(solution([["100", "ryan", "music", "2"],
                    ["200", "apeach", "math", "2"],
                    ["300", "tube", "computer", "3"],
                    ["400", "con", "computer", "4"],
                    ["500", "muzi", "music", "3"],
                    ["600", "apeach", "music", "2"]]))
