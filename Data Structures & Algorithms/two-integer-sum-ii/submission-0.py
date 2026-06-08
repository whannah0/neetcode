class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # brute force way
        result =[]
        for i in range(len(numbers)):
            for j in range(i+1, len(numbers)):
                if numbers[i]+numbers[j] == target:
                    result = [i+1,j+1]
                    return result
                
        
        return result


            
        