#python3

class Solution:
    def numberOfPaths(self, grid: List[List[int]], k: int) -> int:
        MOD = 1_000_000_007
        n = len(grid)
        m = len(grid[0])
        dp = [[[0] * k for _ in range(m)] for _ in range(n)]

        dp[0][0][grid[0][0] % k] = 1

        for j in range(1, m):
            for l in range(k):
                if dp[0][j - 1][l] != 0:
                    dp[0][j][(l + grid[0][j]) % k] += 1
                    break

        for i in range(1, n):
            for l in range(k):
                if dp[i - 1][0][l] != 0:
                    dp[i][0][(l + grid[i][0]) % k] += 1
                    break

        for i in range(1, n):
            for j in range(1, m):
                for l in range(k):
                    mod_index = (l + grid[i][j]) % k
                    top = dp[i - 1][j][l]
                    if top != 0:
                        dp[i][j][mod_index] = top
                    left = dp[i][j - 1][l]
                    if left != 0:
                        dp[i][j][mod_index] = (dp[i][j][mod_index] + left) % MOD

        return dp[n - 1][m - 1][0]