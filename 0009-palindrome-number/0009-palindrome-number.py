class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x >= 0:
            s=str(x)[::-1]
            if(int(s) <= (2**32 - 1) and int(s) >= -(2**31)):
                if(int(s)==x):               
                    return True
                else:                    
                    return False
            else:
                return False
        else:            
            return False