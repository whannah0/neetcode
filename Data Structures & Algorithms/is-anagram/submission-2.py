class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        d = dict()
        if len(s) != len(t):
            return False
        
        for i in range(len(s)):
            if s[i] not in d:
                d[s[i]] = 1
            else:
                val = d.get(s[i])
                d[s[i]] = val +1
        
        
        for j in range(len(t)):
            if t[j] in d:
                val = d.get(t[j])
                d[t[j]] = val - 1
                if d[t[j]] == 0:
                    d.pop(t[j])
                
            else:
                return False
        
        return True

        