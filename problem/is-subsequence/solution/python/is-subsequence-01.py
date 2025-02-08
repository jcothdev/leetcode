class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        pos = -1
        for c in s:
            index = t.find(c, (pos + 1))
            if index <= pos:
                return False
            pos = index
        return True