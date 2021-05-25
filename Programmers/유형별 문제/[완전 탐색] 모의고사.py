def solution(answers):

    one = [1, 2, 3, 4, 5] # 5
    two = [2, 1, 2, 3, 2, 4, 2, 5] # 8
    three = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5] # 10

    cnts = [0, 0, 0] # counts of (one, two, three)
    for i in range(len(answers)):
        if one[i % 5] == answers[i]:
            cnts[0] += 1
        if two[i % 8] == answers[i]:
            cnts[1] += 1
        if three[i % 10] == answers[i]:
            cnts[2] += 1
    print(cnts)
    max_value = max(cnts)

    re = []
    for i, count in enumerate(cnts):
        if count == max_value:
            re.append(i+1)

    return re


if __name__ == '__main__':
    print(solution([1,2,3,4,5]))
    print()
    print(solution([1,3,2,4,2]))