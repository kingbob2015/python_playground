# In a given grid, each cell can have one of three values:

# the value 0 representing an empty cell;
# the value 1 representing a fresh orange;
# the value 2 representing a rotten orange.
# Every minute, any fresh orange that is adjacent (4-directionally) to a rotten orange becomes rotten.

# Return the minimum number of minutes that must elapse until no cell has a fresh orange.  If this is impossible, return -1 instead.

 

# Example 1:



# Input: [[2,1,1],[1,1,0],[0,1,1]]
# Output: 4
# Example 2:

# Input: [[2,1,1],[0,1,1],[1,0,1]]
# Output: -1
# Explanation:  The orange in the bottom left corner (row 2, column 0) is never rotten, because rotting only happens 4-directionally.
# Example 3:

# Input: [[0,2]]
# Output: 0
# Explanation:  Since there are already no fresh oranges at minute 0, the answer is just 0.
 

# Note:

# 1 <= grid.length <= 10
# 1 <= grid[0].length <= 10
# grid[i][j] is only 0, 1, or 2.

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        time = 0
        numOranges = 0
        rottingOranges = set()
        for row in range(len(grid)):
            for col in range(len(grid[row])):
                if grid[row][col] != 0:
                    numOranges += 1
                    if grid[row][col] == 2:
                        rottingOranges.add((row, col))
        
        numRotted = 0
        
        def checkFreshOrange(row, col):
            if row >= 0 and row < len(grid):
                if col >=0 and col < len(grid[row]):
                    if grid[row][col] == 1:
                        return True
            return False
        
        while True:
            tmpSet = set()
            for orange in rottingOranges:
                numRotted+=1
                if checkFreshOrange(orange[0]-1, orange[1]):
                    tmpSet.add((orange[0]-1, orange[1]))
                    grid[orange[0]-1][orange[1]] = 2
                if checkFreshOrange(orange[0], orange[1]-1):
                    tmpSet.add((orange[0], orange[1]-1))
                    grid[orange[0]][orange[1]-1] = 2
                if checkFreshOrange(orange[0]+1, orange[1]):
                    tmpSet.add((orange[0]+1, orange[1]))
                    grid[orange[0]+1][orange[1]] = 2
                if checkFreshOrange(orange[0], orange[1]+1):
                    tmpSet.add((orange[0], orange[1]+1))
                    grid[orange[0]][orange[1]+1] = 2
                rottingOranges = tmpSet
            if len(rottingOranges) == 0:
                break
            time+=1
        if numRotted != numOranges:
            return -1
        else:
            return time