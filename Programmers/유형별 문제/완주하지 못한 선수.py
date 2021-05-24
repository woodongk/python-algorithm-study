from collections import Counter


def solution(participant, completion):
    part = Counter(participant)
    comp = Counter(completion)

    return list((part-comp).keys())[0]


if __name__ == '__main__':
    print(solution(["leo", "kiki", "eden"],["eden", "kiki"]))


