from collections import defaultdict

class Solution(object):
    def canBeEqual(self, target, arr):
        """
        :type target: List[int]
        :type arr: List[int]
        :rtype: bool
        """
    
        arr_dict = defaultdict(int)
        targ_dict = defaultdict(int)

        if len(target) != len(arr):
            return False
        
        for i in range(len(target)):
            arr_dict[arr[i]] += 1
            targ_dict[target[i]] += 1
        
        for key,value in targ_dict.items():
            if key not in arr_dict.keys() or value != arr_dict[key]:
                return False
        
        return True