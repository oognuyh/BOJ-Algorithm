"""
    349. Intersection of Two Arrays
"""
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        return list(set(nums1) & set(nums2))

"""
    - 40 ms 14.4 MB

    # Others
        1. two pointers - 51 ms 14.4 MB
            left = right = 0
            result = set()

            while left < len(nums1) and right < len(nums2)
                if nums1[left] == nums2[right]:
                    result.add(nums1[left])
                    left += 1
                    right += 1
                elif nums1[left] > nums2[right]:
                    right += 1
                else:
                    left += 1
"""