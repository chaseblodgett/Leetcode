from collections import defaultdict
class Solution(object):
    def maxNumberOfBalloons(self, text):
        """
        :type text: str
        :rtype: int
        """

        my_dict = {}

        for let in text:
            if let in "balloon":
                if let in my_dict.keys():
                    my_dict[let] += 1
                else:
                    my_dict[let] = 1
    

        print(my_dict)
        count = 0
        while True:

            for key in "balloon":
                if key not in my_dict.keys():
                    return count
                else:
                    my_dict[key] -= 1
                
                if my_dict[key] < 0:
                    return count
            
            count += 1
        
        return count