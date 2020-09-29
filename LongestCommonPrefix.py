from typing import List


def longestCommonPrefix(strs: List[str]) -> str:

    min_str = strs[0]
    for s in strs:
        if len(s) <= len(min_str):
            min_str = s


    for i in range(len(min_str),0,-1):
        check = False
        check_i = 0
        print("i",i)
        for s in strs:


            check *= s.startswith(min_str)
            if check == True:
                print("fuck",i, s)
                check_i = i
                break;

    print("check index",check_i)

    return min_str[:check_i]


if __name__ == '__main__':
    print(longestCommonPrefix(["flower","flow","flight"]))
    print(longestCommonPrefix(["dog","racecar","car"]))
