'''
피보나치 0과 1 call 개수 구하기
'''


def fibo_recursive(n):
    """
    fibonacci recursive
    """
    if (n == 1) or (n == 2):
        return 1
    else:
        return fibo_recursive(n - 1) + fibo_recursive(n - 2)


def fibo_memoization(n, memo):
    """
    fibonacci memoization (top down)
    """

    # memo list initialized with null
    memo = [None] * (n + 1)

    if memo[n-1] is not None:
        return memo[n]
    if (n == 1) or (n == 2):
        return 1
    else:
        result = fibo_memoization(n - 1, memo) + fibo_memoization(n - 2, memo)
    memo[n] = result
    return result


def fibo_bottom_up(n):
    """
    bottom up approach
    """
    if (n == 1) or (n == 2):
        return 1
    bottom_up_lst = [None] * (n + 1)
    bottom_up_lst[1] = 1
    bottom_up_lst[2] = 1

    for i in range(3, n+1):
        bottom_up_lst[i] = bottom_up_lst[i - 1] + bottom_up_lst[i - 2]

    return bottom_up_lst[n]


if __name__ == '__main__':
    T = int(input())

    for _ in range(T):
        N = int(input())

        if N == 0:
            print(1, 0)
        elif N == 1:
            print(0, 1)
        else:
            print(fibo_bottom_up(N - 1), fibo_bottom_up(N))
