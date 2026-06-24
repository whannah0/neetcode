class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        res = 0

        l = 0
        maxf = 0

        for r in range(len(s)):
            count[s[r]] = 1 + count.get(s[r], 0)
            maxf = max(maxf, count[s[r]])

            # window size - # of most frequent char
            while (r-l +1) - maxf > k:
                count[s[l]] -= 1
                l += 1

            res = max(res, r-l+1)

        return res
        
        # result = 0
        # quota = k
        # if len(s) < 2:
        #     return len(s)
        # for i in range(len(s)-1):
        #     start = i
        #     end = i+1
        #     longestSoFar = 1
        #     while quota > 0 or s[start] == s[end]:
        #         if s[start] == s[end]:
        #             end +=1
        #             longestSoFar +=1

        #         else:
        #             if quota > 0:
        #                 quota-=1
        #                 end +=1
        #                 longestSoFar +=1
                

                
        #         result = max(longestSoFar, result)

        #         if end >= len(s): # reach end of string s
        #             return result


        
        # return result



        