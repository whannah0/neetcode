class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        myMap = {}
        for i in range(len(position)):
            myMap[position[i]] = speed[i]
        
        myMap = sorted(myMap.items(), reverse = True)
        stack = []
        
        for j in range(len(myMap)):
            time = (target - myMap[j][0]) / myMap[j][1]
            #print("time:", time)
            if stack: #if stack is not empty
                top = stack[-1]
                #print(top)
                if time <= top: 
                    continue
                else: 
                    stack.append(time)
            else: # if stack is empty
                stack.append(time)
            #print("stack", stack)
        
        return len(stack)
