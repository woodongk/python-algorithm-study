"""
Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining.



Example 1:


Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6
Explanation: The above elevation map (black section) is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped.
Example 2:

Input: height = [4,2,0,3,2,5]
Output: 9


Constraints:

n == height.length
0 <= n <= 3 * 104
0 <= height[i] <= 105
"""

from typing import List


def trap(height: List[int]) -> int:

    if len(height) == 0:
        return 0

    rain_drop = 0
    max_height = max(height)

    for _ in range(max_height):
        print(height, rain_drop)
        rain_drop += count_rain(height)
        # 한칸씩 올라가기
        height = [i - 1 if i > 0 else 0 for i in height]

    return rain_drop


# 사이에 0 있으면 rain drop count update
def count_rain(height_line):
    # 값 있으면 True, 없으면 False
    visited = [True if i != 0 else False for i in height_line]
    n = len(visited)
    if True not in visited:
        return 0

    start = 0
    end = n - 1
    while start < n & end >= 0:
        start += 1
        end -= 1
        if (visited[start] == True) & (visited[end] == True):
            break

    # start = visited.index(True)
    # end = len(visited) - visited[::-1].index(True) - 1
    print("start{} end{}".format(start, end))
    rain = visited[start:end + 1].count(0)
    return rain


if __name__ == '__main__':
    print(trap([4,2,0,3,2,5]))
