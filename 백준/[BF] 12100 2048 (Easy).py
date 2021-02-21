"""
이 문제에서 다루는 2048 게임은 보드의 크기가 N×N 이다.
보드의 크기와 보드판의 블록 상태가 주어졌을 때, 최대 5번 이동해서 만들 수 있는 가장 큰 블록의 값을 구하는 프로그램을 작성하시오.

입력
첫째 줄에 보드의 크기 N (1 ≤ N ≤ 20)이 주어진다.
둘째 줄부터 N개의 줄에는 게임판의 초기 상태가 주어진다.
0은 빈 칸을 나타내며, 이외의 값은 모두 블록을 나타낸다.
블록에 쓰여 있는 수는 2보다 크거나 같고, 1024보다 작거나 같은 2의 제곱꼴이다.
블록은 적어도 하나 주어진다.

출력
최대 5번 이동시켜서 얻을 수 있는 가장 큰 블록을 출력한다.

예제 입력 1
3
2 2 2
4 4 4
8 8 8

예제 출력 1
16
"""
import numpy as np


def move_right(N, array):
    # di = 0 right, di = 1 down
    # di = 2 left, di = 3 up

    # 1. index move
    new_list = [[0] * N for _ in range(N)]

    # 모든 노드 맨 끝으로 이동시키기
    for xi in range(N):
        last = N - 1
        is_sum = False  # sum은 한번만
        for yi in reversed(range(N)):
            node = array[xi][yi]
            # 노드가 없으면 배치
            if new_list[xi][last] is 0:
                new_list[xi][last] = node
            # 노드가 있으면 비교하고 같으면 두배, 안 같으면 last -1
            else:
                if (new_list[xi][last] == node) & (is_sum == False):
                    new_list[xi][last] = node * 2
                    is_sum = True
                else:
                    last -= 1
                    new_list[xi][last] = node
    return new_list


def move_left(N, array):

    # 1. index move
    new_list = [[0] * N for _ in range(N)]

    # 모든 노드 맨 끝으로 이동시키기
    for xi in range(N):
        last = 0
        is_sum = False  # sum은 한번만
        for yi in range(N):
            node = array[xi][yi]
            # 노드가 없으면 배치
            if new_list[xi][last] is 0:
                new_list[xi][last] = node
            # 노드가 있으면 비교하고 같으면 두배, 안 같으면 last -1
            else:
                if (new_list[xi][last] == node) & (is_sum == False):
                    new_list[xi][last] = node * 2
                    is_sum = True
                else:
                    last += 1
                    new_list[xi][last] = node
    return new_list


def move_down(N, array):

    # 1. index move
    new_list = [[0] * N for _ in range(N)]

    # 모든 노드 맨 끝으로 이동시키기
    for yi in range(N):
        last = N - 1
        is_sum = False  # sum은 한번만
        for xi in reversed(range(N)):
            node = array[xi][yi]
            # 노드가 없으면 배치
            if new_list[last][yi] is 0:
                new_list[last][yi] = node
            # 노드가 있으면 비교하고 같으면 두배, 안 같으면 last -1
            else:
                if (new_list[last][yi] == node) & (is_sum == False):
                    new_list[last][yi] = node * 2
                    is_sum = True
                else:
                    last -= 1
                    new_list[last][yi] = node
    return new_list


def move_up(N, array):

    # 1. index move
    new_list = [[0] * N for _ in range(N)]

    # 모든 노드 맨 끝으로 이동시키기
    for yi in range(N):
        last = 0
        is_sum = False  # sum은 한번만
        for xi in range(N):
            node = array[xi][yi]
            # 노드가 없으면 배치
            if new_list[last][yi] is 0:
                new_list[last][yi] = node
            # 노드가 있으면 비교하고 같으면 두배, 안 같으면 last -1
            else:
                if (new_list[last][yi] == node) & (is_sum == False):
                    new_list[last][yi] = node * 2
                    is_sum = True
                else:
                    last -= 1
                    new_list[last][yi] = node
    return new_list


def max_element(array):
    return max(map(max, array))


if __name__ == '__main__':
    N = int(input())

    mylist = [0 for _ in range(N)]
    for i in range(N):
        mylist[i] = list(map(int, input().split()))
    print("Raw matrix ==> ", mylist)
    print()

    # 2. 최대값 찾기
    max_number = max_element(mylist)
    count = 0

    #di =

    di = [0, 1, 2, 3] # right, left, down, up
    while count < 5:
        if di is not None:
            for d in di:
                if di == 0:
                    newlist = move_right(N, mylist)
                    print("move right", newlist)
                    mylist = newlist
                elif di == 1:
                    newlist = move_left(N, mylist)
                    print("move left",newlist)
                    if newlist == mylist:
                        di.remove(1)
                    else:
                        mylist = newlist
                elif di == 2:
                    newlist = move_down(N, mylist)
                    print("move down", newlist)
                    if newlist == mylist:
                        di.remove(2)
                    else:
                        mylist = newlist
                elif di == 3:
                    newlist = move_up(N, mylist)
                    print("move up", newlist)
                    if newlist == mylist:
                        di.remove(3)
                    else:
                        mylist = newlist
        else:
            break;
            break;

    print(max_element(newlist))
