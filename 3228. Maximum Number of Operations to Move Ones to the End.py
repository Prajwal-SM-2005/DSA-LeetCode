class Solution:
    def maxOperations(self, s: str) -> int:
        ans = 0
        ones = 0

        # Count ones as we go left -> right.
        # Whenever we see a '0' that is immediately followed by '1' or is the last char,
        # that '0' can be the "end" zero used by every '1' seen so far, so add `ones`.
        for i, c in enumerate(s):
            if c == '1':
                ones += 1
            elif i + 1 == len(s) or s[i + 1] == '1':
                ans += ones

        return ans
