class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # check empty
        if not grid:
            return 0
        rows = len(grid)
        columns = len(grid[0])

        totalIsland = 0

        for r in range(rows):
            for c in range(columns):
                if grid[r][c] == "1":

                    totalIsland +=1
                    self.dfs(grid, r, c)
                    
        
        return totalIsland

      

    
    def dfs(self, grid: List[List[str]], r: int, c: int) -> None:
        rows = len(grid)
        columns = len(grid[0])
        # r, c is the coordinate of the current island/water we are looking at
        #check out of bound
        if r < 0 or r >= rows or c < 0 or c >= columns or grid[r][c] == "0":
            return
        
        # mark current island as visited
        grid[r][c] = "0"

        self.dfs(grid, r+1, c)
        self.dfs(grid, r-1, c)
        self.dfs(grid, r, c+1)
        self.dfs(grid, r, c-1)
