class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        
        max_water = min(height[0], height[1])
        high = len(height) -1
        low = 0

        while(high > low):
            curr = (high-low) * min(height[low], height[high])
            if(curr > max_water):
                max_water = curr
            if(height[low] > height[high]):
                high -= 1
            else:
                low += 1
    
        return max_water