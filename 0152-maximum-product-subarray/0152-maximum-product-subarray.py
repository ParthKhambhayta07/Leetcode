class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        ans = max(nums)
        curmax, curmin = 1,1
        
        for i in nums:
            if i == 0:
                curmax, curmin = 1,1
                continue
            tmp =  curmax * i
            curmax  = max(curmax * i, curmin * i, i)
            curmin  = min(tmp, curmin * i, i)
            
            ans = max(ans,curmax)
            
        return ans