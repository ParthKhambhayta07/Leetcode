class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        l = []
        for i in range(numRows):
            ilist = []
            for j in range(i+1):
                if j == i  or j == 0:
                    ilist.append(1)
                else:
                    ilist.append(l[i-1][j-1] + l[i-1][j])
            
            l.append(ilist)
        
        return l
                