from typing import List


def longestCommonSubsequence(text1: str, text2: str) -> int:
    # 공통 subsequence의 최대 길이 찾는 문제
    output = 0

    # 1. 먼저 최소 길이의 text를 찾아서 기준점 설정
    if len(text1) < len(text2):
        min_len_text = text1
        not_min_len_text = text2
    else:
        min_len_text = text2
        text = text1

    # 2. 최소 길이의 text 기준으로 문자 등장 index 찾기
    index_list = []
    for c in min_len_text:
        if text.find(c) != -1: # 문자가 string에 있다면
            index_list.append(text.find(c))
        else:
            index_list.append(-1)

    print(index_list)

    # subsequence index가 오름차순으로 들어가있는 지 체크하고 output 반환
    check_i = index_list[0]
    for i in index_list[1:]:
        if check_i



    print(sorted(index_list))

    # sub sequence 순서가 같을 경우 (순서대로 나올 경우)
    if index_list == sorted(index_list):
        return len(index_list)

    return output


if __name__ == '__main__':
    print(longestCommonSubsequence(text1 = "abcde", text2 = "ace"))
    print(longestCommonSubsequence(text1 = "abcde", text2 = "aec"))
    print(longestCommonSubsequence(text1 = "abc", text2 = "abc"))
    print(longestCommonSubsequence(text1="abcde", text2="aef"))
    print(longestCommonSubsequence(text1="abcde", text2="afc"))
    print(longestCommonSubsequence(text1="abc", text2="def"))
