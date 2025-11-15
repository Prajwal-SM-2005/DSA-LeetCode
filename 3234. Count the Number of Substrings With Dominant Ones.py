class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        n = len(s)
        # collect zero positions
        zeros = [i for i, ch in enumerate(s) if ch == '0']
        zcnt = len(zeros)
        ans = 0

        # handle k = 0 (substrings with zero zeros => all-ones substrings)
        # count contiguous runs of '1'
        i = 0
        while i < n:
            if s[i] == '1':
                j = i
                while j < n and s[j] == '1':
                    j += 1
                length = j - i
                ans += length * (length + 1) // 2
                i = j
            else:
                i += 1

        # maximum k such that k^2 + k <= n (beyond this impossible)
        import math
        max_k = int(math.sqrt(n)) + 2
        max_k = min(max_k, zcnt)  # cannot have more zeros than exist

        # sentinel positions for easier boundary handling
        # prev zero before first is -1, next after last is n
        # we will treat prev_zero = -1 and next_zero = n when needed
        for k in range(1, max_k + 1):
            Lmin = k * k + k  # minimal total length required for given k

            # slide window over zeros array: window of k consecutive zeros
            for start in range(0, zcnt - k + 1):
                left_zero_pos = zeros[start]
                right_zero_pos = zeros[start + k - 1]

                # minimal span covering these k zeros (includes any ones in between)
                span_min = right_zero_pos - left_zero_pos + 1

                # free ones left of left_zero_pos we can include without introducing another zero
                prev_zero_pos = -1 if start == 0 else zeros[start - 1]
                left_free = left_zero_pos - prev_zero_pos  # choices for start shift (0..left_free-1)

                # free ones right of right_zero_pos we can include
                next_zero_pos = n if (start + k - 1 == zcnt - 1) else zeros[start + k]
                right_free = next_zero_pos - right_zero_pos  # choices for end shift (0..right_free-1)

                # needed extra characters (ones) to reach Lmin
                needed_extra = Lmin - span_min

                # if needed_extra <= 0 => every (start shift, end shift) pair is valid
                total_pairs = left_free * right_free
                if needed_extra <= 0:
                    ans += total_pairs
                    continue

                # maximum possible added by shifts = (left_free-1) + (right_free-1)
                max_add = left_free + right_free - 2
                if needed_extra > max_add:
                    # even with maximal extension we can't reach required length
                    # so 0 valid pairs
                    continue

                # count pairs (a,b) with a in [0,left_free-1], b in [0,right_free-1]
                # such that a + b >= needed_extra.
                # valid_pairs = total_pairs - bad_pairs where bad_pairs are a+b < needed_extra.
                t = needed_extra

                # compute bad_pairs = sum_{a=0..left_free-1} max(0, min(right_free, t - a))
                # equivalently for a where t-a > 0
                # let a_max = min(left_free-1, t-1)
                a_max = min(left_free - 1, t - 1)
                if a_max < 0:
                    bad_pairs = 0
                else:
                    # when t - a >= right_free => term = right_free
                    # solve a <= t - right_free
                    a_full = t - right_free
                    if a_full < 0:
                        a_full = -1
                    a_full = min(a_max, a_full)

                    bad_pairs = 0
                    if a_full >= 0:
                        bad_pairs += (a_full + 1) * right_free

                    # remaining a from a_full+1 .. a_max => term = t - a
                    a_start = a_full + 1
                    a_end = a_max
                    if a_start <= a_end:
                        cnt = a_end - a_start + 1
                        # sum_{a=a_start..a_end} (t - a) = cnt * t - sum_{a=a_start..a_end} a
                        sum_a = (a_start + a_end) * cnt // 2
                        bad_pairs += cnt * t - sum_a

                valid = total_pairs - bad_pairs
                ans += valid

        return ans
