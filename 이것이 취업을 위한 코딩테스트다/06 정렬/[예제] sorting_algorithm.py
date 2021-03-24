# 선택 정렬
# 시간 복잡도는 O(n^2)
# !특정한 리스트에서 가장 작은 데이터를 찾는 문제에 사용되는 형태임!
def selection_sort(array):
    for i in range(len(array)):
        print(i, array)
        min_index = i  # 최소 값의 인덱스
        for j in range(i + 1, len(array)):
            if array[min_index] > array[j]:
                # 최소값 만나면 swap
                min_index = j
        array[i], array[min_index] = array[min_index], array[i]  # swap
    return array


# 삽입 정렬
# 대부분 정렬된 상태일 경우 O(N)까지 감소함
# 퀵소트보다 좋음 !
def insertion_sort(array):
    for i in range(1, len(array)):
        print(i, array)
        for j in range(i, 0, -1): # i.. 3, 2, 1 /
            if array[j] < array[j - 1]: # 한 칸씩 왼쪽으로 이동
                array[j], array[j - 1] = array[j - 1], array[j]
            else:  # 자기보다 작은 값 만나면 멈춰! (이미 작은 순으로 정렬된 상태이므로)
                break
    return array


def quick_sort(array, start, end):
    print(array)
    if start >= end: # 원소가 1개인 경우 종료
        return

    pivot = start # 첫번째 원소가 피봇(기준)
    left = start + 1
    right = end

    # left 가 right 을 추월하기 전까지 돌기
    while left <= right:
        # pivot 값보다 큰 left 값을 찾을 때까지 loop
        while (left <= end) and (array[left] <= array[pivot]):
            left += 1
        # pivot 값보다 작은 right 값을 찾을 때까지 loop
        while (right > start) and (array[right] >= array[pivot]):
            right -= 1
        # 엇갈렸다면 작은 데이터와 피봇 swap
        if left > right:
            array[right], array[pivot] = array[pivot], array[right]
        # 엇갈리지 않았다면 작은 값과 큰 값을 swap
        else:
            array[left], array[right] = array[right], array[left]

    # 한 단계의 피봇 턴을 마치면 두 리스트로 분할 된 것
    quick_sort(array, start, right - 1)
    quick_sort(array, right + 1, end)


def simple_quick_sort(array):
    if len(array) <= 1:
        return array

    pivot = array[0] # 첫번째 원소가 피봇
    tail = array[1:] # 피봇을 제외한 리스트

    left_side = [x for x in tail if x <= pivot] # 피봇 중심 왼쪽 부분
    right_side = [x for x in tail if x > pivot] # 피봇 중심 오른쪽 부분

    # 분할 이후 왼쪽과 오른쪽에서 각각 정렬 수행, 전체 리스트 반환
    return simple_quick_sort(left_side) + [pivot] + simple_quick_sort(right_side)


if __name__ == '__main__':
    array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]
    print("선택 정렬 결과 :")
    print(selection_sort(array))
    print()
    array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]
    print("삽입 정렬 결과 :")
    print(insertion_sort(array))
    print()
    array = [5, 7, 9, 0, 3, 1, 6, 2, 4, 8]
    print("퀵 정렬 결과 :")
    quick_sort(array, 0, len(array) - 1)
    print(array)
    print()
    print("간단한 퀵 정렬 결과 : ")
    print(simple_quick_sort(array))