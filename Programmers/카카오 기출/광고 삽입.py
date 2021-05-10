
def time_to_seconds(time_string):
    h, m, s = map(int, time_string.split(":"))
    return h * 60 * 60 + m * 60 + s


def seconds_to_time(seconds):
    h = seconds // 3600
    seconds -= h * 3600
    h = "0"+str(h) if h < 10 else str(h)

    m = seconds // 60
    seconds -= m * 60
    m = "0" + str(m) if m < 10 else str(m)

    s = seconds
    s = "0" + str(s) if s < 10 else str(s)

    return h+":"+m+":"+s


def solution(play_time, adv_time, logs):

    # 둘의 시간이 같다면 바로 반환하기
    if play_time == adv_time:
        return "00:00:00"

    # 1. 초 단위의 리스트 형태로 변환하기
    play_time = time_to_seconds(play_time)
    adv_time = time_to_seconds(adv_time)
    time_view_lst = [0 for i in range(play_time + 1)]

    # 2. 로그를 start, end 로 나누고 해당 구간마다 카운트 세어준다.
    for log in logs:
        start, end = log.split("-")

        start_seconds = time_to_seconds(start)
        end_seconds = time_to_seconds(end)
        for i in range(start_seconds, end_seconds + 1):
            time_view_lst[i] += 1

    # 3. 가장 많이 본 누적 구간 찾기
    view_point = 1
    most_view = 0
    cum_sum = sum(time_view_lst[0:0 + adv_time])
    for i in range(0, play_time - adv_time + 1):
        cum_sum = cum_sum - time_view_lst[i - 1] + time_view_lst[i + adv_time]
        if cum_sum > most_view:
            view_point = i
            most_view = cum_sum
    print(sum(time_view_lst[time_to_seconds("01:00:00"):time_to_seconds("01:00:00")+adv_time+1]))
    print(most_view)
    return seconds_to_time(view_point)


if __name__ == '__main__':
    print(solution("02:03:55","00:14:15",
                   ["01:20:15-01:45:14", "00:40:31-01:00:00", "00:25:50-00:48:29", "01:30:59-01:53:29", "01:37:44-02:02:30"]))
    print(solution("99:59:59","25:00:00",["69:59:59-89:59:59", "01:00:00-21:00:00", "79:59:59-99:59:59", "11:00:00-31:00:00"]))
