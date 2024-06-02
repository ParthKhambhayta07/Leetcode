class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        l = []
        max_l = 0
        if len(s) == 0:
            return 0
        for i in range(len(s)):
            for j in range(i, len(s)):
                if s[j] not in l:
                    l.append(s[j])
                    if len(l) > max_l:
                        max_l = len(l)
                        
                else:
                    l = []
                    break

        return max_l

        