class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        v=sorted(s)
        m=sorted(t)
        for i in range(len(s)):
            if len(v)!=len(m):
                return False
            if v[i]!=m[i]:
                return False
        return True        
        