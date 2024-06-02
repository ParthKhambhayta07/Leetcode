class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        leng = len(nums)
        i = 0
        c = []
        while i != leng:
            if nums[i] not in c:                
                c.append(nums[i])
                i+=1
            else:
                nums.pop(i)
                leng -=1
        
        return len(c)
        