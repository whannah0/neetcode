class LRUCache:

    def __init__(self, capacity: int):
       # assigning to self creates a permanent instance field, overriding any class-level default.
        self.capacity = capacity
        self.arr = []
        
        

    def get(self, key: int) -> int:
        for i in range(len(self.arr)):
            if self.arr[i][0] == key:
                result = self.arr[i][1] 
                # remove and append it back (back is most recently used)
                self.arr.append(self.arr.pop(i))
                return result
        return -1

        

    
    def put(self, key: int, value: int) -> None:
        exist = 0
        #if key alr exist, update value
        for i in range(len(self.arr)):
            if self.arr[i][0] == key:
                self.arr[i][1] = value
                #move to the back
                self.arr.append(self.arr.pop(i))
                exist = 1
        
        # if key not exist
        if not exist:
            if len(self.arr) < self.capacity:
                # add key-val pair into map
                self.arr.append([key, value])
            else:
                #remove LRU
                self.arr.pop(0)
                # then, add key-val pair into map
                self.arr.append([key, value])
                


        
