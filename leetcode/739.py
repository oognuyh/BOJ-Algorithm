"""
    739. Daily Temperatures
"""
class Solution:
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        n, right_max = len(T), float('-inf')
        res = [0 for _ in range(n)]

        for i in range(n - 1, -1, -1):
            t = T[i]
            
            if right_max <= t:
                right_max = t
            else:
                days = 1
                while T[i + days] <= t:
                    days += res[i + days]
                res[i] = days

        return res

"""
    - 492ms 18.6MB

    # Others
        1. stack - 508 ms 19.7 MB
        ans = [0 for _ in range(len(T))]
        stack = []
        
        for i,v in enumerate(T):
            #check whether current val is greater than the last appended stack value.  We will pop all the elements which is lesser than the current temp
            while stack and stack[-1][1] < v:
                index, value = stack.pop()
                ans[index] = i - index # we are checking how many indices we have crossed since we last have a lesser temperature
            #Remember since we are comparing all the stack elements before inserting,all the stack elements will have temperatures greater than the current value	
            stack.append([i, v])      
        
        return ans
"""