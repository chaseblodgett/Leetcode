class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """

        if sum(cost)> sum(gas):
            return -1
        
        highest = -1
        curr_gas = 0
        reached_prev = False
        for i in range(len(gas)):
            
            if gas[i] + curr_gas >= cost[i] and not reached_prev:
                highest = i
                curr_gas += gas[i] - cost[i]
                reached_prev = True
            elif gas[i] + curr_gas <= cost[i]:
                curr_gas = 0
                reached_prev = False
            elif reached_prev:
                curr_gas += gas[i] - cost[i]
            
        return highest