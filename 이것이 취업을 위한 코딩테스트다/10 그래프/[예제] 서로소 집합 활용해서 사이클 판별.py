"""
3 3
1 2
1 3
2 3
"""


def find_parent(parent, x):
    # 루트 노드가 아니라면 루트 노드 찾을 때까지 호출
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]


def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b


if __name__ == '__main__':
    v, e = map(int, input().split())
    parent = [0] * (v + 1) # 부모 테이블 초기화
    for i in range(1, v + 1):
        parent[i] = i # 부모를 자기 자신으로 초기화

    nodes = []
    # union 연산하기
    for i in range(e):
        a, b = map(int, input().split())
        union_parent(parent, a, b)
        nodes.append(a)
        nodes.append(b)

    cycle = False  # 사이클 발생 여부

    for node in nodes:
        if find_parent(parent, node) == node:
            check = True
            break

    if check:
        print("is cycle")
    else:
        print("no cycle")
