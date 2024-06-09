class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hasht = {}
        for i in strs:
            strt = ''.join(sorted(i))
            if strt in hasht.keys():
                val = hasht[strt]
                val.append(i)
                hasht[strt] = val
            else:
                hasht[strt] = [i]
                
        return list(hasht.values())
            
        