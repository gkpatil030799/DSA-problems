class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        def dfs(grid,r,c,visit):
            if(r<0 or c < 0 or c==COLS or r==ROWS or (r,c) in visit or grid[r][c]=='0'):
                return
            
            visit.add((r,c))
            dfs(grid, r+1, c, visit)
            dfs(grid, r-1, c, visit)
            dfs(grid, r, c+1, visit)
            dfs(grid, r, c-1, visit)

        count=0
        visit = set()
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == '1' and (r,c) not in visit:
                    dfs(grid,r,c,visit)
                    count+=1
        return count
