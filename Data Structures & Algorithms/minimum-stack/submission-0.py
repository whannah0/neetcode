class MinStack:

    def __init__(self):
        self.array = []
        #append to array (push), remove last item from arry(pop)
        

    def push(self, val: int) -> None:
        self.array.append(val)


        

    def pop(self) -> None:
        self.array.pop(len(self.array)-1)
        

    def top(self) -> int:
        return self.array[len(self.array)-1]
        

    def getMin(self) -> int:
        sortArr = sorted(self.array)
        return sortArr[0]
        
