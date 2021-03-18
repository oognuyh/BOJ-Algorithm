"""
    15. 3Sum
"""
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        results = set()
        nums.sort()
        nums_length = len(nums)

        for i in range(nums_length - 2):
            if i > 0 and nums[i] == nums[i - 1]: continue

            left, right = i + 1, nums_length - 1

            while left < right:
                s = nums[i] + nums[left] + nums[right]
                if s < 0:
                    left += 1
                elif s > 0:
                    right -= 1
                else:
                    results.add((nums[i], nums[left], nums[right]))
                    
                    left += 1
                    right -= 1

        return results

"""
    - 892 ms 17.3 MB

    # Others
        1. set instead of list - 892 ms	17.4 MB	
            results = set()
            nums.sort()
            nums_length = len(nums)

            for i in range(nums_length - 2):
                if i > 0 and nums[i] == nums[i - 1]: continue

                left, right = i + 1, nums_length - 1

                while left < right:
                    s = nums[i] + nums[left] + nums[right]
                    if s < 0:
                        left += 1
                    elif s > 0:
                        right -= 1
                    else:
                        results.add((nums[i], nums[left], nums[right]))
                        
                        left += 1
                        right -= 1
            
            return result

        2. the sum of 3 integers a <= b <= c to be 0 you can either have: a = 0, b= 0, c=0 or a<0 , c > 0 and b = -(a+c) - 688 ms 17.7 MB
            neg = defaultdict(int)
            pos = defaultdict(int)
            for x in nums:
                if x>0 : pos[x] +=1
                else: neg[x] += 1
                    
            ans = set()
            if 0 in neg and neg[0] >= 3:
                ans.add((0,0,0))
            for x in neg:
                for y in pos:
                    if -x-y == y and pos[y] <2 or -x-y == x and neg[x] < 2:
                        continue
                    if -x-y in pos or -x-y in neg :
                        ans.add(tuple(sorted([x,y,-x-y])))

            return list(ans)
"""