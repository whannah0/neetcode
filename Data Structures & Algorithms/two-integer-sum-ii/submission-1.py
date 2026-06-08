class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # two pointer algorithm
        # nums.sort(), sorts the list in-place and returns None
        # sorted(nums), creates a new array and make the original None
        sortedNumbers = sorted(numbers)
        left = 0
        right = len(numbers)-1
        while not sortedNumbers[left] + sortedNumbers[right] == target:
            if sortedNumbers[left] + sortedNumbers[right] > target:
                right-=1
            else:
                left +=1
        # how to find index in the original array? use arr.index()
        ind1 = numbers.index(sortedNumbers[left])
        ind2 = numbers.index(sortedNumbers[right])
        if ind1 < ind2:
            return [ind1+1, ind2+1]
        
        return [ind2+1, ind1+1]





        # brute force way - O(n^2) runtime
        # result =[]
        # for i in range(len(numbers)):
        #     for j in range(i+1, len(numbers)):
        #         if numbers[i]+numbers[j] == target:
        #             result = [i+1,j+1]
        #             return result
                
        
        # return result


            
        