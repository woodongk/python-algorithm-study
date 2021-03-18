"""
노드 1을 시작 노드로 하여 DFS와 BFS로 하여 방문한 순서대로 출력하라.
"""
import collections


def dfs(graph, v, visited):
    # 현재 노드를 방문 처리
    visited[v] = True
    print(v, end=' ')
    # 현재 노드와 연결된 인접 노드를 재귀적으로 방문
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)
            visited[i] = True


def bfs(graph, start, visited):
    # 초기 큐 정의, start 노드를 삽입
    queue = collections.deque([start])
    # 현재 노드를 방문 처리
    visited[start] = True

    # 큐가 빌 때까지 방문
    while queue:
        # 큐에서 하나의 원소 뽑아 출력
        v = queue.popleft()
        print(v, end = ' ')
        # 재귀적으로 방문, 큐에 삽입
        for i in graph[v]:
            if not visited[i]:
                visited[i] = True
                queue.append(i)


if __name__ == '__main__':
    n = 8

    graph = [
        [],
        [2, 3, 8],
        [1, 7],
        [1, 4, 5],
        [3, 5],
        [3, 4],
        [7],
        [2, 6, 8],
        [1, 7]
    ]
    visited = [False] * (n + 1)
    dfs(graph, 1, visited)
    print()
    visited = [False] * (n + 1)
    bfs(graph, 1, visited)


