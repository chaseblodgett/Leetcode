class Solution(object):
    
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        def rec(target, arr, subarray, answer):
            if sum(subarray) == target:
                answer.append(list(subarray))
                return
            
            if sum(subarray) > target:
                return
            
            if not arr:
                return
            
            for i in range(len(arr)):
                subarray.append(arr[i])
                rec(target, arr[i:], subarray, answer)
                subarray.pop()
            

        answer = []
        rec(target, candidates, [], answer)
        return answer