'''
Figure 1에 나와있는 것 처럼, 순열 그래프 (3, 2, 7, 8, 1, 4, 5, 6) 에는 총 3개의 사이클이 있다. 이러한 사이클을 "순열 사이클" 이라고 한다.

N개의 정수로 이루어진 순열이 주어졌을 때, 순열 사이클의 개수를 구하는 프로그램을 작성하시오.

입력
첫째 줄에 테스트 케이스의 개수 T가 주어진다.
각 테스트 케이스의 첫째 줄에는 순열의 크기 N (2 ≤ N ≤ 1,000)이 주어진다.
둘째 줄에는 순열이 주어지며, 각 정수는 공백으로 구분되어 있다.

출력
각 테스트 케이스마다, 입력으로 주어진 순열에 존재하는 순열 사이클의 개수를 출력한다.

예제 입력 1
2
8
3 2 7 8 1 4 5 6
10
2 1 3 4 5 6 7 9 10 8
예제 출력 1
3
7
'''


def dfs_1(n_arry, arry):
    check = [0] * (n_arry + 1)
    bfs_lst = []

    for idx in range(1, n_arry + 1):
        cycle_list = []

        # 1. if not checked
        if check[idx] != 1:

            # first element
            value = arry[idx]
            cycle_list.append(value)
            check[idx] = 1

            # 2. link to others
            while check[value] != 1:
                new_id = value
                value = arry[new_id]
                cycle_list.append(value)
                check[new_id] = 1

                # print("2", idx, value, cycle_list, check)

        # 3. append
        if len(cycle_list) > 0:
            bfs_lst.append(cycle_list)

    return bfs_lst


# simpler
def dfs(idx):
    visited[idx] = True
    next_node = arry[idx]
    print(idx, next_node)
    if visited[next_node] is not True:
        dfs(next_node)


if __name__ == '__main__':

    for _ in range(int(input())):
        n = int(input())
        arry = [0] + list(map(int, input().split()))
        visited = [0] * (n + 1)
        print(arry, visited)
        num_of_cycles = 0

        for i in range(1, n+1):
            if not visited[i]:
                dfs(i)
                num_of_cycles += 1

        print(num_of_cycles)
