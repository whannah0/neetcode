class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        hashset = set()
        longest = 0
        left = 0

        for right in range(len(s)):
            while s[right] in hashset:
                hashset.remove(s[left])
                left+=1
                

            hashset.add(s[right])

            currStrLen = right - left + 1
            longest = max (currStrLen, longest)
        
        return longest



        