from typing import List


class Solution:
    def canJump_sol(self, nums: List[int]) -> bool:

        if len(nums) == 1:
            return True

        # start index is always 0
        start_jump = nums[0]
        if start_jump == 0:
            return False

        # 최대 num 에 대한 리스트이므로 점프는 1~n 가능함
        flag = False
        while flag is False:
            idx = 0
            for jump in range(start_jump, 0, -1):
                jump = nums[idx]
                idx = idx + jump # update position
                print("next pos is {} jump is {}".format(idx, jump))

                # 가능한 점프 거리가 0이면 진행 불가능
                if jump == 0:
                    flag = True
                # 마지막 위치에 도달하면 break
                if idx == len(nums) - 1:
                    return True

        return False

    def canJump(self, nums: List[int]) -> bool:

        if len(nums) == 1:
            return True

        # start index is always 0
        start_jump = nums[0]
        if start_jump == 0:
            return False








if __name__ == '__main__':
    sol = Solution()
    # print(sol.canJump(nums = [2,3,1,1,4]))
    # print(sol.canJump(nums = [3,2,1,0,4]))
    # print(sol.canJump(nums=[0]))
    print(sol.canJump(nums=[2, 0]))
    print(sol.canJump(nums=[1, 2]))
    print(sol.canJump(nums=[2, 0, 0]))
