class Solution:
   
    def getTotalIsles(self, grid: list[list[str]]) -> int:
    #    write your code here
        if not grid:
            return 0
        
        rows, cols = len(grid), len(grid[0])
        total_islands = 0
        
        def dfs(r, c):
            # Base case: if out of bounds or it's water ('W'), stop
            if r < 0 or c < 0 or r >= rows or c >= cols or grid[r][c] == 'W':
                return
            # Mark this cell as visited by setting it to 'W' (water)
            grid[r][c] = 'W'
            
            # Explore all four possible directions (up, down, left, right)
            dfs(r - 1, c)  # Up
            dfs(r + 1, c)  # Down
            dfs(r, c - 1)  # Left
            dfs(r, c + 1)  # Right
        
        # Loop through every cell in the grid
        for r in range(rows):
            for c in range(cols):
                # If we find land ('L'), this is a new island
                if grid[r][c] == 'L':
                    total_islands += 1
                    dfs(r, c)  # Use DFS to mark the entire island as visited
        
        return total_islands
                    
        
