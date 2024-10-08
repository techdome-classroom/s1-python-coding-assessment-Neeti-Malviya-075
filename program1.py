class Solution:
   
    def getTotalIsles(self, grid: list[list[str]]) -> int:
    #    write your code here
        if not grid:
            return 0
        
        rows, cols = len(grid), len(grid[0])
        total_islands = 0
        
        def dfs(r, c):
           
            if r < 0 or c < 0 or r >= rows or c >= cols or grid[r][c] == 'W':
                return
           
            grid[r][c] = 'W'
            
            
            dfs(r - 1, c) 
            dfs(r + 1, c)  
            dfs(r, c - 1)  
            dfs(r, c + 1)  
        
       
        for r in range(rows):
            for c in range(cols):
               
                if grid[r][c] == 'L':
                    total_islands += 1
                    dfs(r, c) 
        
        return total_islands
                    
        
