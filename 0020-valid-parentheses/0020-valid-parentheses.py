class Solution:
    def isValid(self, s: str) -> bool:
        dic = {'(':')','{':'}','[':']'}
        if len(s) % 2 != 0:
            return False
        cont = []
        for i in s:
            if i in dic.keys():
                cont.append(i)
            else:
                if cont and dic[cont[-1]] == i:
                    cont.pop()
                else:
                    return False
        if len(cont) == 0:
            return True
        else:
            return False