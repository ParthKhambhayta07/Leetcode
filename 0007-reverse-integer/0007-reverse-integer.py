class Solution:
    def reverse(self, x: int) -> int:
        if x==0:
            return 0
        n=str(x).rstrip("0")
        
        if(n[0]=='-'):
            a = int('-'+n[-1:0:-1])
            if (a >= -2147483648 and a <= 2147483647):
                return a
            else:
                return 0
        else:
            a = int(n[::-1])
            if (a >= -2147483648 and a <= 2147483647):
                return a
            else:
                return 0
            