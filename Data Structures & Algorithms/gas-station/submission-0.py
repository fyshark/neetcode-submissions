class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        total_gas, total_cost = 0, 0
        n = len(gas)
        for i in range(n):
            total_gas += gas[i]
            total_cost += cost[i]
        if total_gas < total_cost:
            return -1
        
        start, curr_fuel = 0, 0
        for i in range(n):
            curr_fuel += gas[i] - cost[i]
            if curr_fuel < 0:
                start = i + 1
                curr_fuel = 0
        
        return start