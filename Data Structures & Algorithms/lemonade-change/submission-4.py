class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        # brute force 
        
        five = 0
        ten = 0
        twenty = 0

        for i in range(len(bills)):
            if bills[i] == 5:
                five += 1
            
            if bills[i] == 10:
                if five < 1:
                    return False
                else:
                    ten +=1
                    five -= 1
            
            if bills[i] == 20:
                # 2 conditions 3 fives or 1 ten 1 five
                if five < 3:
                    if five < 1 or ten < 1:
                        return False
                    else : # we do have 1 ten 1 five
                        twenty += 1
                        five -= 1
                        ten -= 1
                else : # we do have 3 fives
                        twenty += 1
                        five -= 3
                
        
        return True
            

        