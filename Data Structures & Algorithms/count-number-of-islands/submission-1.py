class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # 0 is water, 1 is land. what we can do is iterate over the whole grid. when we hit a 1 we haven't seen before, we start checking the adjacent squares (depth first) and keep track of the nodes we've already seen. Once we run out of ALL neighbouring 1s, we move on to the next node in the for loop and continue. th idea is that if we've already seen a 1, we can effectively skip it, hence O(n*m) time, but the seen matrix will result in O(m*n) space.

        m = len(grid)
        n = len(grid[0])
        seen = [[False] * n for _ in range(m)]
        count = 0

        def dfs(row, col):
            seen[row][col] = True


            if row > 0 and grid[row - 1][col] == "1" and not seen[row - 1][col]:
                dfs(row - 1, col)
            if row < m - 1 and grid[row + 1][col] == "1" and not seen[row + 1][col]:
                dfs(row + 1, col)
            if col > 0 and grid[row][col - 1] == "1" and not seen[row][col - 1]:
                dfs(row, col - 1)
            if col < n - 1 and grid[row][col + 1] == "1" and not seen[row][col + 1]:
                dfs(row, col + 1)

        for row in range(m):
            for col in range(n):
                if grid[row][col] == "1" and not seen[row][col]:
                    # this is a new island. find all neighbouring ones using depth first
                    count += 1
                    dfs(row, col)
        return count