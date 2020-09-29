from typing import List


def longestCommonPrefix(strs: List[str]) -> str:

    if len(strs) > 0:
        min_str = strs[0]
        for s in strs:
            if len(s) <= len(min_str):
                min_str = s
    else:
        return ""

    default = ""

    for i in range(len(min_str), 0, -1):
        prefix = min_str[:i]
        print("prefix!", prefix)

        check = 0
        for s in strs:
            if s.startswith(prefix) == True:
                check += 1
                print(i, s, check)

            if check == len(strs):
                return prefix

    return default


if __name__ == '__main__':
    print(longestCommonPrefix(["flower","flow","flight"]))
    print(longestCommonPrefix(["dog","racecar","car"]))
