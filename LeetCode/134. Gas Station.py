from typing import List


class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:

        answer = -1

        # 노드 시작부터 끝까지 계속 돌기
        for start_node in range(len(gas)):
            gas_tank = 0
            node = start_node
            first_check = False
            while True:
                # 기름 채우면서 이동하기
                if first_check is False:  # 초기 주유소
                    gas_tank += gas[node]
                    first_check = True
                    if gas_tank == 0:  # 채워도 0 -> 다음 journey 불가
                        break
                else:  # 초기 이후 주유소
                    if gas_tank - cost[node - 1] >= 0:
                        gas_tank = gas_tank - cost[node - 1] + gas[node]
                    else:
                        break
                node += 1  # 다음 주유소로 이동
                node = node % len(gas)

                # 노드가 초기로 돌아갈 경우 out
                if node == start_node and (gas_tank - cost[node - 1] >= 0):
                    return start_node
                    break

        return -1


if __name__ == '__main__':
    sol = Solution()
    print(sol.canCompleteCircuit(gas = [1,2,3,4,5], cost = [3,4,5,1,2]))
    print(sol.canCompleteCircuit(gas=[2,3,4], cost=[3, 4, 3]))
    print(sol.canCompleteCircuit(gas=[4,0,1], cost=[3, 2,1]))