"""
6 4
1 4
2 3
2 4
5 6
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

    # union 연산하기
    for i in range(e):
        a, b = map(int, input().split())
        union_parent(parent, a, b)

    # 각 원소가 속한 집합 추력하기
    print("각 원소 속한 집합: ",end='')
    for i in range(1, v + 1):
        print(find_parent(parent, i), end=' ')
    print()

    print("부모 테이블: ",end='')
    for i in range(1, v + 1):
        print(parent[i], end=' ')
    print()

