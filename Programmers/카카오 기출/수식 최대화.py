import re
import itertools
from copy import deepcopy


def cal(num1, num2, operator):
    if operator == '*':
        return num1 * num2
    elif operator == '-':
        return num1 - num2
    elif operator == '+':
        return num1 + num2


def solution(expression):

    # 숫자와 연산자를 분리한다.
    expr_lst = [x.strip(' ') for x in re.split('(\W+)', expression)]

    # 연산자와 피연산자를 따로따로 받아준다.
    numbers = [] # 피연산자
    operators = [] # 연산자
    for tk in expr_lst:
        if tk in ['*', '-', '+']:
            operators.append(tk)
        else:
            numbers.append(tk)

    # 순열조합 라이브러리 사용하여 3! 경우의 수 order list 받아준다.
    orders_lst = list(itertools.permutations(['*', '-', '+'], 3))
    values = []
    for order in orders_lst:
        tmp_nums = deepcopy(numbers)
        tmp_ops = deepcopy(operators)
        for op in order:
            while True:
                # 연산자가 존재하면 while 문 작동하게끔.
                if op in tmp_ops:
                    # 연산자의 인덱스를 찾아서 저장한 뒤, 숫자들의 배열에서 같은 인덱스와 그 다음 인덱스를 꺼내 계산해준다.
                    idx = tmp_ops.index(op)
                    num1, num2 = int(tmp_nums[idx]), int(tmp_nums[idx + 1])
                    cal_result = cal(num1, num2, op)

                    # 스택에서 제거해준다. 이때 인덱스가 밀린 상태니까 주의할 것
                    tmp_ops.pop(idx)
                    tmp_nums.pop(idx)
                    tmp_nums.pop(idx)
                    # 결과값은 숫자 스택에 다시 넣어준다.
                    tmp_nums.insert(idx, cal_result)
                # 연산자가 존재하지 않으므로 다음 연산자로 넘어간다.
                else:
                    break
        values.append(abs(cal_result))

    return max(values)


if __name__ == '__main__':

    print(solution("100-200*300-500+20"))