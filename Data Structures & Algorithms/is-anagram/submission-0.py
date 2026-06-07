class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        for char in range(len(s)):
            target = s[char]
            found = False

            for i in range(len(t)):
                if t[i] == target:
            
                    t = t[:i] + t[i+1:]
                    found = True
                    break

            if not found:
                return False

        return True
        # if len(s) != len(t):
        #     return False;
        # slen = len(s);
        
        # for char in range (slen):
        #     target = s[char];
        #     tlen = len(t);
        #     for i in range (tlen):
        #         if t[i] == target:
        #             t=t.replace(t[i],"");
        #             break;
        #         else:
        #             continue;
        #     return False;

        # return True;
        