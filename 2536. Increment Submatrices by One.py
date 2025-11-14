class Solution:
    def rangeAddQueries(self, n: int, queries: List[List[int]]) -> List[List[int]]:
        # Difference array of size (n+1) x (n+1)
        diff = [[0] * (n + 1) for _ in range(n + 1)]

        # Apply difference array marking
        for r1, c1, r2, c2 in queries:
            diff[r1][c1] += 1
            diff[r1][c2 + 1] -= 1
            diff[r2 + 1][c1] -= 1
            diff[r2 + 1][c2 + 1] += 1

        # Prefix sum to build final matrix
        for r in range(n):
            for c in range(n):
                if r > 0:
                    diff[r][c] += diff[r - 1][c]
                if c > 0:
                    diff[r][c] += diff[r][c - 1]
                if r > 0 and c > 0:
                    diff[r][c] -= diff[r - 1][c - 1]

        # Remove extra last row/column
        return [row[:n] for row in diff[:n]]
