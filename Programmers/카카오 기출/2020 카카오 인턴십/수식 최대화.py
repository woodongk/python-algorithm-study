import re
import collections


# infix to postfix 응용 문제 같음
def cal(num1, num2, operator):
    if operator == '*':
        return num1 * num2
    elif operator == '-':
        return num1 - num2
    elif operator == '+':
        return num1 + num2


def solution(expression):
    # 연산자와 피연산자 받기
    expression_queue = collections.deque([i.strip(' ') for i in re.split(r'(\W+)', expression)])
    operators = list(set([i for i in re.split(r'[\w]',expression) if i != ''])) # 연산자]

    print(operators)
    print(expression_queue)

    orders = ['*', '-', '+'] # 실험, 우선순위 순서

    orders = {
        '*' : 3,
        '-' : 2,
        '+' : 1
    }

    op_stack = [] # 연산자 넣는 스택
    numbers = [] # postfix expression
    result = []

    # queue 가 빌 떄까지
    while True:
        while expression_queue:
            op = expression_queue.popleft()
            print("현재 연산자 : {}".format(op))

            if op.isdigit(): # 숫자일 경우
                numbers.append(op)
            else: # 연산자 일 경우
                if len(op_stack) == 0 or orders[op_stack[-1]] <= orders[op]: # top 보다 연산자 우선순위 클 경우 넣기
                    op_stack.append(op)
                else:
                    while orders[op_stack[-1]] > orders[op]:
                        next_op = op_stack.pop()
                        num1 = int(numbers.pop())
                        num2 = int(numbers.pop())

                        result.append(cal(num1, num2, next_op))
                        print(num1, num2, next_op, result)
                        if len(op_stack) == 0:
                            break
                    result.append(op) # 현재 연산자 넣고,
            print("연산자 스택 : {}, 숫자 스택 {}".format(op_stack, numbers))


    while op_stack or numbers:
        next_op = op_stack.pop()
        num1 = int(numbers.pop())
        num2 = int(numbers.pop())
        result.append(cal(num1, num2, next_op))
    print(result)
    ans = cal(result[0], result[1], result[2])

    return ans


if __name__ == '__main__':
    print(solution("5 * 1 - 3 * 5"))
    print()
    print(solution("100-200*300-500+20"))