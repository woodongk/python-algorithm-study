def binary_search(array, target, start, end):
    if start > end:
        return None

    mid = (start + end) // 2
    print("target = {}, start = {}, end = {}".format(target, start, end))

    # target 을 찾으면 return index
    if array[mid] == target:
        return mid

    # 중간값이 타겟 값보다 큰 경우 왼쪽 확인
    elif array[mid] > target:
        print("중간값 {}의 왼쪽에 타겟 {}이 있음 ".format(array[mid], target))
        return binary_search(array, target, start, mid - 1)
    # 중간값이 타겟 값보다 작은 경우 오른쪽 확인
    else:
        print("중간값 {}의 오른쪽에 타겟 {}이 있음 ".format(array[mid], target))
        return binary_search(array, target, mid + 1, end)


def binary_search_iter(array, target, start, end):

    while start <= end:
        mid = (start + end) // 2
        print("target = {}, start = {}, end = {}".format(target, start, end))

        # target 을 찾으면 return index
        if array[mid] == target:
            return mid
        # 중간값이 타겟 값보다 큰 경우 왼쪽 확인
        elif array[mid] > target:
            end = mid - 1
        # 중간값이 타겟 값보다 작은 경우 오른쪽 확인
        else:
            start = mid + 1

    return None


if __name__ == '__main__':
    lst = [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]
    n = 4

    result = binary_search(lst, n, 0, len(lst) - 1)
    if result is None:
        print("원소 없다 ")
    else:
        print(result)
    print()
    result = binary_search_iter(lst, n, 0, len(lst) - 1)
    if result is None:
        print("원소 없다 ")
    else:
        print(result)