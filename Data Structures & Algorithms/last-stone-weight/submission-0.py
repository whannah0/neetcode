class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        #brute force
        n = len(stones)
    
        sortedList = sorted(stones)
        while len(sortedList) > 1:
            sortedList.sort()
            if sortedList[n-2] == sortedList[n-1]:
                sortedList.pop(n-1)
                sortedList.pop(n-2)
                n -=2

            elif sortedList[n-2] < sortedList[n-1]:
                newWeight = sortedList[n-1]- sortedList[n-2]
                sortedList.pop(n-1)
                sortedList.pop(n-2)
                sortedList.append(newWeight)
                n-=1
            
        if len(sortedList) == 0:
            return 0
        else:
            return sortedList[0]



        