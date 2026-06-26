class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # 0 0 T
        # 0 1 T
        # 1 0 F
        # 1 1 complicated
        if len(s1) == 0:
            return True
        if len(s2) == 0:
            return False
        
        left = 0
        right = len(s1) -1
        hashmap = {}

        for i in range (len(s1)):
            hashmap[s1[i]] = 1 + hashmap.get(s1[i], 0)
        #slide the window of size s1 til you find all character in 
        # the window is in the hashmap
        # if right is at the last character and still cannot find all char in hm
        # return false
        match = 0
        while right < len(s2):
            hashcopy = hashmap.copy()
            for i in range(left, right+1):
                
                if s2[i] not in hashcopy:
                    print(s2[i], "not in hashmap")
                    break
                else:
                    print(s2[i], "in hashmap")
                    if hashcopy[s2[i]] == 1:
                        hashcopy.pop(s2[i])
                    else: 
                        hashcopy[s2[i]] -= 1
                    
                    match += 1
            if match == len(s1):
                return True
            else: 
                match = 0
                left += 1
                right += 1
        
        return False