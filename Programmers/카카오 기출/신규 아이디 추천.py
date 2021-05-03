import re


def solution(new_id):

    # 1
    new_id = new_id.lower()

    # 2
    new_id = re.sub('[^a-z0-9-_.]', '', new_id)

    # 3
    while True:
        temp = new_id.replace("..", ".")
        if len(temp) == len(new_id):
            break
        else:
            new_id = temp

    # 4
    if len(new_id) >= 1 and new_id[0] == '.':
        new_id = new_id[1:]
    if len(new_id) >= 1 and new_id[-1] == '.':
        new_id = new_id[:-1]

    # 5 - 6
    new_id = 'a' if len(new_id) == 0 else new_id[:15]
    new_id = new_id[:-1] if new_id[-1] == '.' else new_id

    # 7
    while len(new_id) < 3:
        new_id += new_id[-1]

    return new_id


if __name__ == '__main__':
    print(solution("...!@BaT#*..y.abcdefghijklm"))
    print(solution("z-+.^."))
    print(solution("=.="))
    print(solution("123_.def"))
    print(solution("abcdefghijklmn.p"))