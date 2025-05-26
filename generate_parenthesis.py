class Solution(object):
    def gen_rec(self, n, curr, ret):
        if n == 0:
            stack = []
            valid = True
            for let in curr:

                if let == "(":
                    stack.append(let)
                else:
                    if stack and stack[-1] == "(":
                        stack.pop()
                    else:
                        valid = False
                        break
            
            if valid and not stack and curr not in ret:
                ret.append(curr)
            return
        
        self.gen_rec(n-1, curr + "(", ret)
        self.gen_rec(n-1, curr + ")", ret)
        
            

    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        if n <= 0:
            return []
        
        ret = []
        curr = ""
        self.gen_rec(2*n, curr, ret)
        return ret