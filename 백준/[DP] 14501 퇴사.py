def get_maximum_payment(N, time_list):
    # 1. add pi / ti to list
    time_list = [[ti, pi, pi/ti] for ti,pi in time_list]

    # 2. sort in large pi / ti order
    sorted_time_list = sorted(time_list, key=lambda x: x[2], reverse=True)
    print(sorted_time_list)

    # 3. get maximum
    work_time = []
    payment = 0
    for i, t, p, tp_ratio in enumerate(sorted_time_list):
        print("checkpoint", i, t, p, tp_ratio)
        # when time is not over N
        if (i + 1) + t <= N:






    # compute maximum payment
    payment = 0


if __name__ == '__main__':
    N = int(input())

    time_table = []

    for _ in range(N):
        tp = list(map(int, input().split()))
        time_table.append(tp)

    print(time_table)
    print(get_maximum_payment(N, time_table))
