from typing import List


class Solution:
    def isMatch(self, s: str, p: str) -> bool:

        # '*' matches any sequence.
        if p == "*":
            return True

        # if no wildcard, is_equal
        if not ("*" in p or "?" in p):
            return s == p

        idx_p = idx_s = 0

        chk = True
        while idx_s < len(s) and idx_p < len(p):
            print(idx_s, idx_p)

            # '?' Matches any single character.
            if p[idx_p] == "?":
                print("char is ?")
                idx_s += 1
                idx_p += 1

            # '*' Matches any sequence of characters (including the empty sequence).
            elif p[idx_p] == "*":
                print("char is *")
                while idx_s < len(s) and idx_p < len(p):
                    print("durl",idx_s, idx_p, s[idx_s],p[idx_p])
                    # empty matching
                    try:
                        if s[idx_s] == p[idx_p + 1]:
                            if (idx_s == len(s) - 1) and (idx_p + 1 == len(p) - 1):
                                return True
                            idx_s += 1
                            idx_p += 2
                            break
                        else:
                            idx_s += 1
                    except IndexError:
                        return True

            else:
                print("char is not wildcard")
                chk = (s[idx_s] == p[idx_p])
                idx_s += 1
                idx_p += 1

            if chk is False:
                return False


if __name__ == '__main__':
    sol = Solution()
    print(sol.isMatch(s = "aa", p = "a"))
    print(sol.isMatch(s="aa", p="a*"))
    print(sol.isMatch(s = "aa", p = "*"))
    print(sol.isMatch(s = "cb", p = "?a"))
    print(sol.isMatch(s = "adceb", p = "*a*b"))
    print()
    print(sol.isMatch(s = "acdcb", p = "a*c?b"))

