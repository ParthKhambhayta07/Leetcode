class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        l = []        
        hasht = {}
        for i in nums:
            if i in hasht.keys():
                val = hasht[i]
                hasht[i] = val + 1
            else:
                hasht[i] = 1        

        counts_list = sorted(hasht.items(), key=lambda x:x[1], reverse=True)
        sorted_counts = dict(counts_list[:k])

        return [num for num in sorted_counts]
                
        
        