class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """

        for i in range(len(digits)-1, -1, -1):
            if digits[i] == 9 and i == 0:
                digits[i] = 0
                digits.insert(0,1)
            elif digits[i] == 9:
                digits[i] = 0
            else:
                digits[i] += 1
                break
        
        return digits