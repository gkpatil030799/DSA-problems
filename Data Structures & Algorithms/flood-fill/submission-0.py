class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        ROWS, COLS = len(image), len(image[0])
        org_color = image[sr][sc]

        def dfs(image, r,c,visit):
            if(r<0 or c<0 or r==ROWS or c==COLS or (r,c) in visit):
                return
            
            if image[r][c] == org_color or image[r][c] == color :
                image[r][c] = color
            elif image[r][c] == color:
                image[r][c] = color
            else:
                return
            visit.add((r,c))
            dfs(image,r+1,c,visit)
            dfs(image,r-1,c,visit)
            dfs(image,r,c-1,visit)
            dfs(image,r,c+1,visit)

            return image

        return dfs(image,sr,sc,set())