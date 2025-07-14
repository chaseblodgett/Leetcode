class Solution(object):
    def minCost(self, colors, neededTime):
        """
        :type colors: str
        :type neededTime: List[int]
        :rtype: int
        """
 
        num_balloons = 0
        for i in range(1, len(colors)):
            if colors[i-1] == colors[i]:
                num_balloons += 1

        if num_balloons == 0:
            return 0

        ret = 0
        i = 1
        while i < len(colors):
            total = neededTime[i-1]
            maximum = neededTime[i-1]
            in_row = False
            while i < len(colors) and colors[i] == colors[i-1]:
                in_row = True
                if neededTime[i] > maximum:
                    maximum = neededTime[i]
                total += neededTime[i]
                i += 1
            
            if not in_row:
                i += 1
            else:
                ret += total - maximum
        
        return ret