from typing import List

class Solution:
    def minOperations(self, nums: List[int]) -> int:
        ans = 0
        stack = []
        
        for x in nums:
            if x == 0:
                # zeros split segments; clear stack
                stack.clear()
                continue
            
            # remove larger values that cannot be extended past this smaller number
            while stack and stack[-1] > x:
                stack.pop()
            
            # if top equals x, this x can be covered by existing operation — skip
            if stack and stack[-1] == x:
                continue
            
            # otherwise start a new operation for x
            stack.append(x)
            ans += 1
        
        return ans
