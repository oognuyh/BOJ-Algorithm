"""
    42. Trapping Rain Water
"""
class Solution:
    def trap(self, height: List[int]) -> int:
        if not height: return 0
        
        left, right = 0, len(height) - 1
        max_left, max_right = height[left], height[right] 
        volumn = 0
        
        while left < right:
            max_left, max_right = max(max_left, height[left]), max(max_right, height[right])            
            
            if max_left < max_right:
                volumn += max_left - height[left]
                left += 1
            else:
                volumn += max_right - height[right]
                right -= 1
        
        return volumn

"""
    - 52 ms	14.9 MB

    # Others
        1. stack - 56 ms 14.9 MB
            stack = []
            water = 0
            for i, e in enumerate(height):
                # we need to see if we can form a container
                while stack and e >= stack[-1][0]:
                    popped, _ = stack.pop()
                    # is it a container though? we have a left border?
                    if stack:
                        left_border, j = stack[-1]
                        # we compute the water
                        water += min(left_border-popped, e-popped)*(i-j-1)
                stack.append((e,i))
            return water
   
        2. for - 56 ms 16 MB
            waterLevel = []
            left = 0
            for h in height:
                left = max(left, h) 
                waterLevel += [left] # over-fill it to left max height
            right = 0
            for i, h in reversed(list(enumerate(height))):
                right = max(right, h)
                waterLevel[i] = min(waterLevel[i], right) - h # drain to the right height
            return sum(waterLevel)
"""