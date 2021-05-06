import collections

def solution(n, edge):

    answer = 0

    # 그래프 만들기.
    graph = [[] for _ in range(n + 1)]
    for e in edge:
        a, b = e
        graph[a].append(b)
        graph[b].append(a)
    print(graph)

    # 방문 기록 리스트
    visited = [False for _ in range(n + 1)]
    # 1로부터 얼마나 떨어졌는지에 대한 거리 리스트
    distance = [0 for _ in range(n + 1)]

    start = 1

    queue = collections.deque([start])
    distance[start] = 0
    visited[start] = True
    dist = 1

    while queue:
        for _ in range(len(queue)):
            next_v = queue.popleft()
            for v in graph[next_v]:
                if not visited[v]:
                    queue.append(v)
                    distance[v] = dist
                    visited[v] = True
        dist += 1

    max_dist = max(distance)

    return len([i for i in distance if i == max_dist])


if __name__ == '__main__':

    print(solution(6, [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]))
