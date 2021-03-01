import re


def isPalindrome(s: str) -> bool:

    # 알파벳과 숫자만 사용하니까......
    alphabets = [chr(c).lower() for c in range(65, 65 + 26)]
    numbers = [str(i) for i in range(0, 10)]

    clean_s = s.lower()
    clean_s = [c for c in clean_s if c in alphabets + numbers]

    if clean_s == clean_s[::-1]:
        return True
    else:
        False


def faster_isPalindrome(s: str) -> bool:

    s = s.lower()
    s = re.sub('[^a-z0-9]', '', s) # 암기할 것!!

    return s == s[::-1]


if __name__ == '__main__':
    string = "A man, a plan, a canal: Panama"

    print(isPalindrome(string))
    print(faster_isPalindrome(string))