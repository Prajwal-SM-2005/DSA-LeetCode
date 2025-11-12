from math import gcd
from typing import List

class Solution:
    def minOperations(self, nums: List[int]) -> int:
        n = len(nums)
        ones = nums.count(1)

        # Case 1: If already have 1s
        if ones > 0:
            return n - ones

        # Case 2: Find smallest subarray with gcd == 1
        min_len = n + 1
        for i in range(n):
            curr_gcd = nums[i]
            for j in range(i + 1, n):
                curr_gcd = gcd(curr_gcd, nums[j])
                if curr_gcd == 1:
                    min_len = min(min_len, j - i + 1)
                    break

        # If impossible
        if min_len == n + 1:
            return -1

        # (min_len - 1) + (n - 1)
        return (min_len - 1) + (n - 1)
