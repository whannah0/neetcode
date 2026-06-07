class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # Refactor: utilized zip() to combine 2 arrays into pairs instead of using map

        myMap = sorted(zip(position, speed), reverse = True)
        maxSoFar = 0
        result = 0
        
        for j in range(len(myMap)):
            time = (target - myMap[j][0]) / myMap[j][1]
            #print("time:", time)

            #curr is slower
            if time > maxSoFar:
                result += 1
                maxSoFar = time
            
            
                
                
        return result
