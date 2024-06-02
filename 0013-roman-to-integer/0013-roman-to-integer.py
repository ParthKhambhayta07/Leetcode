class Solution:
    def romanToInt(self, s: str) -> int:
        dicn = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000,'IV':4,'IX':9,'XL':40,'XC':90,'CD':400,'CM':900}
        sum = 0
        for i in range(len(s)):                       
            if i == 0:
                sum += dicn.get(s[i])
            elif dicn.get(s[i]) > dicn.get(s[i-1]):
                sum += dicn.get(s[i]) - (2*(dicn.get(s[i-1])))
            else:
                sum += dicn.get(s[i])
                
        
        return sum