class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums1.extend(nums2)
        nums1.sort()
        median = len(nums1)/2
        if len(nums1)%2 != 0:
            return nums1[math.floor(median)]
        else:
            ans = (nums1[int(median)] + nums1[int(median)-1]) / 2
            return ans
        
        